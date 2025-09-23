import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os
import json
import math

X_AXIS = "1 0 0"
Y_AXIS = "0 1 0"
Z_AXIS = "0 0 1"

BASE_COLOR = "0.5 0.5 0.5 1.0"
HIGHLIGHT_COLOR = "0.0 0.0 0.0 1.0"

APPLY_SCALE_IN_URDF = False

# convert a 0-255 RGB color to a 0-1 
def rgba_to_normalized_string(r, g, b, a):
    normalized = [round(x / 255, 1) for x in (r, g, b, a)]
    return ' '.join(f"{x:.1f}" for x in normalized)

# Function to prettify XML
def prettify_xml(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Function to convert tuple to string, separated by space
def tuple_to_string(input_tuple):
    return ' '.join(map(str, input_tuple))

# Function to create a URDF link element
def create_link(link_name, geometry_type="box", 
                xyz=(0,0,0), rpy=(0,0,0), 
                box_dimensions=(0.1, 0.1, 0.1), 
                sphere_dimensions=(0.1,), 
                cylinder_dimensions=(0.1, 0.05), 
                cylinder_dimensions_visual=None,
                color=BASE_COLOR,
                inertial_origin_xyz=(0,0,0), inertial_origin_rpy=(0,0,0),
                mass=0.1, 
                inertia=(0.001, 0, 0, 0.001, 0, 0.001),
                no_inertial=False,
                robot_name="gen_dog"):  
    '''
        box_dimensions: (length, width, height)
        sphere_dimensions: (radius,)
        cylinder_dimensions: (length, radius)
        inertia: (ixx, ixy, ixz, iyy, iyz, izz) -> inertia matrix elements
    '''
    link = ET.Element('link', name=link_name)

    if no_inertial is False:

        # Inertial element
        inertial = ET.SubElement(link, 'inertial')
        origin_i = ET.SubElement(inertial, 'origin', xyz=tuple_to_string(inertial_origin_xyz), rpy=tuple_to_string(inertial_origin_rpy))
        ET.SubElement(inertial, 'mass', value=str(mass))
        inertia_element = ET.SubElement(inertial, 'inertia', 
                                        ixx=str(inertia[0]), ixy=str(inertia[1]), ixz=str(inertia[2]), 
                                        iyy=str(inertia[3]), iyz=str(inertia[4]), izz=str(inertia[5]))
        
    # Visual element
    visual = ET.SubElement(link, 'visual')
    origin_v = ET.SubElement(visual, 'origin', xyz=tuple_to_string(xyz), rpy=tuple_to_string(rpy))
    geometry_v = ET.SubElement(visual, 'geometry')
    if geometry_type == "box":
        if "dog" in robot_name:
            if "trunk" in link_name:
                ET.SubElement(geometry_v, 'box', size=tuple_to_string((box_dimensions[0], box_dimensions[1]+0.1, box_dimensions[2])))
            else:
                ET.SubElement(geometry_v, 'box', size=tuple_to_string(box_dimensions))
        else:
            ET.SubElement(geometry_v, 'box', size=tuple_to_string(box_dimensions))
    elif geometry_type == "sphere":
        
        if "humanoid" in robot_name:
            if "pelvis" in link_name:
                ET.SubElement(geometry_v, 'box', size=tuple_to_string((0.1, 0.26, 0.15)))
            elif "head" in link_name:
                ET.SubElement(geometry_v, 'sphere', radius=tuple_to_string((0.07,)))
            else:
                ET.SubElement(geometry_v, 'sphere', radius=tuple_to_string(sphere_dimensions))
        else:
            ET.SubElement(geometry_v, 'sphere', radius=tuple_to_string(sphere_dimensions))
    elif geometry_type == "cylinder":
        if "humanoid" in robot_name:
            if "hip_yaw" in link_name:
                ET.SubElement(geometry_v, 'box', size=tuple_to_string((0.1, 0.05, 0.1)))
            elif "hip_roll" in link_name:
                ET.SubElement(geometry_v, 'box', size=tuple_to_string((0.14, 0.1, 0.05)))
            elif "thigh" in link_name:
                ET.SubElement(geometry_v, 'cylinder', length=tuple_to_string((cylinder_dimensions[0]*1.5,)), radius=tuple_to_string((cylinder_dimensions[1],)))
            elif "calf" in link_name:
                ET.SubElement(geometry_v, 'cylinder', length=tuple_to_string((cylinder_dimensions[0]*1.7,)), radius=tuple_to_string((cylinder_dimensions[1],)))
            
            elif "shoulder_pitch" in link_name:
                ET.SubElement(geometry_v, 'cylinder', length=tuple_to_string((cylinder_dimensions[0]*2.5,)), radius=tuple_to_string((cylinder_dimensions[1],)))
            elif "shoulder_roll" in link_name:
                ET.SubElement(geometry_v, 'sphere', radius=tuple_to_string((0.05,)))
            elif "shoulder_yaw" in link_name:
                ET.SubElement(geometry_v, 'cylinder', length=tuple_to_string((cylinder_dimensions[0]*1.5,)), radius=tuple_to_string((cylinder_dimensions[1],)))
            elif "elbow" in link_name:
                ET.SubElement(geometry_v, 'cylinder', length=tuple_to_string((cylinder_dimensions[0]*1.5,)), radius=tuple_to_string((cylinder_dimensions[1],)))    
            
            else:
                ET.SubElement(geometry_v, 'cylinder', length=tuple_to_string((cylinder_dimensions[0],)), radius=tuple_to_string((cylinder_dimensions[1],)))
        else:
            ET.SubElement(geometry_v, 'cylinder', length=tuple_to_string((cylinder_dimensions[0],)), radius=tuple_to_string((cylinder_dimensions[1],)))
        
        # ET.SubElement(geometry_v, 'box', size=tuple_to_string((cylinder_dimensions[1], cylinder_dimensions[1], cylinder_dimensions[0])))
        # if cylinder_dimensions_visual is not None:
        #     ET.SubElement(geometry_v, 'box', size=tuple_to_string((cylinder_dimensions_visual[1], cylinder_dimensions_visual[1], cylinder_dimensions_visual[0])))
        # else:
        #     ET.SubElement(geometry_v, 'box', size=tuple_to_string((cylinder_dimensions[1], cylinder_dimensions[1], cylinder_dimensions[0])))
            
    material = ET.SubElement(visual, 'material', name=f"{link_name}_material")
    # print("robot_name:", robot_name)
    

    # ########### STRONG COLORS ############
    if "dog" in robot_name and color == HIGHLIGHT_COLOR:
        color = rgba_to_normalized_string(54,54,53, 255) # GREY 
    if "dog" in robot_name and color == BASE_COLOR:
        color = rgba_to_normalized_string(195, 58, 38, 255) # RED
    
    if "humanoid" in robot_name and color == HIGHLIGHT_COLOR:
        # color = rgba_to_normalized_string(51,102,204, 255) # BLUE
        # color = rgba_to_normalized_string(200,200,200, 255) # WHITE
        color = rgba_to_normalized_string(54,54,53, 255) # GREY 
    if "humanoid" in robot_name and color == BASE_COLOR:
        # color = rgba_to_normalized_string(200,200,200, 255) # WHITE
        color = rgba_to_normalized_string(51,102,204, 255) # BLUE
    
    if "hexapod" in robot_name and color == HIGHLIGHT_COLOR:
        color = rgba_to_normalized_string(54,54,53, 255) # GREY 
    if "hexapod" in robot_name and color == BASE_COLOR:
        color = rgba_to_normalized_string(255,204,50, 255) # YELLOW
    # ########### STRONG COLORS ############       
        
    ET.SubElement(material, 'color', rgba=color)

    # Collision element
    collision = ET.SubElement(link, 'collision')
    origin_c = ET.SubElement(collision, 'origin', xyz=tuple_to_string(xyz), rpy=tuple_to_string(rpy))
    geometry_c = ET.SubElement(collision, 'geometry')
    if geometry_type == "box":
        ET.SubElement(geometry_c, 'box', size=tuple_to_string(box_dimensions))
    elif geometry_type == "sphere":
        ET.SubElement(geometry_c, 'sphere', radius=tuple_to_string(sphere_dimensions))
    elif geometry_type == "cylinder":
        ET.SubElement(geometry_c, 'cylinder', length=tuple_to_string((cylinder_dimensions[0],)), radius=tuple_to_string((cylinder_dimensions[1],)))

    return link

# Function to create a URDF joint element
def create_joint(joint_name, 
                 parent_link, child_link, 
                 joint_type="revolute", 
                 xyz=(0,0,0), rpy=(0,0,0), axis="1 0 0", 
                 lower_limit=-1.57, upper_limit=1.57, 
                 effort_limit=100, velocity_limit=30):
    
    joint = ET.Element('joint', name=joint_name, type=joint_type)
    ET.SubElement(joint, 'parent', link=parent_link)
    ET.SubElement(joint, 'child', link=child_link)
    ET.SubElement(joint, 'origin', xyz=tuple_to_string(xyz), rpy=tuple_to_string(rpy))
    
    # Add axis and limit only for revolute joints
    if joint_type == "revolute":
        ET.SubElement(joint, 'axis', xyz=axis)
        ET.SubElement(joint, 'limit', lower=str(lower_limit), upper=str(upper_limit), effort=str(effort_limit), velocity=str(velocity_limit))
    
    # For fixed joints, no axis or limit is required
    return joint

def scale_range(a, b, scale_factor):
    """
    Scale a range (a, b) by a given scale factor while keeping the center point fixed.

    Parameters:
        a (float): Start of the original range.
        b (float): End of the original range.
        scale_factor (float): The factor by which to scale the range.

    Returns:
        tuple: New range (new_a, new_b) after scaling.
    """
    assert a < b, "Start of the range must be less than the end of the range."
    # Calculate the center point of the original range
    center = (a + b) / 2
    # Calculate the new length of the range
    new_length = scale_factor * (b - a)
    # Calculate the new start and end of the range
    new_a = center - new_length / 2
    new_b = center + new_length / 2
    return new_a, new_b

# Function to generate URDF for a robot dog
# Template: Unitree Go2
def dog_generate_urdf(input_json_file, robot_name="gen_dog", output_file="gen_dog.urdf"):
    # Root URDF element
    robot = ET.Element('robot', name="gen_dog")
    
    # Body dimensions
    with open(input_json_file, 'r') as file:
        parameters = json.load(file)
    
    knee_nums = parameters["knee_nums"]
    apply_knee_joint_limit_scale_nums = parameters["apply_knee_joint_limit_scale_nums"]
    apply_knee_joint_limit_scale_factor = parameters["apply_knee_joint_limit_scale_factor"]
    true_apply_knee_joint_limit_scale_factor = apply_knee_joint_limit_scale_factor
    if APPLY_SCALE_IN_URDF is False:
        apply_knee_joint_limit_scale_factor = 1.0
    
    body_length = parameters["body_size"]["length"]
    body_width = parameters["body_size"]["width"]
    body_height = parameters["body_size"]["height"]
    
    # hip_link_radius = parameters["hip_link_radius"]
    hip_link_length = parameters["hip_link"]["length"]
    hip_link_radius = parameters["hip_link"]["radius"]
    
    foot_link_radius = parameters["foot_link_radius"]
    
    # thigh_link_length = parameters["thigh_link"]["length"]
    # thigh_link_radius = parameters["thigh_link"]["radius"]
    thigh_link_length = parameters["thigh_link"]["length"]
    thigh_link_width = parameters["thigh_link"]["width"]
    thigh_link_height = parameters["thigh_link"]["height"]
    
    calf_link_length = parameters["calf_link"]["length"]
    calf_link_radius = parameters["calf_link"]["radius"]
    
    calflower_link_length = parameters["calflower_link"]["length"]
    calflower_link_radius = parameters["calflower_link"]["radius"]
    
    calflower1_link_length = parameters["calflower1_link"]["length"]
    calflower1_link_radius = parameters["calflower1_link"]["radius"]  
    
    self_collision_joint_offset = parameters["self_collision_joint_offset"]
    
    ######################### Link parameters #########################
    # Link xyz offsets
    hip_link_xyz_offsets = {
        'front_left': (0, 0.08, 0),
        'front_right': (0, -0.08, 0),
        'rear_left': (0, 0.08, 0),
        'rear_right': (0, -0.08, 0)
    }
    
    calf_link_xyz_offset = (0.008, 0, 0)
    calf_link_rpy_offset = (0, -0.21, 0)
    
    # Inertial origin for each link
    body_link_inertial_origin_xyz = (0.021112, 0, -0.005366)
    body_link_inertial_origin_rpy = (0, 0, 0)
    
    fl_hip_link_inertial_origin_xyz = (-0.0054, 0.00194, -0.000105)
    fr_hip_link_inertial_origin_xyz = (-0.0054, -0.00194, -0.000105)
    rl_hip_link_inertial_origin_xyz = (0.0054, 0.00194, -0.000105)
    rr_hip_link_inertial_origin_xyz = (0.0054, -0.00194, -0.000105)
    hip_link_inertial_origin_xyzs = {
        'front_left': fl_hip_link_inertial_origin_xyz,
        'front_right': fr_hip_link_inertial_origin_xyz,
        'rear_left': rl_hip_link_inertial_origin_xyz,
        'rear_right': rr_hip_link_inertial_origin_xyz
    }
    hip_link_inertial_origin_rpy = (0, 0, 0)
    
    left_thigh_link_inertial_origin_xyz = (-0.00374, -0.0223, -0.0327)
    right_thigh_link_inertial_origin_xyz = (-0.00374, 0.0223, -0.0327)
    thigh_link_inertial_origin_xyzs = {
        'front_left': left_thigh_link_inertial_origin_xyz,
        'front_right': right_thigh_link_inertial_origin_xyz,
        'rear_left': left_thigh_link_inertial_origin_xyz,
        'rear_right': right_thigh_link_inertial_origin_xyz
    }
    thigh_link_inertial_origin_rpy = (0, 0, 0)
    
    left_calf_link_inertial_origin_xyz = (0.00548, -0.000975, -0.115)
    right_calf_link_inertial_origin_xyz = (0.00548, 0.000975, -0.115)
    calf_link_inertial_origin_xyzs = {
        'front_left': left_calf_link_inertial_origin_xyz,
        'front_right': right_calf_link_inertial_origin_xyz,
        'rear_left': left_calf_link_inertial_origin_xyz,
        'rear_right': right_calf_link_inertial_origin_xyz
    }
    calf_link_inertial_origin_rpy = (0, 0, 0)
    
    # Mass for each link
    body_link_mass = 6.921
    hip_link_mass = 0.678
    thigh_link_mass = 1.152
    calf_link_mass = 0.154
    foot_link_mass = 0.04
    
    # Inertia matrix for each link
    body_inertia = (0.02448, 0.00012166, 0.0014849, 0.098077, -3.12E-05, 0.107)
    
    fl_hip_inertia = (0.00048, -3.01E-06, 1.11E-06, 0.000884, -1.42E-06, 0.000596)
    fr_hip_inertia = (0.00048, 3.01E-06, 1.11E-06, 0.000884, 1.42E-06, 0.000596)
    rl_hip_inertia = (0.00048, 3.01E-06, -1.11E-06, 0.000884, -1.42E-06, 0.000596) 
    rr_hip_inertia = (0.00048, -3.01E-06, -1.11E-06, 0.000884, 1.42E-06, 0.000596)
    hip_inertias = {
        'front_left': fl_hip_inertia,
        'front_right': fr_hip_inertia,
        'rear_left': rl_hip_inertia,
        'rear_right': rr_hip_inertia
    }
    
    fl_thigh_inertia = (0.00584, 8.72E-05, -0.000289, 0.0058, 0.000808, 0.00103)
    fr_thigh_inertia = (0.00584, -8.72E-05, -0.000289, 0.0058, -0.000808, 0.00103)
    rl_thigh_inertia = (0.00584, 8.72E-05, -0.000289, 0.0058, 0.000808, 0.00103)
    rr_thigh_inertia = (0.00584, -8.72E-05, -0.000289, 0.0058, -0.000808, 0.00103)
    thigh_inertias = {
        'front_left': fl_thigh_inertia,
        'front_right': fr_thigh_inertia,
        'rear_left': rl_thigh_inertia,
        'rear_right': rr_thigh_inertia
    }
    
    fl_calf_inertia = (0.00108, 3.4E-07, 1.72E-05, 0.0011, 8.28E-06, 3.29E-05)
    fr_calf_inertia = (0.00108, -3.4E-07, 1.72E-05, 0.0011, -8.28E-06, 3.29E-05)
    rl_calf_inertia = (0.00108, 3.4E-07, 1.72E-05, 0.0011, 8.28E-06, 3.29E-05)
    rr_calf_inertia = (0.00108, -3.4E-07, 1.72E-05, 0.0011, -8.28E-06, 3.29E-05)
    calf_inertias = {
        'front_left': fl_calf_inertia,
        'front_right': fr_calf_inertia,
        'rear_left': rl_calf_inertia,
        'rear_right': rr_calf_inertia
    }
    
    foot_inertia = (9.6e-06, 0, 0, 9.6e-06, 0, 9.6e-06)
    ######################### Link parameters #########################
    
    ######################### Joint parameters #########################
    # Joint positions, also the corner positions for each leg
    fl_leg_pos = (body_length/2+self_collision_joint_offset, body_width/2+self_collision_joint_offset, 0)
    fr_leg_pos = (body_length/2+self_collision_joint_offset, -body_width/2-self_collision_joint_offset, 0)
    rl_leg_pos = (-body_length/2-self_collision_joint_offset, body_width/2+self_collision_joint_offset, 0)
    rr_leg_pos = (-body_length/2-self_collision_joint_offset, -body_width/2-self_collision_joint_offset, 0)
    leg_positions = {
        'front_left': fl_leg_pos,    # Front-left corner of the body
        'front_right': fr_leg_pos,  # Front-right corner of the body
        'rear_left': rl_leg_pos,    # Rear-left corner of the body
        'rear_right': rr_leg_pos,  # Rear-right corner of the body
    }
    
    thigh_joint_xyz_offsets = {
        'front_left': (0, 0.0955, 0),
        'front_right': (0, -0.0955, 0),
        'rear_left': (0, 0.0955, 0),
        'rear_right': (0, -0.0955, 0)
    }
    
    calflower_joint_xyz_offset = (0.02, 0, 0)
    calflower_joint_rpy_offset = (0, 0.05, 0)

    calflower1_joint_xyz_offset = (-0.01, 0, 0)
    calflower1_joint_rpy_offset = (0, 0.48, 0)
    
    # Joint limits
    hip_joint_limit_lower = -1.05
    hip_joint_limit_upper = 1.05
    # hip_joint_limit_lower, hip_joint_limit_upper = scale_range(hip_joint_limit_lower, hip_joint_limit_upper, joint_limit_scale_factor)
    
    front_thigh_joint_limit_lower = -1.57
    front_thigh_joint_limit_upper = 3.49
    # front_thigh_joint_limit_lower, front_thigh_joint_limit_upper = scale_range(front_thigh_joint_limit_lower, front_thigh_joint_limit_upper, joint_limit_scale_factor)
    
    rear_thigh_joint_limit_lower = -0.52
    rear_thigh_joint_limit_upper = 4.53
    # rear_thigh_joint_limit_lower, rear_thigh_joint_limit_upper = scale_range(rear_thigh_joint_limit_lower, rear_thigh_joint_limit_upper, joint_limit_scale_factor)
    
    thigh_joint_lower_limits = {
        'front_left': front_thigh_joint_limit_lower,
        'front_right': front_thigh_joint_limit_lower,
        'rear_left': rear_thigh_joint_limit_lower,
        'rear_right': rear_thigh_joint_limit_lower
    }
    thigh_joint_upper_limits = {
        'front_left': front_thigh_joint_limit_upper,
        'front_right': front_thigh_joint_limit_upper,
        'rear_left': rear_thigh_joint_limit_upper,
        'rear_right': rear_thigh_joint_limit_upper
    }
    
    knee_joint_limit_lower = -2.72
    knee_joint_limit_upper = -0.84
    
    if apply_knee_joint_limit_scale_factor != 1:
        raise ValueError("Invalid apply_knee_joint_limit_scale_factor")
    scaled_knee_joint_limit_lower, scaled_knee_joint_limit_upper = scale_range(knee_joint_limit_lower, knee_joint_limit_upper, apply_knee_joint_limit_scale_factor)
    
    final_applied_knee_joint_limit_lower = knee_joint_limit_lower
    final_applied_knee_joint_limit_upper = knee_joint_limit_upper
    
    # if robot_name == "gen_dog_40":
    #     print("Scaled knee joint limits:", scaled_knee_joint_limit_lower, scaled_knee_joint_limit_upper)
    
    # Joint effort limits
    hip_joint_effort_limit = 23.7
    thigh_joint_effort_limit = 23.7
    knee_joint_effort_limit = 45.43
    
    # Joint velocity limits
    hip_joint_velocity_limit = 30.1
    thigh_joint_velocity_limit = 30.1
    knee_joint_velocity_limit = 15.7
    ######################### Joint parameters #########################
    
    # Create the body
    body_link_name = "trunk"
    body_link_size = (body_length, body_width, body_height)
    body_link_inertia = body_inertia
    body_link = create_link(link_name=body_link_name, 
                            geometry_type="box", box_dimensions=body_link_size, 
                            inertial_origin_xyz=body_link_inertial_origin_xyz, 
                            mass=body_link_mass, 
                            inertia=body_link_inertia, robot_name=robot_name)
    robot.append(body_link)

    # Create the four legs
    for leg, leg_position in leg_positions.items():
        
        '''
            For each link, the default origin is its center, the final origin is offset by link_xyz. 
            The link's origin will be mounted at the joint position whose child link is the current link.
        '''
        # Hip link
        hip_link_name = f"{leg}_hip"
        hip_link_type = "cylinder"
        hip_link_dimensions = (hip_link_length, hip_link_radius)
        
        hip_link_xyz= (0, 0, 0)
        hip_link_xyz_offset = hip_link_xyz_offsets[leg]
        hip_link_xyz = tuple(map(sum, zip(hip_link_xyz, hip_link_xyz_offset)))
        hip_link_rpy = (1.57, 0, 0)
        
        hip_link_intertia = hip_inertias[leg]
        hip_link = create_link(link_name=hip_link_name, 
                               geometry_type=hip_link_type, 
                               xyz=hip_link_xyz, 
                               rpy=hip_link_rpy,
                               cylinder_dimensions=hip_link_dimensions, 
                               inertial_origin_xyz=hip_link_inertial_origin_xyzs[leg],
                               mass=hip_link_mass, 
                               inertia=hip_link_intertia, robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(hip_link)
        
        # Hip joint connects the body to the hip, position each leg at the corresponding corner
        hip_pitch_joint_name = f"{leg}_hip_pitch_joint"
        hip_pitch_joint_xyz = leg_position
        hip_pitch_joint_lower_limit = hip_joint_limit_lower
        hip_pitch_joint_upper_limit = hip_joint_limit_upper
        hip_pitch_joint_effort_limit = hip_joint_effort_limit
        hip_pitch_joint_velocity_limit = hip_joint_velocity_limit
        hip_pitch_joint = create_joint(joint_name=hip_pitch_joint_name, 
                                       parent_link=body_link_name, 
                                       child_link=hip_link_name, 
                                       xyz=hip_pitch_joint_xyz, 
                                       axis=X_AXIS, 
                                       lower_limit=hip_pitch_joint_lower_limit, upper_limit=hip_pitch_joint_upper_limit,
                                       effort_limit=hip_pitch_joint_effort_limit, velocity_limit=hip_pitch_joint_velocity_limit)
        robot.append(hip_pitch_joint)
        
        # Thigh link
        thigh_link_name = f"{leg}_thigh"
        thigh_link_type = "box"
        thigh_link_dimensions = (thigh_link_length, thigh_link_width, thigh_link_height)
        thigh_link_xyz = (0, 0, -thigh_link_length/2)
        thigh_link_rpy = (0, 1.57, 0)
        thigh_link_inertia = thigh_inertias[leg]
        thigh_link = create_link(link_name=thigh_link_name, 
                                 geometry_type=thigh_link_type, 
                                 xyz=thigh_link_xyz, 
                                 rpy=thigh_link_rpy,
                                 box_dimensions=thigh_link_dimensions, 
                                 inertial_origin_xyz=thigh_link_inertial_origin_xyzs[leg],
                                 mass=thigh_link_mass, 
                                 inertia=thigh_link_inertia, robot_name=robot_name)
        robot.append(thigh_link)
        
        # Thigh joint connects the hip to the thigh
        thigh_joint_name = f"{leg}_thigh_joint"
        thigh_joint_xyz = (0,0,0-self_collision_joint_offset)
        thigh_joint_xyz_offset = thigh_joint_xyz_offsets[leg]
        thigh_joint_xyz = tuple(map(sum, zip(thigh_joint_xyz, thigh_joint_xyz_offset)))
        thigh_joint_limit_lower = thigh_joint_lower_limits[leg]
        thigh_joint_limit_upper = thigh_joint_upper_limits[leg]
        thigh_joint_effort_limit = thigh_joint_effort_limit
        thigh_joint_velocity_limit = thigh_joint_velocity_limit
        thigh_joint = create_joint(joint_name=thigh_joint_name, 
                                   parent_link=hip_link_name, 
                                   child_link=thigh_link_name, 
                                   xyz=thigh_joint_xyz, 
                                   axis=Y_AXIS, 
                                   lower_limit=thigh_joint_limit_lower, upper_limit=thigh_joint_limit_upper,
                                   effort_limit=thigh_joint_effort_limit, velocity_limit=thigh_joint_velocity_limit)
        robot.append(thigh_joint)
        
        

        # Calf link
        calf_link_name = f"{leg}_calf"
        calf_link_type = "cylinder"
        calf_link_dimensions = (calf_link_length, calf_link_radius)
        calf_link_xyz = (0, 0, -calf_link_length/2)
        calf_link_xyz_offset = calf_link_xyz_offset
        calf_link_xyz = tuple(map(sum, zip(calf_link_xyz, calf_link_xyz_offset)))
        calf_link_rpy = (0, 0, 0)
        calf_link_rpy_offset = calf_link_rpy_offset
        calf_link_rpy = tuple(map(sum, zip(calf_link_rpy, calf_link_rpy_offset)))
        calf_link_inertia = calf_inertias[leg]
        calf_link = create_link(link_name=calf_link_name, 
                                geometry_type=calf_link_type, 
                                xyz=calf_link_xyz, 
                                rpy = calf_link_rpy,
                                cylinder_dimensions=calf_link_dimensions, 
                                inertial_origin_xyz=calf_link_inertial_origin_xyzs[leg],
                                mass=calf_link_mass, 
                                inertia=calf_link_inertia, robot_name=robot_name)
        if knee_nums[leg] != 0:
            robot.append(calf_link)
        
        # Knee joint connects the thigh to the calf
        apply_knee_joint_limit_scale_num = apply_knee_joint_limit_scale_nums[leg]
        
        knee_joint_name = f"{leg}_knee_joint"
        if knee_nums[leg] == 0:
            knee_joint_type = None
        else:
            knee_joint_type = "revolute"
        knee_joint_xyz = (0,0,-thigh_link_length-self_collision_joint_offset)
        if apply_knee_joint_limit_scale_num == 0:
            applied_knee_joint_limit_lower = knee_joint_limit_lower
            applied_knee_joint_limit_upper = knee_joint_limit_upper
        else:
            applied_knee_joint_limit_lower = scaled_knee_joint_limit_lower
            applied_knee_joint_limit_upper = scaled_knee_joint_limit_upper
        
        if applied_knee_joint_limit_lower > final_applied_knee_joint_limit_lower:
            final_applied_knee_joint_limit_lower = applied_knee_joint_limit_lower
        if applied_knee_joint_limit_upper < final_applied_knee_joint_limit_upper:
            final_applied_knee_joint_limit_upper = applied_knee_joint_limit_upper
        
        knee_joint_effort_limit = knee_joint_effort_limit
        knee_joint_velocity_limit = knee_joint_velocity_limit
        knee_joint = create_joint(joint_name=knee_joint_name, 
                                  parent_link=thigh_link_name, 
                                  child_link=calf_link_name, 
                                  joint_type=knee_joint_type,
                                  xyz=knee_joint_xyz, 
                                  axis=Y_AXIS, 
                                  lower_limit=applied_knee_joint_limit_lower, 
                                  upper_limit=applied_knee_joint_limit_upper,
                                  effort_limit=knee_joint_effort_limit, velocity_limit=knee_joint_velocity_limit)
        if knee_nums[leg] != 0:
            robot.append(knee_joint)
        
        lowest_calf_link_name = calf_link_name
        
        if knee_nums[leg] > 1:
            
            count_apply_knee_joint_limit_scale = apply_knee_joint_limit_scale_num
            assert count_apply_knee_joint_limit_scale < knee_nums[leg], "Invalid apply_knee_joint_limit_scale_num"
             
            for i in range(knee_nums[leg]-1):
                additional_calf_link_name = f"{leg}_calf_{i+1}"
                additional_calf_link_type = "cylinder"
                additional_calf_link_dimensions = (calf_link_length, calf_link_radius)
                additional_calf_link_xyz = (0, 0, -calf_link_length/2)
                additional_calf_link_xyz_offset = calf_link_xyz_offset
                additional_calf_link_xyz = tuple(map(sum, zip(additional_calf_link_xyz, additional_calf_link_xyz_offset)))
                additional_calf_link_rpy = (0, 0, 0)
                additional_calf_link_rpy_offset = calf_link_rpy_offset
                additional_calf_link_rpy = tuple(map(sum, zip(additional_calf_link_rpy, additional_calf_link_rpy_offset)))
                additional_calf_link_inertia = calf_inertias[leg]
                additional_calf_link = create_link(link_name=additional_calf_link_name,
                                                    geometry_type=additional_calf_link_type,
                                                    xyz=additional_calf_link_xyz,
                                                    rpy=additional_calf_link_rpy,
                                                    cylinder_dimensions=additional_calf_link_dimensions,
                                                    inertial_origin_xyz=calf_link_inertial_origin_xyzs[leg],
                                                    mass=calf_link_mass,
                                                    inertia=additional_calf_link_inertia, robot_name=robot_name)
                robot.append(additional_calf_link)
                
                # Knee joint connects the thigh to the calf
                additional_knee_joint_name = f"{leg}_knee_{i+1}_joint"
                additional_knee_joint_type = "revolute"
                additional_knee_joint_xyz = (0,0,-calf_link_length-self_collision_joint_offset)
                
                if (count_apply_knee_joint_limit_scale -1) <= 0:
                    additional_knee_joint_limit_lower = -1.57
                    additional_knee_joint_limit_upper = 1.57
                else:
                    additional_knee_joint_limit_lower, additional_knee_joint_limit_upper = scale_range(-1.57, 1.57, apply_knee_joint_limit_scale_factor)
                    count_apply_knee_joint_limit_scale -= 1
                    
                # if additional

                additional_knee_joint_effort_limit = knee_joint_effort_limit
                additional_knee_joint_velocity_limit = knee_joint_velocity_limit
                additional_knee_joint = create_joint(joint_name=additional_knee_joint_name,
                                                    parent_link=lowest_calf_link_name,
                                                    child_link=additional_calf_link_name,
                                                    joint_type=additional_knee_joint_type,
                                                    xyz=additional_knee_joint_xyz,
                                                    axis=Y_AXIS,
                                                    lower_limit=additional_knee_joint_limit_lower, upper_limit=additional_knee_joint_limit_upper,
                                                    effort_limit=additional_knee_joint_effort_limit, velocity_limit=additional_knee_joint_velocity_limit)
                robot.append(additional_knee_joint)
                
                lowest_calf_link_name = additional_calf_link_name
        
        # Calflower link
        calflower_link_name = f"{leg}_calflower"
        calflower_link_type = "cylinder"
        calflower_link_dimensions = (calflower_link_length, calflower_link_radius)
        calflower_link_xyz = (0, 0, -calflower_link_length/2)
        calflower_link_rpy = (0, 0, 0)
        calflower_link = create_link(link_name=calflower_link_name, 
                                geometry_type=calflower_link_type, 
                                xyz=calflower_link_xyz, 
                                rpy = calflower_link_rpy,
                                cylinder_dimensions=calflower_link_dimensions, 
                                no_inertial=True, robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(calflower_link)
        
        # Calflower joint connects the calf to the calflower
        calflower_joint_name = f"{leg}_calflower_joint"
        
        if knee_nums[leg] == 0:
            calflower_joint_xyz = (0,0,-thigh_link_length-self_collision_joint_offset)
        else:
            calflower_joint_xyz = (0,0,-calf_link_length-self_collision_joint_offset)
        calflower_joint_xyz_offset = calflower_joint_xyz_offset
        calflower_joint_xyz = tuple(map(sum, zip(calflower_joint_xyz, calflower_joint_xyz_offset)))
        
        calflower_joint_rpy = (0, 0, 0)
        calflower_joint_rpy_offset = calflower_joint_rpy_offset
        calflower_joint_rpy = tuple(map(sum, zip(calflower_joint_rpy, calflower_joint_rpy_offset)))
        
        if knee_nums[leg] == 0:
            calflower_joint = create_joint(joint_name=calflower_joint_name, 
                                    parent_link=thigh_link_name, 
                                    child_link=calflower_link_name, 
                                    xyz=calflower_joint_xyz, 
                                    rpy=calflower_joint_rpy,
                                    axis=Y_AXIS, 
                                    joint_type="fixed")
            robot.append(calflower_joint)
        else:
            calflower_joint = create_joint(joint_name=calflower_joint_name, 
                                    parent_link=lowest_calf_link_name, 
                                    child_link=calflower_link_name, 
                                    xyz=calflower_joint_xyz, 
                                    rpy=calflower_joint_rpy,
                                    axis=Y_AXIS, 
                                    joint_type="fixed")
            robot.append(calflower_joint)
        
        # Calflower1 link
        calflower1_link_name = f"{leg}_calflower1"
        calflower1_link_type = "cylinder"
        calflower1_link_dimensions = (calflower1_link_length, calflower1_link_radius)
        calflower1_link_xyz = (0, 0, -calflower1_link_length/2)
        calflower1_link_rpy = (0, 0, 0)
        calflower1_link = create_link(link_name=calflower1_link_name, 
                                geometry_type=calflower1_link_type, 
                                xyz=calflower1_link_xyz, 
                                rpy = calflower1_link_rpy,
                                cylinder_dimensions=calflower1_link_dimensions, 
                                no_inertial=True, robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(calflower1_link)
        
        # Calflower1 joint connects the calflower to the calflower1
        calflower1_joint_name = f"{leg}_calflower1_joint"
        
        calflower1_joint_xyz = (0,0,-calflower_link_length-self_collision_joint_offset)
        calflower1_joint_xyz_offset = calflower1_joint_xyz_offset
        calflower1_joint_xyz = tuple(map(sum, zip(calflower1_joint_xyz, calflower1_joint_xyz_offset)))
        
        calflower1_joint_rpy = (0, 0, 0)
        calflower1_joint_rpy_offset = calflower1_joint_rpy_offset
        calflower1_joint_rpy = tuple(map(sum, zip(calflower1_joint_rpy, calflower1_joint_rpy_offset)))
        
        calflower1_joint = create_joint(joint_name=calflower1_joint_name,
                                    parent_link=calflower_link_name,
                                    child_link=calflower1_link_name,
                                    xyz=calflower1_joint_xyz,
                                    rpy=calflower1_joint_rpy,
                                    axis=Y_AXIS,
                                    joint_type="fixed")
        robot.append(calflower1_joint)

        # Foot link
        foot_link_name = f"{leg}_foot"
        foot_link_type = "sphere"
        foot_link_dimensions = (foot_link_radius,)
        foot_link_inertia = foot_inertia
        foot_link = create_link(link_name=foot_link_name, 
                                geometry_type=foot_link_type, 
                                sphere_dimensions=foot_link_dimensions, 
                                mass=foot_link_mass, 
                                inertia=foot_link_inertia, robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(foot_link)

        # Ankle joint connects the calf to the foot
        ankle_joint_name = f"{leg}_ankle_joint"
        ankle_joint_xyz = (0,0,-calflower1_link_length-self_collision_joint_offset)
        ankle_joint = create_joint(joint_name=ankle_joint_name, 
                                   parent_link=calflower1_link_name, 
                                   child_link=foot_link_name, 
                                   joint_type="fixed", 
                                   xyz=ankle_joint_xyz, 
                                   axis=Y_AXIS)
        robot.append(ankle_joint)

    # Generate and prettify URDF tree
    pretty_urdf = prettify_xml(robot)

    if os.path.exists(output_file):
        os.remove(output_file)
    with open(output_file, "w") as f:
        f.write(pretty_urdf)

    # print("Robot Dog URDF file generated:", output_file)
    
    max_knee_num = max(knee_nums.values())
    drop_height = 1.2 * (
        hip_link_radius + \
        thigh_link_length + \
        self_collision_joint_offset + \
        max(max_knee_num, 1)*(calf_link_length + self_collision_joint_offset)+ \
        calflower_link_length + \
        calflower1_link_length + \
        2*foot_link_radius
    )
    
    action_space = 12 + knee_nums['front_left']-1 + knee_nums['front_right']-1 + knee_nums['rear_left']-1 + knee_nums['rear_right']-1
    
    final_applied_knee_joint_nominal_position = -1.5
    
    if APPLY_SCALE_IN_URDF is False:
        if final_applied_knee_joint_nominal_position > final_applied_knee_joint_limit_upper or final_applied_knee_joint_nominal_position < final_applied_knee_joint_limit_lower:
            final_applied_knee_joint_nominal_position = final_applied_knee_joint_limit_upper
        
    if max_knee_num == 0:
        nominal_joint_positions = {
            ".*_left_hip_pitch_joint": 0.1,
            ".*_right_hip_pitch_joint": -0.1,
            "front_.*_thigh_joint": 0,
            "rear_.*_thigh_joint": 0,
            # ".*_knee_joint": final_applied_knee_joint_limit_upper,
            # ".*_knee_.*_joint" : 0
    }
    elif max_knee_num == 1:
        nominal_joint_positions = {
            ".*_left_hip_pitch_joint": 0.1,
            ".*_right_hip_pitch_joint": -0.1,
            "front_.*_thigh_joint": 0.8,
            "rear_.*_thigh_joint": 1.0,
            ".*_knee_joint": final_applied_knee_joint_nominal_position,
            # ".*_knee_.*_joint" : 0
    }
    else:
        nominal_joint_positions = {
                ".*_left_hip_pitch_joint": 0.1,
                ".*_right_hip_pitch_joint": -0.1,
                "front_.*_thigh_joint": 0.8,
                "rear_.*_thigh_joint": 1.0,
                ".*_knee_joint": final_applied_knee_joint_nominal_position,
                ".*_knee_.*_joint" : 0
        }
    
    if max_knee_num == 0:
        reward_cfgs = {
            'feet_ground_contact_cfg': ".*foot",
            'feet_ground_asset_cfg': ".*foot",
            'undesired_contact_cfg': [".*thigh.*", ".*trunk.*"],
            'joint_hip_cfg': [".*hip.*joint"],
            'joint_knee_cfg': [],
            'illegal_contact_cfg': [".*trunk.*", ".*hip.*",".*thigh.*"]
            }
    else:
        reward_cfgs = {
            'feet_ground_contact_cfg': ".*foot",
            'feet_ground_asset_cfg': ".*foot",
            'undesired_contact_cfg': [".*calf.*", ".*thigh.*", ".*trunk.*"],
            'joint_hip_cfg': [".*hip.*joint"],
            'joint_knee_cfg': [".*knee.*joint"],
            'illegal_contact_cfg': [".*trunk.*", ".*hip.*",".*thigh.*", ".*calf.*"]
        }
    
    actuator_cfgs = {
        "base_legs": {
            "motor_type": "DCMotor",
            "joint_names_expr": [".*joint"],
            "effort_limit": 23.5,
            "saturation_effort": 23.5,
            "velocity_limit": 30.0,
            "stiffness": 25.0,
            "damping": 0.5,
            "friction": 0.0
        }
    }
    
    record_apply_joint_limit_scale_nums = {}
    # rename the keys in apply_knee_joint_limit_scale_nums and copy it to record_apply_joint_limit_scale_nums
    for key, value in apply_knee_joint_limit_scale_nums.items():
        # print(key, value)
        hip_pitch_joint_name = f"{key}_hip_pitch_joint"
        record_apply_joint_limit_scale_nums[hip_pitch_joint_name] = value
        thigh_joint_name = f"{key}_thigh_joint"
        record_apply_joint_limit_scale_nums[thigh_joint_name] = value
    

    return_values = {
        'robot_name': robot_name,
        'drop_height': drop_height,
        'action_space': action_space,
        'apply_joint_limit_scale_joint_names': record_apply_joint_limit_scale_nums,
        'apply_joint_limit_scale_factor': true_apply_knee_joint_limit_scale_factor,
        # 'apply_joint_limit_scale_names': record_apply_joint_limit_scale_nums,
        'nominal_joint_positions': nominal_joint_positions,
        'reward_cfgs': reward_cfgs,
        'actuators': actuator_cfgs
    }
    # print("Return values:", return_values)
    
    return return_values 

# Function to generate URDF for a humanoid robot
# Template: Unitree H1
def humanoid_generate_urdf(input_json_file, robot_name="gen_humanoid", output_file="gen_humanoid.urdf"):
    # Root URDF element for the humanoid robot
    robot = ET.Element('robot', name="humanoid_robot")

    # Body dimensions
    with open(input_json_file, 'r') as file:
        parameters = json.load(file)
    
    knee_nums = parameters["knee_nums"]
    apply_knee_joint_limit_scale_nums = parameters["apply_knee_joint_limit_scale_nums"]
    apply_knee_joint_limit_scale_factor = parameters["apply_knee_joint_limit_scale_factor"]   
    true_apply_knee_joint_limit_scale_factor = apply_knee_joint_limit_scale_factor
    if APPLY_SCALE_IN_URDF is False:
        apply_knee_joint_limit_scale_factor = 1.0
    
    torso_size = (parameters["torso_size"]["length"], parameters["torso_size"]["width"], parameters["torso_size"]["height"])
    # head_size = (parameters["head_size"]["diameter"], parameters["head_size"]["diameter"], parameters["head_size"]["height"])
    head_radius = parameters["head"]["radius"]
    pelvis_radius = parameters["pelvis"]["radius"]
    # upper_arm_length = parameters["upper_arm"]["length"]
    elbow_length = parameters["lower_arm"]["length"]
    thigh_length = parameters["thigh"]["length"]
    calf_length = parameters["calf"]["length"]
    elbow_radius = parameters["lower_arm"]["radius"]
    leg_radius = parameters["calf"]["radius"]
    foot_size = (parameters["foot_size"]["length"], parameters["foot_size"]["width"], parameters["foot_size"]["height"])
    self_collision_joint_offset = parameters["self_collision_joint_offset"]
    
    applied_calf_length = calf_length
    
    # Link Parameters
    # Mass
    pelvis_link_mass = 5.39
    torso_link_mass = 17.789
    
    # upper_arm_link_mass = 2.5
    shoulder_pitch_link_mass = 1.033
    shoulder_roll_link_mass = 0.793
    shoulder_yaw_link_mass = 0.839
    elbow_link_mass = 0.723
    
    hip_yaw_link_mass = 2.244
    hip_roll_link_mass = 2.232
    thigh_link_mass = 4.152
    calf_link_mass = 1.721
    foot_link_mass = 0.474
    
    # Inertia
    pelvis_inertia = (0.044582, 8.7034E-05, -1.9893E-05, 0.0082464, 4.021E-06, 0.049021)
    pelvis_inertia_origin_xyz = (-0.0002, 4E-05, -0.04522)
    
    torso_inertia = (0.4873, -0.00053763, 0.0020276, 0.40963, -0.00074582, 0.12785)
    torso_inertia_origin_xyz = (0.000489, 0.002797, 0.20484)
    
    # left_upper_arm_inertia = (0.00042388, -3.6086E-05, 0.00029293, 0.0060062, 4.664E-06, 0.0060023)
    # right_upper_arm_inertia = (0.00042388, 3.6086E-05, 0.00029293, 0.0060062, -4.664E-06, 0.0060023)
    # upper_arm_inertias = {
    #     'left': left_upper_arm_inertia,
    #     'right': right_upper_arm_inertia
    # }
    
    left_shoulder_pitch_link_inertia = (0.0012985, -1.7333E-05, 8.683E-06, 0.00087279, 3.9656E-05, 0.00097338)
    right_shoulder_pitch_link_inertia = (0.0012985, 1.7333E-05, 8.683E-06, 0.00087279, -3.9656E-05, 0.00097338)
    shoulder_pitch_link_inertias = {
        'left': left_shoulder_pitch_link_inertia,
        'right': right_shoulder_pitch_link_inertia
    }
    left_shoulder_pitch_link_inertia_orgin_xyz = (0.005045, 0.053657, -0.015715)
    right_shoulder_pitch_link_inertia_orgin_xyz = (0.005045, -0.053657, -0.015715)
    shoulder_pitch_link_inertia_origin_xyzs = {
        'left': left_shoulder_pitch_link_inertia_orgin_xyz,
        'right': right_shoulder_pitch_link_inertia_orgin_xyz
    }
    
    left_shoulder_yaw_link_inertia = (0.003664, -1.0671E-05, 0.00034733, 0.0040789, 7.0213E-05, 0.00066383)
    right_shoulder_yaw_link_inertia = (0.003664, 1.0671E-05, 0.00034733, 0.0040789, -7.0213E-05, 0.00066383)
    shoulder_yaw_link_inertias = {
        'left': left_shoulder_yaw_link_inertia,
        'right': right_shoulder_yaw_link_inertia
    }
    left_shoulder_yaw_link_inertia_orgin_xyz = (0.01365, 0.002767, -0.16266)
    right_shoulder_yaw_link_inertia_orgin_xyz = (0.01365, -0.002767, -0.16266)
    shoulder_yaw_link_inertia_origin_xyzs = {
        'left': left_shoulder_yaw_link_inertia_orgin_xyz,
        'right': right_shoulder_yaw_link_inertia_orgin_xyz
    }
    
    left_shoulder_roll_link_inertia = (0.0015742, 2.298E-06, -7.2265E-05, 0.0016973, -6.3691E-05, 0.0010183)
    right_shoulder_roll_link_inertia = (0.0015742, -2.298E-06, -7.2265E-05, 0.0016973, 6.3691E-05, 0.0010183)
    shoulder_roll_link_inertias = {
        'left': left_shoulder_roll_link_inertia,
        'right': right_shoulder_roll_link_inertia
    }
    left_shoulder_roll_link_inertia_orgin_xyz = (0.000679, 0.00115, -0.094076)
    right_shoulder_roll_link_inertia_orgin_xyz = (0.000679, -0.00115, -0.094076)
    shoulder_roll_link_inertia_origin_xyzs = {
        'left': left_shoulder_roll_link_inertia_orgin_xyz,
        'right': right_shoulder_roll_link_inertia_orgin_xyz
    }
    
    left_elbow_link_inertia = (0.00042388, -3.6086E-05, 0.00029293, 0.0060062, 4.664E-06, 0.0060023)
    right_elbow_link_inertia = (0.00042388, 3.6086E-05, 0.00029293, 0.0060062, -4.664E-06, 0.0060023)
    elbow_link_inertias = {
        'left': left_elbow_link_inertia,
        'right': right_elbow_link_inertia
    }
    left_elbow_link_inertia_orgin_xyz = (0.164862, 0.000118, -0.015734)
    right_elbow_link_inertia_orgin_xyz = (0.164862, -0.000118, -0.015734)
    elbow_link_inertia_origin_xyzs = {
        'left': left_elbow_link_inertia_orgin_xyz,
        'right': right_elbow_link_inertia_orgin_xyz
    }
    
    left_thigh_inertia = (0.082618, -0.00066654, 0.0040725, 0.081579, 0.0072024, 0.0060081)
    right_thigh_inertia = (0.082618, 0.00066654, 0.0040725, 0.081579, -0.0072024, 0.0060081)
    thigh_inertias = {
        'left': left_thigh_inertia,
        'right': right_thigh_inertia
    }
    left_thigh_inertia_origin_xyz = (0.00746, -0.02346, -0.08193)
    right_thigh_inertia_origin_xyz = (0.00746, 0.02346, -0.08193)
    thigh_inertia_origin_xyzs = {
        'left': left_thigh_inertia_origin_xyz,
        'right': right_thigh_inertia_origin_xyz
    }
    
    left_calf_inertia = (0.012205, -6.8431E-05, 0.0010862, 0.012509, 0.00022549, 0.0020629)
    right_calf_inertia = (0.012205, 6.8431E-05, 0.0010862, 0.012509, -0.00022549, 0.0020629)
    calf_inertias = {
        'left': left_calf_inertia,
        'right': right_calf_inertia
    }
    left_calf_inertia_origin_xyz = (-0.00136, -0.00512, -0.1384)
    right_calf_inertia_origin_xyz = (-0.00136, 0.00512, -0.1384)
    calf_inertia_origin_xyzs = {
        'left': left_calf_inertia_origin_xyz,
        'right': right_calf_inertia_origin_xyz
    }
    
    left_foot_inertia = (0.000159668, -0.000000005, 0.000141063, 0.002900286, 0.000000014, 0.002805438)
    right_foot_inertia = (0.000159668, 0.000000005, 0.000141063, 0.002900286, -0.000000014, 0.002805438)
    foot_inertias = {
        'left': left_foot_inertia,
        'right': right_foot_inertia
    }
    
    left_foot_inertia_origin_xyz = (0.042575, -0.000001, -0.044672)
    right_foot_inertia_origin_xyz = (0.042575, 0.000001, -0.044672)
    foot_inertia_origin_xyzs = {
        'left': left_foot_inertia_origin_xyz,
        'right': right_foot_inertia_origin_xyz
    }
    
    # Joint Parameters
    torso_joint_limit_lower = -2.35
    torso_joint_limit_upper = 2.35
    # torso_joint_limit_lower, torso_joint_limit_upper = scale_range(torso_joint_limit_lower, torso_joint_limit_upper, joint_limit_scale_factor)
    
    # shoulder_joint_limit_lower = -2.9
    # shoulder_joint_limit_upper = 2.9
    # shoulder_joint_limit_lower, shoulder_joint_limit_upper = scale_range(shoulder_joint_limit_lower, shoulder_joint_limit_upper, joint_limit_scale_factor)
    
    elbow_joint_limit_lower = -1.25
    elbow_joint_limit_upper = 2.61
    # elbow_joint_limit_lower, elbow_joint_limit_upper = scale_range(elbow_joint_limit_lower, elbow_joint_limit_upper, joint_limit_scale_factor)
    
    hip_yaw_joint_limit_lower = -0.43
    hip_yaw_joint_limit_upper = 0.43
    # hip_yaw_joint_limit_lower, hip_yaw_joint_limit_upper = scale_range(hip_yaw_joint_limit_lower, hip_yaw_joint_limit_upper, joint_limit_scale_factor)
    
    hip_roll_joint_limit_lower = -0.43
    hip_roll_joint_limit_upper = 0.43
    # hip_roll_joint_limit_lower, hip_roll_joint_limit_upper = scale_range(hip_roll_joint_limit_lower, hip_roll_joint_limit_upper, joint_limit_scale_factor)
    
    hip_pitch_joint_limit_lower = -3.1
    hip_pitch_joint_limit_upper = 2.5
    # hip_pitch_joint_limit_lower, hip_pitch_joint_limit_upper = scale_range(hip_pitch_joint_limit_lower, hip_pitch_joint_limit_upper, joint_limit_scale_factor)
    
    knee_joint_limit_lower = -0.26
    knee_joint_limit_upper = 2
    scaled_knee_joint_limit_lower, scaled_knee_joint_limit_upper = scale_range(knee_joint_limit_lower, knee_joint_limit_upper, apply_knee_joint_limit_scale_factor)
    
    ankle_joint_limit_lower = -0.87
    ankle_joint_limit_upper = 0.52
    # ankle_joint_limit_lower, ankle_joint_limit_upper = scale_range(ankle_joint_limit_lower, ankle_joint_limit_upper, joint_limit_scale_factor)
    
    # Create pelvis link
    pelvis_link_name = "pelvis"
    pelvis_link = create_link(link_name=pelvis_link_name, 
                              geometry_type="sphere", xyz=(0, 0, 0), 
                              sphere_dimensions=(pelvis_radius,), mass=pelvis_link_mass,
                              inertia=pelvis_inertia, inertial_origin_xyz=pelvis_inertia_origin_xyz, robot_name=robot_name)
    robot.append(pelvis_link)
    
    # Create torso link
    torso_link_name = "torso"
    torso_link = create_link(link_name=torso_link_name, 
                            #  geometry_type="box", xyz=(0, 0, 0), 
                             geometry_type="box", xyz=(0, 0, (pelvis_radius + torso_size[2]/2)+0.05), 
                             box_dimensions=torso_size, mass=torso_link_mass,
                             inertia=torso_inertia, inertial_origin_xyz=torso_inertia_origin_xyz, robot_name=robot_name)
    robot.append(torso_link)
    
    # Torso joint connecting pelvis to torso
    torso_joint_name = "torso_joint"
    torso_joint = create_joint(joint_name=torso_joint_name, 
                               parent_link=pelvis_link_name, child_link=torso_link_name, 
                               xyz=(0, 0, 0),
                               axis=Z_AXIS,
                               lower_limit=torso_joint_limit_lower, upper_limit=torso_joint_limit_upper, 
                               effort_limit=200, velocity_limit=23)
    robot.append(torso_joint)

    # Create head link
    head_link_name = "head"
    head_link = create_link(link_name=head_link_name, geometry_type="sphere", xyz=(0, 0, 0), sphere_dimensions=(head_radius,), robot_name=robot_name, color=HIGHLIGHT_COLOR)
    robot.append(head_link)

    # Neck joint (fixed) connecting torso to head
    neck_joint_name = "neck_joint"
    neck_joint = create_joint(joint_name=neck_joint_name, parent_link=torso_link_name, child_link=head_link_name, joint_type="fixed", xyz=(0, 0, torso_size[2]/2 + head_radius + 0.4))
    robot.append(neck_joint)

    # # Shoulder and Arm positions relative to the torso
    left_shoulder_pitch_joint_pos = (0.0055, 0.15535, 0.42999)
    right_shoulder_pitch_joint_pos = (0.0055, -0.15535, 0.42999)
    if torso_size[1]/2 > left_shoulder_pitch_joint_pos[1]:
        left_shoulder_pitch_joint_pos = (0.0055, torso_size[1]/2+(0.15535-0.13), 0.42999+0.05)
        right_shoulder_pitch_joint_pos = (0.0055, -torso_size[1]/2-(0.15535-0.13), 0.42999+0.05)
    
    left_shoulder_roll_joint_pos = (-0.0055, 0.0565, -0.0165)
    right_shoulder_roll_joint_pos = (-0.0055, -0.0565, -0.0165)
    
    left_shoulder_yaw_joint_pos = (0, 0, -0.1343)
    right_shoulder_yaw_joint_pos = (0, 0, -0.1343)

    # Create left and right arms
    for side in ["left", "right"]:
        # shoulder pitch link
        shoulder_pitch_link_name = f"{side}_shoulder_pitch_link"
        shoulder_pitch_link = create_link(link_name=shoulder_pitch_link_name, 
                                          geometry_type="cylinder", 
                                          xyz=(0, -0.05, 0) if side == "left" else (0, 0.05, 0),
                                          rpy=(1.57, 0, 0),
                                          mass = shoulder_pitch_link_mass,
                                          inertia=shoulder_pitch_link_inertias[side],
                                          inertial_origin_xyz=shoulder_pitch_link_inertia_origin_xyzs[side],
                                          cylinder_dimensions=(0.04, 0.03), robot_name=robot_name)
        robot.append(shoulder_pitch_link)
        
        # shoulde pitch joint
        shoulder_pitch_joint_name = f"{side}_shoulder_pitch_joint"
        shoulder_pitch_position = left_shoulder_pitch_joint_pos if side == "left" else right_shoulder_pitch_joint_pos
        shoulder_pitch_joint = create_joint(joint_name=shoulder_pitch_joint_name,
                                            parent_link=torso_link_name, child_link=shoulder_pitch_link_name,
                                            xyz=shoulder_pitch_position, 
                                            rpy = (0.43633, 0, 0) if side == "left" else (-0.43633, 0, 0),
                                            axis=Y_AXIS,
                                            lower_limit=-2.87, upper_limit=2.87,
                                            effort_limit=40, velocity_limit=9)
        robot.append(shoulder_pitch_joint)
        
        # shoulder roll link
        shoulder_roll_link_name = f"{side}_shoulder_roll_link"
        shoulder_roll_link = create_link(link_name=shoulder_roll_link_name,
                                        geometry_type="cylinder", 
                                        xyz=(0, 0, -0.04), 
                                        rpy=(0, 0, 0),
                                        mass = shoulder_roll_link_mass,
                                        inertia=shoulder_roll_link_inertias[side],
                                        inertial_origin_xyz=shoulder_roll_link_inertia_origin_xyzs[side],
                                        cylinder_dimensions=(0.01, 0.04), robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(shoulder_roll_link)
        # shoulder roll joint
        shoulder_roll_joint_name = f"{side}_shoulder_roll_joint"
        shoulder_roll_position = left_shoulder_roll_joint_pos if side == "left" else right_shoulder_roll_joint_pos
        
        shoulder_roll_joint_lower_limits = {
            "left": -0.34,
            "right": -3.11
        }
        shoulder_roll_joint_upper_limits = {
            "left": 3.11,
            "right": 0.34
        }
        
        shoulder_roll_joint = create_joint(joint_name=shoulder_roll_joint_name, 
                                      parent_link=shoulder_pitch_link_name, child_link=shoulder_roll_link_name, 
                                      xyz=shoulder_roll_position, 
                                      rpy = (-0.43633, 0, 0) if side == "left" else (0.43633, 0, 0),
                                      axis=X_AXIS,
                                      lower_limit=shoulder_roll_joint_lower_limits[side], upper_limit=shoulder_roll_joint_upper_limits[side],
                                      effort_limit=40, velocity_limit=9)
        robot.append(shoulder_roll_joint)
        
        # shoulder yaw link
        shoulder_yaw_link_name = f"{side}_shoulder_yaw_link"
        shoulder_yaw_link = create_link(link_name=shoulder_yaw_link_name,
                                        geometry_type="cylinder", 
                                        xyz=(0, 0, -0.11), 
                                        # cylinder_dimensions=(0.01, 0.04), 
                                        cylinder_dimensions=(0.15, 0.04),
                                        mass=shoulder_yaw_link_mass,
                                        inertia=shoulder_yaw_link_inertias[side],
                                        inertial_origin_xyz=shoulder_yaw_link_inertia_origin_xyzs[side], robot_name=robot_name)
        robot.append(shoulder_yaw_link)
        
        # shoulder yaw joint
        shoulder_yaw_joint_name = f"{side}_shoulder_yaw_joint"
        shoulder_yaw_joint_position = left_shoulder_yaw_joint_pos if side == "left" else right_shoulder_yaw_joint_pos
        
        shoulder_yaw_joint_lower_limits = {
            "left": -1.3,
            "right": -4.45
        }
        shoulder_yaw_joint_upper_limits = {
            "left": 4.45,
            "right": 1.3
        }
        
        shoulder_yaw_joint = create_joint(joint_name=shoulder_yaw_joint_name, 
                                      parent_link=shoulder_roll_link_name, child_link=shoulder_yaw_link_name, 
                                      xyz=shoulder_yaw_joint_position, axis=Z_AXIS,
                                      lower_limit=shoulder_yaw_joint_lower_limits[side], upper_limit=shoulder_yaw_joint_upper_limits[side],
                                      effort_limit=18, velocity_limit=20)
        robot.append(shoulder_yaw_joint)

        # # Lower arm link
        # lower_arm_link_name = f"{side}_lower_arm"
        # lower_arm_link_rpy = (0, 1.57 ,0)
        # lower_arm_link = create_link(link_name=lower_arm_link_name, 
        #                              geometry_type="cylinder", 
        #                              xyz=(lower_arm_length, 0, 0), 
        #                              rpy=lower_arm_link_rpy ,
        #                              cylinder_dimensions=(lower_arm_length, elbow_radius), 
        #                              mass=lower_arm_link_mass,
        #                              inertia=lower_arm_inertias[side])
        # robot.append(lower_arm_link)
        
        # elbow link
        elbow_link_name = f"{side}_elbow_link"
        elbow_link_rpy = (0, 1.57 ,0)
        elbow_link = create_link(link_name=elbow_link_name, 
                                     geometry_type="cylinder", 
                                     xyz=(elbow_length+0.035, 0, 0), 
                                     rpy=elbow_link_rpy ,
                                     cylinder_dimensions=(elbow_length, elbow_radius), 
                                     mass=elbow_link_mass,
                                     inertia=elbow_link_inertias[side],
                                     inertial_origin_xyz=elbow_link_inertia_origin_xyzs[side], robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(elbow_link)

        # Elbow joint
        elbow_joint_name = f"{side}_elbow_joint"
        elbow_joint = create_joint(joint_name=elbow_joint_name, 
                                   parent_link=shoulder_yaw_link_name, child_link=elbow_link_name, 
                                   xyz=(0.0185, 0, -0.198), axis=Y_AXIS,
                                   lower_limit=elbow_joint_limit_lower, upper_limit=elbow_joint_limit_upper,
                                   effort_limit=18, velocity_limit=20)
        robot.append(elbow_joint)

    # Leg positions relative to the torso
    # left_hip_pos = (0, torso_size[1]/2, -0.1742)
    # right_hip_pos = (0, -torso_size[1]/2, -0.1742)
    left_hip_pos = (0, 0.26/2, -0.1742)
    right_hip_pos = (0, -0.26/2, -0.1742)

    # Create left and right legs
    for side in ["left", "right"]:
        
        # Hip yaw link
        hip_yaw_link_name = f"{side}_hip_yaw_link"
        hip_yaw_link = create_link(link_name=hip_yaw_link_name, 
                                   geometry_type="cylinder", 
                                   xyz=(0.02, 0, 0), rpy=(0,1.57,0), 
                                   mass = hip_yaw_link_mass,
                                   cylinder_dimensions=(0.02, 0.01), robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(hip_yaw_link)
        
        # Hip yaw joint
        hip_yaw_joint_name = f"{side}_hip_yaw_joint"
        hip_yaw_position = left_hip_pos if side == "left" else right_hip_pos
        hip_yaw_joint = create_joint(joint_name=hip_yaw_joint_name, 
                                     parent_link=pelvis_link_name, child_link=hip_yaw_link_name, 
                                     xyz=hip_yaw_position, axis=Z_AXIS,
                                     lower_limit=hip_yaw_joint_limit_lower, upper_limit=hip_yaw_joint_limit_upper,
                                     effort_limit=200, velocity_limit=23)
        robot.append(hip_yaw_joint)
        
        # Hip roll link
        hip_roll_link_name = f"{side}_hip_roll_link"
        hip_roll_link = create_link(link_name=hip_roll_link_name, 
                                    geometry_type="cylinder", 
                                    xyz=(0, 0.06, 0) if side == "left" else (0, -0.06, 0),
                                    rpy=(1.57,0,0), 
                                    mass = hip_roll_link_mass,
                                    cylinder_dimensions=(0.01, 0.02), robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(hip_roll_link)
        
        # Hip roll joint
        hip_roll_joint_name = f"{side}_hip_roll_joint"
        hip_roll_position = (0.039468, 0, 0)
        hip_roll_joint = create_joint(joint_name=hip_roll_joint_name, 
                                      parent_link=hip_yaw_link_name, child_link=hip_roll_link_name, 
                                      xyz=hip_roll_position, axis=X_AXIS,
                                      lower_limit=hip_roll_joint_limit_lower, upper_limit=hip_roll_joint_limit_upper,
                                      effort_limit=200, velocity_limit=23)
        robot.append(hip_roll_joint)
        
        # Thigh link
        thigh_link_name = f"{side}_thigh_link"
        thigh_link = create_link(link_name=thigh_link_name, 
                                 geometry_type="cylinder", 
                                 xyz=(0, 0, -thigh_length), 
                                 cylinder_dimensions=(thigh_length, leg_radius), 
                                 mass=thigh_link_mass,
                                 inertia=thigh_inertias[side], 
                                 inertial_origin_xyz=thigh_inertia_origin_xyzs[side], robot_name=robot_name)
        robot.append(thigh_link)
        
        # Hip pitch joint
        hip_pitch_joint_name = f"{side}_hip_pitch_joint"
        hip_pitch_position = (0, self_collision_joint_offset/2, 0) if side == "left" else (0, -self_collision_joint_offset/2, 0)
        hip_pitch_joint = create_joint(joint_name=hip_pitch_joint_name, 
                                       parent_link=hip_roll_link_name, child_link=thigh_link_name, 
                                       xyz=hip_pitch_position, axis=Y_AXIS,
                                       lower_limit=hip_pitch_joint_limit_lower, upper_limit=hip_pitch_joint_limit_upper,
                                       effort_limit=200, velocity_limit=23)
        robot.append(hip_pitch_joint)

        # Calf link
        if knee_nums[side] == 0:
            applied_calf_length = -1
        else:
            applied_calf_length = calf_length / knee_nums[side]
        
        
        calf_link_name = f"{side}_calf_link"
        calf_link = create_link(link_name=calf_link_name, 
                                geometry_type="cylinder", 
                                xyz=(0, 0, -applied_calf_length), 
                                cylinder_dimensions=(applied_calf_length, leg_radius), 
                                mass=calf_link_mass,
                                inertia=calf_inertias[side], 
                                inertial_origin_xyz=calf_inertia_origin_xyzs[side], robot_name=robot_name)
        if knee_nums[side] != 0:
            robot.append(calf_link)
        
        # Knee joint
        apply_knee_joint_limit_scale_num = apply_knee_joint_limit_scale_nums[side]
        
        knee_joint_name = f"{side}_knee_joint"
        if knee_nums[side] == 0:
            knee_joint_type = None
        else:
            knee_joint_type = "revolute"
        
        if apply_knee_joint_limit_scale_num == 0:
            applied_knee_joint_limit_lower = knee_joint_limit_lower
            applied_knee_joint_limit_upper = knee_joint_limit_upper
        else:
            applied_knee_joint_limit_lower = scaled_knee_joint_limit_lower
            applied_knee_joint_limit_upper = scaled_knee_joint_limit_upper
        

        knee_joint = create_joint(joint_name=knee_joint_name, 
                                joint_type = knee_joint_type,
                                parent_link=thigh_link_name, child_link=calf_link_name, 
                                # xyz=(0, 0, -thigh_length-self_collision_joint_offset), 
                                xyz=(0, 0, -thigh_length-self_collision_joint_offset),
                                axis=Y_AXIS,
                                lower_limit=applied_knee_joint_limit_lower, upper_limit=applied_knee_joint_limit_upper,
                                effort_limit=300, velocity_limit=14)
        if knee_nums[side] != 0:    
            robot.append(knee_joint)
        
        lowest_calf_link_name = calf_link_name
        if knee_nums[side] > 1:
            for i in range(knee_nums[side]-1):
                
                count_apply_knee_joint_limit_scale = apply_knee_joint_limit_scale_num
                assert count_apply_knee_joint_limit_scale < knee_nums[side], "Invalid apply_knee_joint_limit_scale_num"
                
                additional_calf_link_name = f"{side}_calf_{i+1}_link"
                additional_calf_link = create_link(link_name=additional_calf_link_name, 
                                                   geometry_type="cylinder", 
                                                   xyz=(0, 0, -applied_calf_length/2), 
                                                   cylinder_dimensions=(applied_calf_length, leg_radius), 
                                                   mass=calf_link_mass,
                                                   inertia=calf_inertias[side],
                                                   inertial_origin_xyz=calf_inertia_origin_xyzs[side], robot_name=robot_name)
                robot.append(additional_calf_link)
                
                # Knee joint connects the thigh to the calf
                additional_knee_joint_name = f"{side}_knee_{i+1}_joint"
                
                # if (count_apply_knee_joint_limit_scale -1) == 0:
                #     applied_additional_knee_joint_limit_lower = knee_joint_limit_lower
                #     applied_additional_knee_joint_limit_upper = knee_joint_limit_upper
                # else:
                #     applied_additional_knee_joint_limit_lower = scaled_knee_joint_limit_lower
                #     applied_additional_knee_joint_limit_upper = scaled_knee_joint_limit_upper
                    
                #     count_apply_knee_joint_limit_scale -= 1
                
                if (count_apply_knee_joint_limit_scale -1) <= 0:
                    applied_additional_knee_joint_limit_lower = -1.57
                    applied_additional_knee_joint_limit_upper = 1.57
                else:
                    applied_additional_knee_joint_limit_lower, applied_additional_knee_joint_limit_upper = scale_range(-1.57, 1.57, apply_knee_joint_limit_scale_factor)
                    count_apply_knee_joint_limit_scale -= 1
                
                
                additional_knee_joint = create_joint(joint_name=additional_knee_joint_name,
                                                    parent_link=lowest_calf_link_name,
                                                    child_link=additional_calf_link_name,
                                                    joint_type="revolute",
                                                    # xyz=(0, 0, -applied_calf_length-self_collision_joint_offset),
                                                    xyz=(0, 0, -applied_calf_length-self_collision_joint_offset),
                                                    axis=Y_AXIS,
                                                    lower_limit=applied_additional_knee_joint_limit_lower, 
                                                    upper_limit=applied_additional_knee_joint_limit_upper,
                                                    effort_limit=300, velocity_limit=14)
                robot.append(additional_knee_joint)
                
                lowest_calf_link_name = additional_calf_link_name
        
        # Foot link
        foot_link_name = f"{side}_foot"
        foot_link = create_link(link_name=foot_link_name, 
                                geometry_type="box", 
                                xyz=(foot_size[0]/4, 0, -foot_size[0]/4), 
                                box_dimensions=foot_size, 
                                mass=foot_link_mass,
                                inertia=foot_inertias[side],
                                inertial_origin_xyz=foot_inertia_origin_xyzs[side], robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(foot_link)
        
        # Ankle joint
        ankle_joint_name = f"{side}_ankle_joint"
        if knee_nums[side] == 0:
            ankle_joint = create_joint(joint_name=ankle_joint_name, 
                                   parent_link=thigh_link_name, child_link=foot_link_name, 
                                #    xyz=(0, 0, -thigh_length-self_collision_joint_offset), 
                                   xyz=(0, 0, -thigh_length-self_collision_joint_offset), 
                                   axis=Y_AXIS,
                                   lower_limit=ankle_joint_limit_lower, upper_limit=ankle_joint_limit_upper,
                                   effort_limit=40, velocity_limit=9)
            robot.append(ankle_joint)
        else:
            ankle_joint = create_joint(joint_name=ankle_joint_name, 
                                    parent_link=lowest_calf_link_name, child_link=foot_link_name, 
                                    # xyz=(0, 0, -applied_calf_length-self_collision_joint_offset), 
                                    xyz=(0, 0, -applied_calf_length-self_collision_joint_offset), 
                                    axis=Y_AXIS,
                                    lower_limit=ankle_joint_limit_lower, upper_limit=ankle_joint_limit_upper,
                                    effort_limit=40, velocity_limit=9)
            robot.append(ankle_joint)

    # Generate and prettify URDF tree
    pretty_urdf = prettify_xml(robot)

    if os.path.exists(output_file):
        os.remove(output_file)
    with open(output_file, "w") as f:
        f.write(pretty_urdf)

    # print("Humanoid URDF file generated:", output_file)
    
    max_knee_num = max(knee_nums.values())
    drop_height = 1.2 * ( 
            # 2*head_radius + \
            # self_collision_joint_offset + \
            # torso_size[2] + \
            # self_collision_joint_offset + \
            pelvis_radius + \
            1.5*self_collision_joint_offset + \
            thigh_length + \
            self_collision_joint_offset + \
            max(max_knee_num, 1)*(applied_calf_length + self_collision_joint_offset) + \
            foot_size[2]
        ) 
    
    action_space = 19 + knee_nums['left']-1 + knee_nums['right']-1
    
    # nominal_joint_positions = {
    #         ".*": 0,
    # }
    
    if max_knee_num == 0:
        nominal_joint_positions = {
                ".*torso.*": 0,
                ".*_shoulder_pitch_joint": 0.0,
                ".*_shoulder_roll_joint": 0.0,
                ".*_shoulder_yaw_joint": 0.0,
                ".*elbow.*": 0,
                ".*_hip_yaw_joint": 0.0,
                ".*_hip_roll_joint": 0.0,
                ".*_hip_pitch_joint": 0.0,
                # ".*knee.*": 0,
                ".*ankle.*": 0
        }
    elif max_knee_num == 1:
        nominal_joint_positions = {
                ".*torso.*": 0,
                ".*_shoulder_pitch_joint": 0.0,
                ".*_shoulder_roll_joint": 0.0,
                ".*_shoulder_yaw_joint": 0.0,
                ".*elbow.*": 0,
                ".*_hip_yaw_joint": 0.0,
                ".*_hip_roll_joint": 0.0,
                ".*_hip_pitch_joint": -0.4,
                ".*knee.*": 0.8,
                ".*ankle.*": -0.4
        }
    else:
        nominal_joint_positions = {
                ".*torso.*": 0,
                ".*_shoulder_pitch_joint": 0.0,
                ".*_shoulder_roll_joint": 0.0,
                ".*_shoulder_yaw_joint": 0.0,
                ".*elbow.*": 0,
                ".*_hip_yaw_joint": 0.0,
                ".*_hip_roll_joint": 0.0,
                ".*_hip_pitch_joint": -0.4,
                ".*_knee_joint": 0.8,
                ".*_knee_.*_joint" : 0,
                ".*ankle.*": -0.4
        }
    
    if max_knee_num == 0:
        reward_cfgs = {
            'feet_ground_contact_cfg': ".*foot",
            'feet_ground_asset_cfg': ".*foot",
            'undesired_contact_cfg': [],
            'joint_hip_cfg': [".*hip.*joint", ".*elbow.*joint", ".*shoulder.*joint", ".*torso.*joint"],
            'joint_knee_cfg': [],
            # 'illegal_contact_cfg': [".*head.*", ".*torso.*", ".*arm.*", ".*calf.*"]
            'illegal_contact_cfg': None
            }
    else:
        reward_cfgs = {
            'feet_ground_contact_cfg': ".*foot",
            'feet_ground_asset_cfg': ".*foot",
            'undesired_contact_cfg': [".*calf.*"],
            'joint_hip_cfg': [".*hip.*joint", ".*elbow.*joint", ".*shoulder.*joint", ".*torso.*joint"],
            'joint_knee_cfg': [".*knee.*joint"],
            # 'illegal_contact_cfg': [".*head.*", ".*torso.*", ".*arm.*", ".*calf.*"]
            'illegal_contact_cfg': None
        }
        
    record_apply_joint_limit_scale_nums = {}
    # rename the keys in apply_knee_joint_limit_scale_nums and copy it to record_apply_joint_limit_scale_nums
    for key, value in apply_knee_joint_limit_scale_nums.items():
        # print(key, value)
        hip_yaw_joint_name = f"{key}_hip_yaw_joint"
        record_apply_joint_limit_scale_nums[hip_yaw_joint_name] = value
        hip_roll_joint_name = f"{key}_hip_roll_joint"
        record_apply_joint_limit_scale_nums[hip_roll_joint_name] = value
        hip_pitch_joint_name = f"{key}_hip_pitch_joint"
        record_apply_joint_limit_scale_nums[hip_pitch_joint_name] = value


    return_values = {
        'robot_name': robot_name,
        'drop_height': drop_height,
        'action_space': action_space,
        'apply_knee_joint_limit_scale_joint_names': record_apply_joint_limit_scale_nums,
        'apply_knee_joint_limit_scale_factor': true_apply_knee_joint_limit_scale_factor,
        'nominal_joint_positions': nominal_joint_positions,
        'reward_cfgs': reward_cfgs,
        # 'actuators': actuator_cfgs
    }
    # print("Return values:", return_values)
    
    return return_values 

# Function to generate URDF for a spider-like hexapod robot
def hexapod_generate_urdf(input_json_file, robot_name="gen_hexapod", output_file="gen_hexapod_spider.urdf"):
    '''
    nominal joint angles: 
    for each hip joint: 0.0
    for each thigh joint: 0.79 (45 degrees)
    for each calf joint: 0.79 (45 degrees)
    '''
    
    # Root URDF element
    robot = ET.Element('robot', name="gen_hexapod_spider")
    
    # Body dimensions
    with open(input_json_file, 'r') as file:
        parameters = json.load(file)
    
    knee_nums = parameters["knee_nums"]
    apply_knee_joint_limit_scale_nums = parameters["apply_knee_joint_limit_scale_nums"]
    apply_knee_joint_limit_scale_factor = parameters["apply_knee_joint_limit_scale_factor"]
    true_apply_knee_joint_limit_scale_factor = apply_knee_joint_limit_scale_factor
    if APPLY_SCALE_IN_URDF is False:
        apply_knee_joint_limit_scale_factor = 1.0
    
    body_length = parameters["body_size"]["length"]
    body_width = parameters["body_size"]["width"]
    body_height = parameters["body_size"]["height"]
    hip_link_radius = parameters["hip_link"]["radius"]
    foot_link_radius = parameters["foot_link"]["radius"]
    thigh_link_length = parameters["thigh_link"]["length"]
    thigh_link_radius = parameters["thigh_link"]["radius"]
    calf_link_length = parameters["calf_link"]["length"]
    calf_link_radius = parameters["calf_link"]["radius"]
    self_collision_joint_offset = parameters["self_collision_joint_offset"]
    
    # Joint Parameters
    joint_limit = 1.57
    knee_joint_limit_lower = -joint_limit
    knee_joint_limit_upper = joint_limit
    scaled_joint_limit_lower, scaled_joint_limit_upper = scale_range(knee_joint_limit_lower, knee_joint_limit_upper, apply_knee_joint_limit_scale_factor)
    final_applied_knee_joint_limit_upper = knee_joint_limit_upper
    
    
    # Link Parameters
    # Mass
    body_mass = 6.921
    hip_link_mass = 0.678
    calf_link_mass = 0.154
    foot_link_mass = 0.04
    
    # Inertia

    # Create the body
    body_link_name = "trunk"
    body_size = (body_length, body_width, body_height)
    body_link = create_link(link_name=body_link_name, geometry_type="box", box_dimensions=body_size, mass=body_mass, robot_name=robot_name)
    robot.append(body_link)

    # Define positions for six legs in a spider-like arrangement
    # Legs are placed around the body at 60-degree intervals

    # Angles for leg placement (in radians)
    leg_angles = [math.radians(angle) for angle in [30, 90, 150, 210, 270, 330]]  # Adjust angles for spider-like layout

    leg_positions = {}
    leg_names = ['leg_1', 'leg_2', 'leg_3', 'leg_4', 'leg_5', 'leg_6']

    for i, angle in enumerate(leg_angles):
        x = (max(body_length, body_width) + self_collision_joint_offset) / 2 * math.cos(angle)
        y = (max(body_length, body_width) + self_collision_joint_offset) / 2 * math.sin(angle)
        leg_positions[leg_names[i]] = (x, y, 0)

    # Create the six legs
    for leg, leg_position in leg_positions.items():
        '''
            For each link, the default origin is its center, the final origin is offset by link_xyz. 
            The link's origin will be mounted at the joint position whose child link is the current link.
        '''
        # Hip link
        hip_link_name = f"{leg}_hip"
        hip_link_type = "sphere"
        hip_link_dimensions = (hip_link_radius,)
        hip_link_xyz= (0, 0, 0)
        hip_link = create_link(link_name=hip_link_name, geometry_type=hip_link_type, xyz=hip_link_xyz ,
                               sphere_dimensions=hip_link_dimensions, mass=hip_link_mass, robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(hip_link)
        
        # Joints: hip -> thigh -> knee -> ankle
        # Hip joint connects the body to the hip link, position each at the corresponding corner
        # Adjust the joint orientation to point outward

        # Calculate the rotation angle for the leg
        leg_angle = math.atan2(leg_position[1], leg_position[0])
        # Hip joint connects the body to the hip link
        hip_joint_name = f"{leg}_hip_joint"
        hip_joint = create_joint(joint_name=hip_joint_name, 
                                 parent_link=body_link_name, child_link=hip_link_name, 
                                 xyz=leg_position, rpy=(0, 0, leg_angle), axis=Z_AXIS,
                                 lower_limit=-joint_limit, upper_limit=joint_limit)
        robot.append(hip_joint)
        
        # Thigh link
        thigh_link_name = f"{leg}_thigh"
        thigh_link_type = "cylinder"
        thigh_link_dimensions = (thigh_link_length, thigh_link_radius)
        thigh_link_xyz = (thigh_link_length/2, 0, 0)
        thigh_link_mass = 1.152
        thigh_link_rpy = (0, 1.54, 0)
        thigh_link = create_link(link_name=thigh_link_name, geometry_type=thigh_link_type, xyz=thigh_link_xyz, rpy=thigh_link_rpy, cylinder_dimensions=thigh_link_dimensions, mass=thigh_link_mass, robot_name=robot_name)
        robot.append(thigh_link)
        
        # Thigh joint connects the hip to the thigh
        thigh_joint_name = f"{leg}_thigh_joint"
        thigh_joint_xyz = (0, 0, 0)
        thigh_joint = create_joint(joint_name=thigh_joint_name, 
                                   parent_link=hip_link_name, child_link=thigh_link_name, 
                                   xyz=thigh_joint_xyz, rpy=(0, 0, 0), axis=Y_AXIS,
                                   lower_limit=-joint_limit, upper_limit=joint_limit)
        robot.append(thigh_joint)

        # Calf link
        calf_link_name = f"{leg}_calf"
        calf_link_type = "cylinder"
        calf_link_dimensions = (calf_link_length, calf_link_radius)
        calf_link_xyz = (calf_link_length/2, 0, 0)
        calf_link_rpy = (0, 1.54, 0)
        calf_link = create_link(link_name=calf_link_name, geometry_type=calf_link_type, xyz=calf_link_xyz, rpy=calf_link_rpy, 
                                cylinder_dimensions=calf_link_dimensions, mass=calf_link_mass, robot_name=robot_name, color=HIGHLIGHT_COLOR)
        if knee_nums[leg] != 0:
            robot.append(calf_link)
        
        # Knee joint connects the thigh to the calf
        apply_knee_joint_limit_scale_num = apply_knee_joint_limit_scale_nums[leg]
        
        knee_joint_name = f"{leg}_knee_joint"
        if knee_nums[leg] == 0:
            knee_joint_type = None
        else:
            knee_joint_type = "revolute"
        knee_joint_xyz = (thigh_link_length, 0, 0)
        
        if apply_knee_joint_limit_scale_num == 0:
            applied_knee_joint_limit_lower = knee_joint_limit_lower
            applied_knee_joint_limit_upper = knee_joint_limit_upper
        else:
            applied_knee_joint_limit_lower = scaled_joint_limit_lower
            applied_knee_joint_limit_upper = scaled_joint_limit_upper
        
        if applied_knee_joint_limit_upper < final_applied_knee_joint_limit_upper:
            final_applied_knee_joint_limit_upper = applied_knee_joint_limit_upper
        
        knee_joint = create_joint(joint_name=knee_joint_name, 
                                  parent_link=thigh_link_name, child_link=calf_link_name,
                                  joint_type=knee_joint_type, 
                                  xyz=knee_joint_xyz, rpy=(0, 0, 0), axis=Y_AXIS,
                                  lower_limit=applied_knee_joint_limit_lower, upper_limit=applied_knee_joint_limit_upper)
        if knee_nums[leg] != 0:
            robot.append(knee_joint)
        
        lowest_calf_link_name = calf_link_name
        if knee_nums[leg] > 1:
            
            count_apply_knee_joint_limit_scale = apply_knee_joint_limit_scale_num
            assert count_apply_knee_joint_limit_scale < knee_nums[leg], "Invalid apply_knee_joint_limit_scale_num"
            
            for i in range(knee_nums[leg]-1):
                additional_calf_link_name = f"{leg}_calf_{i+1}"
                additional_calf_link = create_link(link_name=additional_calf_link_name, 
                                                   geometry_type="cylinder", 
                                                   xyz=(calf_link_length/2, 0, 0),
                                                   rpy=(0, 1.54, 0), 
                                                   cylinder_dimensions=(calf_link_length, calf_link_radius), 
                                                   mass=calf_link_mass, robot_name=robot_name)
                robot.append(additional_calf_link)
                
                # Knee joint connects the thigh to the calf
                additional_knee_joint_name = f"{leg}_knee_{i+1}_joint"
                
                if (count_apply_knee_joint_limit_scale -1) <= 0:
                    applied_additional_knee_joint_limit_lower = knee_joint_limit_lower
                    applied_additional_knee_joint_limit_upper = knee_joint_limit_upper
                else:
                    applied_additional_knee_joint_limit_lower = scaled_joint_limit_lower
                    applied_additional_knee_joint_limit_upper = scaled_joint_limit_upper
                    
                    count_apply_knee_joint_limit_scale -= 1
                
                
                additional_knee_joint = create_joint(joint_name=additional_knee_joint_name,
                                                    parent_link=lowest_calf_link_name,
                                                    child_link=additional_calf_link_name,
                                                    joint_type="revolute",
                                                    xyz=(calf_link_length, 0, 0),
                                                    rpy=(0, 0, 0), axis=Y_AXIS,
                                                    lower_limit=applied_additional_knee_joint_limit_lower, 
                                                    upper_limit=applied_additional_knee_joint_limit_upper)
                robot.append(additional_knee_joint)
                
                lowest_calf_link_name = additional_calf_link_name
        
        # Foot link
        foot_link_name = f"{leg}_foot"
        foot_link_type = "sphere"
        foot_link_dimensions = (foot_link_radius,)
        foot_link = create_link(link_name=foot_link_name, geometry_type=foot_link_type, 
                                sphere_dimensions=foot_link_dimensions, mass=foot_link_mass, robot_name=robot_name, color=HIGHLIGHT_COLOR)
        robot.append(foot_link)

        # Ankle joint connects the calf to the foot
        ankle_joint_name = f"{leg}_ankle_joint"
        if knee_nums[leg] == 0:
            ankle_joint_xyz = (thigh_link_length, 0, 0)
        else:
            ankle_joint_xyz = (calf_link_length, 0, 0)
        if knee_nums[leg] == 0:
            ankle_joint = create_joint(joint_name=ankle_joint_name, parent_link=thigh_link_name, 
                                    child_link=foot_link_name, joint_type="fixed", xyz=ankle_joint_xyz)
            robot.append(ankle_joint)
        else:
            ankle_joint = create_joint(joint_name=ankle_joint_name, parent_link=lowest_calf_link_name, 
                                    child_link=foot_link_name, joint_type="fixed", xyz=ankle_joint_xyz)
            robot.append(ankle_joint)
    # Generate and prettify URDF tree
    pretty_urdf = prettify_xml(robot)

    if os.path.exists(output_file):
        os.remove(output_file)
    with open(output_file, "w") as f:
        f.write(pretty_urdf)

    # print("URDF file generated:", output_file)
    
    max_knee_num = max(knee_nums.values())
    drop_height = 1.2 * (
        0.5 * body_height + \
        thigh_link_length + \
        max(max_knee_num, 1)*calf_link_length + \
        2* foot_link_radius
    )
    
    action_space = 18 + knee_nums['leg_1']-1 + knee_nums['leg_2']-1 + knee_nums['leg_3']-1 + knee_nums['leg_4']-1 + knee_nums['leg_5']-1 + knee_nums['leg_6']-1
    
    if max_knee_num == 0:
        if scaled_joint_limit_upper >= 0.79:
            nominal_joint_positions = {
                    ".*_hip_joint": 0,
                    ".*_thigh_joint": 0.79,
                    # ".*_knee_joint": 0.79,
                    # ".*_knee_.*_joint" : 0
            }
        else:
            nominal_joint_positions = {
                    ".*_hip_joint": 0,
                    ".*_thigh_joint": 0.79,
                    # ".*_knee_joint": scaled_joint_limit_upper,
                    # ".*_knee_.*_joint" : 0
            }
    elif max_knee_num == 1:
        if scaled_joint_limit_upper >= 0.79:
            nominal_joint_positions = {
                    ".*_hip_joint": 0,
                    ".*_thigh_joint": 0.79,
                    ".*_knee_joint": 0.79,
                    # ".*_knee_.*_joint" : 0
            }
        else:
            nominal_joint_positions = {
                    ".*_hip_joint": 0,
                    ".*_thigh_joint": 0.79,
                    ".*_knee_joint": scaled_joint_limit_upper,
                    # ".*_knee_.*_joint" : 0
            }
    else:
        if scaled_joint_limit_upper >= 0.79:
            nominal_joint_positions = {
                    ".*_hip_joint": 0,
                    ".*_thigh_joint": 0.79,
                    ".*_knee_joint": 0.79,
                    ".*_knee_.*_joint" : 0
            }
        else:
            nominal_joint_positions = {
                    ".*_hip_joint": 0,
                    ".*_thigh_joint": 0.79,
                    ".*_knee_joint": scaled_joint_limit_upper,
                    ".*_knee_.*_joint" : 0
            }
    
    if max_knee_num == 0:
        reward_cfgs = {
            'feet_ground_contact_cfg': ".*foot",
            'feet_ground_asset_cfg': ".*foot",
            'undesired_contact_cfg': [".*thigh.*", ".*trunk.*"],
            'joint_hip_cfg': [".*hip.*joint"],
            'joint_knee_cfg': [],
            'illegal_contact_cfg': [".*trunk.*", ".*hip.*",".*thigh.*"]
            }
    else:
        reward_cfgs = {
            'feet_ground_contact_cfg': ".*foot",
            'feet_ground_asset_cfg': ".*foot",
            'undesired_contact_cfg': [".*calf.*", ".*thigh.*", ".*trunk.*"],
            'joint_hip_cfg': [".*hip.*joint"],
            'joint_knee_cfg': [".*knee.*joint"],
            'illegal_contact_cfg': [".*trunk.*", ".*hip.*",".*thigh.*", ".*calf.*"]
        }
    
    actuator_cfgs = {
        "base_legs": {
            "motor_type": "DCMotor",
            "joint_names_expr": [".*joint"],
            "effort_limit": 23.5,
            "saturation_effort": 23.5,
            "velocity_limit": 30.0,
            "stiffness": 25.0,
            "damping": 0.5,
            "friction": 0.0
        }
    }
    
    record_apply_joint_limit_scale_nums = {}
    # rename the keys in apply_knee_joint_limit_scale_nums and copy it to record_apply_joint_limit_scale_nums
    for key, value in apply_knee_joint_limit_scale_nums.items():
        # print(key, value)
        hip_joint_name = f"{key}_hip_joint"
        record_apply_joint_limit_scale_nums[hip_joint_name] = value
        thigh_joint_name = f"{key}_thigh_joint"
        record_apply_joint_limit_scale_nums[thigh_joint_name] = value
    
    return_values = {
        'robot_name': robot_name,
        'drop_height': drop_height,
        'action_space': action_space,
        'apply_knee_joint_limit_scale_joint_names': record_apply_joint_limit_scale_nums,
        'apply_knee_joint_limit_scale_factor': true_apply_knee_joint_limit_scale_factor,
        'nominal_joint_positions': nominal_joint_positions,
        'reward_cfgs': reward_cfgs,
        'actuators': actuator_cfgs
    }

    # print("Return values:", return_values)
    
    return return_values