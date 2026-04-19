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
import glob
import os
import subprocess
import time
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

import yaml
import wandb


class ConfigExtractionError(Exception):
    """Raised when essential config fields cannot be extracted from a run."""
    pass


def get_config_name(run) -> str:
    """Extract config name from run.
    
    Raises:
        ConfigExtractionError: If config_name cannot be found in any expected location.
    """
    config = run.config
    
    # Try nested format first: config["meta"]["config_name"]
    meta = config.get("meta", {})
    if isinstance(meta, dict):
        if "config_name" in meta:
            return meta["config_name"]
        if "run_name" in meta:
            return meta["run_name"]
    
    # Try flattened formats: "meta/config_name" or "meta.config_name"
    for key in ["meta/config_name", "meta.config_name", "meta/run_name", "meta.run_name"]:
        if key in config:
            return config[key]
    
    # Debug: print available keys to help diagnose
    print(f"[ERROR] Could not find config_name for run {run.id} ({run.name})")
    print(f"  Available config keys: {list(config.keys())[:20]}...")
    print(f"  meta value: {meta!r}")
    
    raise ConfigExtractionError(
        f"Cannot extract config_name from run {run.id}. "
        f"Available keys: {list(config.keys())}"
    )


def get_ablation_name(run) -> str:
    """Extract ablation name from run.
    
    Raises:
        ConfigExtractionError: If ablation name cannot be found in any expected location.
    """
    config = run.config
    
    # Try nested format first: config["ablation"]["name"]
    ablation = config.get("ablation", {})
    if isinstance(ablation, dict) and "name" in ablation:
        return ablation["name"]
    
    # Try flattened formats: "ablation/name" or "ablation.name"
    for key in ["ablation/name", "ablation.name"]:
        if key in config:
            return config[key]
    
    # Debug: print available keys to help diagnose
    print(f"[ERROR] Could not find ablation name for run {run.id} ({run.name})")
    print(f"  Available config keys: {list(config.keys())[:20]}...")
    print(f"  ablation value: {ablation!r}")
    
    raise ConfigExtractionError(
        f"Cannot extract ablation name from run {run.id}. "
        f"Available keys: {list(config.keys())}"
    )


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


def get_current_slurm_job_ids() -> Set[str]:
    """Get the current SLURM job IDs (base job ID, not array indices)."""
    try:
        result = subprocess.run(
            ["squeue", "--me", "-h", "-o", "%A"],  # Just job IDs
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            # Extract base job ID (strip array index like _[0-5] or _0)
            ids = set()
            for line in result.stdout.strip().split("\n"):
                if line.strip():
                    base_id = line.split("_")[0]  # Get base job ID
                    ids.add(base_id)
            return ids
    except Exception:
        pass
    return set()


def launch_job(config_name: str, ablations_str: str, seeds_str: str, project: str,
               scripts_dir: str, timeout_min: int = 719, wait_for_submission: int = 60,
               check_interval: int = 2, dry_run: bool = False) -> bool:
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
        f"hydra.launcher.timeout_min={timeout_min}",
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
    
    # Get initial job IDs
    initial_job_ids = get_current_slurm_job_ids()
    
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
        current_job_ids = get_current_slurm_job_ids()
        new_jobs = current_job_ids - initial_job_ids
        if new_jobs:
            print(f"Detected new SLURM job IDs: {new_jobs} after {elapsed}s")
            submitted = True
            break
        
        print(f"  Waiting... ({elapsed}s elapsed, jobs: {len(current_job_ids)})")
    
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
    parser.add_argument(
        "--timeout-min",
        type=int,
        default=719,
        help="SLURM job timeout in minutes (default: 719)",
    )
    parser.add_argument(
        "--config-names",
        type=str,
        nargs="+",
        default=None,
        help="List of config names to check. If not provided, auto-discovers from conf/ directory.",
    )
    parser.add_argument(
        "--ablation-names",
        type=str,
        nargs="+",
        default=None,
        help="List of ablation names to check. If not provided, auto-discovers from conf/ablation/ directory.",
    )
    
    args = parser.parse_args()
    
    # Compute scripts directory from this script's location
    # This script is at <repo>/scripts/utility/relaunch_failed_runs.py
    # We need <repo>/scripts/
    scripts_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Scripts directory: {scripts_dir}")
    
    # Discover or use provided config names
    conf_dir = os.path.join(scripts_dir, "distillation", "conf")
    if args.config_names:
        expected_configs: Set[str] = set(args.config_names)
        print(f"Using provided config names: {sorted(expected_configs)}")
    else:
        # Auto-discover: only all_robot_jobs_v7_allrobots_* configs (excluding test_set)
        config_files = glob.glob(os.path.join(conf_dir, "all_robot_jobs_v7_allrobots_*.yaml"))
        expected_configs = set()
        for f in config_files:
            basename = os.path.basename(f)
            if "test_set" in basename:
                continue
            # Config name is the filename without .yaml extension
            config_name = basename.replace(".yaml", "")
            expected_configs.add(config_name)
        print(f"Auto-discovered {len(expected_configs)} config names from {conf_dir}")
    
    # Discover or use provided ablation names
    # NOTE: We need to map from the "name" field in YAML (stored in wandb) to the filename (used for launching)
    ablation_name_to_filename: Dict[str, str] = {}  # Maps name field -> filename (without .yaml)
    
    if args.ablation_names:
        expected_ablations: Set[str] = set(args.ablation_names)
        print(f"Using provided ablation names: {sorted(expected_ablations)}")
        # When provided manually, assume name == filename
        for name in expected_ablations:
            ablation_name_to_filename[name] = name
    else:
        # Auto-discover from conf/ablation/ directory
        # Read the "name" field from each YAML since that's what's stored in wandb
        ablation_dir = os.path.join(conf_dir, "ablation")
        ablation_files = glob.glob(os.path.join(ablation_dir, "*.yaml"))
        expected_ablations = set()
        for f in ablation_files:
            basename = os.path.basename(f)
            filename = basename.replace(".yaml", "")
            # Read the YAML to get the actual "name" field
            with open(f, 'r') as yaml_file:
                try:
                    ablation_config = yaml.safe_load(yaml_file)
                    ablation_name = ablation_config.get("name", filename)  # Fallback to filename if no name field
                except Exception as e:
                    print(f"[WARNING] Could not parse {f}: {e}, using filename as name")
                    ablation_name = filename
            expected_ablations.add(ablation_name)
            ablation_name_to_filename[ablation_name] = filename
        print(f"Auto-discovered {len(expected_ablations)} ablation names from {ablation_dir}")
        print(f"  Name -> Filename mapping: {ablation_name_to_filename}")
    
    # Build the set of all expected (config_name, ablation_name) pairs
    expected_pairs: Set[Tuple[str, str]] = set()
    for config_name in expected_configs:
        for ablation_name in expected_ablations:
            expected_pairs.add((config_name, ablation_name))
    print(f"Total expected (config, ablation) pairs: {len(expected_pairs)}")
    
    print(f"\nConnecting to wandb: {args.entity}/{args.project}")
    
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
    
    # NOTE: api.runs() returns runs with incomplete config data.
    # We need to fetch each run individually to get the full config.
    print("Fetching full run configs...")
    full_runs = []
    for i, run in enumerate(runs_list):
        if (i + 1) % 10 == 0:
            print(f"  Fetched {i + 1}/{len(runs_list)} runs...")
        # Fetch the full run to get complete config
        full_run = api.run(f"{args.entity}/{args.project}/{run.id}")
        full_runs.append(full_run)
    print(f"  Fetched all {len(full_runs)} runs")
    
    # Categorize runs by (config_name, ablation_name) and their status
    # Status: done, running, requeued, maybe_delete
    run_status: Dict[Tuple[str, str], Dict[str, List]] = defaultdict(lambda: {
        "done": [],
        "running": [],
        "requeued": [],
        "maybe_delete": [],
        "other": [],
    })
    
    # Pre-populate run_status with all expected pairs to catch pairs with zero runs
    for pair in expected_pairs:
        _ = run_status[pair]  # Access to initialize with default
    
    skipped_runs = []
    for run in full_runs:
        try:
            config_name = get_config_name(run)
            ablation_name = get_ablation_name(run)
        except ConfigExtractionError as e:
            print(f"[WARNING] Skipping run {run.id} ({run.name}): {e}")
            skipped_runs.append(run)
            continue
            
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
    
    if skipped_runs:
        print(f"\n[WARNING] Skipped {len(skipped_runs)} runs due to missing config fields")
    
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
            # Convert ablation names (from wandb) to filenames (for Hydra)
            ablation_filenames = []
            for name in ablation_list:
                filename = ablation_name_to_filename.get(name, name)  # Fallback to name if not found
                ablation_filenames.append(filename)
            ablations_str = ",".join(ablation_filenames)
            seeds_str = ",".join(["-1"] * seed_count)
            
            success = launch_job(
                config_name=config_name,
                ablations_str=ablations_str,
                seeds_str=seeds_str,
                project=args.project,
                scripts_dir=scripts_dir,
                timeout_min=args.timeout_min,
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
