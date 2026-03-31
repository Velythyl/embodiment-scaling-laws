#!/bin/bash
# Usage: ./remove_robot_from_configs.sh RobotName1 RobotName2 ...
# Example: ./remove_robot_from_configs.sh Genhumanoid102 Genhumanoid166

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONF_DIR="$SCRIPT_DIR/conf"

if [ $# -eq 0 ]; then
    echo "Usage: $0 <robot_name> [robot_name2] ..."
    echo "Example: $0 Genhumanoid102 Genhumanoid166"
    exit 1
fi

for robot in "$@"; do
    echo "Removing references to $robot from yaml configs..."
    grep -l "$robot" "$CONF_DIR"/*.yaml 2>/dev/null | xargs -I{} sed -i "s/ ${robot}[^ ]*//g" {}
    
    # Verify removal
    count=$(grep -c "$robot" "$CONF_DIR"/*.yaml 2>/dev/null | grep -v ':0$' | wc -l)
    if [ "$count" -eq 0 ]; then
        echo "  Done: $robot removed from all configs"
    else
        echo "  Warning: $robot still found in some configs"
        grep -l "$robot" "$CONF_DIR"/*.yaml 2>/dev/null
    fi
done

# ./scripts/distillation/remove_robot_from_configs.sh Genhumanoid102 Genhumanoid166