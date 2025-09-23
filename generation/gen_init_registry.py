import os
import json

def generate_robot_registration_with_consistent_names(base_dir, output_file):
    """
    Reads robot folders and train_cfg.json files in base_dir and generates robot config registration code with consistent names.
    """
    # Collect and sort robot folders
    import re
    robot_folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    # Sort numerically by extracting the first number after underscore from folder names like "genhexapod_0_KneeNum_...", "gendog_10_KneeNum_...", etc.
    def extract_number(folder_name):
        match = re.search(r'_(\d+)', folder_name)
        return int(match.group(1)) if match else 0
    
    robot_folders = sorted(robot_folders, key=extract_number)

    # Open output file for writing the generated registration code
    with open(output_file, 'w') as f_out:
        # Write the comment header
        f_out.write('"""\nRegister customized robot configs.\n'
                    'Due to the large number of configs, ideally we want to automate the process\n"""\n\n')

        # Initialize the id_entry_pair dictionary
        f_out.write("id_entry_pair = {\n")

        for robot_folder in robot_folders:
            # Define paths to train_cfg.json
            train_cfg_path = os.path.join(base_dir, robot_folder, "train_cfg.json")

            # Skip folders without train_cfg.json
            if not os.path.exists(train_cfg_path):
                print(f"Skipping {robot_folder}: Missing train_cfg.json")
                continue

            # Read train_cfg.json
            with open(train_cfg_path, 'r') as f:
                train_cfg = json.load(f)

            # Extract robot name from train_cfg.json
            robot_name = train_cfg.get("robot_name", None)
            if not robot_name:
                print(f"Skipping {robot_folder}: 'robot_name' not found in train_cfg.json.")
                continue

            # Process names
            processed_robot_name = robot_name.replace("_", "").capitalize()  # CamelCase for the id
            class_name = robot_name.replace("_", "").capitalize() + "Cfg"  # CamelCase class name

            # Add entry to the id_entry_pair dictionary
            f_out.write(f'    "{processed_robot_name}": {class_name},\n')

        # Close the id_entry_pair dictionary
        f_out.write("}\n\n")

        # Write the registration loop
        f_out.write("for id, env_cfg_entry_point in id_entry_pair.items():\n")
        f_out.write("    rsl_rl_cfg_entry_point = f\"{algorithm.__name__}.gen_hexapod_1k_ppo_cfg:{id.capitalize()}PPORunnerCfg\"\n")
        f_out.write("    gym.register(\n")
        f_out.write("        id=id,\n")
        f_out.write("        entry_point=\"embodiment_scaling_laws.tasks.environments.gen_direct_env:GenDirectEnv\",\n")
        f_out.write("        disable_env_checker=True,\n")
        f_out.write("        kwargs={\n")
        f_out.write("            \"env_cfg_entry_point\": env_cfg_entry_point,\n")
        f_out.write("            \"rsl_rl_cfg_entry_point\": rsl_rl_cfg_entry_point\n")
        f_out.write("        },\n")
        f_out.write("    )\n")

        print(f"Generated robot registration code for {len(robot_folders)} robots.")


# Example usage
base_dir = "exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/Robots/GenBot1K-v7/gen_hexapods"  # Replace with the actual directory containing robot folders
output_file = "generated_robot_registration.py"  # Output file for the generated registration code
generate_robot_registration_with_consistent_names(base_dir, output_file)
