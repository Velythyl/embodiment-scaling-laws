import os
import re
from xml.etree import ElementTree as ET
import json

def read_urdf_and_verify_terms(urdf_path, term_patterns):
    """
    Reads the URDF file and verifies if given term patterns match any elements in the URDF.

    Args:
        urdf_path (str): Path to the URDF file.
        term_patterns (dict): Dictionary with term names as keys and regex patterns as values.

    Returns:
        dict: Dictionary with term names as keys and boolean values indicating if the term exists.
    """
    term_matches = {term: False for term in term_patterns}

    if not os.path.exists(urdf_path):
        return term_matches  # Return as false for all if URDF file does not exist

    try:
        # Parse the URDF XML
        tree = ET.parse(urdf_path)
        root = tree.getroot()

        # Search for matching terms in URDF elements
        for element in root.iter():
            for term, pattern in term_patterns.items():
                if re.search(pattern, element.tag) or re.search(pattern, str(element.attrib)):
                    term_matches[term] = True
    except ET.ParseError:
        print(f"Error parsing URDF file: {urdf_path}")

    return term_matches

def generate_robot_classes_from_config(base_dir, output_file, cfg_class_parent):
    """
    Reads robot folders and train_cfg.json files in base_dir and generates class definitions based on robot names in the config file.
    Validates required fields by parsing URDF files.
    """
    # Collect and sort robot folders
    robot_folders = sorted(
        [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    )

    # Open output file for writing the generated class definitions
    with open(output_file, 'w') as f_out:
        for idx, robot_folder in enumerate(robot_folders, start=1):
            # Paths for the train_cfg.json and robot configuration
            train_cfg_path = os.path.join(base_dir, robot_folder, "train_cfg_v2.json")
            urdf_path = os.path.join(base_dir, robot_folder, "robot.urdf")
            robot_json_path = os.path.join(base_dir, robot_folder, "robot.json")
            usd_file_path = os.path.join(base_dir, robot_folder, "usd_file", "robot.usd")

            if not os.path.exists(train_cfg_path):
                raise FileNotFoundError(f"Robot train cfg {train_cfg_path} does not exist.")
                # print(f"Skipping {robot_folder}: train_cfg.json not found.")
                # continue

            if not os.path.exists(urdf_path):
                raise FileNotFoundError(f"Robot URDF {urdf_path} does not exist.")
                # print(f"Skipping {robot_folder}: robot.urdf not found.")
                # continue

            if not os.path.exists(robot_json_path):
                raise FileNotFoundError(f"Robot JSON file {robot_json_path} does not exist.")

            if not os.path.exists(usd_file_path):
                raise FileNotFoundError(f"USD file {usd_file_path} does not exist.")

            # Load the train_cfg.json
            with open(train_cfg_path, "r") as f:
                train_cfg = json.load(f)

            # Extract robot name from the configuration
            robot_name = train_cfg.get("robot_name", None)
            if not robot_name:
                raise NotImplementedError(f"Robot name {train_cfg.get('robot_name', None)} not found.")
                # print(f"Skipping {robot_folder}: 'robot_name' not found in train_cfg_v2.json.")
                # continue

            # Capitalize and format the robot name for the class name
            class_name = robot_name.replace("_", "").capitalize() + "Cfg"
            cfg_name = f"{robot_name.upper()}_CFG"

            # Extract action space
            action_space = train_cfg.get("action_space", 0)

            # Validate required terms in URDF
            term_patterns = {
                "trunk": r"pelvis" if 'humanoid' in robot_name else r"trunk",
                "foot": r"foot",
            }
            term_matches = read_urdf_and_verify_terms(urdf_path, term_patterns)

            if not term_matches["trunk"]:
                raise ValueError(f"Validation failed: 'trunk' term not found in URDF for {robot_name}.")

            if not term_matches["foot"]:
                raise ValueError(f"Validation failed: 'foot' term not found in URDF for {robot_name}.")

            # For quadruped and hexapod, trunk_contact_cfg is read from train_cfg,
            #  which typically includes calf link (which is the link directly connected to feet).
            #  It is unclear if having it in the termination condition is desirable,
            #  as avoiding calf-ground contact is very challenging for robots with multiple knees --
            #  there is no way for robots to learn to walk if they are terminated immediately after being spawned
            # for humanoid, the illegal contact should be None, in train_cfg and here.
            illegal_contact_cfg = train_cfg["reward_cfgs"]["illegal_contact_cfg"]
            if "humanoid" in robot_name:
                assert illegal_contact_cfg == None

            if illegal_contact_cfg is None:
                illegal_contact_string = None
            else:
                # illegal_contact_string = f'SceneEntityCfg(\"contact_sensor\", body_names={str(illegal_contact_cfg)})'
                illegal_contact_string = None  # set everything to None

            lock_joint_name_dict = train_cfg.get("apply_knee_joint_limit_scale_joint_names")  # apply_joint_limit_scale_joint_names (dog) or apply_knee_joint_limit_scale_joint_names
            assert lock_joint_name_dict is not None, f"lock_joint_name_dict shouldn't be None"
            lock_joint_names = [k for k, v in lock_joint_name_dict.items() if v == 1]
            if len(lock_joint_names) == 0:
                lock_joint_cfg = None
                lock_joint_factor = 1
            else:
                joint_names = lock_joint_names
                lock_joint_cfg = f"SceneEntityCfg(\"robot\", joint_names={joint_names})"
                lock_joint_factor = train_cfg.get("apply_knee_joint_limit_scale_factor")    # apply_joint_limit_scale_factor (dog) or apply_knee_joint_limit_scale_factor

            # Generate the class definition
            trunk_name = term_patterns['trunk']
            class_definition = (
                f"@configclass\n"
                f"class {class_name}({cfg_class_parent}):\n"
                f"    action_space = {action_space}\n"
                f"    robot: ArticulationCfg = {cfg_name}\n"
                f"    trunk_cfg = SceneEntityCfg(\"robot\", body_names=\"{trunk_name}\")\n"
                f"    trunk_contact_cfg = {illegal_contact_string}\n"
                f"    feet_contact_cfg = SceneEntityCfg(\"contact_sensor\", body_names=\".*foot\")\n"
                f"    lock_joint_cfg = {lock_joint_cfg} \n"
                f"    lock_joint_factor = {lock_joint_factor:.1f} \n\n"
            )

            # Write to the output file
            f_out.write(class_definition)
            print(f"Generated class definition for: {class_name} (Robot Config: {cfg_name})")

        print(f"Generated {len(robot_folders)} class definitions to {output_file}.")

# Example usage
# cfg_class_parent = 'Go2EnvCfg'   # for quadrupeds
# cfg_class_parent = 'GenHexapodEnvCfg'   # for hexapods
cfg_class_parent = 'H1EnvCfg'   # for humanoids

base_dir = 'exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/Robots/GenBot1K-v7/gen_humanoids'
output_file = "tmp_env_cfg.py"
generate_robot_classes_from_config(base_dir, output_file, cfg_class_parent)
