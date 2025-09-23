#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: sh urdf_to_usd_batch.sh source_folder target_folder"
    exit 1
fi

# Assign source and target folder paths
source_folder=$1
target_folder=$2

# Create the target folder if it does not exist
mkdir -p "$target_folder"

# Loop through each .urdf file in the source folder
for source_file in "$source_folder"/*.urdf; do
    # Check if there are any .urdf files
    if [ ! -e "$source_file" ]; then
        echo "No .urdf files found in $source_folder."
        exit 1
    fi

    # Extract the filename without the extension
    filename=$(basename "$source_file" .urdf)

    # Create a directory for each target file in the target folder
    target_dir="$target_folder/$filename"
    mkdir -p "$target_dir"

    # Define the target file path within the newly created directory
    target_file="$target_dir/robot.usd"

    # Execute the conversion command
    ${ISAAC_LAB_PATH}/isaaclab.sh -p ${ISAAC_LAB_PATH}/source/standalone/tools/convert_urdf.py \
        "$source_file" \
        "$target_file" \
        --make-instanceable \
        --no-display
done

echo "Batch conversion complete."
