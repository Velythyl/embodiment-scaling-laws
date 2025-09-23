import os
import re

def check_record_status(logs_path):
    completed_records = set()
    missing_h5_record = set()
    incomplete_records = set()

    # Traverse all sub-folders in logs/rsl_rl
    for subdir in os.listdir(logs_path):
        subdir_path = os.path.join(logs_path, subdir)
        if os.path.isdir(subdir_path):
            # Match prefix name
            match = re.match(r"(Genhumanoid\d+)_", subdir)
            if match:
                prefix_name = match.group(1)
                # Get all timestamp sub-folders
                time_subdirs = [
                    d for d in os.listdir(subdir_path)
                    if os.path.isdir(os.path.join(subdir_path, d))
                ]
                if time_subdirs:
                    # Sort to find the latest folder
                    latest_subdir = sorted(time_subdirs)[-1]
                    latest_subdir_path = os.path.join(subdir_path, latest_subdir)
                    h5py_record_path = os.path.join(latest_subdir_path, "h5py_record")
                    if os.path.exists(h5py_record_path):
                        obs_file = os.path.join(h5py_record_path, "obs_actions_00009.h5")
                        if os.path.exists(obs_file):
                            completed_records.add(prefix_name)
                        else:
                            incomplete_records.add(prefix_name)
                    else:
                        missing_h5_record.add(prefix_name)

    # Sort based on the results
    def sort_by_number(prefix_list):
        return sorted(prefix_list, key=lambda x: int(re.search(r"\d+", x).group()))

    return {
        "Completed Records": sort_by_number(list(completed_records)),
        "Missing h5py_record": sort_by_number(list(missing_h5_record)),
        "Incomplete Records": sort_by_number(list(incomplete_records))
    }


# Example
logs_path = "./logs/rsl_rl"  # Modify to the actual directory
record_status = check_record_status(logs_path)

# Output the results
print("Completed Records:")
print(record_status["Completed Records"])
print("len:", len(record_status["Completed Records"]))

print("\nFailed Records:")
print(record_status["Missing h5py_record"])
print("\nIncomplete Records:")
print(record_status["Incomplete Records"])
