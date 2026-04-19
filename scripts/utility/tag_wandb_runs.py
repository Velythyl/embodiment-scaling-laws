#!/usr/bin/env python3
"""
Script to tag wandb runs based on epoch count and SLURM job status.

This script:
1. Fetches all runs from multiple wandb projects (comma-separated)
2. Groups them by (config_name, ablation_name)
3. Tags runs with epoch >= threshold as "DONE_AUTOTAG"
4. For runs with epoch < threshold:
   - Checks if their SLURM job is still running via squeue
   - Tags as "RUNNING_AUTOTAG" if wandb state is running
   - Tags as "REQUEUED_AUTOTAG" if SLURM job is active
   - Tags as "MAYBE_DELETE_AUTOTAG" if not running
5. For categories that already have enough seeds done, cancels REQUEUED SLURM jobs
"""

import argparse
import json
import subprocess
from collections import defaultdict
from typing import Dict, List, Set, Optional, Tuple

import wandb

# All AUTOTAG tags - only one should be present at a time
AUTOTAGS = [
    "DONE_AUTOTAG",
    "RUNNING_AUTOTAG",
    "REQUEUED_AUTOTAG",
    "MAYBE_DELETE_AUTOTAG",
    "SHOULD_CANCEL_AUTOTAG",
]


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


def set_autotag(run: wandb.apis.public.Run, tag: str, dry_run: bool = False) -> bool:
    """
    Set an AUTOTAG on a run, removing any other AUTOTAGs first.
    
    Only one AUTOTAG should be present at a time.
    
    Returns:
        True if changes were made (or would be in dry_run mode), False if already correct.
    """
    current_tags = list(run.tags) if run.tags else []
    
    # Check if already has the correct tag and no other autotags
    has_target_tag = tag in current_tags
    other_autotags = [t for t in current_tags if t in AUTOTAGS and t != tag]
    
    if has_target_tag and not other_autotags:
        # Already in correct state
        return False
    
    # Remove all autotags, then add the target one
    new_tags = [t for t in current_tags if t not in AUTOTAGS]
    new_tags.append(tag)
    
    removed_tags = [t for t in current_tags if t in AUTOTAGS and t != tag]
    
    if dry_run:
        if removed_tags:
            print(f"  [DRY-RUN] Would remove tags {removed_tags} and add '{tag}' to run {run.id} ({run.name})")
        else:
            print(f"  [DRY-RUN] Would add tag '{tag}' to run {run.id} ({run.name})")
        return True
    else:
        run.tags = new_tags
        run.save()
        if removed_tags:
            print(f"  Removed {removed_tags}, added '{tag}' to run {run.id} ({run.name})")
        else:
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
        help="Wandb project name(s), comma-separated for multiple projects",
    )
    parser.add_argument(
        "--target-seeds",
        type=int,
        default=5,
        help="Target number of seeds per (config, ablation) pair (default: 5)",
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
        default="DONE_AUTOTAG",
        help="Tag to apply to completed runs (default: 'DONE_AUTOTAG')",
    )
    parser.add_argument(
        "--tag-running",
        type=str,
        default="RUNNING_AUTOTAG",
        help="Tag to apply to currently running wandb runs (default: 'RUNNING_AUTOTAG')",
    )
    parser.add_argument(
        "--tag-requeued",
        type=str,
        default="REQUEUED_AUTOTAG",
        help="Tag to apply to runs with active SLURM jobs but not currently running (default: 'REQUEUED_AUTOTAG')",
    )
    parser.add_argument(
        "--tag-maybe-delete",
        type=str,
        default="MAYBE_DELETE_AUTOTAG",
        help="Tag to apply to runs without active SLURM jobs (default: 'MAYBE_DELETE_AUTOTAG')",
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
    parser.add_argument(
        "--scancel-jobs-for-done-categories",
        action="store_true",
        help="Also run scancel for jobs in categories that already have enough done runs",
    )
    
    args = parser.parse_args()
    
    # Parse comma-separated projects
    projects = [p.strip() for p in args.project.split(",")]
    
    print(f"Connecting to wandb: {args.entity}")
    print(f"Projects to process: {projects}")
    
    # Initialize wandb API
    api = wandb.Api()
    
    # Build filters
    filters = {}
    if args.filters:
        filters = json.loads(args.filters)
    
    # Fetch runs from all projects
    print("Fetching runs from all projects...")
    runs_list = []
    for project in projects:
        print(f"  Fetching from {project}...")
        try:
            runs = api.runs(f"{args.entity}/{project}", filters=filters)
            project_runs = list(runs)
            print(f"    Found {len(project_runs)} runs")
            
            # NOTE: api.runs() returns runs with incomplete config data.
            # We need to fetch each run individually to get the full config.
            print(f"    Fetching full run configs...")
            for i, run in enumerate(project_runs):
                if (i + 1) % 10 == 0:
                    print(f"      Fetched {i + 1}/{len(project_runs)} runs...")
                # Fetch the full run to get complete config
                full_run = api.run(f"{args.entity}/{project}/{run.id}")
                runs_list.append(full_run)
            print(f"      Fetched all {len(project_runs)} runs from {project}")
        except ValueError as e:
            if "Could not find project" in str(e):
                print(f"\n[ERROR] Could not find project '{project}' under entity '{args.entity}'")
                print("\nThis could be due to:")
                print("  1. The project name is incorrect")
                print("  2. The entity (username/team) is incorrect")
                print("  3. You don't have access to this project")
                print("  4. You need to login: run 'wandb login'")
                print("\nTrying to list available projects for this entity...")
                try:
                    entity = api.entity(args.entity)
                    proj_list = entity.projects()
                    print(f"\nAvailable projects for '{args.entity}':")
                    for proj in proj_list:
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
    
    # Group runs by (config_name, ablation_name) and track their status
    # Key: (config_name, ablation_name) -> list of run info dicts
    groups: Dict[Tuple[str, str], List[dict]] = defaultdict(list)
    
    # Statistics
    stats = {
        "total": len(runs_list),
        "done": 0,
        "running": 0,
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
        
        run_info = {
            "run": run,
            "epoch": epoch,
            "slurm_job_id": slurm_job_id,
            "final_tag": None,  # Will be set based on processing
        }
        groups[(config_name, ablation_name)].append(run_info)
        
        # Check if wandb run is currently running
        is_wandb_running = run.state == "running"
        
        print(f"\nRun: {run.name} (id: {run.id})")
        print(f"  Config: {config_name}, Ablation: {ablation_name}")
        print(f"  Epoch: {epoch}, SLURM Job: {slurm_job_id}, WandB state: {run.state}")
        print(f"  Current tags: {run.tags}")
        
        # Check if run is done (epoch >= threshold)
        if epoch is not None and epoch >= args.epoch_threshold:
            run_info["final_tag"] = args.tag_done
            if set_autotag(run, args.tag_done, dry_run=args.dry_run):
                stats["done"] += 1
            else:
                stats["already_tagged"] += 1
            continue
        
        # Check if wandb run is currently running (active heartbeat)
        if is_wandb_running:
            run_info["final_tag"] = args.tag_running
            if set_autotag(run, args.tag_running, dry_run=args.dry_run):
                stats["running"] += 1
            else:
                stats["already_tagged"] += 1
            continue
        
        # Run is not done and not currently running - check SLURM status
        if epoch is None:
            print(f"  [WARNING] No epoch data found")
            stats["no_epoch"] += 1
        
        if slurm_job_id is None:
            print(f"  [WARNING] No SLURM job ID found, tagging as MAYBE_DELETE")
            stats["no_slurm_id"] += 1
            run_info["final_tag"] = args.tag_maybe_delete
            if set_autotag(run, args.tag_maybe_delete, dry_run=args.dry_run):
                stats["maybe_delete"] += 1
            else:
                stats["already_tagged"] += 1
            continue
        
        # Check if SLURM job is running/pending
        # Use exact match or prefix match with underscore to avoid false positives
        # e.g. job "1234" should not match "12345_0"
        is_slurm_job_id_in_running_slurm_jobs = (
            slurm_job_id in running_slurm_jobs or
            any(j.startswith(slurm_job_id + "_") for j in running_slurm_jobs)
        )

        if is_slurm_job_id_in_running_slurm_jobs:
            run_info["final_tag"] = args.tag_requeued
            if set_autotag(run, args.tag_requeued, dry_run=args.dry_run):
                stats["requeued"] += 1
            else:
                stats["already_tagged"] += 1
        else:
            run_info["final_tag"] = args.tag_maybe_delete
            if set_autotag(run, args.tag_maybe_delete, dry_run=args.dry_run):
                stats["maybe_delete"] += 1
            else:
                stats["already_tagged"] += 1
    
    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total runs processed: {stats['total']}")
    print(f"Tagged as '{args.tag_done}': {stats['done']}")
    print(f"Tagged as '{args.tag_running}': {stats['running']}")
    print(f"Tagged as '{args.tag_requeued}': {stats['requeued']}")
    print(f"Tagged as '{args.tag_maybe_delete}': {stats['maybe_delete']}")
    print(f"Already had correct tag: {stats['already_tagged']}")
    print(f"Missing epoch data: {stats['no_epoch']}")
    print(f"Missing SLURM job ID: {stats['no_slurm_id']}")
    
    # Print grouped summary and identify runs to cancel
    print("\n" + "=" * 80)
    print("RUNS GROUPED BY (CONFIG, ABLATION)")
    print("=" * 80)
    
    jobs_to_cancel: List[Tuple[str, str, str, dict]] = []  # (config, ablation, slurm_job_id, run_info)
    
    for (config_name, ablation_name), run_infos in sorted(groups.items()):
        done_count = sum(1 for r in run_infos if r["final_tag"] == args.tag_done)
        running_count = sum(1 for r in run_infos if r["final_tag"] == args.tag_running)
        requeued_count = sum(1 for r in run_infos if r["final_tag"] == args.tag_requeued)
        maybe_delete_count = sum(1 for r in run_infos if r["final_tag"] == args.tag_maybe_delete)
        
        epochs = [r["epoch"] for r in run_infos if r["epoch"] is not None]
        epoch_str = f"epochs: {min(epochs)}-{max(epochs)}" if epochs else "no epochs"
        
        # Check if we have enough done runs
        excess = done_count - args.target_seeds
        
        print(f"\n{config_name} / {ablation_name}:")
        print(f"  {len(run_infos)} runs, {epoch_str}")
        print(f"  Done: {done_count}, Running: {running_count}, Requeued: {requeued_count}, Maybe Delete: {maybe_delete_count}")
        print(f"  Target seeds: {args.target_seeds}, Done count: {done_count}, Excess: {excess}")
        
        # If we already have enough done runs, cancel requeued and running runs
        if done_count >= args.target_seeds and (requeued_count > 0 or running_count > 0):
            print(f"  [CANCEL] Category has {done_count} done runs (target: {args.target_seeds}), will tag {requeued_count} requeued + {running_count} running runs for cancellation")
            for r in run_infos:
                if r["final_tag"] in (args.tag_requeued, args.tag_running) and r["slurm_job_id"] is not None:
                    jobs_to_cancel.append((config_name, ablation_name, r["slurm_job_id"], r))
    
    # Tag runs for cancellation instead of directly cancelling
    if jobs_to_cancel:
        print("\n" + "=" * 80)
        print("TAGGING REQUEUED/RUNNING RUNS AS SHOULD_CANCEL FOR COMPLETED CATEGORIES")
        print("=" * 80)
        print(f"\nFound {len(jobs_to_cancel)} runs to tag for cancellation")
        
        tagged = 0
        failed = 0
        
        for config_name, ablation_name, slurm_job_id, run_info in jobs_to_cancel:
            run = run_info["run"]
            print(f"\n  Tagging run {run.name} ({config_name} / {ablation_name})")
            print(f"    SLURM job: {slurm_job_id}")
            
            if set_autotag(run, "SHOULD_CANCEL_AUTOTAG", dry_run=args.dry_run):
                run_info["final_tag"] = "SHOULD_CANCEL_AUTOTAG"
                tagged += 1
            else:
                # Already tagged correctly
                tagged += 1
        
        verb = "would tag" if args.dry_run else "tagged"
        print(f"\nTagging summary: {tagged} {verb} as SHOULD_CANCEL_AUTOTAG")
        
        # Also scancel if requested
        if args.scancel_jobs_for_done_categories:
            print("\n" + "=" * 80)
            print("SCANCELLING SLURM JOBS")
            print("=" * 80)
            
            cancelled = 0
            scancel_failed = 0
            
            for config_name, ablation_name, slurm_job_id, run_info in jobs_to_cancel:
                print(f"\n  Cancelling job {slurm_job_id} ({config_name} / {ablation_name})")
                
                if args.dry_run:
                    print(f"    [DRY-RUN] Would run: scancel {slurm_job_id}")
                    cancelled += 1
                else:
                    try:
                        result = subprocess.run(
                            ["scancel", slurm_job_id],
                            capture_output=True,
                            text=True,
                        )
                        if result.returncode == 0:
                            print(f"    Successfully cancelled")
                            cancelled += 1
                        else:
                            print(f"    [WARNING] scancel returned error: {result.stderr}")
                            scancel_failed += 1
                    except FileNotFoundError:
                        print(f"    [ERROR] scancel command not found")
                        scancel_failed += 1
                    except Exception as e:
                        print(f"    [ERROR] Failed to cancel: {e}")
                        scancel_failed += 1
            
            verb = "would cancel" if args.dry_run else "cancelled"
            print(f"\nScancel summary: {cancelled} {verb}, {scancel_failed} failed")
        else:
            print(f"\nTo cancel these jobs, run: scancel <job_id> for each SLURM job, or use --scancel-jobs-for-done-categories")
    else:
        print("\n" + "=" * 80)
        print("NO RUNS TO TAG FOR CANCELLATION")
        print("=" * 80)
        print("\nAll requeued/running runs are for categories that still need more seeds.")


if __name__ == "__main__":
    main()
