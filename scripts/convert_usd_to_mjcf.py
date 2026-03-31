#!/usr/bin/env python3
"""
Script to convert all GenBot1K-v7 robots from USD to MJCF format.

Usage:
    # Basic conversion (visual only, fast)
    python scripts/convert_usd_to_mjcf.py

    # With collision generation (slower but more complete)
    python scripts/convert_usd_to_mjcf.py --generate_collision

    # With custom parallelism
    python scripts/convert_usd_to_mjcf.py --num_workers 8

    # High-quality collision with custom resolution
    python scripts/convert_usd_to_mjcf.py --generate_collision --preprocess_resolution 40 --resolution 4000

    # Convert only specific robot type
    python scripts/convert_usd_to_mjcf.py --robot_type gen_dogs
"""

import argparse
import os
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Optional
import traceback

# Add the usd2mjcf directory to the path
WORKSPACE_ROOT = Path(__file__).parent.parent
USD2MJCF_PATH = WORKSPACE_ROOT / "usd2mjcf"
sys.path.insert(0, str(USD2MJCF_PATH))

from lightwheel.srl.from_usd.to_mjcf import UsdToMjcf


def convert_single_robot(
    usd_path: str,
    output_path: Optional[str] = None,
    generate_collision: bool = False,
    preprocess_resolution: int = 20,
    resolution: int = 2000,
) -> dict:
    """
    Convert a single USD file to MJCF format.
    
    Args:
        usd_path: Path to the input USD file
        output_path: Path to output directory (default: same as input)
        generate_collision: Whether to generate collision meshes
        preprocess_resolution: Preprocessing voxelization resolution
        resolution: Main voxelization resolution
    
    Returns:
        dict with 'success', 'usd_path', 'mjcf_path', and optionally 'error'
    """
    result = {"success": False, "usd_path": usd_path, "mjcf_path": None, "error": None}
    
    try:
        if output_path is None:
            output_path = os.path.dirname(usd_path)
        
        mjcf_dir = os.path.join(output_path, "MJCF")
        
        # Convert USD to MJCF
        mjcf_file = UsdToMjcf.init_from_file(usd_path).save_to_file(mjcf_dir)
        result["mjcf_path"] = mjcf_file
        
        # Generate collision meshes if requested
        if generate_collision:
            # Import here to avoid loading unless needed
            sys.path.insert(0, str(USD2MJCF_PATH / "utils"))
            from add_collision import add_collision_to_only_visual_mjcf
            add_collision_to_only_visual_mjcf(
                mjcf_file,
                preprocess_resolution=preprocess_resolution,
                resolution=resolution
            )
        
        result["success"] = True
        
    except Exception as e:
        result["error"] = f"{type(e).__name__}: {str(e)}\n{traceback.format_exc()}"
    
    return result


def find_robot_usd_files(robots_dir: str, robot_type: Optional[str] = None) -> list:
    """
    Find all robot USD files in the GenBot1K-v7 directory.
    
    Args:
        robots_dir: Path to the GenBot1K-v7 directory
        robot_type: Optional filter for robot type (gen_dogs, gen_hexapods, gen_humanoids)
    
    Returns:
        List of paths to USD files
    """
    usd_files = []
    robots_path = Path(robots_dir)
    
    # Get subdirectories to search
    if robot_type:
        subdirs = [robots_path / robot_type]
        if not subdirs[0].exists():
            raise ValueError(f"Robot type directory not found: {subdirs[0]}")
    else:
        subdirs = [
            robots_path / "gen_dogs",
            robots_path / "gen_hexapods",
            robots_path / "gen_humanoids",
        ]
    
    for subdir in subdirs:
        if not subdir.exists():
            print(f"Warning: Directory not found: {subdir}")
            continue
        
        # Each robot folder contains usd_file/robot.usd
        for robot_folder in subdir.iterdir():
            if not robot_folder.is_dir() or robot_folder.name.startswith('.'):
                continue
            if robot_folder.name == "meta_data.txt":
                continue
                
            usd_file = robot_folder / "usd_file" / "robot.usd"
            if usd_file.exists():
                usd_files.append(str(usd_file))
            else:
                print(f"Warning: USD file not found: {usd_file}")
    
    return sorted(usd_files)


def main():
    parser = argparse.ArgumentParser(
        description="Convert GenBot1K-v7 robots from USD to MJCF format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--robots_dir",
        type=str,
        default=str(WORKSPACE_ROOT / "exts" / "embodiment_scaling_laws" / "embodiment_scaling_laws" / "assets" / "Robots" / "GenBot1K-v7"),
        help="Path to the GenBot1K-v7 directory"
    )
    parser.add_argument(
        "--robot_type",
        type=str,
        choices=["gen_dogs", "gen_hexapods", "gen_humanoids"],
        default=None,
        help="Convert only a specific robot type"
    )
    parser.add_argument(
        "--generate_collision",
        action="store_true",
        help="Generate collision meshes using convex decomposition"
    )
    parser.add_argument(
        "--preprocess_resolution",
        type=int,
        default=20,
        help="Preprocessing voxelization resolution for convex decomposition"
    )
    parser.add_argument(
        "--resolution",
        type=int,
        default=2000,
        help="Main voxelization resolution for convex decomposition"
    )
    parser.add_argument(
        "--num_workers",
        type=int,
        default=4,
        help="Number of parallel workers for conversion"
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Print what would be converted without actually converting"
    )
    parser.add_argument(
        "--skip_existing",
        action="store_true",
        help="Skip conversion if MJCF directory already exists"
    )
    
    args = parser.parse_args()
    
    # Find all USD files
    print(f"Searching for USD files in: {args.robots_dir}")
    usd_files = find_robot_usd_files(args.robots_dir, args.robot_type)
    print(f"Found {len(usd_files)} USD files to convert")
    
    if args.dry_run:
        print("\nDry run - files that would be converted:")
        for usd_file in usd_files[:10]:
            print(f"  {usd_file}")
        if len(usd_files) > 10:
            print(f"  ... and {len(usd_files) - 10} more")
        return
    
    # Filter out existing conversions if requested
    if args.skip_existing:
        filtered_files = []
        for usd_file in usd_files:
            mjcf_dir = Path(usd_file).parent / "MJCF"
            if not mjcf_dir.exists():
                filtered_files.append(usd_file)
            else:
                print(f"Skipping (already exists): {usd_file}")
        usd_files = filtered_files
        print(f"After filtering: {len(usd_files)} files to convert")
    
    if not usd_files:
        print("No files to convert")
        return
    
    # Convert files
    successful = 0
    failed = 0
    failed_files = []
    
    print(f"\nStarting conversion with {args.num_workers} workers...")
    print(f"Collision generation: {args.generate_collision}")
    
    if args.num_workers == 1:
        # Sequential processing (easier to debug)
        for i, usd_file in enumerate(usd_files):
            print(f"[{i+1}/{len(usd_files)}] Converting: {usd_file}")
            result = convert_single_robot(
                usd_file,
                generate_collision=args.generate_collision,
                preprocess_resolution=args.preprocess_resolution,
                resolution=args.resolution,
            )
            if result["success"]:
                successful += 1
                print(f"  -> Success: {result['mjcf_path']}")
            else:
                failed += 1
                failed_files.append((usd_file, result["error"]))
                print(f"  -> Failed: {result['error'][:100]}...")
    else:
        # Parallel processing
        with ProcessPoolExecutor(max_workers=args.num_workers) as executor:
            futures = {
                executor.submit(
                    convert_single_robot,
                    usd_file,
                    None,
                    args.generate_collision,
                    args.preprocess_resolution,
                    args.resolution,
                ): usd_file
                for usd_file in usd_files
            }
            
            for i, future in enumerate(as_completed(futures)):
                usd_file = futures[future]
                result = future.result()
                
                if result["success"]:
                    successful += 1
                    print(f"[{i+1}/{len(usd_files)}] Success: {Path(usd_file).parent.parent.name}")
                else:
                    failed += 1
                    failed_files.append((usd_file, result["error"]))
                    print(f"[{i+1}/{len(usd_files)}] Failed: {Path(usd_file).parent.parent.name}")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    
    if failed_files:
        print(f"\nFailed conversions:")
        for usd_file, error in failed_files[:10]:
            print(f"  {usd_file}")
            print(f"    Error: {error[:200]}...")
        if len(failed_files) > 10:
            print(f"  ... and {len(failed_files) - 10} more failures")
        
        # Write failed files to a log
        log_file = WORKSPACE_ROOT / "conversion_failures.log"
        with open(log_file, "w") as f:
            for usd_file, error in failed_files:
                f.write(f"{usd_file}\n{error}\n{'='*60}\n")
        print(f"\nFull error log written to: {log_file}")


if __name__ == "__main__":
    main()
