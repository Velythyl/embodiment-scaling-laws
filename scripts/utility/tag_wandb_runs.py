#!/usr/bin/env python3
"""
Script to tag wandb runs based on epoch count and SLURM job status.

This script:
1. Fetches all runs from the wandb project
2. Groups them by config name and ablation name
3. Tags runs with epoch >= 80 as "done"
4. For runs with epoch < 80:
   - Checks if their SLURM job is still running via squeue
   - Tags as "REQUEUED" if running
   - Tags as "MAYBE_DELETE" if not running
"""

import argparse
import subprocess
from collections import defaultdict
from typing import Dict, Set, Optional

import wandb


def get_running_slurm_jobs(debug: bool = False) -> Set[str]:
    """
    Get set of currently running SLURM jobs in format "JOB_ID_TASK_ID".
    
    Returns:
        Set of strings like "1234567_0", "1234567_1", etc.
    """
    running_jobs = set()
    
    try:
        # Get all running/pending jobs for current user
        # Use squeue --me to get jobs, then extract JOBID column
        result = subprocess.run(
            ["squeue", "--me", "-h", "-o", "%i"],  # %i = job id (includes array task id)
            capture_output=True,
            text=True,
        )
        
        if debug:
            print(f"[DEBUG] squeue raw output:\n{result.stdout}")
        
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                job_id = line.strip()
                if job_id:
                    running_jobs.add(job_id)
        else:
            print(f"[WARNING] squeue returned error: {result.stderr}")
            
    except FileNotFoundError:
        print("[ERROR] squeue command not found. Are you on a SLURM cluster?")
    except Exception as e:
        print(f"[ERROR] Failed to run squeue: {e}")
    
    if debug:
        print(f"[DEBUG] Parsed SLURM jobs ({len(running_jobs)} total): {sorted(running_jobs)[:20]}{'...' if len(running_jobs) > 20 else ''}")
    
    return running_jobs


def get_slurm_job_id(run: wandb.apis.public.Run, debug: bool = False) -> Optional[str]:
    """
    Extract SLURM job ID in format "ARRAY_JOB_ID_TASK_ID" from run config.
    
    Returns:
        String like "1234567_0" or None if not available.
    """
    config = run.config
    meta = config.get("meta", {})
    
    array_job_id = meta.get("SLURM_ARRAY_JOB_ID")
    array_task_id = meta.get("SLURM_ARRAY_TASK_ID")
    
    if debug:
        print(f"[DEBUG] Run {run.id}: SLURM_ARRAY_JOB_ID={array_job_id!r} (type={type(array_job_id).__name__}), SLURM_ARRAY_TASK_ID={array_task_id!r} (type={type(array_task_id).__name__})")
    
    if array_job_id is None or array_task_id is None:
        # Try regular job ID if array not available
        job_id = meta.get("SLURM_JOB_ID")
        if job_id is not None:
            return str(job_id)
        return None
    
    # Ensure both are converted to string and formatted consistently
    return f"{array_job_id}_{array_task_id}"


def add_tag_to_run(run: wandb.apis.public.Run, tag: str, dry_run: bool = False) -> bool:
    """
    Add a tag to a run if it doesn't already have it.
    
    Returns:
        True if tag was added (or would be in dry_run mode), False if already present.
    """
    current_tags = list(run.tags) if run.tags else []
    
    if tag in current_tags:
        return False
    
    new_tags = current_tags + [tag]
    
    if dry_run:
        print(f"  [DRY-RUN] Would add tag '{tag}' to run {run.id} ({run.name})")
        return True
    else:
        run.tags = new_tags
        run.save()
        print(f"  Added tag '{tag}' to run {run.id} ({run.name})")
        return True


def get_epoch_count(run: wandb.apis.public.Run) -> Optional[int]:
    """
    Get the current epoch count from a run's summary.
    
    Returns:
        Integer epoch count or None if not available.
    """
    summary = run.summary
    
    # Try different possible epoch field names
    for key in ["epoch", "Epoch", "_step"]:
        if key in summary:
            try:
                return int(summary[key])
            except (ValueError, TypeError):
                pass
    
    return None


def get_config_name(run: wandb.apis.public.Run) -> str:
    """Extract config name from run."""
    config = run.config
    meta = config.get("meta", {})
    return meta.get("config_name", meta.get("run_name", "unknown"))


def get_ablation_name(run: wandb.apis.public.Run) -> str:
    """Extract ablation name from run."""
    config = run.config
    ablation = config.get("ablation", {})
    return ablation.get("name", "unknown")


def main():
    parser = argparse.ArgumentParser(
        description="Tag wandb runs based on epoch count and SLURM job status"
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
        "--epoch-threshold",
        type=int,
        default=80,
        help="Epoch threshold for marking runs as 'done' (default: 80)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without actually tagging",
    )
    parser.add_argument(
        "--tag-done",
        type=str,
        default="done",
        help="Tag to apply to completed runs (default: 'done')",
    )
    parser.add_argument(
        "--tag-requeued",
        type=str,
        default="REQUEUED",
        help="Tag to apply to runs with active SLURM jobs (default: 'REQUEUED')",
    )
    parser.add_argument(
        "--tag-maybe-delete",
        type=str,
        default="MAYBE_DELETE",
        help="Tag to apply to runs without active SLURM jobs (default: 'MAYBE_DELETE')",
    )
    parser.add_argument(
        "--filters",
        type=str,
        default=None,
        help="Additional wandb filters as JSON string (e.g., '{\"state\": \"running\"}')",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print debug information about SLURM job ID matching",
    )
    
    args = parser.parse_args()
    
    print(f"Connecting to wandb: {args.entity}/{args.project}")
    
    # Initialize wandb API
    api = wandb.Api()
    
    # Build filters
    filters = {}
    if args.filters:
        import json
        filters = json.loads(args.filters)
    
    # Fetch all runs
    print("Fetching runs...")
    try:
        runs = api.runs(f"{args.entity}/{args.project}", filters=filters)
        runs_list = list(runs)
    except ValueError as e:
        if "Could not find project" in str(e):
            print(f"\n[ERROR] Could not find project '{args.project}' under entity '{args.entity}'")
            print("\nThis could be due to:")
            print("  1. The project name is incorrect")
            print("  2. The entity (username/team) is incorrect")
            print("  3. You don't have access to this project")
            print("  4. You need to login: run 'wandb login'")
            print("\nTrying to list available projects for this entity...")
            try:
                entity = api.entity(args.entity)
                projects = entity.projects()
                print(f"\nAvailable projects for '{args.entity}':")
                for proj in projects:
                    print(f"  - {proj.name}")
            except Exception as e2:
                print(f"  Could not list projects: {e2}")
            return
        raise
    
    print(f"Found {len(runs_list)} runs")
    
    # Get currently running SLURM jobs
    print("\nChecking SLURM job status...")
    running_slurm_jobs = get_running_slurm_jobs(debug=args.debug)
    print(f"Found {len(running_slurm_jobs)} running/pending SLURM jobs")
    
    # Group runs by config name and ablation name
    groups: Dict[str, Dict[str, list]] = defaultdict(lambda: defaultdict(list))
    
    # Statistics
    stats = {
        "total": len(runs_list),
        "done": 0,
        "requeued": 0,
        "maybe_delete": 0,
        "no_epoch": 0,
        "no_slurm_id": 0,
        "already_tagged": 0,
    }
    
    print("\nProcessing runs...")
    print("=" * 80)
    
    for run in runs_list:
        config_name = get_config_name(run)
        ablation_name = get_ablation_name(run)
        epoch = get_epoch_count(run)
        slurm_job_id = get_slurm_job_id(run, debug=args.debug)
        
        groups[config_name][ablation_name].append({
            "run": run,
            "epoch": epoch,
            "slurm_job_id": slurm_job_id,
        })
        
        print(f"\nRun: {run.name} (id: {run.id})")
        print(f"  Config: {config_name}, Ablation: {ablation_name}")
        print(f"  Epoch: {epoch}, SLURM Job: {slurm_job_id}")
        print(f"  Current tags: {run.tags}")
        
        # Check if run is done (epoch >= threshold)
        if epoch is not None and epoch >= args.epoch_threshold:
            if add_tag_to_run(run, args.tag_done, dry_run=args.dry_run):
                stats["done"] += 1
            else:
                stats["already_tagged"] += 1
            continue
        
        # Run is not done - check SLURM status
        if epoch is None:
            print(f"  [WARNING] No epoch data found")
            stats["no_epoch"] += 1
        
        if slurm_job_id is None:
            print(f"  [WARNING] No SLURM job ID found")
            stats["no_slurm_id"] += 1
            continue
        
        # Check if SLURM job is running
        print(running_slurm_jobs)
       # exit()

        is_slurm_job_id_in_running_slurm_jobs = False
        for running_slurm_job in running_slurm_jobs:
            if running_slurm_job.startswith(slurm_job_id):
                is_slurm_job_id_in_running_slurm_jobs = True
                break

        if is_slurm_job_id_in_running_slurm_jobs:
            if add_tag_to_run(run, args.tag_requeued, dry_run=args.dry_run):
                stats["requeued"] += 1
            else:
                stats["already_tagged"] += 1
        else:
            if add_tag_to_run(run, args.tag_maybe_delete, dry_run=args.dry_run):
                stats["maybe_delete"] += 1
            else:
                stats["already_tagged"] += 1
    
    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total runs processed: {stats['total']}")
    print(f"Tagged as '{args.tag_done}': {stats['done']}")
    print(f"Tagged as '{args.tag_requeued}': {stats['requeued']}")
    print(f"Tagged as '{args.tag_maybe_delete}': {stats['maybe_delete']}")
    print(f"Already had correct tag: {stats['already_tagged']}")
    print(f"Missing epoch data: {stats['no_epoch']}")
    print(f"Missing SLURM job ID: {stats['no_slurm_id']}")
    
    # Print grouped summary
    print("\n" + "=" * 80)
    print("RUNS GROUPED BY CONFIG AND ABLATION")
    print("=" * 80)
    
    for config_name, ablations in sorted(groups.items()):
        print(f"\n{config_name}:")
        for ablation_name, run_infos in sorted(ablations.items()):
            epochs = [r["epoch"] for r in run_infos if r["epoch"] is not None]
            epoch_str = f"epochs: {min(epochs)}-{max(epochs)}" if epochs else "no epochs"
            print(f"  {ablation_name}: {len(run_infos)} runs, {epoch_str}")


if __name__ == "__main__":
    main()
