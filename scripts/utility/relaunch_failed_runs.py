#!/usr/bin/env python3
"""
Script to identify and relaunch failed/deleted wandb runs.

This script:
1. Queries wandb for runs tagged MAYBE_DELETE_AUTOTAG
2. Groups them by (config_name, ablation_name)
3. Counts how many seeds are missing (target: 5 per config/ablation)
4. Directly relaunches the missing runs via subprocess
"""

import argparse
import os
import subprocess
import time
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

import wandb


def get_config_name(run) -> str:
    """Extract config name from run."""
    config = run.config
    meta = config.get("meta", {})
    return meta.get("config_name", meta.get("run_name", "unknown"))


def get_ablation_name(run) -> str:
    """Extract ablation name from run."""
    config = run.config
    ablation = config.get("ablation", {})
    return ablation.get("name", "unknown")


def get_epoch_count(run) -> Optional[int]:
    """Get the current epoch count from a run's summary."""
    summary = run.summary
    for key in ["epoch", "Epoch", "_step"]:
        if key in summary:
            try:
                return int(summary[key])
            except (ValueError, TypeError):
                pass
    return None


def get_current_slurm_job_count() -> int:
    """Get the current number of SLURM jobs for the user."""
    try:
        result = subprocess.run(
            ["squeue", "--me", "-h"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return len([l for l in result.stdout.strip().split("\n") if l.strip()])
    except Exception:
        pass
    return 0


def launch_job(config_name: str, ablations_str: str, seeds_str: str, project: str,
               scripts_dir: str, wait_for_submission: int = 60, check_interval: int = 2, 
               dry_run: bool = False) -> bool:
    """
    Launch a Hydra multirun job and wait for SLURM submission.
    
    Returns True if jobs were successfully submitted.
    """
    cmd = [
        "python3", "distillation/launch_distillation.py",
        "--config-name", config_name,
        "--multirun",
        "hydra/launcher=firsbatch",
        "+hydra/sweep=sbatch",
        "hydra.launcher._target_=hydra_plugins.packed_launcher.packedlauncher.SlurmLauncher",
        "hydra.launcher.tasks_per_node=1",
        "+hydra.launcher.timeout_min=719",
        "hydra.launcher.cpus_per_task=6",
        "hydra.launcher.mem_gb=128",
        "hydra.launcher.array_parallelism=300",
        "meta=auto",
        "optim.gradient_acc_steps=1",
        "dataloading.h5_repeat_factor=3",
        "dataloading.num_workers=5",
        "dataloading.batch_size=1024",
        "optim.lr=0.0006",
        f"ablation={ablations_str}",
        f"meta.project={project}",
        f"meta.seed={seeds_str}",
        "hydra.launcher.name=esl_requeue",
    ]
    
    print(f"\n{'=' * 80}")
    print(f"Launching: {config_name} with ablations [{ablations_str}]")
    print(f"Seeds: {seeds_str}")
    print(f"{'=' * 80}")
    print(f"Working directory: {scripts_dir}")
    print(f"Command: {' '.join(cmd)}")
    
    if dry_run:
        print("[DRY-RUN] Would launch this command")
        return True
    
    # Get initial job count
    initial_jobs = get_current_slurm_job_count()
    
    # Launch the process
    process = subprocess.Popen(
        cmd,
        cwd=scripts_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    
    print(f"Started process with PID: {process.pid}")
    
    # Wait for jobs to be submitted
    elapsed = 0
    submitted = False
    
    while elapsed < wait_for_submission:
        time.sleep(check_interval)
        elapsed += check_interval
        
        # Check if process exited
        if process.poll() is not None:
            print(f"Process exited on its own after {elapsed}s")
            submitted = True
            break
        
        # Check if new jobs appeared
        current_jobs = get_current_slurm_job_count()
        if current_jobs > initial_jobs:
            print(f"Detected new SLURM jobs ({initial_jobs} -> {current_jobs}) after {elapsed}s")
            submitted = True
            break
        
        print(f"  Waiting... ({elapsed}s elapsed, jobs: {current_jobs})")
    
    # Kill process if still running
    if process.poll() is None:
        print(f"Killing launcher process (PID: {process.pid})")
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
    
    if submitted:
        print(f"Jobs submitted for {config_name} / [{ablations_str}]")
    else:
        print(f"WARNING: Timed out waiting for job submission for {config_name} / [{ablations_str}]")
    
    # Small delay before next job
    time.sleep(2)
    
    return submitted


def main():
    parser = argparse.ArgumentParser(
        description="Identify and relaunch failed wandb runs"
    )
    parser.add_argument(
        "--entity",
        type=str,
        default="velythyl",
        help="Wandb entity (username or team)",
    )
    parser.add_argument(
        "--project",
        type=str,
        default="esl_apr10_requeue",
        help="Wandb project name",
    )
    parser.add_argument(
        "--target-seeds",
        type=int,
        default=5,
        help="Target number of seeds per (config, ablation) pair (default: 5)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be launched without actually launching",
    )
    
    args = parser.parse_args()
    
    # Compute scripts directory from this script's location
    # This script is at <repo>/scripts/utility/relaunch_failed_runs.py
    # We need <repo>/scripts/
    scripts_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Scripts directory: {scripts_dir}")
    
    print(f"Connecting to wandb: {args.entity}/{args.project}")
    
    # Initialize wandb API
    api = wandb.Api()
    
    # Fetch all runs
    print("Fetching runs...")
    try:
        runs = api.runs(f"{args.entity}/{args.project}")
        runs_list = list(runs)
    except ValueError as e:
        print(f"[ERROR] Could not find project: {e}")
        return
    
    print(f"Found {len(runs_list)} total runs")
    
    # Categorize runs by (config_name, ablation_name) and their status
    # Status: done, running, requeued, maybe_delete
    run_status: Dict[Tuple[str, str], Dict[str, List]] = defaultdict(lambda: {
        "done": [],
        "running": [],
        "requeued": [],
        "maybe_delete": [],
        "other": [],
    })
    
    for run in runs_list:
        config_name = get_config_name(run)
        ablation_name = get_ablation_name(run)
        tags = run.tags or []
        
        key = (config_name, ablation_name)
        
        if "DONE_AUTOTAG" in tags:
            run_status[key]["done"].append(run)
        elif "RUNNING_AUTOTAG" in tags:
            run_status[key]["running"].append(run)
        elif "REQUEUED_AUTOTAG" in tags:
            run_status[key]["requeued"].append(run)
        elif "MAYBE_DELETE_AUTOTAG" in tags:
            run_status[key]["maybe_delete"].append(run)
        else:
            run_status[key]["other"].append(run)
    
    print("\n" + "=" * 100)
    print("RUN STATUS BY (CONFIG, ABLATION)")
    print("=" * 100)
    
    relaunch_needed: Dict[Tuple[str, str], int] = {}
    
    for (config_name, ablation_name), status in sorted(run_status.items()):
        
        done_count = len(status["done"])
        running_count = len(status["running"])
        requeued_count = len(status["requeued"])
        maybe_delete_count = len(status["maybe_delete"])
        other_count = len(status["other"])
        
        # Active runs = done + running + requeued
        active_count = done_count + running_count + requeued_count
        missing_count = max(0, args.target_seeds - active_count)
        
        print(f"\n{config_name} / {ablation_name}:")
        print(f"  Done: {done_count}, Running: {running_count}, Requeued: {requeued_count}, Maybe Delete: {maybe_delete_count}, Other: {other_count}")
        print(f"  Active: {active_count}/{args.target_seeds}, Missing: {missing_count}")
        
        if missing_count > 0:
            relaunch_needed[(config_name, ablation_name)] = missing_count
    
    # Print summary
    print("\n" + "=" * 100)
    print("SUMMARY: RUNS NEEDING RELAUNCH")
    print("=" * 100)
    
    if not relaunch_needed:
        print("\nAll (config, ablation) pairs have sufficient runs!")
        return
    
    total_missing = sum(relaunch_needed.values())
    print(f"\nTotal missing runs: {total_missing}")
    
    for (config_name, ablation_name), count in sorted(relaunch_needed.items()):
        print(f"  {config_name} / {ablation_name}: {count} missing")
    
    # Group by config_name to create efficient launch commands
    relaunch_by_config: Dict[str, Dict[str, int]] = defaultdict(dict)
    for (config_name, ablation_name), count in relaunch_needed.items():
        relaunch_by_config[config_name][ablation_name] = count
    
    # Launch jobs
    print("\n" + "=" * 100)
    print("LAUNCHING JOBS")
    print("=" * 100)
    
    successful_launches = 0
    failed_launches = 0
    
    for config_name, ablations in sorted(relaunch_by_config.items()):
        # Group ablations by seed count needed
        # Since Hydra does cartesian product: ablation x seeds
        # We need to launch separately for different seed counts
        seeds_to_ablations: Dict[int, List[str]] = defaultdict(list)
        for ablation_name, count in ablations.items():
            seeds_to_ablations[count].append(ablation_name)
        
        for seed_count, ablation_list in seeds_to_ablations.items():
            ablations_str = ",".join(ablation_list)
            seeds_str = ",".join(["-1"] * seed_count)
            
            success = launch_job(
                config_name=config_name,
                ablations_str=ablations_str,
                seeds_str=seeds_str,
                project=args.project,
                scripts_dir=scripts_dir,
                dry_run=args.dry_run,
            )
            
            if success:
                successful_launches += 1
            else:
                failed_launches += 1
    
    # Final summary
    print("\n" + "=" * 100)
    print("LAUNCH SUMMARY")
    print("=" * 100)
    print(f"Successful launches: {successful_launches}")
    print(f"Failed launches: {failed_launches}")
    print(f"\nCheck your jobs with: squeue --me")


if __name__ == "__main__":
    main()
