"""
Extract per-limb point clouds from robot URDF files.

This script generates limb-segmented point clouds for robots, where:
- Each articulated "part" (links connected by fixed joints) gets its own point cloud
- The >FULL< entry contains the concatenated point cloud of all parts with per-limb colors
- Point clouds are sampled from the actual geometry surfaces (primitives or meshes)

Output format (gzipped JSON):
{
    ">ORIGINAL XML<": {"color": "all", "pcd_points": [...], "pcd_colors": [...]},
    ">FULL<": {"color": "all", "pcd_points": [...], "pcd_colors": [...]},
    "part_name_1": {"color": [r, g, b]},
    "part_name_2": {"color": [r, g, b]},
    ...
    ">NO_ACTUATORS<": {"color": [0, 0, 0]}
}

Usage:
    python get_geom_point_clouds.py --root_dir gen_dogs --output_suffix _pcd
    python get_geom_point_clouds.py --urdf_path path/to/robot.urdf --train_cfg_path path/to/train_cfg.json
"""

import argparse
import gzip
import json
import os
import re
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

import numpy as np
import open3d as o3d
from tqdm import tqdm
from urdfpy import URDF


def create_box_mesh(size: List[float]) -> o3d.geometry.TriangleMesh:
    """Create an Open3D box mesh centered at origin."""
    mesh = o3d.geometry.TriangleMesh.create_box(
        width=size[0], height=size[1], depth=size[2]
    )
    # Center the box at origin (Open3D creates box with corner at origin)
    mesh.translate([-size[0] / 2, -size[1] / 2, -size[2] / 2])
    return mesh


def create_cylinder_mesh(radius: float, length: float, resolution: int = 30) -> o3d.geometry.TriangleMesh:
    """Create an Open3D cylinder mesh centered at origin, aligned with Z axis."""
    mesh = o3d.geometry.TriangleMesh.create_cylinder(
        radius=radius, height=length, resolution=resolution
    )
    return mesh


def create_sphere_mesh(radius: float, resolution: int = 20) -> o3d.geometry.TriangleMesh:
    """Create an Open3D sphere mesh centered at origin."""
    mesh = o3d.geometry.TriangleMesh.create_sphere(radius=radius, resolution=resolution)
    return mesh


def create_capsule_mesh(radius: float, length: float, resolution: int = 20) -> o3d.geometry.TriangleMesh:
    """Create a capsule mesh (cylinder with hemispherical caps) centered at origin."""
    # Create cylinder
    cylinder = o3d.geometry.TriangleMesh.create_cylinder(
        radius=radius, height=length, resolution=resolution
    )
    
    # Create two hemispheres
    sphere_top = o3d.geometry.TriangleMesh.create_sphere(radius=radius, resolution=resolution)
    sphere_bottom = o3d.geometry.TriangleMesh.create_sphere(radius=radius, resolution=resolution)
    
    # Position hemispheres at cylinder ends
    sphere_top.translate([0, 0, length / 2])
    sphere_bottom.translate([0, 0, -length / 2])
    
    # Combine meshes
    mesh = cylinder + sphere_top + sphere_bottom
    return mesh


def rpy_to_rotation_matrix(rpy: List[float]) -> np.ndarray:
    """Convert roll-pitch-yaw angles to rotation matrix."""
    roll, pitch, yaw = rpy
    
    # Rotation matrices
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll), np.cos(roll)]
    ])
    Ry = np.array([
        [np.cos(pitch), 0, np.sin(pitch)],
        [0, 1, 0],
        [-np.sin(pitch), 0, np.cos(pitch)]
    ])
    Rz = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw), np.cos(yaw), 0],
        [0, 0, 1]
    ])
    
    return Rz @ Ry @ Rx


def geometry_to_mesh(visual_or_collision, urdf_dir: str) -> Optional[o3d.geometry.TriangleMesh]:
    """Convert urdfpy visual/collision geometry to Open3D mesh.
    
    The urdfpy Geometry object has properties (box, cylinder, sphere, mesh)
    that return the actual shape object or None.
    """
    geom = visual_or_collision.geometry
    
    if geom.box is not None:
        return create_box_mesh(geom.box.size.tolist())
    elif geom.cylinder is not None:
        return create_cylinder_mesh(geom.cylinder.radius, geom.cylinder.length)
    elif geom.sphere is not None:
        return create_sphere_mesh(geom.sphere.radius)
    elif geom.mesh is not None:
        # Load mesh file
        mesh_path = geom.mesh.filename
        if not os.path.isabs(mesh_path):
            mesh_path = os.path.join(urdf_dir, mesh_path)
        
        # Try loading with alternative extensions if needed
        mesh = None
        paths_to_try = [mesh_path]
        
        # If it's a .dae file, also try .obj (Open3D can't read .dae)
        if mesh_path.lower().endswith('.dae'):
            paths_to_try.append(mesh_path[:-4] + '.obj')
        
        for try_path in paths_to_try:
            if os.path.exists(try_path):
                mesh = o3d.io.read_triangle_mesh(try_path)
                if mesh.has_triangles():
                    break
                mesh = None
        
        if mesh is not None and mesh.has_triangles():
            # Apply scale if specified
            if geom.mesh.scale is not None:
                scale = geom.mesh.scale
                if hasattr(scale, '__len__'):
                    mesh.scale(scale[0], center=[0, 0, 0])  # Use first scale component
                else:
                    mesh.scale(scale, center=[0, 0, 0])
            return mesh
        else:
            print(f"Warning: Mesh file not found or empty: {mesh_path}")
            return None
    else:
        print(f"Warning: Unknown or empty geometry")
        return None


def transform_mesh(mesh: o3d.geometry.TriangleMesh, origin) -> o3d.geometry.TriangleMesh:
    """Apply origin transformation (xyz + rpy) to mesh."""
    if origin is None:
        return mesh
    
    # Get translation and rotation from origin
    xyz = origin[:3, 3] if origin.shape == (4, 4) else [0, 0, 0]
    
    if origin.shape == (4, 4):
        # origin is already a 4x4 transformation matrix
        mesh.transform(origin)
    else:
        # Handle as separate xyz and rpy (shouldn't happen with urdfpy)
        mesh.translate(xyz)
    
    return mesh


def compute_nominal_joint_positions(joint_names: List[str], nominal_positions_cfg: Dict) -> Dict[str, float]:
    """Compute nominal joint positions based on regex matching."""
    positions = {}
    for joint_name in joint_names:
        positions[joint_name] = 0.0  # Default
        for pattern, position in nominal_positions_cfg.items():
            if re.match(pattern, joint_name):
                positions[joint_name] = position
                break
    return positions


def get_link_transform(urdf: URDF, link_name: str, joint_positions: Dict[str, float]) -> np.ndarray:
    """Compute world transform for a link given joint positions."""
    # Use urdfpy's forward kinematics
    fk = urdf.link_fk(cfg=joint_positions)
    
    for link, transform in fk.items():
        if link.name == link_name:
            return transform
    
    # If not found, return identity
    return np.eye(4)


def build_articulated_parts(urdf: URDF) -> Dict[str, List[str]]:
    """
    Group links into articulated parts based on joint types.
    Links connected by fixed joints are grouped together.
    The part is named after the first actuated joint leading to it.
    
    Returns:
        Dict mapping part name to list of link names in that part.
    """
    # Build parent-child relationships
    link_to_parent_joint = {}
    for joint in urdf.joints:
        link_to_parent_joint[joint.child] = joint
    
    # Find the root link (no parent joint)
    all_children = {joint.child for joint in urdf.joints}
    root_links = [link.name for link in urdf.links if link.name not in all_children]
    
    # For each link, trace back to find the last non-fixed joint
    link_to_part = {}
    
    def get_part_name(link_name: str) -> str:
        """Get the part name for a link by tracing back through joints."""
        if link_name in root_links:
            return "trunk"  # Root part
        
        current = link_name
        last_actuated_joint = None
        
        while current in link_to_parent_joint:
            joint = link_to_parent_joint[current]
            if joint.joint_type != 'fixed':
                last_actuated_joint = joint.name
                break
            current = joint.parent
        
        if last_actuated_joint is None:
            # All joints to root are fixed, link belongs to trunk
            return "trunk"
        
        return last_actuated_joint
    
    # Group links by part
    parts = defaultdict(list)
    for link in urdf.links:
        part_name = get_part_name(link.name)
        parts[part_name].append(link.name)
        link_to_part[link.name] = part_name
    
    return dict(parts)


def sample_point_cloud(mesh: o3d.geometry.TriangleMesh, num_points: int = 1000) -> np.ndarray:
    """Sample points uniformly from mesh surface."""
    if mesh is None or not mesh.has_triangles():
        return np.array([]).reshape(0, 3)
    
    # Ensure mesh has valid triangles
    mesh.compute_vertex_normals()
    
    try:
        pcd = mesh.sample_points_uniformly(number_of_points=num_points)
        return np.asarray(pcd.points)
    except Exception as e:
        print(f"Warning: Failed to sample points: {e}")
        return np.array([]).reshape(0, 3)


def generate_distinct_colors(n: int) -> List[List[float]]:
    """Generate n visually distinct colors using HSV color space."""
    colors = []
    for i in range(n):
        hue = i / n
        # Convert HSV to RGB (saturation=1, value=1)
        h = hue * 6
        x = 1 - abs(h % 2 - 1)
        
        if h < 1:
            rgb = [1, x, 0]
        elif h < 2:
            rgb = [x, 1, 0]
        elif h < 3:
            rgb = [0, 1, x]
        elif h < 4:
            rgb = [0, x, 1]
        elif h < 5:
            rgb = [x, 0, 1]
        else:
            rgb = [1, 0, x]
        
        colors.append(rgb)
    
    return colors


def extract_point_clouds(
    urdf_path: str,
    train_cfg_path: str,
    points_per_geom: int = 500,
    root_link_name: str = "trunk",
    store_per_part_points: bool = False
) -> Dict:
    """
    Extract per-limb point clouds from a robot URDF.
    
    Args:
        urdf_path: Path to robot URDF file
        train_cfg_path: Path to training config JSON with nominal joint positions
        points_per_geom: Number of points to sample per geometry primitive
        root_link_name: Name of the root link (trunk, pelvis, etc.)
        store_per_part_points: If True, store point clouds directly in each part entry
    
    Returns:
        Dictionary in the target format for gzipped JSON output.
    """
    # Load URDF
    urdf_dir = os.path.dirname(urdf_path)
    urdf = URDF.load(urdf_path)
    
    # Load training config for nominal positions
    with open(train_cfg_path, 'r') as f:
        train_cfg = json.load(f)
    
    # Get joint names and compute nominal positions
    joint_names = [j.name for j in urdf.joints if j.joint_type != 'fixed']
    nominal_cfg = train_cfg.get('nominal_joint_positions', {})
    joint_positions = compute_nominal_joint_positions(joint_names, nominal_cfg)
    
    # Build articulated parts (group fixed-joint links)
    parts = build_articulated_parts(urdf)
    
    # Generate colors for each part
    part_names = sorted(parts.keys())
    colors = generate_distinct_colors(len(part_names))
    part_colors = {name: colors[i] for i, name in enumerate(part_names)}
    
    # Compute FK for all links
    fk = urdf.link_fk(cfg=joint_positions)
    link_transforms = {link.name: transform for link, transform in fk.items()}
    
    # Extract point clouds for each part
    part_point_clouds = {}
    
    for part_name, link_names in parts.items():
        part_points = []
        
        for link_name in link_names:
            # Find the link object
            link = None
            for l in urdf.links:
                if l.name == link_name:
                    link = l
                    break
            
            if link is None:
                continue
            
            # Get link transform
            link_transform = link_transforms.get(link_name, np.eye(4))
            
            # Process visual geometries (prefer visual over collision for point clouds)
            geometries = link.visuals if link.visuals else link.collisions
            
            for geom in geometries:
                # Create mesh from geometry
                mesh = geometry_to_mesh(geom, urdf_dir)
                if mesh is None:
                    continue
                
                # Apply geometry origin transform
                if geom.origin is not None:
                    mesh.transform(geom.origin)
                
                # Apply link world transform
                mesh.transform(link_transform)
                
                # Sample points
                points = sample_point_cloud(mesh, points_per_geom)
                if len(points) > 0:
                    part_points.append(points)
        
        if part_points:
            part_point_clouds[part_name] = np.vstack(part_points)
        else:
            part_point_clouds[part_name] = np.array([]).reshape(0, 3)
    
    # Build output dictionary
    output = {}
    
    # Collect all points with colors for >FULL<
    all_points = []
    all_colors = []
    
    for part_name in part_names:
        points = part_point_clouds.get(part_name, np.array([]).reshape(0, 3))
        color = part_colors[part_name]
        
        if len(points) > 0:
            all_points.append(points)
            all_colors.extend([color] * len(points))
    
    if all_points:
        full_points = np.vstack(all_points)
    else:
        full_points = np.array([]).reshape(0, 3)
    
    # >ORIGINAL XML< - same as >FULL< for our case (no XML parsing difference)
    output[">ORIGINAL XML<"] = {
        "color": "all",
        "pcd_points": full_points.tolist(),
        "pcd_colors": all_colors
    }
    
    # >FULL< - the full robot point cloud with per-limb colors
    output[">FULL<"] = {
        "color": "all",
        "pcd_points": full_points.tolist(),
        "pcd_colors": all_colors
    }
    
    # Individual parts (store color and optionally points)
    for part_name in part_names:
        part_entry = {
            "color": part_colors[part_name]
        }
        if store_per_part_points:
            points = part_point_clouds.get(part_name, np.array([]).reshape(0, 3))
            part_entry["pcd_points"] = points.tolist()
        output[part_name] = part_entry
    
    # >NO_ACTUATORS< - for links with no actuators (using black color)
    output[">NO_ACTUATORS<"] = {
        "color": [0, 0, 0]
    }
    
    return output


def save_gzipped_json(data: Dict, output_path: str):
    """Save dictionary as gzipped JSON (with .json extension)."""
    with gzip.open(output_path, 'wt', encoding='utf-8') as f:
        json.dump(data, f)


def process_robot(
    urdf_path: str,
    train_cfg_path: str,
    output_path: str,
    points_per_geom: int = 500,
    root_link_name: str = "trunk",
    store_per_part_points: bool = False
):
    """Process a single robot and save point cloud JSON."""
    data = extract_point_clouds(
        urdf_path=urdf_path,
        train_cfg_path=train_cfg_path,
        points_per_geom=points_per_geom,
        root_link_name=root_link_name,
        store_per_part_points=store_per_part_points
    )
    save_gzipped_json(data, output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Extract per-limb point clouds from robot URDF files."
    )
    parser.add_argument(
        "--urdf_path", type=str, default=None,
        help="Path to a single URDF file to process"
    )
    parser.add_argument(
        "--train_cfg_path", type=str, default=None,
        help="Path to training config JSON with nominal joint positions"
    )
    parser.add_argument(
        "--output_path", type=str, default=None,
        help="Output path for gzipped JSON (used with --urdf_path)"
    )
    parser.add_argument(
        "--root_dir", type=str, default=None,
        help="Directory containing robot assets (gen_dogs, gen_hexapods, gen_humanoids)"
    )
    parser.add_argument(
        "--root_link_name", type=str, default=None,
        help="Name of root link (default: trunk for dogs/hexapods, pelvis for humanoids)"
    )
    parser.add_argument(
        "--output_suffix", type=str, default="_pcd",
        help="Suffix for output file (e.g., '_pcd' for robot_pcd.json)"
    )
    parser.add_argument(
        "--points_per_geom", type=int, default=500,
        help="Number of points to sample per geometry primitive"
    )
    parser.add_argument(
        "--store_per_part_points", action="store_true",
        help="Store per-part point clouds directly in addition to colors"
    )
    parser.add_argument(
        "--dry_run", action="store_true",
        help="Print what would be done without actually doing it"
    )
    args = parser.parse_args()
    
    if args.urdf_path:
        # Single file mode
        if args.train_cfg_path is None:
            raise ValueError("--train_cfg_path required when using --urdf_path")
        
        output_path = args.output_path
        if output_path is None:
            output_path = args.urdf_path.replace('.urdf', f'{args.output_suffix}.json')
        
        root_link_name = args.root_link_name or "trunk"
        
        if args.dry_run:
            print(f"[DRY RUN] Would process: {args.urdf_path}")
            print(f"[DRY RUN] Output: {output_path}")
        else:
            print(f"Processing: {args.urdf_path}")
            process_robot(
                urdf_path=args.urdf_path,
                train_cfg_path=args.train_cfg_path,
                output_path=output_path,
                points_per_geom=args.points_per_geom,
                root_link_name=root_link_name,
                store_per_part_points=args.store_per_part_points
            )
            print(f"Saved: {output_path}")
    
    elif args.root_dir:
        # Batch mode - process all robots in directory
        
        # Default root link name based on robot type
        if args.root_link_name is None:
            if 'humanoid' in args.root_dir.lower():
                root_link_name = 'pelvis'
            else:
                root_link_name = 'trunk'
        else:
            root_link_name = args.root_link_name
        
        # Find all robot directories
        asset_dirs = sorted([
            os.path.join(args.root_dir, name)
            for name in os.listdir(args.root_dir)
            if os.path.isdir(os.path.join(args.root_dir, name))
        ])
        
        output_filename = f'robot{args.output_suffix}.json'
        
        if args.dry_run:
            print(f"[DRY RUN] Would process {len(asset_dirs)} robots in {args.root_dir}")
            print(f"[DRY RUN] Root link name: {root_link_name}")
            print(f"[DRY RUN] Output filename: {output_filename}")
            print(f"[DRY RUN] Points per geometry: {args.points_per_geom}")
            print(f"[DRY RUN] Store per-part points: {args.store_per_part_points}")
            print(f"[DRY RUN] Sample directories: {asset_dirs[:3]}")
        else:
            for asset_dir in tqdm(asset_dirs, desc="Processing robots"):
                urdf_path = os.path.join(asset_dir, 'robot.urdf')
                train_cfg_path = os.path.join(asset_dir, 'train_cfg_v2.json')
                output_path = os.path.join(asset_dir, output_filename)
                
                if not os.path.exists(urdf_path):
                    print(f"Warning: URDF not found: {urdf_path}")
                    continue
                
                if not os.path.exists(train_cfg_path):
                    # Try fallback
                    train_cfg_path = os.path.join(asset_dir, 'train_cfg.json')
                    if not os.path.exists(train_cfg_path):
                        print(f"Warning: Train config not found for {asset_dir}")
                        continue
                
                try:
                    process_robot(
                        urdf_path=urdf_path,
                        train_cfg_path=train_cfg_path,
                        output_path=output_path,
                        points_per_geom=args.points_per_geom,
                        root_link_name=root_link_name,
                        store_per_part_points=args.store_per_part_points
                    )
                except Exception as e:
                    print(f"Error processing {asset_dir}: {e}")
    
    else:
        parser.print_help()
        print("\nError: Either --urdf_path or --root_dir must be specified.")
