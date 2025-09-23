import argparse
import os

import tqdm
from omni.isaac.lab.sim.converters import UrdfConverter, UrdfConverterCfg
from omni.isaac.lab.utils.assets import check_file_path
from omni.isaac.lab.app import AppLauncher


def convert_urdf_to_usd(urdf_path, dest_dir, merge_joints=False, fix_base=False, make_instanceable=False):
    # Prepare output directory and file path
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, os.path.basename(urdf_path).replace(".urdf", ".usd"))

    # Configure URDF to USD conversion
    urdf_converter_cfg = UrdfConverterCfg(
        asset_path=urdf_path,
        usd_dir=dest_dir,
        usd_file_name=os.path.basename(dest_path),
        fix_base=fix_base,
        merge_fixed_joints=merge_joints,
        force_usd_conversion=True,
        make_instanceable=make_instanceable,
    )

    # Perform the conversion
    print(f"Converting {urdf_path} to {dest_path}...")
    urdf_converter = UrdfConverter(urdf_converter_cfg)
    print(f"Conversion complete: {urdf_converter.usd_path}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Batch convert URDF files in a folder to USD format.")
    parser.add_argument("source_folder", type=str, help="Path to the folder containing URDF files.")
    parser.add_argument("target_folder", type=str, help="Path to save the converted USD files.")
    parser.add_argument("--merge-joints", action="store_true", default=False, help="Merge links connected by fixed joints.")
    parser.add_argument("--make-instanceable", action="store_true", default=True, help="Make the model instanceable.")
    args = parser.parse_args()

    # Verify source folder
    if not os.path.isdir(args.source_folder):
        raise ValueError(f"Source folder does not exist: {args.source_folder}")

    # Launch simulator in headless mode
    app_launcher = AppLauncher()
    simulation_app = app_launcher.app

    # Process each URDF file in the source folder
    for filename in tqdm.tqdm(os.listdir(args.source_folder)):
        if filename.endswith(".urdf"):
            urdf_path = os.path.join(args.source_folder, filename)
            target_subfolder = os.path.join(args.target_folder, os.path.splitext(filename)[0])

            # Check if URDF file is valid
            if check_file_path(urdf_path):
                convert_urdf_to_usd(
                    urdf_path,
                    target_subfolder,
                    merge_joints=args.merge_joints,
                    fix_base=args.fix_base,
                    make_instanceable=args.make_instanceable
                )
            else:
                print(f"Skipping invalid URDF file: {urdf_path}")

    # Close the simulator
    simulation_app.close()
    print("Batch conversion complete.")

if __name__ == "__main__":
    main()
