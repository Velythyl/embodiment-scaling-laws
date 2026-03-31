"""
Render point clouds and MuJoCo visualizations side by side for verification.

This script generates point clouds for selected robots and saves:
1. Point cloud renders from 9 canonical viewpoints using Open3D
2. MuJoCo renders from matching viewpoints

Usage:
    python render_geom_point_clouds.py
"""

import argparse
import gzip
import json
import os
import re
from typing import Dict, List

# Set environment for headless MuJoCo rendering BEFORE importing
os.environ['MUJOCO_GL'] = 'osmesa'

import mujoco
import numpy as np
import open3d as o3d
from PIL import Image

# Import from the point cloud generation script
from get_geom_point_clouds import extract_point_clouds, build_articulated_parts, generate_distinct_colors
from urdfpy import URDF


# 9 canonical viewpoints defined as camera parameters
# azimuth: rotation around vertical axis, elevation: angle from horizontal
VIEWPOINTS = {
    "front":    {"azim": 90,   "elev": -20, "dist": 1.5},
    "back":     {"azim": -90,  "elev": -20, "dist": 1.5},
    "left":     {"azim": 180,  "elev": -20, "dist": 1.5},
    "right":    {"azim": 0,    "elev": -20, "dist": 1.5},
    "top":      {"azim": 90,   "elev": -89, "dist": 1.5},
    "bottom":   {"azim": 90,   "elev": 89,  "dist": 1.5},
    "iso_fr":   {"azim": 45,   "elev": -30, "dist": 1.8},
    "iso_fl":   {"azim": 135,  "elev": -30, "dist": 1.8},
    "iso_back": {"azim": -135, "elev": -30, "dist": 1.8},
}


def compute_nominal_joint_positions(joint_names: List[str], nominal_positions_cfg: Dict) -> Dict[str, float]:
    """Compute nominal joint positions based on regex matching."""
    positions = {}
    for joint_name in joint_names:
        positions[joint_name] = 0.0
        for pattern, position in nominal_positions_cfg.items():
            if re.match(pattern, joint_name):
                positions[joint_name] = position
                break
    return positions


def azim_elev_to_eye(azim_deg: float, elev_deg: float, dist: float, center: np.ndarray) -> np.ndarray:
    """Convert azimuth/elevation/distance to eye position."""
    azim = np.radians(azim_deg)
    elev = np.radians(elev_deg)
    
    # Spherical to cartesian
    x = dist * np.cos(elev) * np.cos(azim)
    y = dist * np.cos(elev) * np.sin(azim)
    z = dist * np.sin(-elev)  # Negative because elevation is angle from horizontal looking down
    
    return center + np.array([x, y, z])


def render_point_cloud_view(
    pcd_points: np.ndarray,
    pcd_colors: np.ndarray,
    view_params: Dict,
    center: np.ndarray,
    width: int = 640,
    height: int = 480,
) -> np.ndarray:
    """Render point cloud from a specific viewpoint using Open3D offscreen."""
    # Create point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pcd_points)
    pcd.colors = o3d.utility.Vector3dVector(pcd_colors)
    
    # Create offscreen renderer
    renderer = o3d.visualization.rendering.OffscreenRenderer(width, height)
    renderer.scene.set_background([1.0, 1.0, 1.0, 1.0])  # White background
    
    # Add point cloud with material
    mat = o3d.visualization.rendering.MaterialRecord()
    mat.shader = "defaultUnlit"
    mat.point_size = 5.0
    renderer.scene.add_geometry("pcd", pcd, mat)
    
    # Add coordinate axes for reference
    axes = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.15)
    renderer.scene.add_geometry("axes", axes, o3d.visualization.rendering.MaterialRecord())
    
    # Compute eye position from azim/elev/dist
    eye = azim_elev_to_eye(view_params["azim"], view_params["elev"], view_params["dist"], center)
    up = np.array([0, 0, 1])
    
    renderer.setup_camera(60.0, center, eye, up)
    
    # Render
    img = renderer.render_to_image()
    return np.asarray(img)


def setup_mujoco_model(
    urdf_path: str,
    train_cfg: Dict,
    width: int = 640,
    height: int = 480,
):
    """Load MuJoCo model and set up nominal pose. Returns model, data, center."""
    try:
        model = mujoco.MjModel.from_xml_path(urdf_path)
    except Exception as e:
        print(f"    Failed to load URDF in MuJoCo: {e}")
        return None, None, np.array([0, 0, 0])
    
    data = mujoco.MjData(model)
    
    # Set nominal joint positions
    nominal_cfg = train_cfg.get('nominal_joint_positions', {})
    joint_names = []
    for i in range(model.njnt):
        joint_names.append(model.joint(i).name)
    
    positions = compute_nominal_joint_positions(joint_names, nominal_cfg)
    
    for i in range(model.njnt):
        joint_name = model.joint(i).name
        if joint_name in positions:
            qpos_adr = model.jnt_qposadr[i]
            data.qpos[qpos_adr] = positions[joint_name]
    
    mujoco.mj_forward(model, data)
    
    # Get robot center
    body_positions = []
    for i in range(model.nbody):
        body_positions.append(data.xpos[i])
    center = np.mean(body_positions, axis=0) if body_positions else np.zeros(3)
    
    return model, data, center


def render_mujoco_view(
    urdf_path: str,
    train_cfg: Dict,
    view_params: Dict,
    width: int = 640,
    height: int = 480,
) -> np.ndarray:
    """Render robot in MuJoCo from a specific viewpoint."""
    model, data, center = setup_mujoco_model(urdf_path, train_cfg, width, height)
    
    if model is None:
        img = np.ones((height, width, 3), dtype=np.uint8) * 255
        return img, center
    
    # Create renderer
    renderer = mujoco.Renderer(model, height, width)
    
    # Set up camera
    cam = mujoco.MjvCamera()
    cam.lookat[:] = center
    cam.distance = view_params["dist"]
    cam.azimuth = view_params["azim"]
    cam.elevation = view_params["elev"]
    
    renderer.update_scene(data, camera=cam)
    img = renderer.render()
    renderer.close()
    
    return img, center


def render_mujoco_segmented_view(
    urdf_path: str,
    train_cfg: Dict,
    view_params: Dict,
    part_colors: Dict[str, List[float]],
    parts: Dict[str, List[str]],
    width: int = 640,
    height: int = 480,
) -> np.ndarray:
    """
    Render robot in MuJoCo with limb-segmented colors matching point cloud colors.
    
    Args:
        urdf_path: Path to URDF
        train_cfg: Training config dict
        view_params: Camera view parameters
        part_colors: Dict mapping part name to RGB color (0-1 range)
        parts: Dict mapping part name to list of link names
    """
    model, data, center = setup_mujoco_model(urdf_path, train_cfg, width, height)
    
    if model is None:
        img = np.ones((height, width, 3), dtype=np.uint8) * 255
        return img, center
    
    # Build reverse mapping: link_name -> part_name
    link_to_part = {}
    for part_name, link_names in parts.items():
        for link_name in link_names:
            link_to_part[link_name] = part_name
    
    # Build mapping: MuJoCo body_id -> part_name
    body_to_part = {}
    for i in range(model.nbody):
        body_name = model.body(i).name
        if body_name in link_to_part:
            body_to_part[i] = link_to_part[body_name]
    
    # Set geom colors based on their parent body's part
    for i in range(model.ngeom):
        body_id = model.geom_bodyid[i]
        if body_id in body_to_part:
            part_name = body_to_part[body_id]
            if part_name in part_colors:
                color = part_colors[part_name]
                model.geom_rgba[i] = [color[0], color[1], color[2], 1.0]
    
    # Forward kinematics again with updated colors
    mujoco.mj_forward(model, data)
    
    # Create renderer
    renderer = mujoco.Renderer(model, height, width)
    
    # Set up camera
    cam = mujoco.MjvCamera()
    cam.lookat[:] = center
    cam.distance = view_params["dist"]
    cam.azimuth = view_params["azim"]
    cam.elevation = view_params["elev"]
    
    renderer.update_scene(data, camera=cam)
    img = renderer.render()
    renderer.close()
    
    return img, center


def process_robot(
    urdf_path: str,
    train_cfg_path: str,
    output_dir: str,
    robot_type: str,
    points_per_geom: int = 300,
):
    """Process a single robot: generate point clouds and renders."""
    print(f"\nProcessing {robot_type}: {os.path.basename(os.path.dirname(urdf_path))}")
    
    # Load train config
    with open(train_cfg_path, 'r') as f:
        train_cfg = json.load(f)
    
    # Determine root link name
    root_link_name = "pelvis" if "humanoid" in robot_type.lower() else "trunk"
    
    # Generate point clouds
    print("  Generating point clouds...")
    pcd_data = extract_point_clouds(
        urdf_path=urdf_path,
        train_cfg_path=train_cfg_path,
        points_per_geom=points_per_geom,
        root_link_name=root_link_name,
        store_per_part_points=True
    )
    
    # Extract full point cloud
    full_points = np.array(pcd_data[">FULL<"]["pcd_points"])
    full_colors = np.array(pcd_data[">FULL<"]["pcd_colors"])
    
    print(f"  Total points: {len(full_points)}")
    
    # Load URDF to get parts mapping for segmented rendering
    urdf = URDF.load(urdf_path)
    parts = build_articulated_parts(urdf)
    
    # Extract part colors from pcd_data
    part_colors = {}
    part_names = sorted(parts.keys())
    for part_name in part_names:
        if part_name in pcd_data and "color" in pcd_data[part_name]:
            part_colors[part_name] = pcd_data[part_name]["color"]
    
    print(f"  Parts: {list(part_colors.keys())}")
    
    # Create output directory
    render_dir = os.path.join(output_dir, "renders")
    os.makedirs(render_dir, exist_ok=True)
    
    # First render MuJoCo to get the center point
    print("  Getting robot center from MuJoCo...")
    first_view = list(VIEWPOINTS.values())[0]
    _, center = render_mujoco_view(urdf_path, train_cfg, first_view)
    print(f"  Robot center: {center}")
    
    # Render from all viewpoints
    for view_name, view_params in VIEWPOINTS.items():
        print(f"  Rendering view: {view_name}")
        
        # Render MuJoCo (original colors)
        mj_img, _ = render_mujoco_view(urdf_path, train_cfg, view_params)
        mj_path = os.path.join(render_dir, f"mujoco_{view_name}.png")
        Image.fromarray(mj_img).save(mj_path)
        
        # Render MuJoCo (segmented with limb colors)
        mj_seg_img, _ = render_mujoco_segmented_view(
            urdf_path, train_cfg, view_params, part_colors, parts
        )
        mj_seg_path = os.path.join(render_dir, f"mujoco_seg_{view_name}.png")
        Image.fromarray(mj_seg_img).save(mj_seg_path)
        
        # Render point cloud with same camera params
        pcd_img = render_point_cloud_view(
            full_points, full_colors, view_params, center
        )
        pcd_path = os.path.join(render_dir, f"pcd_{view_name}.png")
        Image.fromarray(pcd_img).save(pcd_path)
    
    # Create comparison grid
    print("  Creating comparison grid...")
    create_comparison_grid(render_dir, robot_type)
    
    print(f"  Saved renders to: {render_dir}")


def create_comparison_grid(render_dir: str, robot_type: str):
    """Create a side-by-side comparison grid of PCD vs MuJoCo (original) vs MuJoCo (segmented) renders."""
    views = list(VIEWPOINTS.keys())
    
    pcd_images = []
    mj_images = []
    mj_seg_images = []
    
    for view_name in views:
        pcd_path = os.path.join(render_dir, f"pcd_{view_name}.png")
        mj_path = os.path.join(render_dir, f"mujoco_{view_name}.png")
        mj_seg_path = os.path.join(render_dir, f"mujoco_seg_{view_name}.png")
        
        if os.path.exists(pcd_path):
            pcd_images.append(Image.open(pcd_path))
        if os.path.exists(mj_path):
            mj_images.append(Image.open(mj_path))
        if os.path.exists(mj_seg_path):
            mj_seg_images.append(Image.open(mj_seg_path))
    
    if not pcd_images or not mj_images:
        return
    
    # Get image dimensions
    img_w, img_h = pcd_images[0].size
    
    # Create 3x3 grid for each type, then stack horizontally
    grid_w = 3
    grid_h = 3
    
    pcd_grid = Image.new('RGB', (img_w * grid_w, img_h * grid_h), (255, 255, 255))
    mj_grid = Image.new('RGB', (img_w * grid_w, img_h * grid_h), (255, 255, 255))
    mj_seg_grid = Image.new('RGB', (img_w * grid_w, img_h * grid_h), (255, 255, 255))
    
    for i, pcd_img in enumerate(pcd_images):
        row = i // grid_w
        col = i % grid_w
        pcd_grid.paste(pcd_img, (col * img_w, row * img_h))
    
    for i, mj_img in enumerate(mj_images):
        row = i // grid_w
        col = i % grid_w
        mj_grid.paste(mj_img, (col * img_w, row * img_h))
    
    for i, mj_seg_img in enumerate(mj_seg_images):
        row = i // grid_w
        col = i % grid_w
        mj_seg_grid.paste(mj_seg_img, (col * img_w, row * img_h))
    
    # Combine all three side by side with gaps
    gap = 20
    num_panels = 3
    combined = Image.new('RGB', (img_w * grid_w * num_panels + gap * (num_panels - 1), img_h * grid_h), (200, 200, 200))
    combined.paste(pcd_grid, (0, 0))
    combined.paste(mj_seg_grid, (img_w * grid_w + gap, 0))
    combined.paste(mj_grid, (img_w * grid_w * 2 + gap * 2, 0))
    
    combined.save(os.path.join(render_dir, f"comparison_{robot_type}.png"))
    
    # Also save labeled version
    try:
        from PIL import ImageDraw, ImageFont
        draw = ImageDraw.Draw(combined)
        # Try to use a font, fall back to default
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        except:
            font = ImageFont.load_default()
        draw.text((10, 10), "Point Cloud (urdfpy FK)", fill=(0, 0, 0), font=font)
        draw.text((img_w * grid_w + gap + 10, 10), "MuJoCo Segmented", fill=(0, 0, 0), font=font)
        draw.text((img_w * grid_w * 2 + gap * 2 + 10, 10), "MuJoCo Original", fill=(0, 0, 0), font=font)
        combined.save(os.path.join(render_dir, f"comparison_{robot_type}_labeled.png"))
    except Exception as e:
        print(f"  Warning: Could not add labels: {e}")


def main():
    parser = argparse.ArgumentParser(description="Render point cloud vs MuJoCo comparisons")
    parser.add_argument("--points_per_geom", type=int, default=300,
                        help="Points per geometry primitive")
    
    # Get workspace root (two directories up from generation/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.dirname(script_dir)
    default_base = os.path.join(workspace_root, "exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/Robots/GenBot1K-v7")
    
    parser.add_argument("--base_path", type=str,
                        default=default_base,
                        help="Base path to robot assets")
    args = parser.parse_args()
    
    # Select one robot of each type
    robots = {
        "dog": {
            "dir": "gen_dogs/gendog_1_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_2",
        },
        "hexapod": {
            "dir": "gen_hexapods/genhexapod_0_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_0",
        },
        "humanoid": {
            "dir": "gen_humanoids/genhumanoid_0_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_0",
        },
    }
    
    for robot_type, info in robots.items():
        robot_dir = os.path.join(args.base_path, info["dir"])
        urdf_path = os.path.join(robot_dir, "robot.urdf")
        train_cfg_path = os.path.join(robot_dir, "train_cfg_v2.json")
        
        if not os.path.exists(train_cfg_path):
            train_cfg_path = os.path.join(robot_dir, "train_cfg.json")
        
        if not os.path.exists(urdf_path):
            print(f"Warning: URDF not found: {urdf_path}")
            continue
        
        process_robot(
            urdf_path=urdf_path,
            train_cfg_path=train_cfg_path,
            output_dir=robot_dir,
            robot_type=robot_type,
            points_per_geom=args.points_per_geom,
        )
    
    print("\nDone! Check the 'renders' folder in each robot directory.")
    print("\nComparison images saved as 'comparison_<robot_type>_labeled.png'")
    print("Left side = Point Cloud (our urdfpy FK), Right side = MuJoCo rendering")


if __name__ == "__main__":
    main()
