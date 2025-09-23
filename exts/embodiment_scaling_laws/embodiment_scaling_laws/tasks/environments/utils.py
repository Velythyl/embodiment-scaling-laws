import yaml
from types import SimpleNamespace
import numpy as np
import re
import torch


# Function to convert dict to SimpleNamespace recursively
def dict_to_namespace(config_dict):
    if isinstance(config_dict, dict):
        return SimpleNamespace(**{key: dict_to_namespace(value) for key, value in config_dict.items()})
    elif isinstance(config_dict, list):
        return [dict_to_namespace(item) for item in config_dict]
    return config_dict

# Regular expression to match scientific notation
scientific_notation_pattern = re.compile(r"^-?\d+(\.\d+)?[eE][-+]?\d+$")

# Function to ensure only float-like values (including scientific notation) are converted to floats, preserving integers
def enforce_float_conversion(config_dict):
    if isinstance(config_dict, dict):
        return {key: enforce_float_conversion(value) for key, value in config_dict.items()}
    elif isinstance(config_dict, list):
        return [enforce_float_conversion(item) for item in config_dict]
    else:
        # If it's already an int, return as-is
        if isinstance(config_dict, int):
            return config_dict
        # If it's already a float, return as-is
        elif isinstance(config_dict, float):
            return config_dict
        # If it's a string that represents scientific notation, convert to float
        elif isinstance(config_dict, str) and scientific_notation_pattern.match(config_dict):
            return float(config_dict)
        # Return as-is for other types
        else:
            return config_dict

# Load YAML file and enforce the correct conversion
def load_config(file_path):
    with open(file_path, 'r') as file:
        config_dict = yaml.safe_load(file)
    # Ensure float-like numbers (including scientific notation in strings) are floats, but preserve integers
    config_dict = enforce_float_conversion(config_dict)
    return dict_to_namespace(config_dict)

def quat_to_matrix(quat):
    """
    Convert a quaternion to a 3x3 rotation matrix.
    Args:
        quat (torch.tensor): Quaternion (w, x, y, z) with shape (N, 4).
    Returns:
        torch.tensor: Rotation matrix with shape (N, 3, 3).
    """
    w, x, y, z = quat[:, 0], quat[:, 1], quat[:, 2], quat[:, 3]

    # Compute the rotation matrix elements
    tx, ty, tz = 2.0 * x, 2.0 * y, 2.0 * z
    twx, twy, twz = tx * w, ty * w, tz * w
    txx, txy, txz = tx * x, tx * y, tx * z
    tyy, tyz, tzz = ty * y, ty * z, tz * z

    rotation_matrix = torch.stack([
        1.0 - (tyy + tzz), txy - twz, txz + twy,
        txy + twz, 1.0 - (txx + tzz), tyz - twx,
        txz - twy, tyz + twx, 1.0 - (txx + tyy)
    ], dim=-1).view(-1, 3, 3)

    return rotation_matrix

# # Example of loading the config
# config = load_config("/home/research/github/embodiment-scaling-law/training/environments/robots/unitree_go1/config.yaml")
# import ipdb; ipdb.set_trace()
