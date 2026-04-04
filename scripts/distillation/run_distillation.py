import torch
import numpy as np
from torch.cuda.amp import GradScaler, autocast
import random
import gc
import sys, os
import shlex

import wandb
from omegaconf import DictConfig, OmegaConf
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # for urma_model
sys.path.append("/home/cgauthie/projects/def-lpaull/cgauthie/embodiment-scaling-laws/scripts")
try:
    if os.path.exists("/home/cgauthie/projects/def-lpaull/cgauthie/embodiment-scaling-laws/scripts"):
        os.chdir("/home/cgauthie/projects/def-lpaull/cgauthie/embodiment-scaling-laws/scripts")
except Exception as e:
    print(f"[WARNING] Failed to change directory: {e}")
from utility_functions import (get_most_recent_h5py_record_path, save_checkpoint, AverageMeter,
                   compute_gradient_norm, get_process_ram_usage, get_system_ram_usage)
from dataset_functions import LocomotionDataset
import tqdm
from urma_model.policy_3head_scale2 import get_policy
print("Loaded URMA initially without error")

class CudaPrefetcher:
    """Prefetch batches to GPU using a separate CUDA stream.

    Overlaps CPU→GPU data transfer with the previous iteration's compute,
    hiding transfer latency behind forward/backward passes.
    """

    def __init__(self, loader, device):
        self.loader = loader
        self.device = device
        self.stream = torch.cuda.Stream(device=device)
        self._iter = None
        self._next_batch = None
        self._exhausted = False

    def __iter__(self):
        self._iter = iter(self.loader)
        self._exhausted = False
        self._prefetch()
        return self

    def _prefetch(self):
        try:
            batch = next(self._iter)
            with torch.cuda.stream(self.stream):
                batch_inputs, batch_targets, data_source_name, io_times, processing_times = batch
                batch_inputs = tuple(x.to(self.device, non_blocking=True) for x in batch_inputs)
                batch_targets = batch_targets.to(self.device, non_blocking=True)
                self._next_batch = (batch_inputs, batch_targets, data_source_name, io_times, processing_times)
        except StopIteration:
            self._next_batch = None
            self._exhausted = True

    def __next__(self):
        if self._exhausted:
            raise StopIteration
        # Wait for the prefetch transfer to complete before consuming the batch
        torch.cuda.current_stream(self.device).wait_stream(self.stream)
        batch = self._next_batch
        if batch is None:
            raise StopIteration
        self._prefetch()  # start loading next batch while GPU processes current
        return batch

    def __len__(self):
        return len(self.loader)


def set_seed(seed):
    random.seed(seed)  # Set Python's random seed
    np.random.seed(seed)  # Set NumPy's random seed
    torch.manual_seed(seed)  # Set PyTorch's CPU seed
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)  # Set PyTorch's GPU seed (if using CUDA)
        torch.cuda.manual_seed_all(seed)  # Set the seed for all GPUs (if using multiple GPUs)
        torch.backends.cudnn.deterministic = True  # Ensure deterministic behavior
        torch.backends.cudnn.benchmark = True  # Disable optimizations for reproducibility


def get_meter_dict_avg(meter_dicts):
    active = [meter.avg for meter in meter_dicts.values() if meter.count > 0]
    if len(active) == 0:
        return None
    return sum(active) / len(active)



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
          log_dir, checkpoint_interval, gradient_acc_steps, batch_size, num_workers, use_amp, start_epoch,
          log_epoch_pct=10.0):
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

        _dl_create_start = time.time()
        train_dataloader = train_dataset.get_data_loader(
            batch_size=batch_size, shuffle=True, num_workers=num_workers
        )
        print(f"[TIMING] DataLoader creation took {time.time() - _dl_create_start:.1f}s", flush=True)

        prefetcher = CudaPrefetcher(train_dataloader, model_device)
        with tqdm.tqdm(prefetcher, total=len(train_dataloader), desc=f"Training Epoch {epoch + 1}/{num_epochs}", unit="batch") as pbar:
            train_phase_start_time = time.time()
            iteration_start_time = time.time()
            _batch_fetch_start = time.time()
            next_log_pct = log_epoch_pct
            for index, (batch_inputs, batch_targets, data_source_name, io_times, processing_times) in enumerate(pbar):
                _batch_fetch_time = time.time() - _batch_fetch_start
                if _batch_fetch_time > 10.0:
                    print(f"[STALL] Batch {index} took {_batch_fetch_time:.1f}s to fetch from dataloader", flush=True)
                iteration = index + epoch * len(train_dataloader)
                dataloader_time = time.time() - iteration_start_time

                # Data already on GPU via CudaPrefetcher (non-blocking H2D overlap)
                move_cuda_time = 0.0

                start_time = time.time()
                with torch.autocast(device_type='cuda', dtype=torch.float16, enabled=use_amp):
                    batch_predictions = policy(*batch_inputs)

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
                current_pct = 100.0 * (index + 1) / len(train_dataloader)
                if current_pct >= next_log_pct or index == 0:
                    next_log_pct = current_pct - (current_pct % log_epoch_pct) + log_epoch_pct
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
                        "epoch_progress": epoch + (index + 1) / len(train_dataloader),
                    }
                    if grad_norm is not None:
                        log_dict["Train/grad_norm-iter"] = grad_norm
                    wandb.log(log_dict)
                    train_bps = (index + 1) / (time.time() - train_phase_start_time)
                    print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - Train: {current_pct:.1f}% ({index+1}/{len(train_dataloader)}) | Loss: {loss.item():.4f} | {train_bps:.2f} batch/s")

                # Step the LR scheduler by iteration
                if scheduler is not None:
                    scheduler.step()

                iteration_start_time = time.time()  # start time of next iteration
                _batch_fetch_start = time.time()

        # Collect training metrics (logged together with val/test at end of epoch)
        epoch_log_dict = {f"Train-Per-Robot/{robot_name}": meter.avg for robot_name, meter in train_loss_meters.items()}
        epoch_log_dict["Train/epoch-loss/avg"] = get_meter_dict_avg(train_loss_meters)
        epoch_log_dict["Train/lr"] = optimizer.param_groups[0]['lr']
        epoch_log_dict["epoch"] = epoch + 1
        train_total_bps = len(train_dataloader) / (time.time() - train_phase_start_time)

        _del_start = time.time()
        del train_dataloader
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
            val_prefetcher = CudaPrefetcher(val_dataloader, model_device)
            with tqdm.tqdm(val_prefetcher, total=len(val_dataloader), desc=f"Validation Epoch {epoch + 1}/{num_epochs}", unit="batch") as pbar:
                for index, (batch_inputs, batch_targets, data_source_name, _, _) in enumerate(pbar):

                    batch_predictions = policy(*batch_inputs)

                    loss = criterion(batch_predictions, batch_targets)

                    # Update validation loss tracker
                    if data_source_name not in val_loss_meters:
                        val_loss_meters[data_source_name] = AverageMeter()
                    val_loss_meters[data_source_name].update(loss.item(), n=batch_targets.size(0))

                    # Update progress bar with current loss
                    pbar.set_postfix(
                        {"Loss": f"{get_meter_dict_avg(val_loss_meters) or 0:.4f}"})

                    if index > 0.03 * len(val_dataloader):
                        break

        # Collect validation metrics (skip robots not seen in this epoch's sample)
        val_log_dict = {f"Val-Per-Robot/{robot_name}": meter.avg for robot_name, meter in val_loss_meters.items() if meter.count > 0}
        val_avg = get_meter_dict_avg(val_loss_meters)
        if val_avg is not None:
            val_log_dict["Val/epoch-loss/avg"] = val_avg
        epoch_log_dict.update(val_log_dict)
        val_total_bps = (index + 1) / (time.time() - val_phase_start_time)
        print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - Val complete | Avg Loss: {val_avg if val_avg is not None else 'N/A'} | {val_total_bps:.2f} batch/s")

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
                test_prefetcher = CudaPrefetcher(test_dataloader, model_device)
                with tqdm.tqdm(test_prefetcher, total=len(test_dataloader), desc=f"Test Epoch {epoch + 1}/{num_epochs}", unit="batch") as pbar:
                    for index, (batch_inputs, batch_targets, data_source_name, _, _) in enumerate(pbar):

                        batch_predictions = policy(*batch_inputs)

                        loss = criterion(batch_predictions, batch_targets)

                        # Update validation loss tracker
                        if data_source_name not in test_loss_meters:
                            test_loss_meters[data_source_name] = AverageMeter()
                        test_loss_meters[data_source_name].update(loss.item(), n=batch_targets.size(0))

                        # Update progress bar with current loss
                        pbar.set_postfix(
                            {"Loss": f"{get_meter_dict_avg(test_loss_meters) or 0:.4f}"})

                        if index > 0.03 * len(test_dataloader):
                            break

            # Collect test metrics (skip robots not seen in this epoch's sample)
            test_log_dict = {f"Test-Per-Robot/{robot_name}": meter.avg for robot_name, meter in test_loss_meters.items() if meter.count > 0}
            test_avg = get_meter_dict_avg(test_loss_meters)
            if test_avg is not None:
                test_log_dict["Test/epoch-loss/avg"] = test_avg
            epoch_log_dict.update(test_log_dict)
            test_total_bps = (index + 1) / (time.time() - test_phase_start_time)
            print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - Test complete | Avg Loss: {test_avg if test_avg is not None else 'N/A'} | {test_total_bps:.2f} batch/s")

            del test_dataloader

        # Log all metrics for this epoch in a single wandb.log call
        wandb.log(epoch_log_dict)

        # Save checkpoints periodically
        if (epoch + 1) % checkpoint_interval == 0:
            save_checkpoint(policy, optimizer, epoch + 1, log_dir)

        # Save the best model based on validation loss
        if val_avg is not None and val_avg < best_val_loss:
            best_val_loss = val_avg
            save_checkpoint(policy, optimizer, epoch + 1, log_dir, is_best=True)

        test_avg_display = get_meter_dict_avg(test_loss_meters)
        print(f"Epoch [{epoch + 1}/{num_epochs}], Train Loss: {get_meter_dict_avg(train_loss_meters):.6f}, "
              f"Val Loss: {val_avg if val_avg is not None else 'N/A'}, Best Val Loss: {best_val_loss:.6f}, "
              f"Test Loss: {test_avg_display if test_avg_display is not None else 'N/A'}")

    if wandb.run is not None:
        wandb.finish()
    print("[INFO] Training completed. Wandb logs saved.")


def main(cfg: DictConfig):
    # Pretty print config
    print("\n" + "="*50)
    print("Configuration:")
    print("="*50)
    print(OmegaConf.to_yaml(cfg, resolve=True))
    print("="*50 + "\n")

    # Set seed
    seed = cfg.meta.seed
    if seed >= 0:
        set_seed(seed)

    # Initialize wandb
    wandb_mode = cfg.meta.wandb_mode
    if wandb_mode != "disabled":
        wandb.init(
            project=cfg.meta.project,
            name=cfg.meta.run_name,
            config=OmegaConf.to_container(cfg, resolve=True),
            mode=wandb_mode,
            tags=list(cfg.meta.tags) if cfg.meta.tags else None,
            notes=cfg.meta.notes or None,
        )
        print(f"[INFO] Wandb initialized (mode={wandb_mode})")

    # Use wandb's run directory for logging, fall back to cwd/log_dir
    log_dir = os.path.join(os.getcwd(), "log_dir")
    os.makedirs(log_dir, exist_ok=True)

    # Save config to a YAML file for reproducibility
    config_save_path = os.path.join(log_dir, "config.yaml")
    OmegaConf.save(cfg, config_save_path)
    print(f"[INFO] Config saved to {config_save_path}")

    # Debug: Check dataset directory contents
    import subprocess
    dataset_dir = cfg.dataloading.dataset_dir
    print(f"[INFO] Checking dataset directory: {dataset_dir}")
    sys.stdout.flush()
    try:
        result = subprocess.run(['ls', dataset_dir], capture_output=True, text=True, timeout=30)
        lines = result.stdout.strip().split('\n')
        print(f"[INFO] ls {dataset_dir} (first 10 lines of {len(lines)} total):")
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
    train_set = list(cfg.train_set)
    test_set = list(cfg.test_set) if cfg.test_set else []
    assert len(train_set) > 0, "Please specify train_set"
    train_set_paths = [get_most_recent_h5py_record_path(dataset_dir, task) for task in train_set]
    if test_set:
        test_set_paths = [get_most_recent_h5py_record_path(dataset_dir, task) for task in test_set]
    else:
        test_set_paths = list()
        print(f'[INFO] No test set provided.')

    # Expand environment variables in asset_base_path (e.g., $SCRATCH)
    asset_base_path = os.path.expandvars(cfg.ablation.asset_base_path)
    description_filename = cfg.ablation.description_filename

    # Training dataset
    train_dataset = LocomotionDataset(
        folder_paths=train_set_paths,
        train_mode=True,
        val_ratio=cfg.dataloading.val_ratio,
        max_files_in_memory=cfg.dataloading.max_files_in_memory,
        h5_repeat_factor=cfg.dataloading.h5_repeat_factor,
        max_parallel_envs_per_file=cfg.dataloading.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=cfg.dataloading.max_envs_per_file_in_memory,
        description_filename=description_filename,
        asset_base_path=asset_base_path
    )

    # Validation dataset
    val_dataset = LocomotionDataset(
        folder_paths=train_set_paths,
        train_mode=False,
        val_ratio=cfg.dataloading.val_ratio,
        max_files_in_memory=cfg.dataloading.max_files_in_memory,
        h5_repeat_factor=1,
        max_parallel_envs_per_file=cfg.dataloading.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=cfg.dataloading.max_envs_per_file_in_memory,
        description_filename=description_filename,
        asset_base_path=asset_base_path
    )

    # Test dataset
    test_dataset = LocomotionDataset(
        folder_paths=test_set_paths,
        train_mode=False,
        val_ratio=cfg.dataloading.val_ratio,
        max_files_in_memory=cfg.dataloading.max_files_in_memory,
        h5_repeat_factor=1,
        max_parallel_envs_per_file=cfg.dataloading.max_parallel_envs_per_file,
        max_envs_per_file_in_memory=cfg.dataloading.max_envs_per_file_in_memory,
        description_filename=description_filename,
        asset_base_path=asset_base_path
    )

    model_device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"[INFO] Using device: {model_device}")

    # Determine dynamic joint description dimension via auto-detection
    if train_dataset.use_limb_bboxes:
        dynamic_joint_des_dim = 18 + train_dataset.extra_des_dim
        print(f"[INFO] Limb bboxes detected, dynamic_joint_des_dim={dynamic_joint_des_dim} (18 base + {train_dataset.extra_des_dim} extra)")
    else:
        dynamic_joint_des_dim = 18
        print("[INFO] No limb bboxes in description file, using baseline dynamic_joint_des_dim=18")

    # Define model, optimizer, and loss
    print("[INFO] Loading URMA model...")
    sys.stdout.flush()
    try:
        from urma_model.policy_3head_scale2 import get_policy
        policy = get_policy(model_device, dynamic_joint_des_dim=dynamic_joint_des_dim)
        print("[INFO] get_policy() completed successfully")
        sys.stdout.flush()
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
        lr=cfg.optim.lr,
        weight_decay=1e-5,
    )
    print("[INFO] Optimizer created successfully")
    sys.stdout.flush()

    # Create dataloader to measure iteration count for scheduler
    print("[INFO] Creating train dataloader for scheduler setup...")
    sys.stdout.flush()
    try:
        train_dataloader = train_dataset.get_data_loader(
            batch_size=cfg.dataloading.batch_size, shuffle=True, num_workers=cfg.dataloading.num_workers
        )
        print(f"[INFO] Train dataloader created, length={len(train_dataloader)}")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] Failed to create train dataloader: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise
    total_iterations = cfg.optim.num_epochs * len(train_dataloader)
    if cfg.optim.warmup_pct > 0:
        warmup_iters = max(1, int(cfg.optim.warmup_pct * total_iterations))
        warmup_scheduler = torch.optim.lr_scheduler.LinearLR(
            optimizer, start_factor=1e-2, end_factor=1.0, total_iters=warmup_iters
        )
        cosine_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=total_iterations - warmup_iters
        )
        scheduler = torch.optim.lr_scheduler.SequentialLR(
            optimizer, schedulers=[warmup_scheduler, cosine_scheduler], milestones=[warmup_iters]
        )
        print(f"[INFO] Scheduler created with linear warmup ({warmup_iters} iters, {cfg.optim.warmup_pct*100:.1f}%) + cosine annealing")
    else:
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=total_iterations)
        print("[INFO] Scheduler created with cosine annealing (no warmup)")
    sys.stdout.flush()

    # Load checkpoint if path specified
    if cfg.resume:
        checkpoint = torch.load(cfg.resume, map_location="cpu")
        policy.load_state_dict(checkpoint["state_dict"])
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        start_epoch = checkpoint["epoch"]
        print(f"[INFO] Loaded checkpoint from {cfg.resume}, resuming from epoch {start_epoch}")
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
            num_epochs=cfg.optim.num_epochs,
            model_device=model_device,
            log_dir=log_dir,
            checkpoint_interval=cfg.optim.checkpoint_interval,
            gradient_acc_steps=cfg.optim.gradient_acc_steps,
            batch_size=cfg.dataloading.batch_size,
            num_workers=cfg.dataloading.num_workers,
            use_amp=bool(cfg.optim.use_amp),
            start_epoch=start_epoch,
            log_epoch_pct=cfg.optim.log_epoch_pct
        )
        print("[INFO] Training function returned successfully")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] Training failed with exception: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise


if __name__ == "__main__":
    # When run directly (e.g. from HYDRA_SPOOF re-launch), delegate to the
    # lightweight launcher that doesn't import torch at module level.
    print("[INFO] run_distillation.py invoked directly, delegating to launch_distillation.hydra_main...")
    sys.stdout.flush()
    from launch_distillation import hydra_main
    hydra_main()
