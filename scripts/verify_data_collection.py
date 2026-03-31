#!/usr/bin/env python3
"""
Script to verify that all data collection scripts completed successfully.

Each folder in logs/rsl_rl/* should contain:
  - A timestamp subfolder (e.g., 2025-04-14_00-31-06)
  - Within that, an h5py_record/ directory with:
    - metadata.yaml
    - obs_actions_*.h5 files
    - reward_dict.yaml
    - reward_log_file.json
"""

import os
import glob
import argparse
from pathlib import Path
from typing import NamedTuple


class VerificationResult(NamedTuple):
    folder_name: str
    has_timestamp_folder: bool
    has_h5py_record: bool
    has_metadata: bool
    has_obs_actions: bool
    obs_actions_count: int
    has_reward_dict: bool
    has_reward_log: bool
    is_complete: bool
    error_message: str = ""


def get_clean_name(folder_name: str) -> str:
    """Extract clean experiment name from folder name.
    
    E.g., 'Gendog30_gendog_30_KneeNum_...' -> 'Gendog30'
          'Genhexapod97_genhexapod_97_KneeNum_...' -> 'Genhexapod97'
    """
    return folder_name.split("_")[0]


def verify_experiment_folder(experiment_path: Path) -> VerificationResult:
    """Verify that an experiment folder has all required data collection files."""
    folder_name = experiment_path.name
    
    # Find timestamp subfolder(s)
    subdirs = [d for d in experiment_path.iterdir() if d.is_dir()]
    timestamp_folders = [d for d in subdirs if d.name[0].isdigit()]
    
    if not timestamp_folders:
        return VerificationResult(
            folder_name=folder_name,
            has_timestamp_folder=False,
            has_h5py_record=False,
            has_metadata=False,
            has_obs_actions=False,
            obs_actions_count=0,
            has_reward_dict=False,
            has_reward_log=False,
            is_complete=False,
            error_message="No timestamp folder found"
        )
    
    # Use the first (or latest) timestamp folder
    timestamp_folder = sorted(timestamp_folders)[-1]
    h5py_record_path = timestamp_folder / "h5py_record"
    
    if not h5py_record_path.exists():
        return VerificationResult(
            folder_name=folder_name,
            has_timestamp_folder=True,
            has_h5py_record=False,
            has_metadata=False,
            has_obs_actions=False,
            obs_actions_count=0,
            has_reward_dict=False,
            has_reward_log=False,
            is_complete=False,
            error_message=f"h5py_record folder not found in {timestamp_folder.name}"
        )
    
    # Check for required files
    has_metadata = (h5py_record_path / "metadata.yaml").exists()
    has_reward_dict = (h5py_record_path / "reward_dict.yaml").exists()
    has_reward_log = (h5py_record_path / "reward_log_file.json").exists()
    
    # Count obs_actions files
    obs_actions_files = list(h5py_record_path.glob("obs_actions_*.h5"))
    obs_actions_count = len(obs_actions_files)
    has_obs_actions = obs_actions_count > 0
    
    # Determine if complete
    is_complete = all([
        has_metadata,
        has_obs_actions,
        has_reward_dict,
        has_reward_log
    ])
    
    error_parts = []
    if not has_metadata:
        error_parts.append("missing metadata.yaml")
    if not has_obs_actions:
        error_parts.append("missing obs_actions_*.h5")
    if not has_reward_dict:
        error_parts.append("missing reward_dict.yaml")
    if not has_reward_log:
        error_parts.append("missing reward_log_file.json")
    
    return VerificationResult(
        folder_name=folder_name,
        has_timestamp_folder=True,
        has_h5py_record=True,
        has_metadata=has_metadata,
        has_obs_actions=has_obs_actions,
        obs_actions_count=obs_actions_count,
        has_reward_dict=has_reward_dict,
        has_reward_log=has_reward_log,
        is_complete=is_complete,
        error_message="; ".join(error_parts)
    )


def main():
    parser = argparse.ArgumentParser(
        description="Verify data collection completed for all experiments"
    )
    parser.add_argument(
        "--logs-dir",
        type=str,
        default="logs/rsl_rl",
        help="Path to the logs directory (default: logs/rsl_rl)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output for each folder"
    )
    parser.add_argument(
        "--only-failures",
        action="store_true",
        help="Only show folders with failures"
    )
    parser.add_argument(
        "--min-obs-files",
        type=int,
        default=1,
        help="Minimum number of obs_actions files required (default: 1)"
    )
    parser.add_argument(
        "--list-failed-names",
        action="store_true",
        help="Print only the clean names of failed experiments (e.g., Gendog30)"
    )
    parser.add_argument(
        "--filter-prefix",
        type=str,
        default=None,
        help="Filter experiments by prefix (e.g., 'Gendog', 'Genhexapod', 'Genhumanoid')"
    )
    args = parser.parse_args()
    
    logs_path = Path(args.logs_dir)
    if not logs_path.exists():
        print(f"Error: Logs directory not found: {logs_path}")
        return 1
    
    # Get all experiment folders
    experiment_folders = sorted([
        d for d in logs_path.iterdir() 
        if d.is_dir() and not d.name.startswith(".")
    ])
    
    # Apply prefix filter if specified
    if args.filter_prefix:
        experiment_folders = [
            d for d in experiment_folders 
            if d.name.startswith(args.filter_prefix)
        ]
    
    if not experiment_folders:
        print(f"No experiment folders found in {logs_path}")
        return 1
    
    results = []
    for exp_folder in experiment_folders:
        result = verify_experiment_folder(exp_folder)
        results.append(result)
    
    # Categorize results
    complete = [r for r in results if r.is_complete and r.obs_actions_count >= args.min_obs_files]
    incomplete = [r for r in results if not r.is_complete or r.obs_actions_count < args.min_obs_files]
    
    # If --list-failed-names, just print clean names and exit
    if args.list_failed_names:
        for r in incomplete:
            print(get_clean_name(r.folder_name))
        return 0 if not incomplete else 1
    
    print(f"Checking {len(experiment_folders)} experiment folders...\n")
    
    # Print summary
    print("=" * 80)
    print(f"SUMMARY: {len(complete)}/{len(results)} experiments complete")
    print("=" * 80)
    
    if incomplete:
        print(f"\n{'='*80}")
        print(f"INCOMPLETE/FAILED ({len(incomplete)}):")
        print("=" * 80)
        for r in incomplete:
            issues = []
            if not r.has_timestamp_folder:
                issues.append("no timestamp folder")
            elif not r.has_h5py_record:
                issues.append("no h5py_record")
            else:
                if not r.has_metadata:
                    issues.append("no metadata.yaml")
                if not r.has_obs_actions:
                    issues.append("no obs_actions")
                elif r.obs_actions_count < args.min_obs_files:
                    issues.append(f"only {r.obs_actions_count} obs_actions (need {args.min_obs_files})")
                if not r.has_reward_dict:
                    issues.append("no reward_dict.yaml")
                if not r.has_reward_log:
                    issues.append("no reward_log_file.json")
            
            print(f"  {r.folder_name}")
            print(f"    Issues: {', '.join(issues)}")
    
    if args.verbose and not args.only_failures:
        print(f"\n{'='*80}")
        print(f"COMPLETE ({len(complete)}):")
        print("=" * 80)
        for r in complete:
            print(f"  {r.folder_name} ({r.obs_actions_count} obs_actions files)")
    
    # Statistics
    print(f"\n{'='*80}")
    print("STATISTICS:")
    print("=" * 80)
    
    obs_counts = [r.obs_actions_count for r in results if r.has_obs_actions]
    if obs_counts:
        print(f"  obs_actions file counts: min={min(obs_counts)}, max={max(obs_counts)}, avg={sum(obs_counts)/len(obs_counts):.1f}")
    
    missing_metadata = sum(1 for r in results if r.has_h5py_record and not r.has_metadata)
    missing_obs = sum(1 for r in results if r.has_h5py_record and not r.has_obs_actions)
    missing_reward_dict = sum(1 for r in results if r.has_h5py_record and not r.has_reward_dict)
    missing_reward_log = sum(1 for r in results if r.has_h5py_record and not r.has_reward_log)
    no_timestamp = sum(1 for r in results if not r.has_timestamp_folder)
    no_h5py = sum(1 for r in results if r.has_timestamp_folder and not r.has_h5py_record)
    
    print(f"  Missing timestamp folder: {no_timestamp}")
    print(f"  Missing h5py_record: {no_h5py}")
    print(f"  Missing metadata.yaml: {missing_metadata}")
    print(f"  Missing obs_actions: {missing_obs}")
    print(f"  Missing reward_dict.yaml: {missing_reward_dict}")
    print(f"  Missing reward_log_file.json: {missing_reward_log}")
    
    return 0 if not incomplete else 1


if __name__ == "__main__":
    exit(main())
