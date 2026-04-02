import torch
import numpy as np
from torch.cuda.amp import GradScaler, autocast
import random
import gc
import sys, os
import shlex

import wandb
import hydra
from omegaconf import DictConfig
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # for urma_model
sys.path.append("/home/cgauthie/projects/def-lpaull/cgauthie/embodiment-scaling-laws/scripts")
try:
    if os.path.exists("/home/cgauthie/projects/def-lpaull/cgauthie/embodiment-scaling-laws/scripts"):
        os.chdir("/home/cgauthie/projects/def-lpaull/cgauthie/embodiment-scaling-laws/scripts")
except Exception as e:
    print(f"[ERROR] Failed to change directory: {e}")
from utility_functions import (get_most_recent_h5py_record_path, save_checkpoint, AverageMeter,
                   save_args_to_yaml, compute_gradient_norm, get_process_ram_usage, get_system_ram_usage)
from dataset_functions import LocomotionDataset
import tqdm
import argparse
import yaml
from urma_model.policy_3head_scale2 import get_policy
print("Loaded URMA initially without error")

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
    parser.add_argument("--checkpoint_interval", type=int, default=5, help="Save checkpoint every N epochs.")
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
    parser.add_argument("--max_parallel_envs_per_file", type=int, default=2048,
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
    
    # Robot description arguments (for description vector ablation experiments)
    parser.add_argument("--description_filename", type=str, default=None,
                        help="Name of robot description JSON to load from each robot's asset folder. "
                             "If not specified, uses baseline 18-dim joint description (no limb bboxes). "
                             "Examples: 'robot_description_vec_with_bboxes.json' for computed bboxes, "
                             "'robot_description_vec_custom.json' for custom vectors.")
    parser.add_argument("--asset_base_path", type=str,
                        default=os.path.join(os.environ.get("SCRATCH", ""), "embodiment-scaling-laws/exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/Robots/GenBot1K-v7"),
                        help="Base path to robot assets (required if description_filename is provided)")
    parser.add_argument("--dynamic_joint_des_dim", type=int, default=None,
                        help="Dimension of joint description vector. If not specified, auto-detected: "
                             "18 for baseline, 24 when using description files with limb bboxes.")
    
    # Wandb arguments
    parser.add_argument("--wandb", action=argparse.BooleanOptionalAction, default=True, help="Enable wandb logging (syncs tensorboard). Use --no-wandb to disable.")
    parser.add_argument("--wandb_project", type=str, default="esl", help="Wandb project name.")
    parser.add_argument("--wandb_entity", type=str, default="velythyl", help="Wandb entity (team/username).")
    parser.add_argument("--wandb_name", type=str, default=None, help="Wandb run name. Defaults to exp_name.")

    args = parser.parse_args()

    # Pretty print args (YAML-like), skipping long list fields
    print("\n" + "="*50)
    print("Arguments:")
    print("="*50)
    skip_fields = {'train_set', 'test_set'}
    for key, value in sorted(vars(args).items()):
        if key in skip_fields:
            print(f"  {key}: <{len(value) if value else 0} items>")
        else:
            print(f"  {key}: {value}")
    print("="*50 + "\n")

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
            train_phase_start_time = time.time()
            iteration_start_time = time.time()
            for index, (batch_inputs, batch_targets, data_source_name, io_times, processing_times) in enumerate(pbar):
                iteration = index + epoch * len(train_dataloader)
                dataloader_time = time.time() - iteration_start_time

                # Move data to device
                start_time = time.time()
                batch_inputs = tuple(x.cuda(non_blocking=True) for x in batch_inputs)
                batch_targets = batch_targets.cuda(non_blocking=True)
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
                    log_dict = {
                        "Train/times/io_per_thread": io_times.mean().item(),
                        "Train/times/data_processing_per_thread": processing_times.mean().item(),
                        "Train/times/dataloader_time": dataloader_time,
                        "Train/times/move_cuda": move_cuda_time,
                        "Train/times/forward": forward_time,
                        "Train/times/backward": backward_time,
                        # Memory
                        "Train/ram-system-used": get_system_ram_usage(),
                        "Train/ram-process-used": get_process_ram_usage(),
                        # Loss and lr by iteration
                        "Train/loss-iter/avg": loss.item(),
                        "Train/lr-iter": optimizer.param_groups[0]['lr'],
                        "iteration": iteration,
                    }
                    if grad_norm is not None:
                        log_dict["Train/grad_norm-iter"] = grad_norm
                    wandb.log(log_dict)
                    pct = 100.0 * (index + 1) / len(train_dataloader)
                    train_bps = (index + 1) / (time.time() - train_phase_start_time)
                    print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - Train: {pct:.1f}% ({index+1}/{len(train_dataloader)}) | Loss: {loss.item():.4f} | {train_bps:.2f} batch/s")

                # Step the LR scheduler by iteration
                if scheduler is not None:
                    scheduler.step(iteration)

                iteration_start_time = time.time()  # start time of next iteration

        del train_dataloader

        # Log training loss to wandb
        train_log_dict = {f"Train/loss/{robot_name}": meter.avg for robot_name, meter in train_loss_meters.items()}
        train_log_dict["Train/loss/avg"] = get_meter_dict_avg(train_loss_meters)
        train_log_dict["Train/lr"] = optimizer.param_groups[0]['lr']
        train_log_dict["epoch"] = epoch + 1
        wandb.log(train_log_dict)
        train_total_bps = len(train_dataloader) / (time.time() - train_phase_start_time)
        print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - Train complete | Avg Loss: {get_meter_dict_avg(train_loss_meters):.4f} | {train_total_bps:.2f} batch/s")

        # Validation phase
        policy.eval()
        for meter in val_loss_meters.values():
            meter.reset()
        print(f"[INFO] Starting epoch {epoch + 1}/{num_epochs} - Validation.")

        val_dataloader = val_dataset.get_data_loader(
            batch_size=batch_size, shuffle=True, num_workers=num_workers
        )

        with torch.no_grad():
            val_phase_start_time = time.time()
            with tqdm.tqdm(val_dataloader, desc=f"Validation Epoch {epoch + 1}/{num_epochs}", unit="batch") as pbar:
                for index, (batch_inputs, batch_targets, data_source_name, _, _) in enumerate(pbar):
                    batch_inputs = tuple(x.cuda(non_blocking=True) for x in batch_inputs)
                    batch_targets = batch_targets.cuda(non_blocking=True)

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

        # Log validation loss to wandb
        val_log_dict = {f"Val/loss/{robot_name}": meter.avg for robot_name, meter in val_loss_meters.items()}
        val_log_dict["Val/loss/avg"] = get_meter_dict_avg(val_loss_meters)
        val_log_dict["epoch"] = epoch + 1
        wandb.log(val_log_dict)
        val_total_bps = (index + 1) / (time.time() - val_phase_start_time)
        print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - Val complete | Avg Loss: {get_meter_dict_avg(val_loss_meters):.4f} | {val_total_bps:.2f} batch/s")

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
                test_phase_start_time = time.time()
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

            # Log test loss to wandb
            test_log_dict = {f"Test/loss/{robot_name}": meter.avg for robot_name, meter in test_loss_meters.items()}
            test_log_dict["Test/loss/avg"] = get_meter_dict_avg(test_loss_meters)
            test_log_dict["epoch"] = epoch + 1
            wandb.log(test_log_dict)
            test_total_bps = (index + 1) / (time.time() - test_phase_start_time)
            print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - Test complete | Avg Loss: {get_meter_dict_avg(test_loss_meters):.4f} | {test_total_bps:.2f} batch/s")

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

    if wandb.run is not None:
        wandb.finish()
    print("[INFO] Training completed. Wandb logs saved.")


def main():
    args_cli = parse_arguments()

    # Prepare log directory
    log_dir = os.path.join(args_cli.log_dir, args_cli.exp_name)
    os.makedirs(log_dir, exist_ok=True)

    # Save args to a YAML file for reproducibility
    config_save_path = os.path.join(log_dir, "config.yaml")
    save_args_to_yaml(args_cli, config_save_path)
    print(f"[INFO] Config saved to {config_save_path}")

    # Initialize wandb
    if args_cli.wandb:
        wandb.init(
            project=args_cli.wandb_project,
            entity=args_cli.wandb_entity,
            name=args_cli.wandb_name or args_cli.exp_name,
            config=vars(args_cli),
            dir=log_dir
        )
        print(f"[INFO] Wandb initialized")

    # Debug: Check dataset directory contents
    import subprocess
    print(f"[INFO] Checking dataset directory: {args_cli.dataset_dir}")
    sys.stdout.flush()
    try:
        result = subprocess.run(['ls', args_cli.dataset_dir], capture_output=True, text=True, timeout=30)
        lines = result.stdout.strip().split('\n')
        print(f"[INFO] ls {args_cli.dataset_dir} (first 10 lines of {len(lines)} total):")
        for line in lines[:10]:
            print(f"  {line}")
        if len(lines) > 10:
            print(f"  ... and {len(lines) - 10} more")
        if result.stderr:
            print(f"[WARN] ls stderr: {result.stderr}")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] Failed to ls dataset directory: {e}")
        sys.stdout.flush()

    # Dataset paths
    assert args_cli.train_set is not None, f"Please specify value for arg --train_set"
    train_set_paths = [get_most_recent_h5py_record_path(args_cli.dataset_dir, task) for task in args_cli.train_set]
    if args_cli.test_set:
        test_set_paths = [get_most_recent_h5py_record_path(args_cli.dataset_dir, task) for task in args_cli.test_set]
    else:
        test_set_paths = list()
        print(f'[INFO] No test set provided.')

    # Expand environment variables in asset_base_path (e.g., $SCRATCH)
    asset_base_path = os.path.expandvars(args_cli.asset_base_path)

    # Training dataset
    train_dataset = LocomotionDataset(
        folder_paths=train_set_paths,
        train_mode=True,
        val_ratio=args_cli.val_ratio,
        max_files_in_memory=args_cli.max_files_in_memory,
        h5_repeat_factor=args_cli.h5_repeat_factor,
        max_parallel_envs_per_file=args_cli.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=args_cli.max_envs_per_file_in_memory,
        description_filename=args_cli.description_filename,
        asset_base_path=asset_base_path
    )

    # Validation dataset
    val_dataset = LocomotionDataset(
        folder_paths=train_set_paths,
        train_mode=False,
        val_ratio=args_cli.val_ratio,
        max_files_in_memory=args_cli.max_files_in_memory,
        h5_repeat_factor=1,
        max_parallel_envs_per_file=args_cli.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=args_cli.max_envs_per_file_in_memory,
        description_filename=args_cli.description_filename,
        asset_base_path=asset_base_path
    )

    # Test dataset
    test_dataset = LocomotionDataset(
        folder_paths=test_set_paths,
        train_mode=False,
        val_ratio=args_cli.val_ratio,       # only use a proportion of the data as the test set
        max_files_in_memory=args_cli.max_files_in_memory,
        h5_repeat_factor=1,
        max_parallel_envs_per_file=args_cli.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=args_cli.max_envs_per_file_in_memory,
        description_filename=args_cli.description_filename,
        asset_base_path=asset_base_path
    )

    model_device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"[INFO] Using device: {model_device}")

    # Determine dynamic joint description dimension
    # Auto-detect based on whether the dataset is using limb bboxes
    if args_cli.dynamic_joint_des_dim is not None:
        dynamic_joint_des_dim = args_cli.dynamic_joint_des_dim
    elif train_dataset.use_limb_bboxes:
        # 18 is the baseline, extra_des_dim is auto-detected from description file
        dynamic_joint_des_dim = 18 + train_dataset.extra_des_dim
        print(f"[INFO] Limb bboxes detected, auto-setting dynamic_joint_des_dim={dynamic_joint_des_dim} (18 base + {train_dataset.extra_des_dim} extra)")
    else:
        dynamic_joint_des_dim = 18  # baseline
        print("[INFO] No limb bboxes in description file, using baseline dynamic_joint_des_dim=18")

    # Define model, optimizer, and loss
    print(f"[INFO] About to load model: {args_cli.model}")
    sys.stdout.flush()
    try:
        if args_cli.model == 'urma':
            print("[INFO] Importing urma_model.policy_3head_scale2...")
            sys.stdout.flush()
            from urma_model.policy_3head_scale2 import get_policy
            print("[INFO] Import successful, calling get_policy()...")
            sys.stdout.flush()
            policy = get_policy(model_device, dynamic_joint_des_dim=dynamic_joint_des_dim)
            print("[INFO] get_policy() completed successfully")
            sys.stdout.flush()
        else:
            raise NotImplementedError(f'model type {args_cli.model} not implemented')
    except Exception as e:
        print(f"[ERROR] Failed to load model: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise

    print('policy architecture:\n', policy)
    sys.stdout.flush()

    print("[INFO] Setting up criterion and optimizer...")
    sys.stdout.flush()
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.AdamW(
        policy.parameters(),
        lr=args_cli.lr,
        weight_decay=1e-5,
    )
    print("[INFO] Optimizer created successfully")
    sys.stdout.flush()

    # We need to get the actual iteration length by checking the dataloader, but note that the length varies
    # for different training hyper-params. Be careful when fine-tuning models.
    print("[INFO] Creating train dataloader for scheduler setup...")
    sys.stdout.flush()
    try:
        train_dataloader = train_dataset.get_data_loader(
            batch_size=args_cli.batch_size, shuffle=True, num_workers=args_cli.num_workers
        )
        print(f"[INFO] Train dataloader created, length={len(train_dataloader)}")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] Failed to create train dataloader: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer,
                                                           T_max=args_cli.num_epochs*len(train_dataloader))
    print("[INFO] Scheduler created successfully")
    sys.stdout.flush()

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
    print(f"[INFO] About to start training from epoch {start_epoch}...")
    sys.stdout.flush()
    try:
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
        print("[INFO] Training function returned successfully")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] Training failed with exception: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise


@hydra.main(config_path="conf", config_name="config", version_base=None)
def hydra_main(cfg: DictConfig):
    """Hydra entry point for launching with hydra-submitit.
    
    Extracts argparse arguments from cfg.argparse and calls main().
    """
    # If HYDRA_SPOOF is set, we're in a submitit-unpickled process where sys.path
    # is wrong. Re-launch ourselves as a fresh subprocess from the correct directory.
    spoof_dir = os.environ.pop("HYDRA_SPOOF", None)
    if spoof_dir:
        import subprocess
        from hydra.core.hydra_config import HydraConfig

        hc = HydraConfig.get()
        overrides = list(hc.overrides.task)
        config_name = hc.job.config_name

        activate = os.path.normpath(os.path.join(spoof_dir, "..", "env_isaaclab", "bin", "activate"))
        script = os.path.join("distillation", "run_distillation.py")
        cmd_parts = ["python", script, "--config-name", config_name] + overrides
        bash_cmd = f"source {shlex.quote(activate)} && cd {shlex.quote(spoof_dir)} && {shlex.join(cmd_parts)}"

        print(f"[INFO] HYDRA_SPOOF active, re-launching from {spoof_dir}")
        print(f"[INFO] bash -c {bash_cmd}")
        sys.stdout.flush()

        result = subprocess.run(["bash", "-c", bash_cmd], cwd=spoof_dir)
        sys.exit(result.returncode)

    sys.argv = [sys.argv[0]] + shlex.split(cfg.argparse + " " + cfg.append_argparse)
    try:
        print("[INFO] hydra_main: Calling main()...")
        sys.stdout.flush()
        main()
        print("[INFO] hydra_main: main() completed successfully")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] hydra_main: main() raised exception: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise


if __name__ == "__main__":
    print("[INFO] Script starting, calling hydra_main...")
    sys.stdout.flush()
    try:
        hydra_main()
    except Exception as e:
        print(f"[ERROR] Top-level exception: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise


"""
# debugging
ln -s /home/mila/c/charlie.gauthier/embodiment-scaling-laws/ /tmp
python3 distillation/run_distillation.py  --config-name  all_robot_jobs_v7_allrobots_1.0.yaml append_argparse="--max_files_in_memory 256"


python3 distillation/run_distillation.py  --config-name  all_robot_jobs_v7_allrobots_1.0.yaml --multirun hydra/launcher=sbatch +hydra/sweep=sbatch hydra.launcher._target_=hydra_plugins.packed_launcher.packedlauncher.SlurmLauncher hydra.launcher.tasks_per_node=1 +hydra.launcher.timeout_min=7000 hydra.launcher.gres=gpu:l40s:1 +hydra.launcher.constraint='40gb|48gb'  hydra.launcher.cpus_per_task=6 hydra.launcher.mem_gb=128 hydra.launcher.array_parallelism=300 hydra.launcher.partition=long 
python3 distillation/run_distillation.py  --config-name  all_robot_jobs_v7_allrobots_1.0.yaml --multirun hydra/launcher=sbatch +hydra/sweep=sbatch hydra.launcher._target_=hydra_plugins.packed_launcher.packedlauncher.SlurmLauncher hydra.launcher.tasks_per_node=1 +hydra.launcher.timeout_min=7000 hydra.launcher.gres=gpu:l40s:1 +hydra.launcher.constraint='40gb|48gb'  hydra.launcher.cpus_per_task=6 hydra.launcher.mem_gb=48 hydra.launcher.array_parallelism=300 hydra.launcher.partition=main append_argparse="--max_files_in_memory 256"
python3 distillation/run_distillation.py  --config-name  all_robot_jobs_v7_allrobots_1.0.yaml --multirun hydra/launcher=firsbatch +hydra/sweep=sbatch hydra.launcher._target_=hydra_plugins.packed_launcher.packedlauncher.SlurmLauncher hydra.launcher.tasks_per_node=1 +hydra.launcher.timeout_min=4319   hydra.launcher.cpus_per_task=6 hydra.launcher.mem_gb=128 hydra.launcher.array_parallelism=300

"""