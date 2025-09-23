import os
import json
import time

robot_version = 'v7'

def generate_code(base_dir, output_file):
    """
    Reads robot folders in base_dir, parses train_cfg.json, and generates configuration code.
    """
    # Collect and sort robot folders
    robot_folders = sorted(
        [os.path.join(base_dir, f) for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    )
    robot_folder_name = os.path.basename(base_dir)

    # Open output file for writing the generated code
    with open(output_file, 'w') as f_out:
        for idx, robot_folder in enumerate(robot_folders, start=1):
            # Define paths to train_cfg.json and USD file
            train_cfg_path = os.path.join(robot_folder, 'train_cfg_v2.json')
            usd_file_path = os.path.join(robot_folder, 'usd_file', 'robot.usd')

            # Skip if required files do not exist
            if not os.path.exists(train_cfg_path) or not os.path.exists(usd_file_path):
                raise FileNotFoundError(f'Could not find {train_cfg_path} or {usd_file_path}')

            # Read train_cfg.json
            with open(train_cfg_path, 'r') as f:
                train_cfg = json.load(f)

            # Extract robot_name; raise an error if it's missing
            robot_name = train_cfg.get("robot_name")
            if not robot_name:
                raise ValueError(f"'robot_name' is missing in train_cfg_v2.json for folder: {robot_folder}")

            # Generate CFG name
            cfg_name = f"{robot_name.upper()}_CFG"  # Consistent CFG naming

            # Extract relevant values
            if 'humanoid' in robot_folder_name:
                drop_height = train_cfg.get("drop_height") - 0.05  # H1 has drop height 1.05, but the computed value for GT humanoid is 1.12
            else:
                drop_height = train_cfg.get("drop_height")  # Go2 has drop height 0.325, but the computed value for GT dog is 0.331
            joint_positions = train_cfg.get("nominal_joint_positions", {})
            joint_positions_str = ",\n            ".join(
                f'"{k}": {v:.5f}' for k, v in joint_positions.items()
            )

            # Use the folder name to construct USD path
            folder_name = os.path.basename(robot_folder)  # Get the actual folder name
            usd_path = f'{{ISAAC_ASSET_DIR}}/Robots/GenBot1K-{robot_version}/{robot_folder_name}/{folder_name}/usd_file/robot.usd'

            # Handle actuators
            if 'humanoid' in robot_folder_name:
                actuators_var_name = "actuators_without_knee" if 'KneeNum_l0_r0' in folder_name else 'actuators_with_knee'
            else:
                actuators_var_name = 'actuators'

            # Generate code block
            code_block = f"""
{cfg_name} = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{usd_path}",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, {drop_height:.5f}),
        joint_pos={{
            {joint_positions_str}
        }},
        joint_vel={{".*": 0.0}},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators={actuators_var_name},
    prim_path=prim_path
)
"""
            # Write to output file
            f_out.write(code_block)
            time.sleep(0.01)        # buffer time for writing
            print(f"Generated configuration for: {robot_name}")

    print(f"Successfully processed {len(robot_folders)} robot folders to {output_file}.")


# Example usage
base_dir = f"exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/Robots/GenBot1K-{robot_version}/gen_humanoids"  # Replace with the actual directory containing robot folders
output_file = "tmp_articulation_cfgs.py"  # Output file for the generated code
generate_code(base_dir, output_file)
