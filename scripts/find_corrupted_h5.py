#!/usr/bin/env python3
"""Scan a dataset directory for corrupted/truncated HDF5 files.

Usage:
    python find_corrupted_h5.py /path/to/dataset -j 16 -o report.txt
"""

import argparse
import glob
import os
import sys
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed

import h5py


def check_file(file_path):
    """Try to open an HDF5 file. Returns (path, size, error) if corrupted, else None."""
    try:
        with h5py.File(file_path, "r") as f:
            list(f.keys())
        return None
    except Exception as e:
        try:
            size = os.path.getsize(file_path)
        except OSError:
            size = -1
        return (file_path, size, str(e))


def extract_robot_name(file_path, data_dir):
    """Extract the top-level robot folder name from a file path."""
    rel = os.path.relpath(file_path, data_dir)
    return rel.split(os.sep)[0]


def main():
    parser = argparse.ArgumentParser(description="Find corrupted HDF5 files in a dataset directory.")
    parser.add_argument("data_dir", help="Root directory to scan (e.g. ./logs/rsl_rl)")
    parser.add_argument("-j", "--jobs", type=int, default=min(16, os.cpu_count() or 4),
                        help="Number of parallel workers (default: min(16, cpu_count))")
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="Write report to this file (in addition to stdout)")
    args = parser.parse_args()

    data_dir = os.path.abspath(args.data_dir)

    print(f"Scanning for .h5 files in {data_dir} ...")
    h5_files = glob.glob(os.path.join(data_dir, "**", "*.h5"), recursive=True)
    total = len(h5_files)
    print(f"Found {total:,} .h5 files. Checking with {args.jobs} workers...")

    corrupted = []
    checked = 0
    t0 = time.time()

    # Submit in batches via ProcessPoolExecutor
    BATCH = 512
    with ProcessPoolExecutor(max_workers=args.jobs) as executor:
        # Submit all at once — executor handles queuing internally
        future_to_path = {executor.submit(check_file, fp): fp for fp in h5_files}

        for future in as_completed(future_to_path):
            checked += 1
            result = future.result()
            if result is not None:
                corrupted.append(result)
            if checked % 500 == 0 or checked == total:
                elapsed = time.time() - t0
                rate = checked / elapsed if elapsed > 0 else 0
                print(f"  [{checked:,}/{total:,}] {len(corrupted)} corrupted | {rate:.0f} files/s", end="\r")

    elapsed = time.time() - t0
    print(f"\n\nDone in {elapsed:.1f}s ({total:,} files checked)")

    # Build report
    lines = []
    if corrupted:
        # Group by robot
        by_robot = defaultdict(list)
        for path, size, error in corrupted:
            robot = extract_robot_name(path, data_dir)
            by_robot[robot].append((path, size, error))

        lines.append("=" * 80)
        lines.append(f"CORRUPTION REPORT — {len(corrupted)} corrupted files across {len(by_robot)} robots")
        lines.append("=" * 80)
        lines.append("")

        for robot in sorted(by_robot.keys()):
            entries = by_robot[robot]
            lines.append(f"[{robot}] — {len(entries)} corrupted file(s)")
            for path, size, error in sorted(entries):
                size_str = f"{size:,} bytes" if size >= 0 else "MISSING"
                lines.append(f"    {os.path.relpath(path, data_dir)}  ({size_str})")
                lines.append(f"      Error: {error}")
            lines.append("")

        lines.append("-" * 80)
        lines.append("AFFECTED ROBOTS (copy-paste list):")
        lines.append("-" * 80)
        for robot in sorted(by_robot.keys()):
            lines.append(f"  {robot}")

        lines.append("")
        lines.append("-" * 80)
        lines.append("ALL CORRUPTED FILE PATHS (for deletion):")
        lines.append("-" * 80)
        for path, _, _ in sorted(corrupted):
            lines.append(path)
    else:
        lines.append("All files OK!")

    report = "\n".join(lines)
    print(report)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report + "\n")
        print(f"\nReport written to {args.output}")

    return 1 if corrupted else 0


if __name__ == "__main__":
    sys.exit(main())
