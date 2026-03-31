"""
Script to compute bounding boxes for all links/limbs of robots using SAPIEN.

This script takes robot names as input (e.g., Gendog0, Gendog1) and computes
the bounding box for each link in the robot. The output is saved as
'all_robot_limb_bbox.json' in each robot's asset folder.

Usage:
    python generation/compute_limb_bbox_sapien.py --robots Gendog0 Gendog1 Gendog2
    python generation/compute_limb_bbox_sapien.py --robots Genhexapod0 Genhexapod1
    python generation/compute_limb_bbox_sapien.py --robots Genhumanoid0 Genhumanoid1
    
    # Process all robots of a type
    python generation/compute_limb_bbox_sapien.py --robot_type dog --all
    
Requirements:
    - sapien (pip install sapien)
    - urdfpy (pip install urdfpy && pip install --upgrade networkx)
    - numpy 1.x (numpy 2 causes silent errors with SAPIEN)
"""

import sapien.core as sapien
import json
import numpy as np
import re
import os
import argparse
from tqdm import tqdm
from urdfpy import URDF


# Asset base path
ASSET_BASE_PATH = "exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/Robots/GenBot1K-v7"

# Robot type to folder mapping
ROBOT_TYPE_TO_FOLDER = {
    "dog": "gen_dogs",
    "hexapod": "gen_hexapods", 
    "humanoid": "gen_humanoids",
}

# Robot type to root link name mapping
ROBOT_TYPE_TO_ROOT_LINK = {
    "dog": "trunk",
    "hexapod": "trunk",
    "humanoid": "pelvis",
}


def get_local_bbox_for_link(link):
    """Compute the local bounding box for a link based on its collision shapes."""
    mins = np.array([np.inf, np.inf, np.inf])
    maxs = -mins
    
    shapes = link.get_collision_shapes()
    if len(shapes) == 0:
        # No collision shapes, return empty/zero bbox
        return np.zeros(3), np.zeros(3)
    
    for shape in shapes:
        if shape.type == 'box':
            x, y, z = shape.geometry.half_lengths
            vertices = np.array([
                [x, y, z], [x, y, -z], [x, -y, z], [x, -y, -z],
                [-x, y, z], [-x, y, -z], [-x, -y, z], [-x, -y, -z]
            ])
        elif shape.type == 'sphere':
            x = shape.geometry.radius
            vertices = np.array([
                [x, 0, 0], [-x, 0, 0], [0, x, 0], [0, -x, 0], [0, 0, x], [0, 0, -x]
            ])
        elif shape.type == 'capsule':
            x = y = shape.geometry.radius
            z = shape.geometry.half_length
            vertices = np.array([
                [x, y, z], [x, y, -z], [x, -y, z], [x, -y, -z],
                [-x, y, z], [-x, y, -z], [-x, -y, z], [-x, -y, -z]
            ])
        elif hasattr(shape.geometry, 'vertices'):
            # Mesh geometry
            vertices = shape.geometry.vertices * shape.geometry.scale
        else:
            print(f"Warning: Unknown shape type '{shape.type}' for link, skipping")
            continue
            
        mins = np.minimum(mins, vertices.min(0))
        maxs = np.maximum(maxs, vertices.max(0))
    
    # Handle case where no valid shapes were found
    if np.any(np.isinf(mins)):
        return np.zeros(3), np.zeros(3)
        
    return mins, maxs


def compute_nominal_joint_positions(joint_names, nominal_positions_cfg):
    """
    Computes nominal joint positions for each joint based on regex patterns.
    """
    nominal_positions = np.zeros(len(joint_names))
    for idx, joint in enumerate(joint_names):
        for pattern, position in nominal_positions_cfg.items():
            if re.match(pattern, joint):
                nominal_positions[idx] = position
                break
    return nominal_positions


def parse_robot_name(robot_name: str) -> tuple:
    """
    Parse a robot name like 'Gendog0' to get robot type and index.
    
    Returns:
        tuple: (robot_type, robot_index)
        Example: ('dog', 0) for 'Gendog0'
    """
    # Match patterns like Gendog0, Genhexapod10, Genhumanoid5
    match = re.match(r'^Gen(dog|hexapod|humanoid)(\d+)$', robot_name, re.IGNORECASE)
    if not match:
        raise ValueError(f"Invalid robot name format: {robot_name}. Expected format like 'Gendog0', 'Genhexapod10', 'Genhumanoid5'")
    
    robot_type = match.group(1).lower()
    robot_index = int(match.group(2))
    return robot_type, robot_index


def find_robot_folder(robot_name: str, asset_base_path: str = ASSET_BASE_PATH) -> str:
    """
    Find the full folder path for a robot given its short name.
    
    Args:
        robot_name: Short name like 'Gendog0'
        asset_base_path: Base path to robot assets
        
    Returns:
        Full path to the robot's asset folder
    """
    robot_type, robot_index = parse_robot_name(robot_name)
    
    # Get the folder containing this robot type
    type_folder = ROBOT_TYPE_TO_FOLDER[robot_type]
    type_path = os.path.join(asset_base_path, type_folder)
    
    if not os.path.exists(type_path):
        raise FileNotFoundError(f"Robot type folder not found: {type_path}")
    
    # Find folder starting with gendog_{index}_ or genhexapod_{index}_ etc.
    prefix = f"gen{robot_type}_{robot_index}_"
    
    matching_folders = [
        f for f in os.listdir(type_path)
        if f.startswith(prefix) and os.path.isdir(os.path.join(type_path, f))
    ]
    
    if len(matching_folders) == 0:
        raise FileNotFoundError(f"No folder found for {robot_name} with prefix '{prefix}' in {type_path}")
    elif len(matching_folders) > 1:
        raise ValueError(f"Multiple folders found for {robot_name}: {matching_folders}")
    
    return os.path.join(type_path, matching_folders[0])


def get_all_robot_names(robot_type: str, asset_base_path: str = ASSET_BASE_PATH) -> list:
    """
    Get all robot names of a given type.
    
    Args:
        robot_type: 'dog', 'hexapod', or 'humanoid'
        asset_base_path: Base path to robot assets
        
    Returns:
        List of robot short names like ['Gendog0', 'Gendog1', ...]
    """
    type_folder = ROBOT_TYPE_TO_FOLDER[robot_type]
    type_path = os.path.join(asset_base_path, type_folder)
    
    if not os.path.exists(type_path):
        raise FileNotFoundError(f"Robot type folder not found: {type_path}")
    
    robot_names = []
    prefix = f"gen{robot_type}_"
    
    for folder in os.listdir(type_path):
        if folder.startswith(prefix) and os.path.isdir(os.path.join(type_path, folder)):
            # Extract index from folder name
            match = re.match(rf'^gen{robot_type}_(\d+)_', folder)
            if match:
                idx = int(match.group(1))
                robot_names.append(f"Gen{robot_type.capitalize()}{idx}")
    
    # Sort by index
    robot_names.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    return robot_names


def extract_limb_bbox(robot_urdf_path: str, train_cfg_path: str, root_name: str) -> dict:
    """
    Extract bounding boxes for all links in a robot.
    
    Args:
        robot_urdf_path: Path to robot.urdf
        train_cfg_path: Path to train_cfg_v2.json
        root_name: Name of the root link (e.g., 'trunk', 'pelvis')
        
    Returns:
        Dictionary containing:
        - link_info: Per-link bounding box and mass
        - joint_to_child_link: Mapping from joint names to child link names
    """
    # Set up SAPIEN engine and scene
    engine = sapien.Engine()
    renderer = sapien.SapienRenderer()
    engine.set_renderer(renderer)
    
    scene_config = sapien.SceneConfig()
    scene = engine.create_scene(scene_config)
    scene.set_timestep(1 / 240.0)
    scene.add_ground(0)
    scene.set_ambient_light([0.5, 0.5, 0.5])
    scene.add_directional_light([0, 1, -1], [0.5, 0.5, 0.5])
    
    # Load robot
    loader = scene.create_urdf_loader()
    loader.fix_root_link = False
    robot = loader.load(robot_urdf_path)
    
    # Load training config for initial pose
    with open(train_cfg_path, "r") as f:
        train_cfg = json.load(f)
    
    # Verify root link
    assert robot.get_links()[0].name == root_name, \
        f"Root link is '{robot.get_links()[0].name}', expected '{root_name}'"
    
    # Set robot pose
    robot.set_root_pose(sapien.Pose([0, 0, train_cfg['drop_height']], [1, 0, 0, 0]))
    
    # Set initial joint positions
    active_joint_names = [j.name for j in robot.get_active_joints()]
    init_qpos = compute_nominal_joint_positions(
        active_joint_names, train_cfg['nominal_joint_positions']
    )
    robot.set_qpos(init_qpos)
    
    # Extract link information
    link_info = {}
    for link in robot.get_links():
        bbox_min, bbox_max = get_local_bbox_for_link(link)
        link_info[link.name] = {
            'bbox': [bbox_min.tolist(), bbox_max.tolist()],
            'mass': link.mass,
        }
    
    # Extract joint-to-child-link mapping from URDF
    robot_urdf = URDF.load(robot_urdf_path)
    joint_to_child_link = {}
    for joint_urdf in robot_urdf.joints:
        if joint_urdf.joint_type != 'fixed':  # Only active joints
            joint_to_child_link[joint_urdf.name] = joint_urdf.child
    
    return {
        'link_info': link_info,
        'joint_to_child_link': joint_to_child_link,
    }


def process_robot(robot_name: str, asset_base_path: str = ASSET_BASE_PATH, 
                  output_filename: str = "all_robot_limb_bbox.json") -> str:
    """
    Process a single robot and save limb bbox info.
    
    Args:
        robot_name: Short name like 'Gendog0'
        asset_base_path: Base path to robot assets
        output_filename: Name of output JSON file
        
    Returns:
        Path to the saved JSON file
    """
    # Find robot folder
    robot_folder = find_robot_folder(robot_name, asset_base_path)
    
    # Get robot type to determine root link name
    robot_type, _ = parse_robot_name(robot_name)
    root_link = ROBOT_TYPE_TO_ROOT_LINK[robot_type]
    
    # Paths
    urdf_path = os.path.join(robot_folder, "robot.urdf")
    train_cfg_path = os.path.join(robot_folder, "train_cfg_v2.json")
    output_path = os.path.join(robot_folder, output_filename)
    
    # Verify required files exist
    if not os.path.exists(urdf_path):
        raise FileNotFoundError(f"URDF not found: {urdf_path}")
    if not os.path.exists(train_cfg_path):
        raise FileNotFoundError(f"Training config not found: {train_cfg_path}")
    
    # Extract limb bbox info
    info = extract_limb_bbox(urdf_path, train_cfg_path, root_link)
    
    # Add metadata
    info['robot_name'] = robot_name
    info['robot_folder'] = os.path.basename(robot_folder)
    
    # Save to file
    with open(output_path, 'w') as f:
        json.dump(info, f, indent=4)
    
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Compute limb bounding boxes for robots using SAPIEN."
    )
    parser.add_argument(
        "--robots", 
        nargs='+', 
        help="List of robot names to process (e.g., Gendog0 Gendog1 Gendog2)"
    )
    parser.add_argument(
        "--robot_type",
        choices=['dog', 'hexapod', 'humanoid'],
        help="Robot type when using --all"
    )
    parser.add_argument(
        "--all",
        action='store_true',
        help="Process all robots of the specified type"
    )
    parser.add_argument(
        "--asset_base_path",
        default=ASSET_BASE_PATH,
        help=f"Base path to robot assets (default: {ASSET_BASE_PATH})"
    )
    parser.add_argument(
        "--output_filename",
        default="all_robot_limb_bbox.json",
        help="Output filename (default: all_robot_limb_bbox.json)"
    )
    parser.add_argument(
        "--dry_run",
        action='store_true',
        help="Show what would be processed without actually processing"
    )
    
    args = parser.parse_args()
    
    # Determine which robots to process
    if args.all:
        if not args.robot_type:
            parser.error("--robot_type is required when using --all")
        robots = get_all_robot_names(args.robot_type, args.asset_base_path)
    elif args.robots:
        robots = args.robots
    else:
        parser.error("Either --robots or --all with --robot_type must be specified")
    
    print(f"Processing {len(robots)} robot(s)...")
    
    if args.dry_run:
        print("\nDry run - would process:")
        for robot_name in robots:
            try:
                robot_folder = find_robot_folder(robot_name, args.asset_base_path)
                print(f"  {robot_name}: {robot_folder}")
            except Exception as e:
                print(f"  {robot_name}: ERROR - {e}")
        return
    
    # Process each robot
    successful = []
    failed = []
    
    for robot_name in tqdm(robots, desc="Processing robots"):
        try:
            output_path = process_robot(
                robot_name, 
                args.asset_base_path,
                args.output_filename
            )
            successful.append((robot_name, output_path))
        except Exception as e:
            failed.append((robot_name, str(e)))
            print(f"\nError processing {robot_name}: {e}")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Summary: {len(successful)} successful, {len(failed)} failed")
    
    if successful:
        print(f"\nSuccessfully processed:")
        for robot_name, path in successful[:5]:  # Show first 5
            print(f"  {robot_name}: {path}")
        if len(successful) > 5:
            print(f"  ... and {len(successful) - 5} more")
    
    if failed:
        print(f"\nFailed:")
        for robot_name, error in failed:
            print(f"  {robot_name}: {error}")


if __name__ == '__main__':
    main()
