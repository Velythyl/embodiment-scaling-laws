import torch
import numpy as np
from torch.cuda.amp import GradScaler, autocast
import random
import gc
import sys, os
import shlex
import signal
import threading
import subprocess

import wandb
from omegaconf import DictConfig, OmegaConf
import time
import yaml
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


LATEST_CHECKPOINT_NAME = "latest_checkpoint.pt"
RESUME_STATE_NAME = "resume_state.yaml"

# Global preemption state - set by signal handler, checked by training loop
_preemption_requested = threading.Event()

# Global background rsync process - started early to overlap data sync with training
_background_rsync_process = None


def _start_background_rsync(source_dir: str, target_dir: str) -> "subprocess.Popen | None":
    """Start a background rsync process to copy training data from SCRATCH to local storage.
    
    This allows training to start immediately using fallback (SCRATCH) while the data
    is being copied to fast local storage. As files complete, subsequent loads will
    find them locally.
    
    Args:
        source_dir: Source directory (e.g., $SCRATCH/embodiment-scaling-laws/logs/rsl_rl)
        target_dir: Target directory (e.g., $SLURM_TMPDIR/embodiment-scaling-laws/logs/rsl_rl)
    
    Returns:
        subprocess.Popen: The background rsync process (or None if skipped)
    """
    global _background_rsync_process
    
    # Check if source and target directories are valid
    source_dir = os.path.expandvars(source_dir)
    target_dir = os.path.expandvars(target_dir)
    
    if not os.path.isdir(source_dir):
        print(f"[WARN] Background rsync: source directory does not exist: {source_dir}")
        return None
    
    if not os.path.isdir(target_dir):
        print(f"[INFO] Background rsync: creating target directory: {target_dir}")
        os.makedirs(target_dir, exist_ok=True)
    
    # Build the rsync command - same as was in firsbatch.yaml but runs in background
    # Uses find + xargs for parallel directory-level rsync (P64 = 64 parallel rsyncs)
    cmd = (
        f'find "{source_dir}" -mindepth 1 -maxdepth 1 -print0 | '
        f'xargs -0 -P64 -I% rsync --quiet -Pa % "{target_dir}"'
    )
    
    print(f"[INFO] Starting background rsync from {source_dir} to {target_dir}")
    print(f"[INFO] Training will use fallback ($SCRATCH) until local copies are ready")
    sys.stdout.flush()
    
    # Start the process in background - use shell=True for pipes
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        start_new_session=True,  # Detach from parent process group
    )
    _background_rsync_process = process
    
    # Start a thread to monitor completion and log any errors
    def _monitor_rsync():
        try:
            _, stderr = process.communicate()
            if process.returncode == 0:
                print(f"[INFO] Background rsync completed successfully")
            else:
                print(f"[WARN] Background rsync exited with code {process.returncode}")
                if stderr:
                    print(f"[WARN] rsync stderr: {stderr.decode('utf-8', errors='replace')}")
        except Exception as e:
            print(f"[WARN] Background rsync monitor error: {e}")
        sys.stdout.flush()
    
    monitor_thread = threading.Thread(target=_monitor_rsync, daemon=True)
    monitor_thread.start()
    
    return process


class PreemptionHandler:
    """Handle SLURM preemption signals (SIGTERM) by saving checkpoint and requeueing.
    
    On clusters with preemption, SLURM sends SIGTERM before SIGKILL. This handler:
    1. Sets a flag that the training loop checks
    2. The training loop saves checkpoint and requeues when it sees the flag
    
    We use a flag + check pattern (not direct save in handler) because:
    - Signal handlers should be quick and avoid I/O
    - We need access to training state (model, optimizer, etc.)
    """
    
    def __init__(self):
        self.original_sigterm = None
        self.enabled = False
    
    def install(self):
        """Install the SIGTERM handler."""
        if self.enabled:
            return
        self.original_sigterm = signal.signal(signal.SIGTERM, self._handle_sigterm)
        self.enabled = True
        print("[INFO] Preemption handler installed (SIGTERM)")
    
    def uninstall(self):
        """Restore original signal handler."""
        if not self.enabled:
            return
        if self.original_sigterm is not None:
            signal.signal(signal.SIGTERM, self.original_sigterm)
        self.enabled = False
        print("[INFO] Preemption handler uninstalled")
    
    def _handle_sigterm(self, signum, frame):
        """Signal handler - just sets the flag, actual work done in training loop."""
        print(f"\n[PREEMPT] Received SIGTERM (signal {signum}) - requesting graceful shutdown", flush=True)
        _preemption_requested.set()
        # Don't exit - let training loop handle checkpoint and requeue


def _is_preemption_requested():
    """Check if preemption was requested (SIGTERM received)."""
    return _preemption_requested.is_set()


def _get_hydra_output_dir(cfg=None):
    """Get the Hydra output directory, with multiple fallback strategies.
    
    Priority (for multirun/SLURM jobs):
    1. HYDRA_SWEEP_DIR env var + SLURM_ARRAY_TASK_ID (most reliable on requeue)
    2. cfg.meta.SLURM_HYDRA_DIR parent (uses resolved config values)
    3. HydraConfig.get().runtime.output_dir (standard Hydra way - but wrong after HYDRA_SPOOF)
    4. None (caller should handle fallback)
    """
    # For SLURM multirun jobs: use env vars directly (survives requeue + HYDRA_SPOOF)
    sweep_dir = os.environ.get("HYDRA_SWEEP_DIR")
    task_id = os.environ.get("SLURM_ARRAY_TASK_ID")
    if sweep_dir and task_id:
        log_dir = os.path.join(sweep_dir, task_id)
        print(f"[INFO] Using HYDRA_SWEEP_DIR + SLURM_ARRAY_TASK_ID: {log_dir}")
        return log_dir
    
    # Fallback: use SLURM_HYDRA_DIR from config (parent of .hydra folder)
    if cfg is not None:
        slurm_hydra_dir = getattr(cfg.meta, "SLURM_HYDRA_DIR", None)
        if slurm_hydra_dir and slurm_hydra_dir != "null" and os.path.basename(slurm_hydra_dir) == ".hydra":
            parent = os.path.dirname(slurm_hydra_dir)
            if parent:
                print(f"[INFO] Using SLURM_HYDRA_DIR parent as log_dir: {parent}")
                return parent
    
    # Standard Hydra method (works for non-SLURM runs, but NOT after HYDRA_SPOOF relaunch)
    try:
        from hydra.core.hydra_config import HydraConfig
        hydra_dir = HydraConfig.get().runtime.output_dir
        if hydra_dir:
            print(f"[INFO] Using HydraConfig.runtime.output_dir: {hydra_dir}")
            return hydra_dir
    except Exception:
        pass
    
    return None


def _load_resume_state(log_dir):
    resume_state_path = os.path.join(log_dir, RESUME_STATE_NAME)
    if not os.path.exists(resume_state_path):
        return {}

    with open(resume_state_path, "r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle) or {}
    if not isinstance(loaded, dict):
        raise ValueError(f"Invalid resume state in {resume_state_path}: expected a mapping")
    return loaded


def _save_resume_state(log_dir, resume_state):
    resume_state_path = os.path.join(log_dir, RESUME_STATE_NAME)
    with open(resume_state_path, "w", encoding="utf-8") as handle:
        yaml.safe_dump(resume_state, handle, sort_keys=True)
    print(f"[INFO] Resume state saved to {resume_state_path}")


def _resolve_resume_checkpoint(config_resume_path, log_dir, resume_state):
    if config_resume_path:
        return config_resume_path

    candidates = [
        resume_state.get("latest_checkpoint"),
        os.path.join(log_dir, LATEST_CHECKPOINT_NAME),
    ]
    for candidate in candidates:
        if candidate and os.path.exists(candidate):
            return candidate
    return None


def _choose_runtime_seed(configured_seed):
    if configured_seed is not None and int(configured_seed) >= 0:
        return int(configured_seed)
    return int.from_bytes(os.urandom(8), byteorder="big", signed=False) % (2**31 - 1)


def _should_stop_for_walltime(walltime_deadline):
    """Check if we've reached the walltime deadline.
    
    Args:
        walltime_deadline: time.monotonic() value when we should stop, or None if disabled.
    """
    if walltime_deadline is None:
        return False
    return time.monotonic() >= walltime_deadline


def _check_stop_reason(walltime_deadline):
    """Check if we should stop for preemption or walltime.
    
    Returns:
        str or None: 'preemption' if SIGTERM received, 'walltime' if deadline reached, None otherwise.
    """
    if _is_preemption_requested():
        return "preemption"
    if _should_stop_for_walltime(walltime_deadline):
        return "walltime"
    return None


def _requeue_current_slurm_job():
    job_id = os.environ.get("SLURM_JOB_ID")
    if not job_id:
        print("[WARN] Not running under SLURM; skipping requeue")
        return False

    import subprocess

    result = subprocess.run(["scontrol", "requeue", job_id], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ERROR] Failed to requeue SLURM job {job_id}: {result.stderr.strip()}")
        return False

    print(f"[INFO] Requeued SLURM job {job_id}")
    return True


def _parse_slurm_time(t):
    """Parse SLURM time format (D-HH:MM:SS or HH:MM:SS or MM:SS) to seconds."""
    if t == "UNLIMITED" or t == "INVALID":
        return None
    try:
        days = 0
        if "-" in t:
            days_str, t = t.split("-", 1)
            days = int(days_str)
        parts = t.split(":")
        if len(parts) == 3:
            h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
        elif len(parts) == 2:
            h, m, s = 0, int(parts[0]), int(parts[1])
        else:
            return None
        return days * 86400 + h * 3600 + m * 60 + s
    except (ValueError, AttributeError):
        return None


def _get_slurm_deadline(buffer_minutes=10):
    """Query SLURM once to get the deadline (monotonic time) when we should stop.
    
    Args:
        buffer_minutes: Stop this many minutes before the actual time limit.
    
    Returns:
        float or None: time.monotonic() value when we should stop, or None if not in SLURM.
    """
    job_id = os.environ.get("SLURM_JOB_ID")
    if not job_id:
        print("[INFO] Not running under SLURM; walltime budget disabled")
        return None
    
    import subprocess
    
    # Query job time limit (%l) and elapsed time (%M)
    result = subprocess.run(
        ["squeue", "-j", job_id, "-h", "-o", "%l %M"],
        capture_output=True, text=True, timeout=30
    )
    
    if result.returncode != 0:
        print(f"[WARN] Failed to query SLURM job {job_id}: {result.stderr.strip()}")
        return None
    
    parts = result.stdout.strip().split()
    if len(parts) < 2:
        print(f"[WARN] Unexpected squeue output: {result.stdout.strip()}")
        return None
    
    time_limit_str, elapsed_str = parts[0], parts[1]
    time_limit = _parse_slurm_time(time_limit_str)
    elapsed = _parse_slurm_time(elapsed_str)
    
    if time_limit is None:
        print(f"[INFO] SLURM time limit is {time_limit_str}; walltime budget disabled")
        return None
    
    if elapsed is None:
        print(f"[WARN] Could not parse SLURM elapsed time: {elapsed_str}")
        elapsed = 0
    
    remaining = time_limit - elapsed
    budget = remaining - buffer_minutes * 60
    
    if budget <= 0:
        print(f"[WARN] SLURM time budget already exhausted (remaining={remaining/60:.1f}min, buffer={buffer_minutes}min)")
        return time.monotonic()  # Stop immediately
    
    deadline = time.monotonic() + budget
    print(f"[INFO] SLURM walltime: limit={time_limit/60:.0f}min, elapsed={elapsed/60:.1f}min, "
          f"remaining={remaining/60:.1f}min → will stop in {budget/60:.1f}min (buffer={buffer_minutes}min)")
    
    return deadline


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


def _checkpoint_metadata(best_val_loss, runtime_seed, checkpoint_reason, epoch_index, batch_index=None, last_iteration=None):
    return {
        "best_val_loss": None if best_val_loss == float("inf") else float(best_val_loss),
        "runtime_seed": int(runtime_seed),
        "checkpoint_reason": checkpoint_reason,
        "epoch_index": int(epoch_index),
        "batch_index": None if batch_index is None else int(batch_index),
        "last_iteration": None if last_iteration is None else int(last_iteration),
        "saved_at_unix": time.time(),
    }


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


def _run_eval(policy, criterion, dataloader, model_device, loss_meters, phase_name, epoch, num_epochs, sample_pct=0.03):
    """Run a validation or test evaluation pass, sampling sample_pct of the dataloader."""
    policy.eval()
    for meter in loss_meters.values():
        meter.reset()

    with torch.no_grad():
        phase_start_time = time.time()
        prefetcher = CudaPrefetcher(dataloader, model_device)
        max_batches = max(1, int(sample_pct * len(dataloader)))
        with tqdm.tqdm(prefetcher, total=len(dataloader), desc=f"{phase_name} Epoch {epoch + 1}/{num_epochs}", unit="batch") as pbar:
            for index, (batch_inputs, batch_targets, data_source_name, _, _) in enumerate(pbar):
                batch_predictions = policy(*batch_inputs)
                loss = criterion(batch_predictions, batch_targets)

                if data_source_name not in loss_meters:
                    loss_meters[data_source_name] = AverageMeter()
                loss_meters[data_source_name].update(loss.item(), n=batch_targets.size(0))

                pbar.set_postfix({"Loss": f"{get_meter_dict_avg(loss_meters) or 0:.4f}"})

                if index >= max_batches:
                    break

        avg_loss = get_meter_dict_avg(loss_meters)
        bps = (index + 1) / (time.time() - phase_start_time) if index >= 0 else 0
        print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - {phase_name} complete | Avg Loss: {avg_loss if avg_loss is not None else 'N/A'} | {bps:.2f} batch/s")

    return avg_loss


def train(policy, criterion, optimizer, scheduler, train_dataset, val_dataset, test_dataset, num_epochs, model_device,
          log_dir, checkpoint_interval, gradient_acc_steps, batch_size, num_workers, use_amp, start_epoch,
          log_epoch_pct=10.0, eval_epoch_pct=None, scaler=None, walltime_deadline=None,
          initial_best_val_loss=float("inf"), runtime_seed=0, resume_from_iteration=0):
    """Training loop with validation, TensorBoard logging, and checkpoint saving.
    
    Args:
        walltime_deadline: time.monotonic() value when we should stop for walltime, or None if disabled.
        resume_from_iteration: Skip wandb logging until we reach this iteration.
            Used to avoid duplicate data points when resuming mid-epoch.
    """
    scaler = scaler or torch.cuda.amp.GradScaler(enabled=use_amp)

    train_loss_meters = {}
    val_loss_meters = {}
    test_loss_meters = {}
    best_val_loss = initial_best_val_loss
    last_logged_iteration = resume_from_iteration  # Track for checkpoint metadata

    def _save_training_checkpoint(next_epoch, checkpoint_reason, is_best=False, batch_index=None, update_latest=True, iteration=None):
        nonlocal last_logged_iteration
        metadata = _checkpoint_metadata(
            best_val_loss=best_val_loss,
            runtime_seed=runtime_seed,
            checkpoint_reason=checkpoint_reason,
            epoch_index=epoch,
            batch_index=batch_index,
            last_iteration=iteration if iteration is not None else last_logged_iteration,
        )
        return save_checkpoint(
            policy,
            optimizer,
            next_epoch,
            log_dir,
            is_best=is_best,
            scheduler=scheduler,
            scaler=scaler,
            metadata=metadata,
            update_latest=update_latest,
        )

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

        # Create val/test dataloaders once per epoch for mid-epoch evaluation
        if eval_epoch_pct is not None and eval_epoch_pct > 0:
            val_dataloader = val_dataset.get_data_loader(
                batch_size=batch_size, shuffle=True, num_workers=num_workers
            )
            test_dataloader = None
            if len(test_dataset) > 0:
                test_dataloader = test_dataset.get_data_loader(
                    batch_size=batch_size, shuffle=True, num_workers=num_workers, prefetch_factor=25
                )
            next_eval_pct = eval_epoch_pct

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
                # BUG: loss is NOT divided by gradient_acc_steps before .backward().
                # When gradient_acc_steps > 1, accumulated gradients are gradient_acc_steps times
                # larger than a single equivalent large batch. This means the effective learning
                # rate is lr * gradient_acc_steps. To fix, use (loss / gradient_acc_steps).backward().
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

                # Log times - skip if we're catching up from a resume to avoid duplicate data points
                current_pct = 100.0 * (index + 1) / len(train_dataloader)
                should_log_this_iteration = iteration >= resume_from_iteration
                if should_log_this_iteration and (current_pct >= next_log_pct or index == 0):
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
                    last_logged_iteration = iteration
                    train_bps = (index + 1) / (time.time() - train_phase_start_time)
                    print(f"[PROGRESS] Epoch {epoch+1}/{num_epochs} - Train: {current_pct:.1f}% ({index+1}/{len(train_dataloader)}) | Loss: {loss.item():.4f} | {train_bps:.2f} batch/s")
                elif not should_log_this_iteration and index == 0:
                    print(f"[INFO] Skipping logging until iteration {resume_from_iteration} (currently at {iteration})")

                # Mid-epoch validation/test evaluation - also skip if catching up
                if should_log_this_iteration and eval_epoch_pct is not None and eval_epoch_pct > 0 and current_pct >= next_eval_pct:
                    next_eval_pct = current_pct - (current_pct % eval_epoch_pct) + eval_epoch_pct
                    epoch_progress = epoch + (index + 1) / len(train_dataloader)
                    print(f"[INFO] Mid-epoch eval at {current_pct:.1f}% of epoch {epoch + 1}")

                    # Validation
                    val_avg = _run_eval(policy, criterion, val_dataloader, model_device,
                                        val_loss_meters, "Validation", epoch, num_epochs)
                    eval_log_dict = {"epoch_progress": epoch_progress}
                    eval_log_dict.update({f"Val-Per-Robot/{rn}": m.avg for rn, m in val_loss_meters.items() if m.count > 0})
                    if val_avg is not None:
                        eval_log_dict["Val/epoch-loss/avg"] = val_avg

                    # Test
                    if test_dataloader is not None:
                        test_avg = _run_eval(policy, criterion, test_dataloader, model_device,
                                             test_loss_meters, "Test", epoch, num_epochs)
                        eval_log_dict.update({f"Test-Per-Robot/{rn}": m.avg for rn, m in test_loss_meters.items() if m.count > 0})
                        if test_avg is not None:
                            eval_log_dict["Test/epoch-loss/avg"] = test_avg

                    wandb.log(eval_log_dict)

                    # Save best model based on mid-epoch val loss
                    if val_avg is not None and val_avg < best_val_loss:
                        best_val_loss = val_avg
                        _save_training_checkpoint(
                            epoch + 1,
                            checkpoint_reason="best_val",
                            is_best=True,
                            update_latest=False,
                        )

                    # Switch back to training mode
                    policy.train()

                # Step the LR scheduler by iteration
                if scheduler is not None:
                    scheduler.step()

                stop_reason = _check_stop_reason(walltime_deadline)
                if stop_reason:
                    optimizer.zero_grad()
                    checkpoint_path = _save_training_checkpoint(
                        next_epoch=epoch,
                        checkpoint_reason=f"{stop_reason}_mid_epoch",
                        batch_index=index + 1,
                        iteration=iteration,
                    )
                    print(
                        f"[INFO] Stop requested ({stop_reason}) during epoch {epoch + 1}; "
                        f"saved {checkpoint_path} and requesting requeue"
                    )
                    return {
                        "status": "requeue_requested",
                        "checkpoint_path": checkpoint_path,
                        "next_epoch": epoch,
                        "stop_reason": stop_reason,
                        "last_iteration": iteration,
                    }

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

        # Clean up mid-epoch eval dataloaders
        if eval_epoch_pct is not None and eval_epoch_pct > 0:
            del val_dataloader
            if test_dataloader is not None:
                del test_dataloader

        # End-of-epoch Validation phase
        val_avg = _run_eval(policy, criterion,
                            val_dataset.get_data_loader(batch_size=batch_size, shuffle=True, num_workers=num_workers),
                            model_device, val_loss_meters, "Validation", epoch, num_epochs)

        val_log_dict = {f"Val-Per-Robot/{robot_name}": meter.avg for robot_name, meter in val_loss_meters.items() if meter.count > 0}
        if val_avg is not None:
            val_log_dict["Val/epoch-loss/avg"] = val_avg
        epoch_log_dict.update(val_log_dict)

        if epoch == 0:
            if val_avg is not None and val_avg < best_val_loss:
                best_val_loss = val_avg
                _save_training_checkpoint(
                    epoch + 1,
                    checkpoint_reason="best_val",
                    is_best=True,
                    update_latest=False,
                )
            if (epoch + 1) % checkpoint_interval == 0:
                _save_training_checkpoint(epoch + 1, checkpoint_reason="periodic_epoch")
            wandb.log(epoch_log_dict)
            stop_reason = _check_stop_reason(walltime_deadline)
            if stop_reason:
                checkpoint_path = _save_training_checkpoint(epoch + 1, checkpoint_reason=f"{stop_reason}_epoch_boundary")
                print(
                    f"[INFO] Stop requested ({stop_reason}) after epoch {epoch + 1}; "
                    f"saved {checkpoint_path} and requesting requeue"
                )
                return {
                    "status": "requeue_requested",
                    "checkpoint_path": checkpoint_path,
                    "next_epoch": epoch + 1,
                    "stop_reason": stop_reason,
                }
            continue

        if len(test_dataset) > 0:
            # Test phase
            test_avg = _run_eval(policy, criterion,
                                 test_dataset.get_data_loader(batch_size=batch_size, shuffle=True, num_workers=num_workers, prefetch_factor=25),
                                 model_device, test_loss_meters, "Test", epoch, num_epochs)

            test_log_dict = {f"Test-Per-Robot/{robot_name}": meter.avg for robot_name, meter in test_loss_meters.items() if meter.count > 0}
            if test_avg is not None:
                test_log_dict["Test/epoch-loss/avg"] = test_avg
            epoch_log_dict.update(test_log_dict)

        # Log all metrics for this epoch in a single wandb.log call
        wandb.log(epoch_log_dict)

        # Save checkpoints periodically
        if (epoch + 1) % checkpoint_interval == 0:
            _save_training_checkpoint(epoch + 1, checkpoint_reason="periodic_epoch")

        # Save the best model based on validation loss
        if val_avg is not None and val_avg < best_val_loss:
            best_val_loss = val_avg
            _save_training_checkpoint(
                epoch + 1,
                checkpoint_reason="best_val",
                is_best=True,
                update_latest=False,
            )

        test_avg_display = get_meter_dict_avg(test_loss_meters)
        print(f"Epoch [{epoch + 1}/{num_epochs}], Train Loss: {get_meter_dict_avg(train_loss_meters):.6f}, "
              f"Val Loss: {val_avg if val_avg is not None else 'N/A'}, Best Val Loss: {best_val_loss:.6f}, "
              f"Test Loss: {test_avg_display if test_avg_display is not None else 'N/A'}")

        # Switch back to train mode for next epoch
        policy.train()

        stop_reason = _check_stop_reason(walltime_deadline)
        if stop_reason:
            checkpoint_path = _save_training_checkpoint(epoch + 1, checkpoint_reason=f"{stop_reason}_epoch_boundary")
            print(
                f"[INFO] Stop requested ({stop_reason}) after epoch {epoch + 1}; "
                f"saved {checkpoint_path} and requesting requeue"
            )
            return {
                "status": "requeue_requested",
                "checkpoint_path": checkpoint_path,
                "next_epoch": epoch + 1,
                "stop_reason": stop_reason,
            }

    print("[INFO] Training completed. Wandb logs saved.")
    return {"status": "completed"}


def main(cfg: DictConfig):
    # Pretty print config
    print("\n" + "="*50)
    print("Configuration:")
    print("="*50)
    print(OmegaConf.to_yaml(cfg, resolve=True))
    print("="*50 + "\n")

    # Start background rsync to copy data from SCRATCH to local fast storage
    # Training will start immediately using fallback (SCRATCH) while data syncs
    fallback_dataset_dir = getattr(cfg.dataloading, 'fallback_dataset_dir', None)
    dataset_dir = getattr(cfg.dataloading, 'dataset_dir', None)
    try:
        slurm_tmpdir = os.environ.get("SLURM_TMPDIR")
        if slurm_tmpdir is None:
            slurm_tmpdir = "/tmp/"
    except Exception:
        slurm_tmpdir = "/tmp/"
    if fallback_dataset_dir and slurm_tmpdir:
        # Resolve env vars in paths
        source_dir = os.path.expandvars(fallback_dataset_dir)
        # Target is SLURM_TMPDIR (symlinked to dataset_dir via /tmp/...)
        target_dir = os.path.join(slurm_tmpdir, "embodiment-scaling-laws/logs/rsl_rl")
        _start_background_rsync(source_dir, target_dir)
    else:
        print(f"[INFO] Background rsync skipped: fallback_dataset_dir={fallback_dataset_dir}, SLURM_TMPDIR={slurm_tmpdir}")

    stable_log_dir = _get_hydra_output_dir(cfg) or os.path.join(os.getcwd(), "log_dir")
    print(f"[INFO] Resolved log directory: {stable_log_dir}")
    os.makedirs(stable_log_dir, exist_ok=True)

    resume_state = _load_resume_state(stable_log_dir)
    if resume_state:
        print(f"[INFO] Loaded resume state: {resume_state}")
    else:
        print(f"[INFO] No resume state found at {stable_log_dir}/{RESUME_STATE_NAME}")
    resume_checkpoint_path = _resolve_resume_checkpoint(cfg.resume, stable_log_dir, resume_state)
    if resume_checkpoint_path:
        print(f"[INFO] Will resume from checkpoint: {resume_checkpoint_path}")

    runtime_seed = _choose_runtime_seed(cfg.meta.seed)
    set_seed(runtime_seed)
    print(f"[INFO] Using runtime seed: {runtime_seed}")

    # Initialize wandb
    wandb_mode = cfg.meta.wandb_mode
    if wandb_mode != "disabled":
        from hydra.core.hydra_config import HydraConfig
        wandb_config = OmegaConf.to_container(cfg, resolve=True)
        wandb_config["meta"]["config_name"] = HydraConfig.get().job.config_name
        wandb_config["meta"]["runtime_seed"] = runtime_seed
        wandb_id = resume_state.get("wandb_run_id")
        
        # Debug: show what we're passing to wandb.init
        print(f"[INFO] Wandb init: project={cfg.meta.project}, dir={stable_log_dir}")
        print(f"[INFO] Wandb resume: id={wandb_id}, resume={'allow' if wandb_id else None}")
        
        # Disable wandb's SIGTERM handler - we handle preemption ourselves
        # wandb's handler restarts from scratch; ours saves checkpoint and requeues
        os.environ["WANDB_DISABLE_SERVICE"] = "true"  # Disable wandb service (uses signals)
        
        wandb.init(
            project=cfg.meta.project,
            name=cfg.meta.run_name,
            config=wandb_config,
            mode=wandb_mode,
            tags=list(cfg.meta.tags) if cfg.meta.tags else None,
            notes=cfg.meta.notes or None,
            dir=stable_log_dir,
            id=wandb_id,
            resume="allow" if wandb_id else None,
        )
        print(f"[INFO] Wandb initialized (mode={wandb_mode}, run_id={wandb.run.id if wandb.run else 'None'})")

    # Install our preemption handler for SIGTERM (SLURM preemption)
    preemption_handler = PreemptionHandler()
    preemption_handler.install()

    log_dir = stable_log_dir
    if wandb.run is not None:
        print(f"[INFO] Wandb run directory: {wandb.run.dir}")
    print(f"[INFO] Checkpoints will be saved to {log_dir}")

    resume_state.update(
        {
            "log_dir": log_dir,
            "latest_checkpoint": os.path.join(log_dir, LATEST_CHECKPOINT_NAME),
            "wandb_run_id": wandb.run.id if wandb.run is not None else resume_state.get("wandb_run_id"),
            "requeue_count": int(resume_state.get("requeue_count", 0)),
            "last_runtime_seed": runtime_seed,
        }
    )
    _save_resume_state(log_dir, resume_state)

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

    # Expand environment variables in asset_base_path (e.g., $SCRATCH)
    asset_base_path = os.path.expandvars(cfg.ablation.asset_base_path)
    description_filename = cfg.ablation.description_filename

    # Resolve fallback dataset directory (may contain env vars like $SCRATCH)
    fallback_dataset_dir = getattr(cfg.dataloading, 'fallback_dataset_dir', None)
    if fallback_dataset_dir:
        fallback_dataset_dir = os.path.expandvars(fallback_dataset_dir)
        print(f"[INFO] Fallback dataset directory: {fallback_dataset_dir}")

    fallback_count = 0
    def _resolve_h5py_path(task):
        """Try primary dataset_dir first, fall back to fallback_dataset_dir."""
        nonlocal fallback_count
        try:
            return get_most_recent_h5py_record_path(dataset_dir, task)
        except FileNotFoundError:
            if fallback_dataset_dir:
                fallback_count += 1
                return get_most_recent_h5py_record_path(fallback_dataset_dir, task)
            raise

    # Dataset paths
    train_set = list(cfg.train_set)
    test_set = list(cfg.test_set) if cfg.test_set else []
    assert len(train_set) > 0, "Please specify train_set"
    train_set_paths = [_resolve_h5py_path(task) for task in train_set]
    if test_set:
        test_set_paths = [_resolve_h5py_path(task) for task in test_set]
    else:
        test_set_paths = list()
        print(f'[INFO] No test set provided.')
    if fallback_count > 0:
        print(f"[INFO] {fallback_count}/{len(train_set) + len(test_set)} tasks resolved from fallback directory")

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
        asset_base_path=asset_base_path,
        dataset_dir=dataset_dir,
        fallback_dataset_dir=fallback_dataset_dir,
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
        asset_base_path=asset_base_path,
        dataset_dir=dataset_dir,
        fallback_dataset_dir=fallback_dataset_dir,
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
        asset_base_path=asset_base_path,
        dataset_dir=dataset_dir,
        fallback_dataset_dir=fallback_dataset_dir,
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
    policy = torch.compile(policy, mode="reduce-overhead", dynamic=True)

    print('policy architecture:\n', policy)
    sys.stdout.flush()

    print("[INFO] Setting up criterion and optimizer...")
    sys.stdout.flush()
    criterion = torch.nn.MSELoss()

    optimizer_name = getattr(cfg.optim, "optimizer", "adamw").lower()
    if optimizer_name == "adamw":
        optimizer = torch.optim.AdamW(
            policy.parameters(),
            lr=cfg.optim.lr,
            weight_decay=1e-5,
        )
    elif optimizer_name == "lamb":
        from lamb_optimizer import Lamb
        optimizer = Lamb(
            policy.parameters(),
            lr=cfg.optim.lr,
            weight_decay=1e-5,
        )
    else:
        raise ValueError(f"Unknown optimizer: {optimizer_name}. Supported: adamw, lamb")
    print(f"[INFO] Optimizer created successfully: {optimizer_name}")
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

    start_epoch = 0
    initial_best_val_loss = float("inf")
    resume_from_iteration = 0
    scaler = torch.cuda.amp.GradScaler(enabled=bool(cfg.optim.use_amp))

    # Load checkpoint if path specified or auto-discovered
    if resume_checkpoint_path:
        checkpoint = torch.load(resume_checkpoint_path, map_location="cpu")
        policy.load_state_dict(checkpoint["state_dict"])
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        if checkpoint.get("scheduler_state_dict") is not None:
            scheduler.load_state_dict(checkpoint["scheduler_state_dict"])
        if checkpoint.get("scaler_state_dict") is not None:
            scaler.load_state_dict(checkpoint["scaler_state_dict"])
        start_epoch = checkpoint["epoch"]
        checkpoint_metadata = checkpoint.get("metadata") or {}
        if checkpoint_metadata.get("best_val_loss") is not None:
            initial_best_val_loss = checkpoint_metadata["best_val_loss"]
        # Get last logged iteration to avoid duplicate wandb data points
        if checkpoint_metadata.get("last_iteration") is not None:
            resume_from_iteration = checkpoint_metadata["last_iteration"] + 1
            print(f"[INFO] Will skip logging until iteration {resume_from_iteration} to avoid duplicates")
        print(f"[INFO] Loaded checkpoint from {resume_checkpoint_path}, resuming from epoch {start_epoch}")
    else:
        # Save initial (untrained) policy
        save_checkpoint(
            policy,
            optimizer,
            0,
            log_dir,
            scheduler=scheduler,
            scaler=scaler,
            metadata=_checkpoint_metadata(
                best_val_loss=initial_best_val_loss,
                runtime_seed=runtime_seed,
                checkpoint_reason="initial",
                epoch_index=0,
            ),
        )
        print(f"[INFO] Initial policy saved to {log_dir}")

    # Calculate walltime deadline from SLURM (queries squeue once)
    # Buffer of 10 minutes before SLURM time limit to allow for checkpoint saving
    walltime_deadline = _get_slurm_deadline(buffer_minutes=10)

    # Train the policy
    print(f"[INFO] About to start training from epoch {start_epoch}...")
    sys.stdout.flush()
    try:
        train_result = train(
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
            log_epoch_pct=cfg.optim.log_epoch_pct,
            eval_epoch_pct=getattr(cfg.optim, 'eval_epoch_pct', None),
            scaler=scaler,
            walltime_deadline=walltime_deadline,
            initial_best_val_loss=initial_best_val_loss,
            runtime_seed=runtime_seed,
            resume_from_iteration=resume_from_iteration,
        )
        print(f"[INFO] Training function returned with status={train_result['status']}")
        if train_result["status"] == "requeue_requested":
            stop_reason = train_result.get("stop_reason", "unknown")
            resume_state["requeue_count"] = int(resume_state.get("requeue_count", 0)) + 1
            resume_state["last_requeue_reason"] = stop_reason
            resume_state["last_runtime_seed"] = runtime_seed
            _save_resume_state(log_dir, resume_state)

            # Finish wandb BEFORE requeue - scontrol requeue may trigger SIGTERM immediately
            if wandb.run is not None:
                wandb.finish()
                print("[INFO] Wandb finished before requeue")

            if getattr(cfg.meta, "auto_requeue", True):
                requeue_succeeded = _requeue_current_slurm_job()
                if not requeue_succeeded:
                    raise RuntimeError(f"Checkpoint saved ({stop_reason}), but SLURM requeue failed")
                # Exit quickly after requeue - SLURM will terminate us soon anyway
                sys.exit(0)
            else:
                print(f"[WARN] auto_requeue is disabled; stopping after saving checkpoint ({stop_reason})")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] Training failed with exception: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise
    finally:
        preemption_handler.uninstall()
        # wandb.finish() is idempotent - safe to call even if already finished in requeue path
        if wandb.run is not None:
            wandb.finish()


if __name__ == "__main__":
    # When run directly (e.g. from HYDRA_SPOOF re-launch), delegate to the
    # lightweight launcher that doesn't import torch at module level.
    print("[INFO] run_distillation.py invoked directly, delegating to launch_distillation.hydra_main...")
    sys.stdout.flush()
    from launch_distillation import hydra_main
    hydra_main()
