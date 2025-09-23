import sapien.core as sapien
from sapien.utils.viewer import Viewer
import json
import numpy as np
import re
from tqdm import tqdm
import os
from urdfpy import URDF
# Please use numpy 1 (e.g., 1.26); numpy 2 causes silent errors with SAPIEN

def visualize(viewer, scene, robot):
    while not viewer.closed:
        scene.update_render()
        viewer.render()


def find_link_by_name(articulation: sapien.Articulation, name: str):
    for link in articulation.get_links():
        if link.get_name() == name:
            return link
    return None


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

                x, y, z = shape.geometry.half_lengths  # TODO: this gives wrong shape for box types
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
            else:
                vertices = shape.geometry.vertices * shape.geometry.scale
            vertices = vertices @ T[:3, :3].T + T[:3, 3]
            mins = np.minimum(mins, vertices.min(0))
            maxs = np.maximum(maxs, vertices.max(0))
    return mins, maxs


def get_local_bbox_for_link(link):
    mins = np.array([np.inf, np.inf, np.inf])
    maxs = -mins
    # lp = link.pose
    for shape in link.get_collision_shapes():
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
        else:
            raise NotImplementedError(f"Unknown shape type: {shape.type}")
        mins = np.minimum(mins, vertices.min(0))
        maxs = np.maximum(maxs, vertices.max(0))
    return mins, maxs


def extract_info(robot_urdf_path, train_cfg_path, save_path, root_name):
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
    robot.set_root_pose(sapien.Pose([0, 0, train_cfg['drop_height']], [1, 0, 0, 0]))
    # joint_names = [j.name for j in robot.get_joints()]
    active_joint_names = [j.name for j in robot.get_active_joints()]
    init_qpos = compute_nominal_joint_positions(
        active_joint_names, train_cfg['nominal_joint_positions'],
    )
    robot.set_qpos(init_qpos)
    # visualize(viewer, scene, robot)

    #############################################
    # Extract information from URDF
    #############################################
    info = {}

    # Joint axis and position
    joint_info = {}
    # import ipdb; ipdb.set_trace()
    robot_urdf = URDF.load(robot_urdf_path) # sapien URDF loader does not read certain information
    # NOTE(tmu): the above line requires `pip install urdfpy && pip install --upgrade networkx`
    for i, joint in enumerate(robot.get_active_joints()):
        for joint_urdf in robot_urdf.joints:
            if joint_urdf.name == joint.name:
                break
        assert joint_urdf.name == joint.name, f"Joint {joint.name} not found in URDF"
        joint_pose = joint.get_global_pose()
        joint_axis = joint_pose.to_transformation_matrix()[:3, 0]
        joint_pos = joint_pose.p
        # print(f"===============Joint {joint.name}===============")
        # print(f"Axis: {joint_axis}")
        # print(f"Position: {joint_pos}")
        joint_info[joint.name] = {
            'axis': joint_axis.tolist(),
            'position': joint_pos.tolist(),
            'init_qpos': init_qpos[i],
            'torque_limit': joint_urdf.limit.effort,
            'velocity_limit': joint_urdf.limit.velocity,
            'damping': 'no_such_info',
            'armature': 'no_such_info',
            'stiffness': 'no_such_info',
            'friction': 'no_such_info',
            'range': joint.get_limits()[0].tolist(),
            'gains_and_action_scaling_factor': 'no_such_info',
            'mass': 'no_such_info',
        }

    info['joint_info'] = joint_info

    # Robot dimensions (3d bounding box)
    bbox = get_axis_aligned_bbox_for_articulation(robot)
    # print('================Robot Bounding Box================')
    # print(bbox)
    info['bbox'] = list([x.tolist() for x in bbox])

    # Foot information
    foot_info = {}
    for link in robot.get_links():
        if 'foot' in link.name:
            foot_info[link.name] = {
                'position': link.get_pose().p.tolist(),
                'gains_and_action_scaling_factor': 'no_such_info',
                'mass': link.mass,
                'bbox': [x.tolist() for x in get_local_bbox_for_link(link)]
            }
    info['foot_info'] = foot_info

    # Save information to file
    with open(save_path, 'w') as f:
        json.dump(info, f, indent=4)

    # #############################################
    # # Clean up
    # #############################################


if __name__ == '__main__':
    root_dir = 'gen_dogs'
    root_link_name = 'trunk'        # truck for Gendog/Genhexapod, base for go2, and pelvis for Genhumanoid 
    asset_dirs = sorted([os.path.join(root_dir, name) for name in os.listdir(root_dir) if
                  os.path.isdir(os.path.join(root_dir, name))])

    for asset_dir in tqdm(asset_dirs):
        extract_info(
            robot_urdf_path=f'{asset_dir}/robot.urdf',
            train_cfg_path=f'{asset_dir}/train_cfg_v2.json',
            save_path=f'{asset_dir}/robot_description_vec.json',
            root_name=root_link_name,
        )
