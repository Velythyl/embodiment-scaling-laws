import json
import os
import subprocess
import itertools
from gen_urdf_color import dog_generate_urdf, humanoid_generate_urdf, hexapod_generate_urdf
import argparse

# Define the path to Isaac SDK scripts
ISAAC_SCRIPTS_PATH = "/home/liudai/hdd_0/projects/cross_em/isaac/scripts"

def dog_generate_multiple_variations(base_parameters, base_output_dir="output_files", gen_usd=False):

    def dog_generate_json_file(parameters, output_file="output.json"):
        """
        Generates a JSON file with the specified structure based on input parameters.
        """
        data = {
            "body_size": {
                "length": parameters["body_size_length"],
                "width": parameters["body_size_width"],
                "height": parameters["body_size_height"]
            },
            "hip_link": {
                "length": parameters["hip_link_length"],
                "radius": parameters["hip_link_radius"]
            },
            "thigh_link": {
                "length": parameters["thigh_link_length"],
                "width": parameters["thigh_link_width"],
                "height": parameters["thigh_link_height"]
            },
            "calf_link": {
                "length": parameters["calf_link_length"],
                "radius": parameters["calf_link_radius"]
            },
            "calflower_link": {
                "length": parameters["calflower_link_length"],
                "radius": parameters["calflower_link_radius"]
            },
            "calflower1_link": {
                "length": parameters["calflower1_link_length"],
                "radius": parameters["calflower1_link_radius"]
            },
            "foot_link_radius": parameters["foot_link_radius"],
            "self_collision_joint_offset": parameters["self_collision_joint_offset"],
            
            "knee_nums": {
                "front_left": parameters["knee_nums_front_left"],
                "front_right": parameters["knee_nums_front_right"],
                "rear_left": parameters["knee_nums_rear_left"],
                "rear_right": parameters["knee_nums_rear_right"]
            },
            "apply_knee_joint_limit_scale_nums": {
                "front_left": parameters["apply_knee_joint_limit_scale_nums_front_left"],
                "front_right": parameters["apply_knee_joint_limit_scale_nums_front_right"],
                "rear_left": parameters["apply_knee_joint_limit_scale_nums_rear_left"],
                "rear_right": parameters["apply_knee_joint_limit_scale_nums_rear_right"]
            },
            "apply_knee_joint_limit_scale_factor": parameters["apply_knee_joint_limit_scale_factor"]
        }

        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
        # print(f"Generated: {output_file}")

    def dog_generate_all_variations(base_parameters, joint_num_variations, joint_limit_variations, geometry_variations, base_output_dir="output_files", gen_usd=False):
        """
        Generates all combinations of variations and outputs JSON/URDF/USD files.
        """

        # Loop over all combinations
        count = 0
        GT_FOLDER_NAME = None
        for joint_num_var in joint_num_variations:
            
            # Check if there is no knee joint
            no_knee_joint = False
            if joint_num_var['knee_nums']['front_left'] == 0 and joint_num_var['knee_nums']['front_right'] == 0 and joint_num_var['knee_nums']['rear_left'] == 0 and joint_num_var['knee_nums']['rear_right'] == 0:
                no_knee_joint = True
            joint_limit_applied_num = 0
            
            for joint_limit_var in joint_limit_variations:
                # Skip applying knee joint limit if no knee joint except for the first time
                if no_knee_joint is True and joint_limit_applied_num >= 1:
                    continue
                joint_limit_applied_num += 1
                
                for geo_var in geometry_variations:

                    # Start with a copy of base_parameters each time
                    parameters = base_parameters.copy()

                    # Update parameters with joint_num_variations
                    knee_nums = joint_num_var['knee_nums']
                    parameters['knee_nums_front_left'] = knee_nums['front_left']
                    parameters['knee_nums_front_right'] = knee_nums['front_right']
                    parameters['knee_nums_rear_left'] = knee_nums['rear_left']
                    parameters['knee_nums_rear_right'] = knee_nums['rear_right']

                    # Update parameters with joint_limit_variations
                    joint_limit_nums = joint_limit_var['apply_knee_joint_limit_scale_nums']
                    parameters['apply_knee_joint_limit_scale_nums_front_left'] = joint_limit_nums['front_left']
                    parameters['apply_knee_joint_limit_scale_nums_front_right'] = joint_limit_nums['front_right']
                    parameters['apply_knee_joint_limit_scale_nums_rear_left'] = joint_limit_nums['rear_left']
                    parameters['apply_knee_joint_limit_scale_nums_rear_right'] = joint_limit_nums['rear_right']
                    parameters['apply_knee_joint_limit_scale_factor'] = joint_limit_var['apply_knee_joint_limit_scale_factor']

                    # Apply geometry variations directly
                    category = geo_var['category']
                    factor = geo_var['factor']

                    if category == "scale_all":
                        # Scale all dimensions by a factor
                        for key in parameters:          
                            # exclude knee_nums and apply_knee_joint_limit_scale              
                            if "knee_nums" not in key and "apply_knee_joint_limit_scale" not in key:
                                parameters[key] *= factor
                                    
                    elif category == "lengthen_thigh":
                        # Change the length of the thigh
                        parameters["thigh_link_length"] *= factor

                    elif category == "lengthen_calf":
                        # Change the length of the calf
                        parameters["calf_link_length"] *= factor
                        
                        # skip no calf robots
                        if knee_nums['front_left']==0 and knee_nums['front_right']==0 and knee_nums['rear_left']==0 and knee_nums['rear_right'] ==0:
                            continue
                    
                    elif category == "scale_foot_size":
                        # Change the radius of the foot
                        parameters["foot_link_radius"] *= factor

                    # Generate output filename with detailed information
                    # Sanitize values to be filename-friendly
                    def sanitize(value):
                        value = round(value, 1)
                        return str(value).replace('.', '_')

                    knee_nums_str = f"fl{parameters['knee_nums_front_left']}_fr{parameters['knee_nums_front_right']}_rl{parameters['knee_nums_rear_left']}_rr{parameters['knee_nums_rear_right']}"
                    joint_limit_nums_str = f"fl{parameters['apply_knee_joint_limit_scale_nums_front_left']}_fr{parameters['apply_knee_joint_limit_scale_nums_front_right']}_rl{parameters['apply_knee_joint_limit_scale_nums_rear_left']}_rr{parameters['apply_knee_joint_limit_scale_nums_rear_right']}"
                    joint_limit_factor_str = sanitize(parameters['apply_knee_joint_limit_scale_factor'])
                    geo_category_str = category
                    factor_str = sanitize(factor)

                    output_folder_name = f"gendog_{str(count)}_KneeNum_{knee_nums_str}__ScaleJointLimit_{joint_limit_nums_str}_{joint_limit_factor_str}__Geo_{geo_category_str}_{factor_str}"
                    output_folder_dir = os.path.join(base_output_dir, output_folder_name)
                    if not os.path.exists(output_folder_dir):
                        os.makedirs(output_folder_dir)

                    # Generate JSON file
                    output_json_file = os.path.join(output_folder_dir, "robot.json")
                    dog_generate_json_file(parameters, output_json_file)
                    
                    # Generate URDF file
                    robot_name = "gen_dog_"+str(count)
                    output_urdf_file = os.path.join(output_folder_dir, "robot.urdf")
                    return_values = dog_generate_urdf(output_json_file, robot_name, output_urdf_file)
                    
                    return_values_json_file = os.path.join(output_folder_dir, f"train_cfg.json")
                    with open(return_values_json_file, "w") as f:
                        json.dump(return_values, f, indent=4)
                    
                    if gen_usd:
                        cmd_input_urdf_file_path = output_urdf_file
                        cmd_output_usd_folder = os.path.join(output_folder_dir, f"usd_file")
                        cmd_output_usd_file_path = os.path.join(cmd_output_usd_folder, "robot.usd")
                        os.makedirs(cmd_output_usd_folder)
                        command = f'sh {os.path.join(ISAAC_SCRIPTS_PATH, "urdf_to_usd.sh")} {cmd_input_urdf_file_path} {cmd_output_usd_file_path}'
                        subprocess.run(command, shell=True)
                    
                    if "KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_0" in output_folder_name:
                        GT_FOLDER_NAME = output_folder_name
                    
                    count += 1

        print(f"Generated {count} dog files. \nThe GT file is: {GT_FOLDER_NAME}")
        # write the GT folder name to a file
        with open(os.path.join(base_output_dir, "meta_data.txt"), "w") as f:
            f.write(f"Generated {count} gendog files. \nThe GT file is: {GT_FOLDER_NAME}")

    joint_nums = [0, 1, 2, 3]
    joint_num_variations = [
        {
             "knee_nums": {
                "front_left": num,
                "front_right": num,
                "rear_left": num,
                "rear_right": num
             }
        }
        for num in joint_nums
    ]
    
    joint_limit_variations = [
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 0,
                "front_right": 0,
                "rear_left": 0,
                "rear_right": 0
            },
         "apply_knee_joint_limit_scale_factor": 1.0
        }, 
        
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 1,
                "front_right": 0,
                "rear_left": 0,
                "rear_right": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 1,
                "front_right": 0,
                "rear_left": 0,
                "rear_right": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 0,
                "front_right": 1,
                "rear_left": 0,
                "rear_right": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 0,
                "front_right": 1,
                "rear_left": 0,
                "rear_right": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 0,
                "front_right": 0,
                "rear_left": 1,
                "rear_right": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 0,
                "front_right": 0,
                "rear_left": 1,
                "rear_right": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 0,
                "front_right": 0,
                "rear_left": 0,
                "rear_right": 1
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "front_left": 0,
                "front_right": 0,
                "rear_left": 0,
                "rear_right": 1
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
    ]
        
    geometry_variations = [
        {"category": "scale_all", "factor": 1.0},  # 0, No change
        {"category": "scale_all", "factor": 1.2},  # 1, up Scale all 
        {"category": "scale_all", "factor": 0.8},  # 2, down Scale all 
        {"category": "lengthen_thigh", "factor": 1.6},  # 3, Lengthen thigh 
        {"category": "lengthen_thigh", "factor": 1.2},  # 4, Lengthen thigh 
        {"category": "lengthen_thigh", "factor": 0.8},  # 5, Shorten thigh 
        {"category": "lengthen_thigh", "factor": 0.4},  # 6, Shorten thigh 
        {"category": "lengthen_calf", "factor": 1.6},  # 7, Lengthen calf 
        {"category": "lengthen_calf", "factor": 1.2},  # 8, Lengthen calf
        {"category": "lengthen_calf", "factor": 0.8},  # 9, Shorten calf 
        {"category": "lengthen_calf", "factor": 0.4},  # 10, Shorten calf
        {"category": "scale_foot_size", "factor": 2.0},  # 11, up scale foot radius
    ]
    
    dog_generate_all_variations(base_parameters, joint_num_variations, joint_limit_variations, geometry_variations, base_output_dir, gen_usd)
    
def humanoid_generate_multiple_variations(base_parameters, base_output_dir="output_files", gen_usd=False):
    """
    Generates multiple JSON files based on predefined variation categories.
    """

    def humanoid_generate_json_file(parameters, output_file="output.json"):
        """
        Generates a JSON file with the specified structure based on input parameters.
        """
        data = {
            "torso_size": {
                "length": parameters["torso_size_length"],
                "width": parameters["torso_size_width"],
                "height": parameters["torso_size_height"]
            },
            "head": {
                "radius": parameters["head_radius"]
            },
            "pelvis": {
                "radius": parameters["pelvis_radius"]
            },
            "upper_arm": {
                "length": parameters["upper_arm_length"],
                "radius": parameters["arm_radius"]
            },
            "lower_arm": {
                "length": parameters["lower_arm_length"],
                "radius": parameters["arm_radius"]
            },
            "thigh": {
                "length": parameters["thigh_length"],
                "radius": parameters["leg_radius"]
            },
            "calf": {
                "length": parameters["calf_length"],
                "radius": parameters["leg_radius"]
            },
            "foot_size": {
                "length": parameters["foot_size_length"],
                "width": parameters["foot_size_width"],
                "height": parameters["foot_size_height"]
            },
            "self_collision_joint_offset": parameters["self_collision_joint_offset"],
            
            "knee_nums": {
                "left": parameters["knee_nums_left"],
                "right": parameters["knee_nums_right"],
            },
            "apply_knee_joint_limit_scale_nums": {
                "left": parameters["apply_knee_joint_limit_scale_nums_left"],
                "right": parameters["apply_knee_joint_limit_scale_nums_right"]
            },
            "apply_knee_joint_limit_scale_factor": parameters["apply_knee_joint_limit_scale_factor"]
        }

        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
        # print(f"Generated: {output_file}")

    def humanoid_generate_all_variations(base_parameters, joint_num_variations, joint_limit_variations, geometry_variations, base_output_dir="output_files", gen_usd=False):
        """
        Generates all combinations of variations and outputs JSON/URDF/USD files.
        """

        # Loop over all combinations
        count = 0
        GT_FOLDER_NAME = None
        for joint_num_var in joint_num_variations:
            
            # Check if there is no knee joint
            no_knee_joint = False
            if joint_num_var['knee_nums']['left'] == 0 and joint_num_var['knee_nums']['right'] == 0:
                no_knee_joint = True
            joint_limit_applied_num = 0
            
            for joint_limit_var in joint_limit_variations:
                # Skip applying knee joint limit if no knee joint except for the first time
                if no_knee_joint is True and joint_limit_applied_num >= 1:
                    continue
                joint_limit_applied_num += 1
                
                for geo_var in geometry_variations:

                    # Start with a copy of base_parameters each time
                    parameters = base_parameters.copy()

                    # Update parameters with joint_num_variations
                    knee_nums = joint_num_var['knee_nums']
                    parameters['knee_nums_left'] = knee_nums['left']
                    parameters['knee_nums_right'] = knee_nums['right']

                    # Update parameters with joint_limit_variations
                    joint_limit_nums = joint_limit_var['apply_knee_joint_limit_scale_nums']
                    parameters['apply_knee_joint_limit_scale_nums_left'] = joint_limit_nums['left']
                    parameters['apply_knee_joint_limit_scale_nums_right'] = joint_limit_nums['right']
                    parameters['apply_knee_joint_limit_scale_factor'] = joint_limit_var['apply_knee_joint_limit_scale_factor']

                    # Apply geometry variations directly
                    category = geo_var['category']
                    factor = geo_var['factor']

                    if category == "scale_all":
                        # Scale all dimensions by a factor
                        for key in parameters:          
                            # exclude knee_nums and apply_knee_joint_limit_scale              
                            if "knee_nums" not in key and "apply_knee_joint_limit_scale" not in key:
                                parameters[key] *= factor
                                    
                    elif category == "lengthen_thigh":
                        # Change the length of the thigh
                        parameters["thigh_length"] *= factor

                    elif category == "lengthen_calf":
                        # Change the length of the calf
                        parameters["calf_length"] *= factor
                        
                        # skip no calf robots
                        if knee_nums['left']==0 and knee_nums['right']==0:
                            continue
                        
                    elif category == "scale_torso":
                        # Change the length of the calf
                        parameters["torso_size_length"] *= factor
                        parameters["torso_size_width"] *= factor
                        parameters["torso_size_height"] *= factor
                    
                    elif category == "scale_foot_size":
                        # Change the size of the foot
                        parameters["foot_size_length"] *= factor
                        parameters["foot_size_width"] *= factor
                        parameters["foot_size_height"] *= factor

                    # Generate output filename with detailed information
                    # Sanitize values to be filename-friendly
                    def sanitize(value):
                        value = round(value, 1)
                        return str(value).replace('.', '_')

                    knee_nums_str = f"l{parameters['knee_nums_left']}_r{parameters['knee_nums_right']}"
                    joint_limit_nums_str = f"l{parameters['apply_knee_joint_limit_scale_nums_left']}_r{parameters['apply_knee_joint_limit_scale_nums_right']}"
                    joint_limit_factor_str = sanitize(parameters['apply_knee_joint_limit_scale_factor'])
                    geo_category_str = category
                    factor_str = sanitize(factor)

                    output_folder_name = f"genhumanoid_{str(count)}_KneeNum_{knee_nums_str}__ScaleJointLimit_{joint_limit_nums_str}_{joint_limit_factor_str}__Geo_{geo_category_str}_{factor_str}"
                    output_folder_dir = os.path.join(base_output_dir, output_folder_name)
                    if not os.path.exists(output_folder_dir):
                        os.makedirs(output_folder_dir)

                    # Generate JSON file
                    output_json_file = os.path.join(output_folder_dir, "robot.json")
                    humanoid_generate_json_file(parameters, output_json_file)
                    
                    # Generate URDF file
                    robot_name = "gen_humanoid_"+str(count)
                    output_urdf_file = os.path.join(output_folder_dir, "robot.urdf")
                    return_values = humanoid_generate_urdf(output_json_file, robot_name, output_urdf_file)
                    
                    return_values_json_file = os.path.join(output_folder_dir, f"train_cfg.json")
                    with open(return_values_json_file, "w") as f:
                        json.dump(return_values, f, indent=4)
                    
                    if gen_usd:
                        cmd_input_urdf_file_path = output_urdf_file
                        cmd_output_usd_folder = os.path.join(output_folder_dir, f"usd_file")
                        cmd_output_usd_file_path = os.path.join(cmd_output_usd_folder, "robot.usd")
                        os.makedirs(cmd_output_usd_folder)
                        command = f'sh {os.path.join(ISAAC_SCRIPTS_PATH, "urdf_to_usd.sh")} {cmd_input_urdf_file_path} {cmd_output_usd_file_path}'
                        subprocess.run(command, shell=True)
                    
                    if "KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_0" in output_folder_name:
                        GT_FOLDER_NAME = output_folder_name
                    
                    count += 1

        print(f"Generated {count} genhumanoid files. \nThe GT file is: {GT_FOLDER_NAME}")
        # write the GT folder name to a file
        with open(os.path.join(base_output_dir, "meta_data.txt"), "w") as f:
            f.write(f"Generated {count} genhumanoid files. \nThe GT file is: {GT_FOLDER_NAME}")

    joint_nums = [0, 1, 2, 3]
    joint_num_variations = [
        {
             "knee_nums": {
                "left": num,
                "right": num
             }
        }
        for num in joint_nums
    ]
    
    joint_limit_variations = [
        {"apply_knee_joint_limit_scale_nums": {
                "left": 0,
                "right": 0
            },
         "apply_knee_joint_limit_scale_factor": 1.0
        }, 
        
        {"apply_knee_joint_limit_scale_nums": {
                "left": 1,
                "right": 0,
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "left": 1,
                "right": 0,
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "left": 1,
                "right": 1,
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "left": 1,
                "right": 1
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "left": 0,
                "right": 1,
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "left": 0,
                "right": 1,
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },

    ]
    
    geometry_variations = [
        {"category": "scale_all", "factor": 1.0},  # 0, No change
        {"category": "scale_all", "factor": 1.2},  # 1, up Scale all 
        {"category": "scale_all", "factor": 0.8},  # 2, down Scale all 
        {"category": "lengthen_thigh", "factor": 1.6},  # 3, Lengthen thigh 
        {"category": "lengthen_thigh", "factor": 1.2},  # 4, Lengthen thigh 
        {"category": "lengthen_thigh", "factor": 0.8},  # 5, Shorten thigh 
        {"category": "lengthen_thigh", "factor": 0.4},  # 6, Shorten thigh 
        {"category": "lengthen_calf", "factor": 1.6},  # 7, Lengthen calf 
        {"category": "lengthen_calf", "factor": 1.2},  # 8, Lengthen calf
        {"category": "lengthen_calf", "factor": 0.8},  # 9, Shorten calf 
        {"category": "lengthen_calf", "factor": 0.4},  # 10, Shorten calf
        {"category": "scale_torso", "factor": 1.6},  # 11, up scale torso
        {"category": "scale_torso", "factor": 1.2},  # 12, up scale torso
        {"category": "scale_torso", "factor": 0.8},  # 13, down scale torso
        {"category": "scale_torso", "factor": 0.4},  # 14, down scale torso
        {"category": "scale_foot_size", "factor": 2.0},  # 15, up scale foot size
    ]

    humanoid_generate_all_variations(base_parameters, joint_num_variations, joint_limit_variations, geometry_variations, base_output_dir, gen_usd)
        
def hexapod_generate_multiple_variations(base_parameters, base_output_dir="output_files", gen_usd=False):

    def hexapod_generate_json_file(parameters, output_file="output.json"):
        """
        Generates a JSON file with the specified structure based on input parameters.
        """
        data = {
            "body_size": {
                "length": parameters["body_size_length"],
                "width": parameters["body_size_width"],
                "height": parameters["body_size_height"]
            },
            "hip_link": {
                "radius": parameters["hip_link_radius"]
            },
            "foot_link": {
                "radius": parameters["foot_link_radius"]
            },
            "thigh_link": {
                "length": parameters["thigh_link_length"],
                "radius": parameters["thigh_link_radius"],
            },
            "calf_link": {
                "length": parameters["calf_link_length"],
                "radius": parameters["calf_link_radius"]
            },
            "self_collision_joint_offset": parameters["self_collision_joint_offset"],
            
            "knee_nums": {
                "leg_1": parameters["knee_nums_leg_1"],
                "leg_2": parameters["knee_nums_leg_2"],
                "leg_3": parameters["knee_nums_leg_3"],
                "leg_4": parameters["knee_nums_leg_4"],
                "leg_5": parameters["knee_nums_leg_5"],
                "leg_6": parameters["knee_nums_leg_6"]
            },
            "apply_knee_joint_limit_scale_nums": {
                "leg_1": parameters["apply_knee_joint_limit_scale_nums_leg_1"],
                "leg_2": parameters["apply_knee_joint_limit_scale_nums_leg_2"],
                "leg_3": parameters["apply_knee_joint_limit_scale_nums_leg_3"],
                "leg_4": parameters["apply_knee_joint_limit_scale_nums_leg_4"],
                "leg_5": parameters["apply_knee_joint_limit_scale_nums_leg_5"],
                "leg_6": parameters["apply_knee_joint_limit_scale_nums_leg_6"]
            },
            "apply_knee_joint_limit_scale_factor": parameters["apply_knee_joint_limit_scale_factor"]
        }

        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
        # print(f"Generated: {output_file}")

    def hexapod_generate_all_variations(base_parameters, joint_num_variations, joint_limit_variations, geometry_variations, base_output_dir="output_files", gen_usd=False):
        """
        Generates all combinations of variations and outputs JSON/URDF/USD files.
        """

        # Loop over all combinations
        count = 0
        GT_FOLDER_NAME = None
        for joint_num_var in joint_num_variations:
            
            # Check if there is no knee joint
            no_knee_joint = False
            if joint_num_var['knee_nums']['leg_1'] == 0 and joint_num_var['knee_nums']['leg_2'] == 0 and joint_num_var['knee_nums']['leg_3'] == 0 and joint_num_var['knee_nums']['leg_4'] == 0 and joint_num_var['knee_nums']['leg_5'] == 0 and joint_num_var['knee_nums']['leg_6'] == 0:
                no_knee_joint = True
            joint_limit_applied_num = 0
            
            for joint_limit_var in joint_limit_variations:
                # Skip applying knee joint limit if no knee joint except for the first time
                if no_knee_joint is True and joint_limit_applied_num >= 1:
                    continue
                joint_limit_applied_num += 1
                
                for geo_var in geometry_variations:

                    # Start with a copy of base_parameters each time
                    parameters = base_parameters.copy()

                    # Update parameters with joint_num_variations
                    knee_nums = joint_num_var['knee_nums']
                    parameters['knee_nums_leg_1'] = knee_nums['leg_1']
                    parameters['knee_nums_leg_2'] = knee_nums['leg_2']
                    parameters['knee_nums_leg_3'] = knee_nums['leg_3']
                    parameters['knee_nums_leg_4'] = knee_nums['leg_4']
                    parameters['knee_nums_leg_5'] = knee_nums['leg_5']
                    parameters['knee_nums_leg_6'] = knee_nums['leg_6']

                    # Update parameters with joint_limit_variations
                    joint_limit_nums = joint_limit_var['apply_knee_joint_limit_scale_nums']
                    parameters['apply_knee_joint_limit_scale_nums_leg_1'] = joint_limit_nums['leg_1']
                    parameters['apply_knee_joint_limit_scale_nums_leg_2'] = joint_limit_nums['leg_2']
                    parameters['apply_knee_joint_limit_scale_nums_leg_3'] = joint_limit_nums['leg_3']
                    parameters['apply_knee_joint_limit_scale_nums_leg_4'] = joint_limit_nums['leg_4']
                    parameters['apply_knee_joint_limit_scale_nums_leg_5'] = joint_limit_nums['leg_5']
                    parameters['apply_knee_joint_limit_scale_nums_leg_6'] = joint_limit_nums['leg_6']
                    parameters['apply_knee_joint_limit_scale_factor'] = joint_limit_var['apply_knee_joint_limit_scale_factor']
                    
                    # Apply geometry variations directly
                    category = geo_var['category']
                    factor = geo_var['factor']

                    if category == "scale_all":
                        # Scale all dimensions by a factor
                        for key in parameters:          
                            # exclude knee_nums and apply_knee_joint_limit_scale              
                            if "knee_nums" not in key and "apply_knee_joint_limit_scale" not in key:
                                parameters[key] *= factor
                                    
                    elif category == "lengthen_thigh":
                        # Change the length of the thigh
                        parameters["thigh_link_length"] *= factor

                    elif category == "lengthen_calf":
                        # Change the length of the calf
                        parameters["calf_link_length"] *= factor
                        # skip no calf robots
                        if knee_nums['leg_1']==0 and knee_nums['leg_2']==0 and knee_nums['leg_3']==0 and knee_nums['leg_4']==0 and knee_nums['leg_5']==0 and knee_nums['leg_6']==0:
                            continue
                    elif category == "scale_foot_size":
                        # Change the radius of the foot
                        parameters["foot_link_radius"] *= factor

                    # Generate output filename with detailed information
                    # Sanitize values to be filename-friendly
                    def sanitize(value):
                        value = round(value, 1)
                        return str(value).replace('.', '_')

                    # knee_nums_str = f"fl{parameters['knee_nums_front_left']}_fr{parameters['knee_nums_front_right']}_rl{parameters['knee_nums_rear_left']}_rr{parameters['knee_nums_rear_right']}"
                    # joint_limit_nums_str = f"fl{parameters['apply_knee_joint_limit_scale_nums_front_left']}_fr{parameters['apply_knee_joint_limit_scale_nums_front_right']}_rl{parameters['apply_knee_joint_limit_scale_nums_rear_left']}_rr{parameters['apply_knee_joint_limit_scale_nums_rear_right']}"
                    
                    knee_nums_str = f"l1-{parameters['knee_nums_leg_1']}_l2-{parameters['knee_nums_leg_2']}_l3-{parameters['knee_nums_leg_3']}_l4-{parameters['knee_nums_leg_4']}_l5-{parameters['knee_nums_leg_5']}_l6-{parameters['knee_nums_leg_6']}"
                    joint_limit_nums_str = f"l1-{parameters['apply_knee_joint_limit_scale_nums_leg_1']}_l2-{parameters['apply_knee_joint_limit_scale_nums_leg_2']}_l3-{parameters['apply_knee_joint_limit_scale_nums_leg_3']}_l4-{parameters['apply_knee_joint_limit_scale_nums_leg_4']}_l5-{parameters['apply_knee_joint_limit_scale_nums_leg_5']}_l6-{parameters['apply_knee_joint_limit_scale_nums_leg_6']}" 
                    joint_limit_factor_str = sanitize(parameters['apply_knee_joint_limit_scale_factor'])
                    geo_category_str = category
                    factor_str = sanitize(factor)

                    output_folder_name = f"genhexapod_{str(count)}_KneeNum_{knee_nums_str}__ScaleJointLimit_{joint_limit_nums_str}_{joint_limit_factor_str}__Geo_{geo_category_str}_{factor_str}"
                    output_folder_dir = os.path.join(base_output_dir, output_folder_name)
                    if not os.path.exists(output_folder_dir):
                        os.makedirs(output_folder_dir)

                    # Generate JSON file
                    output_json_file = os.path.join(output_folder_dir, "robot.json")
                    hexapod_generate_json_file(parameters, output_json_file)
                    
                    # Generate URDF file
                    robot_name = "gen_hexapod_"+str(count)
                    output_urdf_file = os.path.join(output_folder_dir, "robot.urdf")
                    return_values = hexapod_generate_urdf(output_json_file, robot_name, output_urdf_file)
                    
                    return_values_json_file = os.path.join(output_folder_dir, f"train_cfg.json")
                    with open(return_values_json_file, "w") as f:
                        json.dump(return_values, f, indent=4)
                    
                    if gen_usd:
                        cmd_input_urdf_file_path = output_urdf_file
                        cmd_output_usd_folder = os.path.join(output_folder_dir, f"usd_file")
                        cmd_output_usd_file_path = os.path.join(cmd_output_usd_folder, "robot.usd")
                        os.makedirs(cmd_output_usd_folder)
                        command = f'sh {os.path.join(ISAAC_SCRIPTS_PATH, "urdf_to_usd.sh")} {cmd_input_urdf_file_path} {cmd_output_usd_file_path}'
                        subprocess.run(command, shell=True)
                    
                    if "KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_0" in output_folder_name:
                        GT_FOLDER_NAME = output_folder_name 
                    
                    count += 1

        print(f"Generated {count} genhexapod files. \nThe GT file is: {GT_FOLDER_NAME}")
        # write the GT folder name to a file
        with open(os.path.join(base_output_dir, "meta_data.txt"), "w") as f:
            f.write(f"Generated {count} genhexapod files. \nThe GT file is: {GT_FOLDER_NAME}")


    joint_nums = [0, 1, 2, 3]
    joint_num_variations = [
        {
             "knee_nums": {
                "leg_1": num,
                "leg_2": num,
                "leg_3": num,
                "leg_4": num,
                "leg_5": num,
                "leg_6": num
             }
        }
        for num in joint_nums
    ]
    
    joint_limit_variations = [
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 0,
                "leg_2": 0,
                "leg_3": 0,
                "leg_4": 0,
                "leg_5": 0,
                "leg_6": 0
            },
         "apply_knee_joint_limit_scale_factor": 1.0
        }, 
        
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 1,
                "leg_2": 0,
                "leg_3": 0,
                "leg_4": 0,
                "leg_5": 0,
                "leg_6": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 1,
                "leg_2": 0,
                "leg_3": 0,
                "leg_4": 0,
                "leg_5": 0,
                "leg_6": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        }, 
        
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 0,
                "leg_2": 0,
                "leg_3": 1,
                "leg_4": 0,
                "leg_5": 0,
                "leg_6": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        }, 
        
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 0,
                "leg_2": 0,
                "leg_3": 1,
                "leg_4": 0,
                "leg_5": 0,
                "leg_6": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
        
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 0,
                "leg_2": 0,
                "leg_3": 0,
                "leg_4": 1,
                "leg_5": 0,
                "leg_6": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 0,
                "leg_2": 0,
                "leg_3": 0,
                "leg_4": 1,
                "leg_5": 0,
                "leg_6": 0
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 0,
                "leg_2": 0,
                "leg_3": 0,
                "leg_4": 0,
                "leg_5": 0,
                "leg_6": 1
            },
         "apply_knee_joint_limit_scale_factor": 0.6
        },
        
        {"apply_knee_joint_limit_scale_nums": {
                "leg_1": 0,
                "leg_2": 0,
                "leg_3": 0,
                "leg_4": 0,
                "leg_5": 0,
                "leg_6": 1
            },
         "apply_knee_joint_limit_scale_factor": 0.2
        },
        
    ]
        
    geometry_variations = [
        {"category": "scale_all", "factor": 1.0},  # 0, No change
        {"category": "scale_all", "factor": 1.2},  # 1, up Scale all 
        {"category": "scale_all", "factor": 0.8},  # 2, down Scale all 
        {"category": "lengthen_thigh", "factor": 1.6},  # 3, Lengthen thigh 
        {"category": "lengthen_thigh", "factor": 1.2},  # 4, Lengthen thigh 
        {"category": "lengthen_thigh", "factor": 0.8},  # 5, Shorten thigh 
        {"category": "lengthen_thigh", "factor": 0.4},  # 6, Shorten thigh 
        {"category": "lengthen_calf", "factor": 1.6},  # 7, Lengthen calf 
        {"category": "lengthen_calf", "factor": 1.2},  # 8, Lengthen calf
        {"category": "lengthen_calf", "factor": 0.8},  # 9, Shorten calf 
        {"category": "lengthen_calf", "factor": 0.4},  # 10, Shorten calf
        {"category": "scale_foot_size", "factor": 2.0},  # 11, up scale foot radius
    ]
    
    hexapod_generate_all_variations(base_parameters, joint_num_variations, joint_limit_variations, geometry_variations, base_output_dir, gen_usd)

def main():
    
    import time
    parser = argparse.ArgumentParser()
    parser.add_argument('--gen_usd', action='store_true', help='Generate USD files')
    args = parser.parse_args()

    gen_usd = args.gen_usd
    start_time = time.time()
    
    base_outpit_dir = "output_files"
    if os.path.exists(base_outpit_dir):
        os.system(f"rm -rf {base_outpit_dir}")
    os.makedirs(base_outpit_dir)
    
    # Base parameters for the robot dog
    dog_base_parameters = {
        "body_size_length": 0.3762,
        "body_size_width": 0.0935,
        "body_size_height": 0.114,
        "hip_link_length": 0.04,
        "hip_link_radius": 0.046,
        "thigh_link_length": 0.213,
        "thigh_link_width": 0.0245,
        "thigh_link_height": 0.034,
        "calf_link_length": 0.12,
        "calf_link_radius": 0.013,
        "calflower_link_length": 0.065,
        "calflower_link_radius": 0.011,
        "calflower1_link_length": 0.03,
        "calflower1_link_radius": 0.0155,
        "foot_link_radius": 0.022,
        "self_collision_joint_offset": 0,
        "knee_nums_front_left": 1,
        "knee_nums_front_right": 1,
        "knee_nums_rear_left": 1,
        "knee_nums_rear_right": 1,
        "apply_knee_joint_limit_scale_nums_front_left": 0,
        "apply_knee_joint_limit_scale_nums_front_right": 0,
        "apply_knee_joint_limit_scale_nums_rear_left": 0,
        "apply_knee_joint_limit_scale_nums_rear_right": 0,
        "apply_knee_joint_limit_scale_factor": 1.0,
    }
    dog_gen_output_root_folder = os.path.join(base_outpit_dir, "gen_dogs")
    os.makedirs(dog_gen_output_root_folder)
    dog_generate_multiple_variations(dog_base_parameters, dog_gen_output_root_folder, gen_usd)

    # Base parameters for the humanoid robot
    humanoid_base_parameters = {
        "torso_size_length": 0.08,
        
        # "torso_size_width": 0.16,
        "torso_size_width": 0.26,
        
        # "torso_size_height": 0.1,
        "torso_size_height": 0.18,
        
        "head_radius": 0.05,
        "pelvis_radius": 0.05,
        "upper_arm_length": 0.2,
        
        # "lower_arm_length": 0.09,
        "lower_arm_length": 0.1,
        
        "thigh_length": 0.2,
        "calf_length": 0.2,
        
        # "arm_radius": 0.03, # only applies for elbow link
        "arm_radius": 0.04, # only applies for elbow link
        
        "leg_radius": 0.05,
        "foot_size_length": 0.28,
        "foot_size_width": 0.03,
        "foot_size_height": 0.024,
        "self_collision_joint_offset": 0.2,
        "knee_nums_left": 1,
        "knee_nums_right": 1,
        "apply_knee_joint_limit_scale_nums_left": 0,
        "apply_knee_joint_limit_scale_nums_right": 0,
        "apply_knee_joint_limit_scale_factor": 1.0,
    }
    humanoid_gen_output_root_folder = os.path.join(base_outpit_dir, "gen_humanoids")
    os.makedirs(humanoid_gen_output_root_folder)
    humanoid_generate_multiple_variations(humanoid_base_parameters, humanoid_gen_output_root_folder, gen_usd)
    
    # Base parameters for the hexapod robot
    hexapod_base_parameters = {
        "body_size_length": 0.8,
        "body_size_width": 0.5,
        "body_size_height": 0.1,
        "hip_link_radius": 0.05,
        # "foot_link_radius": 0.02,
        "foot_link_radius": 0.03,
        "thigh_link_length": 0.22,
        "thigh_link_radius": 0.03,
        "calf_link_length": 0.22,
        "calf_link_radius": 0.025,
        "self_collision_joint_offset": 0.3,
        "knee_nums_leg_1": 1,
        "knee_nums_leg_2": 1,
        "knee_nums_leg_3": 1,
        "knee_nums_leg_4": 1,
        "knee_nums_leg_5": 1,
        "knee_nums_leg_6": 1,
        "apply_knee_joint_limit_scale_nums_leg_1": 0,
        "apply_knee_joint_limit_scale_nums_leg_2": 0,
        "apply_knee_joint_limit_scale_nums_leg_3": 0,
        "apply_knee_joint_limit_scale_nums_leg_4": 0,
        "apply_knee_joint_limit_scale_nums_leg_5": 0,
        "apply_knee_joint_limit_scale_nums_leg_6": 0,
        "apply_knee_joint_limit_scale_factor": 1.0,
    }
    hexapod_gen_output_root_folder = os.path.join(base_outpit_dir, "gen_hexapods")
    os.makedirs(hexapod_gen_output_root_folder)
    hexapod_generate_multiple_variations(hexapod_base_parameters, hexapod_gen_output_root_folder, gen_usd)
    
    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
