import sapien.core as sapien
from sapien.utils.viewer import Viewer
import json
import numpy as np
import re
from tqdm import tqdm
import os


def visualize(viewer, scene, robot):
    while not viewer.closed:
        scene.update_render()
        viewer.render()

# Function to compute nominal joint positions based on regex matching
def compute_nominal_joint_positions(joint_names, nominal_positions_cfg):
    """
    Computes nominal joint positions for each joint based on regex patterns from configuration.

    Args:
        joint_names (list): List of joint names.
        nominal_positions_cfg (dict): Configuration with regex patterns and their respective nominal positions.

    Returns:
        np.ndarray: Nominal joint positions in the correct order.
    """
    nominal_positions = np.zeros(len(joint_names))
    for idx, joint in enumerate(joint_names):
        for pattern, position in nominal_positions_cfg.items():
            if re.match(pattern, joint):
                nominal_positions[idx] = position
                break
    return nominal_positions


def get_axis_aligned_bbox_for_articulation(art: sapien.Articulation):
    mins = np.array([np.inf, np.inf, np.inf])
    maxs = -mins
    for link in art.get_links():
        lp = link.pose
        for shape in link.get_collision_shapes():
            p = lp * shape.get_local_pose()
            T = p.to_transformation_matrix()
            # print(shape.type)
            if shape.type == 'box':
                x, y, z = shape.geometry.half_lengths
                vertices = np.array([
                    [x, y, z], [x, y, -z], [x, -y, z], [x, -y, -z],
                    [-x, y, z], [-x, y, -z], [-x, -y, z], [-x, -y, -z]
                ])
            elif shape.type == 'sphere':
                x = y = z = shape.geometry.radius
                vertices = np.array([
                    [x, y, z], [x, y, -z], [x, -y, z], [x, -y, -z],
                    [-x, y, z], [-x, y, -z], [-x, -y, z], [-x, -y, -z]
                ])
            elif shape.type == 'capsule':
                x = y = shape.geometry.radius
                z = shape.geometry.half_length
                vertices = np.array([
                    [x, y, z], [x, y, -z], [x, -y, z], [x, -y, -z],
                    [-x, y, z], [-x, y, -z], [-x, -y, z], [-x, -y, -z]
                ])
            else:
                vertices = shape.geometry.vertices * shape.geometry.scale
            vertices = vertices @ T[:3, :3].T + T[:3, 3]
            mins = np.minimum(mins, vertices.min(0))
            maxs = np.maximum(maxs, vertices.max(0))
    return mins, maxs


def update_height(robot_urdf_path, train_cfg_path, save_path, root_name):
    #############################################
    # Set up the engine, renderer and scene
    #############################################
    engine = sapien.Engine()
    renderer = sapien.SapienRenderer()
    engine.set_renderer(renderer)

    scene_config = sapien.SceneConfig()
    scene = engine.create_scene(scene_config)
    scene.set_timestep(1 / 240.0)
    scene.add_ground(0)

    scene.set_ambient_light([0.5, 0.5, 0.5])
    scene.add_directional_light([0, 1, -1], [0.5, 0.5, 0.5])

    viewer = Viewer(renderer)
    viewer.set_scene(scene)
    viewer.set_camera_xyz(x=-2, y=0, z=1)
    viewer.set_camera_rpy(r=0, p=-0.3, y=0)

    #############################################
    # Load robot URDF
    #############################################
    loader: sapien.URDFLoader = scene.create_urdf_loader()
    loader.fix_root_link = False
    robot: sapien.Articulation = loader.load(robot_urdf_path)

    #############################################
    # Set robot pose and initial joint positions
    #############################################
    with open(train_cfg_path, "r") as f:
        train_cfg = json.load(f)
    assert robot.get_links()[0].name == root_name, f"Root link is not {root_name}"
    robot.set_root_pose(sapien.Pose([0, 0, 0], [1, 0, 0, 0]))
    # joint_names = [j.name for j in robot.get_joints()]
    active_joint_names = [j.name for j in robot.get_active_joints()]
    init_qpos = compute_nominal_joint_positions(
        active_joint_names, train_cfg['nominal_joint_positions'],
    )
    robot.set_qpos(init_qpos)
    # visualize(viewer, scene, robot)

    #############################################
    # Update height
    #############################################
    
    # Robot dimensions (3d bounding box)
    mins, maxs = get_axis_aligned_bbox_for_articulation(robot)
    z_lower_bound = mins[2]
    robot.set_root_pose(sapien.Pose([0, 0, -z_lower_bound], [1, 0, 0, 0]))
    # visualize(viewer, scene, robot)


    # Save information to file
    train_cfg['drop_height'] = -z_lower_bound
    with open(save_path, 'w') as f:
        json.dump(train_cfg, f, indent=4)


    #############################################
    # Clean up
    #############################################

    viewer.close()


if __name__ == '__main__':
    root_dir = "gen_humanoids"
    asset_dirs = [os.path.join(root_dir, name) for name in os.listdir(root_dir) if
                  os.path.isdir(os.path.join(root_dir, name))]

    for asset_dir in tqdm(asset_dirs):
        update_height(
            robot_urdf_path=f'{asset_dir}/robot.urdf',
            train_cfg_path=f'{asset_dir}/train_cfg.json',
            save_path=f'{asset_dir}/train_cfg_v2.json',
            root_name="pelvis",  # trunk for dogs and hexapods, pelvis for humanoids
        )
