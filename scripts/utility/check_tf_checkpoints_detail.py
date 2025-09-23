import os
import re
from argparse import ArgumentParser


def extract_index(folder_name, keyword):
    """Extract the numeric index from a folder name using the given keyword."""
    pattern = rf"{keyword}(\d+)"
    match = re.match(pattern, folder_name)
    return int(match.group(1)) if match else None


def analyze_latest_pt(root_dir, keyword):
    """
    For each robot (folder matching the keyword) in the root directory,
    find the checkpoint (.pt) file with the largest epoch index (across all subfolders).
    Build and return a dictionary where the key is the largest epoch (int)
    and the value is a list of robot folder names that reached that epoch.
    """
    result = {}
    # Find all folders in the root directory that match the naming pattern
    folders = [f for f in os.listdir(root_dir)
               if os.path.isdir(os.path.join(root_dir, f)) and extract_index(f, keyword) is not None]
    
    for folder in folders:
        gen_name = keyword + str(extract_index(folder, keyword))
        folder_path = os.path.join(root_dir, folder)
        max_epoch = None
        
        # Iterate over all subfolders within this robot folder
        subfolders = [d for d in os.listdir(folder_path)
                      if os.path.isdir(os.path.join(folder_path, d))]
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            pt_files = [f for f in os.listdir(subfolder_path) if f.endswith(".pt")]
            
            for pt in pt_files:
                try:
                    # Assuming filename format: <prefix>_<epoch>.pt, e.g., "checkpoint_3000.pt"
                    epoch = int(pt.split("_")[1].split(".")[0])
                except (IndexError, ValueError):
                    # Skip files that don't follow the expected naming scheme
                    continue
                
                if max_epoch is None or epoch > max_epoch:
                    max_epoch = epoch
        
        # If a valid .pt file was found, update the result dictionary
        if max_epoch is not None:
            result.setdefault(max_epoch, []).append(gen_name)
                
    return result


def add_missing_entries(pt_dict, keyword, max_index):
    """
    Add an entry to the dictionary with the key "missing" that contains a list of robot
    names (from keyword0 to keyword(max_index-1)) which are not found in the given pt_dict.
    """
    # Get all found robot names from the dictionary values
    found_robots = {robot for robots in pt_dict.values() for robot in robots if isinstance(robots, list)}
    # Create expected robot names based on provided max_index
    expected_robots = {f"{keyword}{i}" for i in range(max_index)}
    # Determine the missing robots
    missing = sorted(list(expected_robots - found_robots), key=lambda x: int(re.search(r'\d+', x).group()))
    # Add missing entry into the dictionary
    pt_dict["missing"] = missing
    return pt_dict


if __name__ == "__main__":
    # Parse command-line arguments
    parser = ArgumentParser(
        description="Determine the highest checkpoint epoch reached for each robot folder and group them."
    )
    parser.add_argument("--root", type=str, required=True,
                        help="Root directory containing the robot log folders.")
    parser.add_argument("--keyword", type=str, default="Gendog",
                        help="Keyword used in naming robot folders (e.g., 'Gendog').")
    parser.add_argument("--max-index", type=int, required=True,
                        help="The maximum index (exclusive) for expected robot folders. "
                             "Robot folders are assumed to be named as keyword+number (e.g., 'Gendog0').")
    args = parser.parse_args()

    # Analyze the logs based on the modified logic
    pt_dict = analyze_latest_pt(args.root, args.keyword)
    # Sort the dictionary by epoch keys (exclude the eventual "missing" key if present)
    pt_dict = {key: pt_dict[key] for key in sorted(pt_dict) if isinstance(key, int)}
    
    # Add missing robot entries based on the provided max-index
    pt_dict = add_missing_entries(pt_dict, args.keyword, args.max_index)
    
    # Print the resulting dictionary
    print("Dictionary of maximum checkpoint epochs to robot folders (including missing):\n")
    for key, value in pt_dict.items():
        print(f"{key}: len:{len(value)} value:{sorted(value)}\n")
