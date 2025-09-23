import torch
import numpy as np
from torch.cuda.amp import GradScaler, autocast
import random
import gc
import sys, os

from torch.utils.tensorboard import SummaryWriter
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utility_functions import (get_most_recent_h5py_record_path, save_checkpoint, AverageMeter,
                   save_args_to_yaml, compute_gradient_norm, get_process_ram_usage, get_system_ram_usage)
from dataset_functions import LocomotionDataset
import tqdm
import argparse
import yaml

def set_seed(seed):
    random.seed(seed)  # Set Python's random seed
    np.random.seed(seed)  # Set NumPy's random seed
    torch.manual_seed(seed)  # Set PyTorch's CPU seed
    torch.cuda.manual_seed(seed)  # Set PyTorch's GPU seed (if using CUDA)
    torch.cuda.manual_seed_all(seed)  # Set the seed for all GPUs (if using multiple GPUs)
    torch.backends.cudnn.deterministic = True  # Ensure deterministic behavior
    torch.backends.cudnn.benchmark = True  # Disable optimizations for reproducibility

set_seed(0)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Train an agent using supervised learning.")

    # Define arguments with defaults
    parser.add_argument("--train_set", nargs="+", type=str, default=None, required=True,
                        help="List of robot names as the training set.")
    parser.add_argument("--test_set", nargs="+", type=str, default=None, required=False,
                        help="List of robot names as the test set.")
    parser.add_argument("--num_epochs", type=int, default=10, help="Number of epochs to run.")
    parser.add_argument("--batch_size", type=int, default=256, help="Batch size. 4096*16 takes 10G")
    parser.add_argument("--exp_name", type=str, default=None,
                        help="Name of the experiment. If provided, the current date and time will be appended. "
                             "Default is the current date and time.")
    parser.add_argument("--checkpoint_interval", type=int, default=1, help="Save checkpoint every N epochs.")
    parser.add_argument("--log_dir", type=str, default="log_dir", help="Base directory for logs and checkpoints.")
    parser.add_argument("--lr", type=float, default=3e-4, help="Unit learning rate (for a batch size of 512)")
    parser.add_argument("--num_workers", type=int, default=0, help="Number of workers for torch data loader.")
    parser.add_argument("--max_files_in_memory", type=int, default=1, help="Max number of data files in memory.")
    parser.add_argument("--val_ratio", type=float, default=0.15, help="Validation set size.")
    parser.add_argument("--gradient_acc_steps", type=int, default=1,
                        help="Number of batches before one gradient update.")
    parser.add_argument("--h5_repeat_factor", type=int, default=1, help="Number of times we repeat sampling data from"
                                                                        "cache consecutively in one epoch.")
    parser.add_argument("--use_amp", type=int, default=0, help="Whether to use automatic mixed precision.")
    parser.add_argument("--max_parallel_envs_per_file", type=int, default=4096,
                        help="Number of parallel envs per file.")
    parser.add_argument("--max_envs_per_file_in_memory", type=int, default=512,
                       help="Number of envs per file that can be stored in cache.")
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        choices=["urma"],
        help="Model type."
    )
    # Add argument for YAML configuration
    parser.add_argument("--config", type=str, help="Path to YAML configuration file.")
    parser.add_argument("--dataset_dir", type=str,
                        default="logs/rsl_rl",
                        help="Directory containing the dataset.")
    parser.add_argument("--resume", type=str, default=None, help="Path to checkpoint for resume training.")

    args = parser.parse_args()

    # Load and override arguments from YAML file if specified
    if args.config:
        print(f'Loading configuration from {args.config}. Specified params will be overridden.')

        with open(args.config, 'r') as file:
            config_args = yaml.safe_load(file)

        for key, value in config_args.items():
            if hasattr(args, key):
                setattr(args, key, value)

    # Fill missing arguments with defaults
    for action in parser._actions:
        if action.dest == "help":
            continue
        if getattr(args, action.dest) is None and action.default is not None:
            setattr(args, action.dest, action.default)

    return args


def get_meter_dict_avg(meter_dicts):
    if len(meter_dicts) == 0:
        return 0
    return sum([meter.avg for meter in meter_dicts.values()])/len(meter_dicts)



reweighting = False
important_indices_humanoid = [12, 13, 14, 16, 17, 20, 21, 24, 25, 28, 60, 92, 44, 76, 108]
important_indices_gendog = [9, 10, 12, 13, 16, 17, 20, 44, 68, 92, 32, 56, 80, 104]
def reweight_loss(loss, data_source_name):
    # reweighting: scale down quadruped losses since they are easy
    # if "Gendog" in data_source_name: # quadruped
    #     loss = loss * 0.6
    # Gendog: use a coefficient of 1 for them as a baseline, except
    # scaling up losses for important ones
    if any([f"Gendog{robot}_" in data_source_name for robot in important_indices_humanoid]):
        # print(f"[INFO] Important dog in batch: {data_source_name}")
        loss = loss * 3
    # scale up hexapod losses a little bit since they are harder than Gendogs
    if "Genhexapod" in data_source_name:
        loss = loss * 1.25
    # scale up humanoid losses, particularly for the important ones
    if any([f"Genhumanoid{robot}_" in data_source_name for robot in important_indices_humanoid]):
        # print(f"[INFO] Important humanonid in batch: {data_source_name}")
        loss = loss * 8
    elif "Genhumanoid" in data_source_name:
        loss = loss * 2

    return loss


def train(policy, criterion, optimizer, scheduler, train_dataset, val_dataset, test_dataset, num_epochs, model_device,
          log_dir, checkpoint_interval, model, gradient_acc_steps, batch_size, num_workers, use_amp, start_epoch):
    """Training loop with validation, TensorBoard logging, and checkpoint saving."""
    scaler = torch.cuda.amp.GradScaler()

    writer = SummaryWriter(log_dir=log_dir)
    train_loss_meters = {}
    val_loss_meters = {}
    test_loss_meters = {}
    best_val_loss = float("inf")

    print("[INFO] Starting supervised training.")
    for epoch in range(start_epoch, num_epochs):
        # clean up memory
        gc.collect()

        # Training phase
        policy.train()
        for meter in train_loss_meters.values():
            meter.reset()
        print(f"[INFO] Starting epoch {epoch + 1}/{num_epochs} - Training.")

        train_dataloader = train_dataset.get_data_loader(
            batch_size=batch_size, shuffle=True, num_workers=num_workers
        )

        with tqdm.tqdm(train_dataloader, desc=f"Training Epoch {epoch + 1}/{num_epochs}", unit="batch") as pbar:
            iteration_start_time = time.time()
            for index, (batch_inputs, batch_targets, data_source_name, io_times, processing_times) in enumerate(pbar):
                iteration = index + epoch * len(train_dataloader)
                dataloader_time = time.time() - iteration_start_time

                # Move data to device
                start_time = time.time()
                move_cuda_time = time.time() - start_time

                start_time = time.time()
                with torch.autocast(device_type='cuda', dtype=torch.float16, enabled=use_amp):
                    if model in ['urma']:
                        batch_predictions = policy(*batch_inputs)
                    else:
                        one_input = torch.cat([
                            component.flatten(1) for component in batch_inputs
                        ], dim=1)
                        batch_predictions = policy(one_input)

                    loss = criterion(batch_predictions, batch_targets)

                if reweighting:
                    loss = reweight_loss(loss, data_source_name)

                forward_time = time.time() - start_time

                # Backward pass and optimization
                start_time = time.time()

                if use_amp:
                    scaler.scale(loss).backward()
                else:
                    loss.backward()

                # Only update optimizer after accumulating enough gradients
                grad_norm = None  # Initialize gradient norm
                if index % gradient_acc_steps == gradient_acc_steps - 1:
                    if use_amp:
                        # Compute gradient norm before unscaled gradients are modified
                        # scaler.unscale_(optimizer)  # Unscale gradients for logging (optional with AMP)
                        grad_norm = compute_gradient_norm(policy)  # Log this value
                        scaler.step(optimizer)
                        scaler.update()
                    else:
                        # Compute gradient norm before optimizer step
                        torch.nn.utils.clip_grad_value_(policy.parameters(), clip_value=5.0)
                        grad_norm = compute_gradient_norm(policy)  # Log this value
                        optimizer.step()

                    optimizer.zero_grad()  # Zero gradients after optimization step

                backward_time = time.time() - start_time

                # Update training loss tracker
                if data_source_name not in train_loss_meters:
                    train_loss_meters[data_source_name] = AverageMeter()
                train_loss_meters[data_source_name].update(loss.item(), n=batch_targets.size(0))

                # Update progress bar with current loss
                pbar.set_postfix({"Loss": f"{get_meter_dict_avg(train_loss_meters):.4f}"})

                # Log times
                # start_time = time.time()
                if index % 100 == 0:
                    writer.add_scalar("Train/times/io_per_thread", io_times.mean().item(), iteration)
                    writer.add_scalar("Train/times/data_processing_per_thread", processing_times.mean().item(), iteration)
                    writer.add_scalar("Train/times/dataloader_time", dataloader_time, iteration)
                    writer.add_scalar("Train/times/move_cuda", move_cuda_time, iteration)
                    writer.add_scalar("Train/times/forward", forward_time, iteration)
                    writer.add_scalar("Train/times/backward", backward_time, iteration)

                    # Log memory
                    writer.add_scalar("Train/ram-system-used", get_system_ram_usage(), iteration)
                    writer.add_scalar("Train/ram-process-used", get_process_ram_usage(), iteration)
                    # print(f'{time.time() - start_time:.4f} | {get_meter_dict_avg(train_loss_meters)}')

                    # Log loss and lr by iteration
                    writer.add_scalar("Train/loss-iter/avg", loss.item(), iteration)
                    writer.add_scalar("Train/lr-iter", optimizer.param_groups[0]['lr'], iteration)
                    if grad_norm is not None:
                        writer.add_scalar("Train/grad_norm-iter", grad_norm, iteration)

                # Step the LR scheduler by iteration
                if scheduler is not None:
                    scheduler.step(iteration)

                iteration_start_time = time.time()  # start time of next iteration

        del train_dataloader

        # Log training loss to TensorBoard
        for robot_name, meter in train_loss_meters.items():
            writer.add_scalar(f"Train/loss/{robot_name}", meter.avg, epoch + 1)
        writer.add_scalar("Train/loss/avg", get_meter_dict_avg(train_loss_meters), epoch + 1)
        writer.add_scalar("Train/lr", optimizer.param_groups[0]['lr'], epoch + 1)

        # Validation phase
        policy.eval()
        for meter in val_loss_meters.values():
            meter.reset()
        print(f"[INFO] Starting epoch {epoch + 1}/{num_epochs} - Validation.")

        val_dataloader = val_dataset.get_data_loader(
            batch_size=batch_size, shuffle=True, num_workers=num_workers
        )

        with torch.no_grad():
            with tqdm.tqdm(val_dataloader, desc=f"Validation Epoch {epoch + 1}/{num_epochs}", unit="batch") as pbar:
                for index, (batch_inputs, batch_targets, data_source_name, _, _) in enumerate(pbar):

                    if model in ['urma']:
                        batch_predictions = policy(*batch_inputs)
                    else:
                        one_input = torch.cat([
                            component.flatten(1) for component in batch_inputs
                        ], dim=1)
                        batch_predictions = policy(one_input)

                    loss = criterion(batch_predictions, batch_targets)

                    # Update validation loss tracker
                    if data_source_name not in val_loss_meters:
                        val_loss_meters[data_source_name] = AverageMeter()
                    val_loss_meters[data_source_name].update(loss.item(), n=batch_targets.size(0))

                    # Update progress bar with current loss
                    pbar.set_postfix(
                        {"Loss": f"{get_meter_dict_avg(val_loss_meters):.4f}"})

                    if index > 0.03 * len(val_dataloader):
                        break

        # Log validation loss to TensorBoard
        for robot_name, meter in val_loss_meters.items():
            writer.add_scalar(f"Val/loss/{robot_name}", meter.avg, epoch + 1)
        writer.add_scalar("Val/loss/avg", get_meter_dict_avg(val_loss_meters), epoch + 1)

        del val_dataloader
        if epoch == 0:
            continue

        if len(test_dataset) > 0:
            # Test phase
            for meter in test_loss_meters.values():
                meter.reset()
            print(f"[INFO] Starting epoch {epoch + 1}/{num_epochs} - Test.")

            test_dataloader = test_dataset.get_data_loader(
                batch_size=batch_size, shuffle=True, num_workers=num_workers, prefetch_factor=25
            )

            with torch.no_grad():
                with tqdm.tqdm(test_dataloader, desc=f"Test Epoch {epoch + 1}/{num_epochs}", unit="batch") as pbar:
                    for index, (batch_inputs, batch_targets, data_source_name, _, _) in enumerate(pbar):
                        # Move data to device
                        batch_inputs = [x.to(model_device) for x in batch_inputs]
                        batch_targets = batch_targets.to(model_device)

                        if model in ['urma']:
                            batch_predictions = policy(*batch_inputs)
                        else:
                            one_input = torch.cat([
                                component.flatten(1) for component in batch_inputs
                            ], dim=1)
                            batch_predictions = policy(one_input)

                        loss = criterion(batch_predictions, batch_targets)

                        # Update validation loss tracker
                        if data_source_name not in test_loss_meters:
                            test_loss_meters[data_source_name] = AverageMeter()
                        test_loss_meters[data_source_name].update(loss.item(), n=batch_targets.size(0))

                        # Update progress bar with current loss
                        pbar.set_postfix(
                            {"Loss": f"{get_meter_dict_avg(test_loss_meters):.4f}"})

                        if index > 0.03 * len(test_dataloader):
                            break

            # Log validation loss to TensorBoard
            for robot_name, meter in test_loss_meters.items():
                writer.add_scalar(f"Test/loss/{robot_name}", meter.avg, epoch + 1)
            writer.add_scalar("Test/loss/avg", get_meter_dict_avg(test_loss_meters), epoch + 1)

            del test_dataloader

        # Save checkpoints periodically
        if (epoch + 1) % checkpoint_interval == 0:
            save_checkpoint(policy, optimizer, epoch + 1, log_dir)

        # Save the best model based on validation loss
        if get_meter_dict_avg(val_loss_meters) < best_val_loss:
            best_val_loss = get_meter_dict_avg(val_loss_meters)
            save_checkpoint(policy, optimizer, epoch + 1, log_dir, is_best=True)

        print(f"Epoch [{epoch + 1}/{num_epochs}], Train Loss: {get_meter_dict_avg(train_loss_meters):.6f}, "
              f"Val Loss: {get_meter_dict_avg(val_loss_meters):.6f}, Best Val Loss: {best_val_loss:.6f}, "
              f"Test Loss: {get_meter_dict_avg(test_loss_meters):.6f}")

    writer.close()
    print("[INFO] Training completed. TensorBoard logs saved.")


def main():
    args_cli = parse_arguments()

    # Prepare log directory
    log_dir = os.path.join(args_cli.log_dir, args_cli.exp_name)
    os.makedirs(log_dir, exist_ok=True)

    # Save args to a YAML file for reproducibility
    config_save_path = os.path.join(log_dir, "config.yaml")
    save_args_to_yaml(args_cli, config_save_path)
    print(f"[INFO] Config saved to {config_save_path}")

    # Dataset paths
    assert args_cli.train_set is not None, f"Please specify value for arg --train_set"
    train_set_paths = [get_most_recent_h5py_record_path(args_cli.dataset_dir, task) for task in args_cli.train_set]
    if args_cli.test_set:
        test_set_paths = [get_most_recent_h5py_record_path(args_cli.dataset_dir, task) for task in args_cli.test_set]
    else:
        test_set_paths = list()
        print(f'[INFO] No test set provided.')

    # Training dataset
    train_dataset = LocomotionDataset(
        folder_paths=train_set_paths,
        train_mode=True,
        val_ratio=args_cli.val_ratio,
        max_files_in_memory=args_cli.max_files_in_memory,
        h5_repeat_factor=args_cli.h5_repeat_factor,
        max_parallel_envs_per_file=args_cli.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=args_cli.max_envs_per_file_in_memory
    )

    # Validation dataset
    val_dataset = LocomotionDataset(
        folder_paths=train_set_paths,
        train_mode=False,
        val_ratio=args_cli.val_ratio,
        max_files_in_memory=args_cli.max_files_in_memory,
        h5_repeat_factor=1,
        max_parallel_envs_per_file=args_cli.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=args_cli.max_envs_per_file_in_memory
    )

    # Test dataset
    test_dataset = LocomotionDataset(
        folder_paths=test_set_paths,
        train_mode=False,
        val_ratio=args_cli.val_ratio,       # only use a proportion of the data as the test set
        max_files_in_memory=args_cli.max_files_in_memory,
        h5_repeat_factor=1,
        max_parallel_envs_per_file=args_cli.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=args_cli.max_envs_per_file_in_memory
    )

    model_device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # Define model, optimizer, and loss
    if args_cli.model == 'urma':
        from urma_model.policy_3head_scale2 import get_policy
        policy = get_policy(model_device)
    else:
        raise NotImplementedError(f'model type {args_cli.model} not implemented')

    print('policy architecture:\n', policy)

    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.AdamW(
        policy.parameters(),
        lr=args_cli.lr,
        weight_decay=1e-5,
    )

    # We need to get the actual iteration length by checking the dataloader, but note that the length varies
    # for different training hyper-params. Be careful when fine-tuning models.
    train_dataloader = train_dataset.get_data_loader(
        batch_size=args_cli.batch_size, shuffle=True, num_workers=args_cli.num_workers
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer,
                                                           T_max=args_cli.num_epochs*len(train_dataloader))

    # load checkpoint if path specified
    if args_cli.resume:
        checkpoint = torch.load(args_cli.resume, map_location="cpu")
        policy.load_state_dict(checkpoint["state_dict"])
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        start_epoch = checkpoint["epoch"]
        print(f"[INFO] Loaded checkpoint from {args_cli.resume}, resuming from epoch {start_epoch}")
    else:
        start_epoch = 0

    # Train the policy
    train(
        policy=policy,
        criterion=criterion,
        optimizer=optimizer,
        scheduler=scheduler,
        train_dataset=train_dataset,
        val_dataset=val_dataset,
        test_dataset=test_dataset,
        num_epochs=args_cli.num_epochs,
        model_device=model_device,
        log_dir=log_dir,
        checkpoint_interval=args_cli.checkpoint_interval,
        model=args_cli.model,
        gradient_acc_steps=args_cli.gradient_acc_steps,
        batch_size=args_cli.batch_size,
        num_workers=args_cli.num_workers,
        use_amp=bool(args_cli.use_amp),
        start_epoch=start_epoch
    )

if __name__ == "__main__":
    main()
