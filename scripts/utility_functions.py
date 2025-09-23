import os
from datetime import datetime
import yaml
import torch
import re


class AverageMeter:
    """
    Computes and stores the average and current value of a metric.
    """
    def __init__(self):
        self.reset()

    def reset(self):
        """Resets all the statistics."""
        self.val = 0          # Current value
        self.avg = 0          # Average value
        self.sum = 0          # Sum of all values
        self.count = 0        # Number of updates

    def update(self, val, n=1):
        """
        Updates the meter with a new value.

        Args:
            val (float): The new value to add.
            n (int): The weight of this value (e.g., batch size).
        """
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count if self.count != 0 else 0

    def __str__(self):
        """String representation of the average and current value."""
        return f"Val: {self.val:.4f}, Avg: {self.avg:.4f}"


class RewardDictLogger:
    def __init__(self, num_envs):
        """
        Initializes the RewardDictLogger to track reward statistics.

        Args:
            num_envs (int): Number of parallel environments (N).
        """
        self.reward_avg_meter_dict = {}
        self.cumulative_rewards = torch.zeros(num_envs).cuda()  # Track total rewards for each robot
        self.full_trajectory_rewards = []  # Log summed rewards for completed robot trajectories
        self.full_trajectory_term_rewards = {}  # Per-term rewards for completed robots
        self.num_envs = num_envs

    def update(self, env, rewards, dones, seen_dones=None):
        """
        Updates reward statistics and cumulative rewards.

        Args:
            env: Environment object providing reward terms.
            rewards (torch.Tensor): Reward tensor (N,).
            dones (torch.Tensor): Done flags (N,) indicating robot termination.
            seen_dones (torch.Tensor, optional): Seen done flags (N,) indicating robot termination prior to this step.
        """
        reward_dict = env.unwrapped.extras["log"]  # Access reward terms

        for key, values in reward_dict.items():
            if key not in self.reward_avg_meter_dict:
                self.reward_avg_meter_dict[key] = AverageMeter()

            if seen_dones is not None:
                values = values * (1 - seen_dones.float())
                nr_not_terminated = torch.sum(1 - seen_dones.float())
                if nr_not_terminated == 0:
                    return
                else:
                    mean_reward = values.sum().item() / nr_not_terminated.item()
            else:
                mean_reward = values.mean().item()
            self.reward_avg_meter_dict[key].update(mean_reward)

            # Convert to float tensor if required
            values = values.detach() if values.requires_grad else values

            # Initialize per-term rewards tensor if not already
            if key not in self.full_trajectory_term_rewards:
                self.full_trajectory_term_rewards[key] = torch.zeros_like(rewards)

            # Accumulate rewards for current step
            self.full_trajectory_term_rewards[key] += values

        # Update cumulative rewards and handle robot termination
        self.cumulative_rewards += rewards
        for i in range(len(dones)):
            if dones[i] == 1:  # Robot dies
                # Log total reward for the robot
                self.full_trajectory_rewards.append(self.cumulative_rewards[i].item())
                self.cumulative_rewards[i] = 0.0  # Reset

                # Log per-term rewards
                for key in self.full_trajectory_term_rewards:
                    self.full_trajectory_term_rewards[key][i] = 0.0  # Reset per-term reward

    def print(self, curr_timestep, mode="sum"):
        """
        Prints reward statistics based on the mode.

        Args:
            curr_timestep (int): Current timestep.
            mode (str): "avg" or "sum" for average rewards or summed rewards.
        """
        assert mode in ["avg", "sum"], "Mode must be 'sum' or 'avg'"

        print("[INFO] =========================================================")
        print(f"[INFO] Timestep: {curr_timestep}")

        if mode == "avg":
            print("[INFO] Reward Averages (per timestep):")
            total_avg = 0
            for key, meter in self.reward_avg_meter_dict.items():
                print(f"  [INFO] {key:<20}: {meter.avg:.4f}")
                total_avg += meter.avg
            print(f"[INFO] Sum of Averages    : {total_avg:.4f}")

        elif mode == "sum":
            print("[INFO] Reward Sums (per trajectory, averaged across envs):")
            total_sum = 0
            for key, meter in self.reward_avg_meter_dict.items():
                term_sum = torch.mean(self.full_trajectory_term_rewards[key])
                print(f"  [INFO] {key:<20}: {term_sum:.4f}")
                total_sum += term_sum
            print(f"[INFO] Sum of Rewards     : {total_sum:.4f}")

            # Print cumulative rewards of completed trajectories
            avg_full_reward = (
                sum(self.full_trajectory_rewards) / len(self.full_trajectory_rewards)
                if self.full_trajectory_rewards
                else 0
            )
            print(f"[INFO] Full Trajectory Rewards Logged: {len(self.full_trajectory_rewards)}")
            print(f"[INFO] Average Full Trajectory Reward: {avg_full_reward:.4f}")

        print("[INFO] =========================================================")

    def write_to_yaml(self, path, mode="sum"):
        """
        Writes the reward statistics to a YAML file.

        Args:
            path (str): Path to the output YAML file.
            mode (str): "avg" or "sum" for average rewards or summed rewards.
        """
        assert mode in ["avg", "sum"], "Mode must be 'sum' or 'avg'"

        # Prepare data for YAML
        data = {
            "timestep_mode": mode,
            "statistics": {},
        }

        # Collect reward data
        if mode == "avg":
            total_avg = 0
            for key, meter in self.reward_avg_meter_dict.items():
                data["statistics"][key] = {"average": meter.avg}
                total_avg += meter.avg
            data["sum_of_averages"] = total_avg

        elif mode == "sum":
            total_sum = 0
            for key, meter in self.reward_avg_meter_dict.items():
                term_sum = torch.mean(self.full_trajectory_term_rewards[key]).item()
                data["statistics"][key] = {"sum": term_sum}
                total_sum += term_sum
            data["sum_of_rewards"] = total_sum

            # Add average full trajectory reward
            avg_full_reward = (
                sum(self.full_trajectory_rewards) / len(self.full_trajectory_rewards)
                if self.full_trajectory_rewards
                else 0
            )
            data["average_full_trajectory_reward"] = avg_full_reward

            # Add count of full trajectories
            data["full_trajectory_rewards_logged"] = len(self.full_trajectory_rewards)

        # Write to YAML
        with open(path, "w") as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)

        print(f"[INFO] Statistics written to {path}")


def get_most_recent_h5py_record_path(base_path, task_name):
    """Find the most recent folder for a given task and return the path to its `h5py_record` subfolder."""
    task_path = os.path.join(base_path, task_name)

    if not os.path.exists(task_path):
        raise FileNotFoundError(f"Task folder '{task_name}' not found at {base_path}")

    # if "genhumanoid" in task_name:
    #     subdirectories = [
    #         d for d in os.listdir(task_path)
    #         if os.path.isdir(os.path.join(task_path, d)) and d[:-5].replace("_", "-").replace("-", "").isdigit()
    #     ]
    #     try:
    #         subdirectories.sort(key=lambda d: datetime.strptime(d[:-5], "%Y-%m-%d_%H-%M-%S"), reverse=True)
    #     except:
    #         import ipdb; ipdb.set_trace()
    # else:
    subdirectories = [
        d for d in os.listdir(task_path)
        if os.path.isdir(os.path.join(task_path, d)) and d.replace("_", "-").replace("-", "").isdigit()
    ]
    subdirectories.sort(key=lambda d: datetime.strptime(d, "%Y-%m-%d_%H-%M-%S"), reverse=True)


    if not subdirectories:
        raise FileNotFoundError(f"No subfolders found for task '{task_name}' in {task_path}")

    most_recent_folder = subdirectories[0]

    h5py_record_path = os.path.join(task_path, most_recent_folder, "h5py_record")
    if not os.path.exists(h5py_record_path):
        raise FileNotFoundError(f"h5py_record folder not found in '{os.path.join(task_path, most_recent_folder)}'")

    return h5py_record_path


def save_checkpoint(policy, optimizer, epoch, log_dir, is_best=False):
    """Save the model checkpoint."""
    checkpoint = {
        "epoch": epoch,
        "state_dict": policy.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
    }
    checkpoint_path = os.path.join(log_dir, f"checkpoint_epoch_{epoch}.pt")
    torch.save(checkpoint, checkpoint_path)
    print(f"[INFO] Checkpoint saved to {checkpoint_path}")

    if is_best:
        best_checkpoint_path = os.path.join(log_dir, "best_model.pt")
        torch.save(checkpoint, best_checkpoint_path)
        print(f"[INFO] Best model saved to {best_checkpoint_path}")


def one_policy_observation_to_inputs(one_policy_observation: torch.tensor, metadata, device):
    """
        Transform one policy observation into 5 inputs that a one policy model accept
        Args:
            one_policy_observation (tensor): The one policy observation. eg. For GenDog1, the size is 340 on the last dimension.
            meta: could be anything that provide the metadata of robot joint and foot numbers. By default, pass in env.unwrapped.
            device: 
        """
    # Dynamic Joint Observations
    nr_dynamic_joint_observations = metadata.nr_dynamic_joint_observations
    single_dynamic_joint_observation_length = metadata.single_dynamic_joint_observation_length
    dynamic_joint_observation_length = metadata.dynamic_joint_observation_length
    dynamic_joint_description_size = metadata.dynamic_joint_description_size

    dynamic_joint_combined_state = one_policy_observation[:, :dynamic_joint_observation_length].view((-1, nr_dynamic_joint_observations, single_dynamic_joint_observation_length))
    dynamic_joint_description = dynamic_joint_combined_state[:, :, :dynamic_joint_description_size]
    dynamic_joint_state = dynamic_joint_combined_state[:, :, dynamic_joint_description_size:]

    # # Dynamic Foot Observations
    # nr_dynamic_foot_observations = metadata.nr_dynamic_foot_observations
    # single_dynamic_foot_observation_length = metadata.single_dynamic_foot_observation_length
    # dynamic_foot_observation_length = metadata.dynamic_foot_observation_length
    # dynamic_foot_description_size = metadata.dynamic_foot_description_size

    # dynamic_foot_combined_state = one_policy_observation[:, dynamic_joint_observation_length:dynamic_joint_observation_length + dynamic_foot_observation_length].view((-1, nr_dynamic_foot_observations, single_dynamic_foot_observation_length))
    # dynamic_foot_description = dynamic_foot_combined_state[:, :, :dynamic_foot_description_size]
    # dynamic_foot_state = dynamic_foot_combined_state[:, :, dynamic_foot_description_size:]

    # policy_general_state_start_index = dynamic_joint_observation_length + dynamic_foot_observation_length
    # policy_general_state_end_index = one_policy_observation.shape[1]
    # policy_general_state_mask = torch.arange(policy_general_state_start_index, policy_general_state_end_index, device=device)
    # # exclude truck_linear_vel and height # 20->16
    # policy_exlucion_index = torch.tensor((metadata.trunk_linear_vel_update_obs_idx + metadata.height_update_obs_idx), device=device)
    # policy_general_state_mask = policy_general_state_mask[~torch.isin(policy_general_state_mask, policy_exlucion_index)]
    # general_policy_state = one_policy_observation[:, policy_general_state_mask]
    # General Policy State Transformation
    trunk_angular_vel_update_obs_idx = metadata.trunk_angular_vel_update_obs_idx
    goal_velocity_update_obs_idx = metadata.goal_velocity_update_obs_idx
    projected_gravity_update_obs_idx = metadata.projected_gravity_update_obs_idx
    general_policy_state = one_policy_observation[..., trunk_angular_vel_update_obs_idx+goal_velocity_update_obs_idx+projected_gravity_update_obs_idx]
    GENERAL_POLICY_STATE_LEN = 11
    general_policy_state = torch.cat((general_policy_state, one_policy_observation[..., -GENERAL_POLICY_STATE_LEN:]), dim=-1) # gains_and_action_scaling_factor; mass; robot_dimensions


    # # General Policy State Mask
    # policy_general_state_mask = torch.arange(303, 320, device=self.device)
    # policy_general_state_mask = policy_general_state_mask[policy_general_state_mask != 312]

    # general_policy_state = one_policy_observation[:, policy_general_state_mask]
    inputs = (
        dynamic_joint_description,
        dynamic_joint_state,
        # dynamic_foot_description,
        # dynamic_foot_state,
        general_policy_state
    )
    return inputs

def ensure_unique_save_path(save_path):
    base_name, ext = os.path.splitext(save_path)
    counter = 1
    while os.path.exists(save_path):
        save_path = f"{base_name}_{counter}{ext}"
        counter += 1
    return save_path


def save_args_to_yaml(args, output_file):
    """
    Saves argparse arguments to a YAML file.

    Args:
        args (argparse.Namespace): The parsed arguments.
        output_file (str): The path to the output YAML file.
    """
    # Convert argparse Namespace to a dictionary
    args_dict = vars(args)

    # Write the dictionary to a YAML file
    with open(output_file, 'w') as file:
        yaml.dump(args_dict, file, default_flow_style=False)

    print(f"Arguments saved to {output_file}")


def compute_gradient_norm(model):
    total_norm = 0.0
    for p in model.parameters():
        if p.grad is not None:
            param_norm = p.grad.data.norm(2)  # Compute the L2 norm
            total_norm += param_norm.item() ** 2
    total_norm = total_norm ** 0.5
    return total_norm


import psutil

# Function to get memory usage of the current process
def get_process_ram_usage():
    """
    Returns the RAM usage of the current process in MB.
    """
    process = psutil.Process()
    ram_usage = process.memory_info().rss / (1024 ** 3)  # Convert bytes to GB
    return ram_usage

# Function to get system-wide memory information
def get_system_ram_usage():
    """
    Returns system-wide memory usage statistics.
    Returns:
        total (float): Total system memory in MB.
        used (float): Used system memory in MB.
        available (float): Available system memory in MB.
    """
    memory = psutil.virtual_memory()
    total = memory.total / (1024 ** 2)  # Convert bytes to MB
    used = memory.used / (1024 ** 3)    # Convert bytes to GB
    available = memory.available / (1024 ** 3)  # Convert bytes to GB
    return used

# Get the epoch number from the logs/rsl_rl/Gendog... checkpoint directory
def extract_epoch(file_path):
    # Get the file name from the path
    file_name = os.path.basename(file_path)
    # Use regex to extract a number after 'model_' and before the file extension
    match = re.search(r'model_(\d+)\.pt', file_name)
    if match:
        return int(match.group(1))
    return None  # Return None if no match is found