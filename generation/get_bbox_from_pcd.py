"""
Extract per-limb bounding boxes from robot point cloud files.

This script computes limb bounding boxes from pre-generated point cloud data (robot_pcd.json),
avoiding the need to set up SAPIEN for URDF parsing.

The script copies the existing robot_description_vec.json and adds a 'bbox' field to each
entry in 'joint_info', computed from the corresponding part in the point cloud data.

Usage:
    # Batch mode - process all robots in a directory
    python get_bbox_from_pcd.py --root-dir gen_dogs --output-filename robot_description_vec_with_bboxes.json
    
    # Single file
    python get_bbox_from_pcd.py --pcd-path path/to/robot_pcd.json --desc-path path/to/robot_description_vec.json
    
    # Dry run to see what would be processed
    python get_bbox_from_pcd.py --root-dir gen_dogs --dry-run
"""

import argparse
import gzip
import json
import os
from typing import Dict, List, Tuple

import numpy as np
from tqdm import tqdm


def load_pcd_json(pcd_path: str) -> Dict:
    """Load a gzipped point cloud JSON file."""
    with gzip.open(pcd_path, 'rt', encoding='utf-8') as f:
        return json.load(f)


def segment_points_by_color(
    pcd_data: Dict,
) -> Dict[str, np.ndarray]:
    """
    Segment the full point cloud into per-part point clouds based on color.
    
    Args:
        pcd_data: The loaded point cloud JSON data
        
    Returns:
        Dictionary mapping part names to their point cloud arrays (N x 3)
    """
    # Get the full point cloud data
    full_data = pcd_data.get('>FULL<', pcd_data.get('>ORIGINAL XML<'))
    if full_data is None:
        raise ValueError("Point cloud JSON missing '>FULL<' or '>ORIGINAL XML<' entry")
    
    points = np.array(full_data['pcd_points'])
    colors = full_data['pcd_colors']
    
    if len(points) == 0:
        return {}
    
    # Build color -> part name mapping from the part entries
    color_to_part = {}
    for part_name, part_data in pcd_data.items():
        # Skip special entries
        if part_name.startswith('>'):
            continue
        if 'color' in part_data and isinstance(part_data['color'], list):
            # Convert to tuple for hashability (rounded to avoid float precision issues)
            color_key = tuple(round(c, 6) for c in part_data['color'])
            color_to_part[color_key] = part_name
    
    # Segment points by color
    part_points = {name: [] for name in color_to_part.values()}
    
    for point, color in zip(points, colors):
        color_key = tuple(round(c, 6) for c in color)
        if color_key in color_to_part:
            part_points[color_to_part[color_key]].append(point)
    
    # Convert to numpy arrays
    return {
        name: np.array(pts) if pts else np.array([]).reshape(0, 3)
        for name, pts in part_points.items()
    }


def compute_bbox(points: np.ndarray) -> List[List[float]]:
    """
    Compute axis-aligned bounding box from points.
    
    Args:
        points: Nx3 array of points
        
    Returns:
        Bounding box as [[min_x, min_y, min_z], [max_x, max_y, max_z]]
    """
    if len(points) == 0:
        return [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    
    min_xyz = points.min(axis=0).tolist()
    max_xyz = points.max(axis=0).tolist()
    return [min_xyz, max_xyz]


def add_bboxes_to_description(
    desc_path: str,
    pcd_path: str,
    output_path: str,
    verbose: bool = False
):
    """
    Copy robot description and add bbox to each joint_info entry.
    
    Args:
        desc_path: Path to existing robot_description_vec.json
        pcd_path: Path to gzipped robot_pcd.json
        output_path: Path for output JSON with added bboxes
        verbose: Print detailed progress
    """
    # Load existing description
    with open(desc_path, 'r') as f:
        desc = json.load(f)
    
    # Load and segment point cloud
    pcd_data = load_pcd_json(pcd_path)
    part_points = segment_points_by_color(pcd_data)
    
    # Compute bbox for each part
    part_bboxes = {}
    for part_name, points in part_points.items():
        part_bboxes[part_name] = compute_bbox(points)
    
    # Add bbox to each joint in joint_info
    joint_info = desc.get('joint_info', {})
    matched = 0
    missing = []
    
    for joint_name in joint_info:
        if joint_name in part_bboxes:
            joint_info[joint_name]['bbox'] = part_bboxes[joint_name]
            matched += 1
        else:
            # Joint not found in PCD - use zero bbox
            joint_info[joint_name]['bbox'] = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
            missing.append(joint_name)
    
    if verbose:
        print(f"  Matched {matched}/{len(joint_info)} joints")
        if missing:
            print(f"  Missing joints (zero bbox): {missing}")
    
    # Save updated description
    with open(output_path, 'w') as f:
        json.dump(desc, f, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Extract per-limb bounding boxes from robot point cloud files and add to robot description."
    )
    parser.add_argument(
        "--pcd-path", type=str, default=None,
        help="Path to a single robot_pcd.json file (gzipped)"
    )
    parser.add_argument(
        "--desc-path", type=str, default=None,
        help="Path to existing robot_description_vec.json (used with --pcd-path)"
    )
    parser.add_argument(
        "--output-path", type=str, default=None,
        help="Output path for the new description JSON (used with --pcd-path)"
    )
    parser.add_argument(
        "--root-dir", type=str, default=None,
        help="Directory containing robot assets (gen_dogs, gen_hexapods, gen_humanoids)"
    )
    parser.add_argument(
        "--pcd-filename", type=str, default="robot_pcd.json",
        help="Name of the point cloud file to read (default: robot_pcd.json)"
    )
    parser.add_argument(
        "--desc-filename", type=str, default="robot_description_vec.json",
        help="Name of existing description file (default: robot_description_vec.json)"
    )
    parser.add_argument(
        "--output-filename", type=str, default="robot_description_vec_with_bboxes.json",
        help="Name of output file (default: robot_description_vec_with_bboxes.json)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be done without actually doing it"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print detailed progress"
    )
    args = parser.parse_args()
    
    if args.pcd_path:
        # Single file mode
        if args.desc_path is None:
            # Default to same directory
            base_dir = os.path.dirname(args.pcd_path)
            args.desc_path = os.path.join(base_dir, "robot_description_vec.json")
        
        output_path = args.output_path
        if output_path is None:
            base_dir = os.path.dirname(args.pcd_path)
            output_path = os.path.join(base_dir, args.output_filename)
        
        if args.dry_run:
            print(f"[DRY RUN] Would process:")
            print(f"  PCD: {args.pcd_path}")
            print(f"  Description: {args.desc_path}")
            print(f"  Output: {output_path}")
        else:
            print(f"Processing: {args.pcd_path}")
            add_bboxes_to_description(args.desc_path, args.pcd_path, output_path, verbose=True)
            print(f"Done! Output: {output_path}")
    
    elif args.root_dir:
        # Batch mode - process all robots in directory
        if not os.path.isdir(args.root_dir):
            print(f"Error: {args.root_dir} is not a directory")
            return
        
        # Find all robot directories
        asset_dirs = sorted([
            os.path.join(args.root_dir, name)
            for name in os.listdir(args.root_dir)
            if os.path.isdir(os.path.join(args.root_dir, name))
        ])
        
        # Filter to directories that have both PCD and description files
        valid_dirs = []
        for asset_dir in asset_dirs:
            pcd_path = os.path.join(asset_dir, args.pcd_filename)
            desc_path = os.path.join(asset_dir, args.desc_filename)
            if os.path.exists(pcd_path) and os.path.exists(desc_path):
                valid_dirs.append(asset_dir)
        
        if args.dry_run:
            print(f"[DRY RUN] Would process {len(valid_dirs)} robots in {args.root_dir}")
            print(f"[DRY RUN] PCD filename: {args.pcd_filename}")
            print(f"[DRY RUN] Description filename: {args.desc_filename}")
            print(f"[DRY RUN] Output filename: {args.output_filename}")
            if valid_dirs:
                print(f"[DRY RUN] Sample directories: {valid_dirs[:3]}")
            
            skipped = len(asset_dirs) - len(valid_dirs)
            if skipped > 0:
                print(f"[DRY RUN] Skipping {skipped} directories without required files")
        else:
            print(f"Processing {len(valid_dirs)} robots from {args.root_dir}...")
            
            for asset_dir in tqdm(valid_dirs, desc="Adding bboxes"):
                pcd_path = os.path.join(asset_dir, args.pcd_filename)
                desc_path = os.path.join(asset_dir, args.desc_filename)
                output_path = os.path.join(asset_dir, args.output_filename)
                
                try:
                    add_bboxes_to_description(desc_path, pcd_path, output_path, verbose=args.verbose)
                except Exception as e:
                    print(f"\nError processing {asset_dir}: {e}")
                    continue
            
            print(f"\nDone! Processed {len(valid_dirs)} robots.")
            print(f"Output files: {args.output_filename}")
    
    else:
        parser.print_help()
        print("\nError: Either --pcd-path or --root-dir must be specified.")


if __name__ == '__main__':
    main()
