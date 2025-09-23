import os
from datetime import datetime
from tqdm import tqdm
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
import matplotlib.pyplot as plt

def read_tensorboard_scalars(log_folder, topics=None):
    """
    Reads scalar time series from a TensorBoard event file in the given folder.
    Returns a dictionary where the key is the scalar name and the value is a list of values.

    Parameters:
    - log_folder: Path to the folder containing the TensorBoard event file.
    - topics: Optional. A list of scalar tags (topics) to filter. If None, all topics are returned.

    Returns:
    - A dictionary where the key is the scalar tag and the value is a list of scalar values.
    """
    event_file = [f for f in os.listdir(log_folder) if f.startswith("events.out.tfevents")]
    if not event_file:
        return None  # No event file found
    event_file_path = os.path.join(log_folder, event_file[0])
    event_acc = EventAccumulator(event_file_path)
    event_acc.Reload()

    scalars = {}
    all_tags = event_acc.Tags().get("scalars", [])
    tags_to_read = topics if topics else all_tags  # If topics are specified, filter by them; otherwise, use all tags

    for tag in tags_to_read:
        if tag in all_tags:  # Only process tags that exist in the log file
            scalar_events = event_acc.Scalars(tag)
            scalars[tag] = [event.value for event in scalar_events]  # Collect only the values

    return scalars

def parse_datetime(folder_name):
    """
    Parses a folder name in the format 'YYYY-MM-DD_HH-MM-SS' and returns a datetime object.
    Returns None if the parsing fails.
    """
    try:
        return datetime.strptime(folder_name, "%Y-%m-%d_%H-%M-%S")
    except ValueError:
        return None

def process_training_results(base_folder, step_index, keyword='Gendog'):
    """
    Given a base folder, find the latest date-time subfolder for each "Gendogx" folder,
    read the TensorBoard logs, and return a mapping from "Gendogx" to their scalar dictionaries.
    """
    results = {}
    folders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f)) and f.startswith(keyword)]

    # Progress bar
    with tqdm(total=len(folders), desc=f"Processing {keyword} folders", unit="folder") as pbar:
        for folder in folders:
            folder_path = os.path.join(base_folder, folder)

            # Find the latest date-time subfolder
            subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
            dated_subfolders = [(subfolder, parse_datetime(subfolder[:19])) for subfolder in subfolders]
            dated_subfolders = [(name, dt) for name, dt in dated_subfolders if dt is not None]

            if not dated_subfolders:
                pbar.update(1)
                continue

            # Sort subfolders by datetime and take the latest
            latest_subfolder = max(dated_subfolders, key=lambda x: x[1])[0]
            latest_path = os.path.join(folder_path, latest_subfolder)

            # Read TensorBoard scalars
            scalars = read_tensorboard_scalars(latest_path, topics=["Train/mean_return", "Train/mean_episode_length"])
            if scalars is not None and "Train/mean_return" in scalars and len(scalars["Train/mean_return"]) > step_index:
                results[folder] = scalars

            pbar.update(1)

    return results

def plot_finished_trainings(results, step_index, save_path=None):
    """
    Plots a histogram of the specified step index 'Train/mean_return' for all completed trainings.
    Optionally saves the plot to a specified path.

    Args:
        results (dict): Dictionary containing training results.
        step_index (int): Step index to plot.
        save_path (str, optional): Path to save the figure. If None, the figure is not saved.
    """
    finished_returns = []
    max_mean_return = -float("inf")
    min_mean_return = float("inf")
    
    for folder, scalars in results.items():
        if "Train/mean_return" in scalars and len(scalars["Train/mean_return"]) > step_index:
            finished_returns.append(scalars["Train/mean_return"][step_index])
            
            if scalars["Train/mean_return"][step_index] > max_mean_return:
                max_mean_return = scalars["Train/mean_return"][step_index]
            if scalars["Train/mean_return"][step_index] < min_mean_return:
                min_mean_return = scalars["Train/mean_return"][step_index]

    print(f"Total trainings completed: {len(finished_returns)}")
    print(f"Max mean return: {max_mean_return}")
    print(f"Min mean return: {min_mean_return}")
    if finished_returns:
        plt.hist(finished_returns, bins=10, edgecolor='black')
        plt.title(f"Histogram of 'Train/mean_return' (Step {step_index})")
        plt.xlabel("Mean Return")
        plt.ylabel("Frequency")

        if save_path:
            plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')
            print(f"Figure saved to {save_path}")

        plt.show()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Plot training results from TensorBoard logs.")
    parser.add_argument("--log_path", type=str, default="../logs/rsl_rl", help="Path to the RSL RL logs.")
    parser.add_argument("--step_index", type=int, required=True, help="Step index to plot.")
    parser.add_argument("--save_path", type=str, default="reward_his.jpg", help="Path to save the histogram.")
    parser.add_argument("--keyword", type=str, default="Gendog")

    args = parser.parse_args()

    results = process_training_results(args.log_path, args.step_index, args.keyword)
    
    # sort rewards and write them to rewards.txt
    sorted_rewards = []
    for folder, scalars in results.items():
        if "Train/mean_return" in scalars and len(scalars["Train/mean_return"]) > args.step_index:
            reward_val = scalars["Train/mean_return"][args.step_index]
            sorted_rewards.append((folder, reward_val))

    sorted_rewards.sort(key=lambda x: x[1])

    with open(args.save_path+".txt", "w", encoding="utf-8") as f:
        for folder, reward_val in sorted_rewards:
            f.write(f"{folder}\t{reward_val}\n")
    print("rewards.txt done")
    
    plot_finished_trainings(results, args.step_index, args.save_path)

