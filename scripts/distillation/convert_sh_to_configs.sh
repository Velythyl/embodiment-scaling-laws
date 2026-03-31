#!/bin/bash
# Convert all .sh files in urma_distillation/*/* to hydra config files

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
URMA_DIR="$SCRIPT_DIR/urma_distillation"
CONF_DIR="$SCRIPT_DIR/conf"

# Find all .sh files
find "$URMA_DIR" -name "*.sh" | while read -r sh_file; do
    # Get directory name and script name
    dir_name=$(basename "$(dirname "$sh_file")")
    script_name=$(basename "$sh_file" .sh)
    
    # Config name: dirname_scriptname.yaml
    config_name="${dir_name}_${script_name}.yaml"
    config_path="$CONF_DIR/$config_name"
    
    # Extract everything after 'run_distillation.py '
    args=$(grep -oP '(?<=run_distillation\.py ).*' "$sh_file" | head -1)
    
    # If no match, try a simpler extraction (everything after .py)
    if [[ -z "$args" ]]; then
        args=$(sed -n 's/.*\.py \(.*\)/\1/p' "$sh_file" | head -1)
    fi
    
    # Add --dataset_dir if not present
    if [[ ! "$args" =~ --dataset_dir ]]; then
        args="$args --dataset_dir /tmp/embodiment-scaling-laws/logs/rsl_rl"
    else
        # Replace existing dataset_dir value
        args=$(echo "$args" | sed 's|--dataset_dir [^ ]*|--dataset_dir /tmp/embodiment-scaling-laws/logs/rsl_rl|')
    fi
    
    # Escape double quotes in args for YAML (they need to be escaped)
    args_escaped=$(echo "$args" | sed 's/"/\\"/g')
    
    # Create the config file
    cat > "$config_path" << EOF
# Hydra configuration generated from $sh_file
# Use with: python run_distillation.py --config-name=$(basename "$config_name" .yaml)

defaults:
  - _self_

# Argparse arguments as a string (parsed with shlex.split)
argparse: "$args_escaped"
EOF
    
    echo "Created: $config_path"
done

echo "Done! Created configs in $CONF_DIR"
