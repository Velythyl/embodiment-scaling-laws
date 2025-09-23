import argparse

def extract_indices(robot_names, indices):
    # Extract indices from the robot_names argument
    robot_names_indices = []
    for item in robot_names.split():
        if "Genhumanoid" in item:
            parts = item.split("_")
            for part in parts:
                if part.startswith("Genhumanoid"):
                    index = part[len("Genhumanoid"):]
                    if index.isdigit():
                        robot_names_indices.append(int(index))

    # Extract indices from the indices argument
    indices_list = sorted([int(x.split(',')[0]) for x in indices])

    return sorted(robot_names_indices), indices_list

def format_bash_array(indices):
    """Format the indices into a Bash-compatible array string with the 'Genhumanoid' prefix."""
    formatted = " ".join(f"\"Genhumanoid{i}\"" for i in indices)
    return f"tasks=({formatted})"

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Extract and compare indices from robot names and indices.")
    parser.add_argument("--robot_names", type=str, required=True, nargs='+', help="String containing robot names with indices separated by spaces.")
    parser.add_argument("--indices", type=str, nargs='+', required=True, help="Comma and space-separated list of indices.")
    args = parser.parse_args()

    # Join robot names into a single string
    robot_names = " ".join(args.robot_names)

    # Extract and sort indices
    robot_names_indices, indices_list = extract_indices(robot_names, args.indices)

    # Find missing indices
    missing_in_indices = [x for x in robot_names_indices if x not in indices_list]
    missing_in_robot_names = [x for x in indices_list if x not in robot_names_indices]

    # Print results
    print("Sorted indices from robot_names:", robot_names_indices)
    # print("Sorted Gendog names from robot_names:", str([f"Gendog{i}" for i in robot_names_indices]))
    print("Sorted indices from indices (Ground Truth):", indices_list)
    print("Indices in robot_names but missing from indices:", missing_in_indices)
    print("Indices in indices but missing from robot_names:", missing_in_robot_names)

    # Print Bash-formatted array using ground truth indices
    print("\nGround Truth Bash-formatted array:")
    print(format_bash_array(indices_list))

if __name__ == "__main__":
    main()
