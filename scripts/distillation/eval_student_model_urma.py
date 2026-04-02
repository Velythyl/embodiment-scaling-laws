"""Script to evaluate and collect data from a student urma model."""

"""Launch Isaac Sim Simulator first."""

import argparse
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # for urma_model
import cli_args

from omni.isaac.lab.app import AppLauncher

# add argparse arguments
parser = argparse.ArgumentParser(description="Evaluate a student model in simulation.")
parser.add_argument(
    "--disable_fabric", action="store_true", default=False, help="Disable fabric and use USD I/O operations."
)
parser.add_argument("--num_envs", type=int, default=2048, help="Number of environments to simulate.")
parser.add_argument("--task", type=str, default=None, help="Name of the task.")
parser.add_argument("--seed", type=int, default=0, help="Seed used for the environment")
parser.add_argument("--ckpt_path", type=str, default=None, help="Load the specified policy from this directory.")
parser.add_argument("--log_file", type=str, default=None, help="Store return information in this file.")
parser.add_argument("--export_onnx", action="store_true", default=False, help="Export the policy to ONNX format.")
parser.add_argument(
    "--model",
    type=str,
    required=True,
    choices=["urma"],
    help="Model type."
)

# append RSL-RL cli arguments
cli_args.add_rsl_rl_args(parser)
# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)

args_cli = parser.parse_args()

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Rest everything follows."""

import gymnasium as gym
import os
import torch

from rsl_rl.runners import OnPolicyRunner
from rsl_rl.env import VecEnv

# Import extensions to set up environment tasks
import embodiment_scaling_laws.tasks  # noqa: F401

from omni.isaac.lab.utils.dict import print_dict
from omni.isaac.lab_tasks.utils import get_checkpoint_path, parse_env_cfg
from omni.isaac.lab_tasks.utils.wrappers.rsl_rl import RslRlOnPolicyRunnerCfg, RslRlVecEnvWrapper, export_policy_as_onnx

from rsl_rl.modules import ActorCritic

from utility_functions import one_policy_observation_to_inputs


class InferenceOnePolicyRunner:
    """A simple runner to handle inference using the one policy."""

    def __init__(self, env: VecEnv, device: str = "cpu", model_type: str = "urma"):
        """
        Initialize the one policy runner.

        Args:
            device (str): The device for computation ('cpu' or 'cuda').
        """
        
        # Define model
        if model_type == 'urma':
            from urma_model.policy_3head_scale2 import get_policy
            policy = get_policy(device)
        self.policy = policy
        self.device = device
        self.env = env

    def get_inference_policy(self, device: str = 'cpu'):
        """
        Prepare and return the inference-ready policy network.

        Returns:
            nn.Module: The policy network set to evaluation mode and moved to the correct device.
        """
        self.device = device
        self.policy.eval()  # Ensure evaluation mode
        self.policy.to(self.device)  # Ensure the policy is on the correct device
        print("[INFO] Inference policy is ready.")
        return self.policy

    def load(self, best_checkpoint_path: str, optimizer=None):
        """
        Load the policy network from the specified checkpoint path.

        Args:
            best_checkpoint_path (str): Full path to the 'best_model.pt' checkpoint.
            optimizer (torch.optim.Optimizer, optional): Optimizer to restore, if provided.

        Returns:
            int: The epoch at which the checkpoint was saved.
        """
        checkpoint = torch.load(best_checkpoint_path, map_location=self.device)
        if self.policy is None:
            self.policy = get_policy(self.device)  # Initialize policy if not already initialized
        self.policy.load_state_dict(checkpoint["state_dict"])
        if optimizer:
            optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        self.policy.to(self.device)
        self.policy.eval()
        print(f"[INFO] Checkpoint loaded successfully from {best_checkpoint_path}")

        return checkpoint["epoch"]

    def infer(self, one_policy_observation: torch.Tensor):
        """
        Preprocess the input one_policy_observation and run inference with the policy network.

        Args:
            one_policy_observation (torch.Tensor): The input one_policy_observation tensor.

        Returns:
            torch.Tensor: The action predicted by the policy.
        """
        (
            dynamic_joint_description,
            dynamic_joint_state,
            general_policy_state
        ) = one_policy_observation_to_inputs(one_policy_observation, self.env.unwrapped, self.device)
        # Feed processed data into the policy network
        with torch.no_grad():
            action = self.policy(
                dynamic_joint_description,
                dynamic_joint_state,
                general_policy_state
            )

        return action


def main():
    # parse configuration
    env_cfg = parse_env_cfg(
        args_cli.task, num_envs=args_cli.num_envs, use_fabric=not args_cli.disable_fabric
    )
    agent_cfg: RslRlOnPolicyRunnerCfg = cli_args.parse_rsl_rl_cfg(args_cli.task, args_cli)

    # create isaac environment
    env = gym.make(args_cli.task, cfg=env_cfg, render_mode=None)
    env.unwrapped.env_curriculum_eval = True

    # wrap around environment for rsl-rl
    env = RslRlVecEnvWrapper(env)

    # Specify the policy file directory if needed (instead of loading the newest one)
    if args_cli.ckpt_path != parser.get_default('policy_file_directory'):
        policy_file_path = args_cli.ckpt_path

    # Create one policy runner for inference and load trained model parameters
    print(f"[INFO]: Loading model checkpoint from: {policy_file_path}")
    model_device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # load previously trained model
    one_policy_runner = InferenceOnePolicyRunner(env, device=model_device, model_type=args_cli.model)
    one_policy_runner.load(policy_file_path)

    # Reset environment and start simulation
    obs, observations = env.get_observations()
    one_policy_observation = observations["observations"]["urma_obs"]
    curr_timestep = 0

    # export policy to onnx
    if args_cli.export_onnx:
        export_model_dir = os.path.join(os.path.dirname(policy_file_path), "exported")
        if not os.path.exists(export_model_dir):
            os.makedirs(export_model_dir)
        torch.onnx.export(
            one_policy_runner.policy,
            one_policy_observation_to_inputs(one_policy_observation, env.unwrapped, model_device),
            os.path.join(export_model_dir, "policy.onnx"),
            export_params=True,
            opset_version=11,
            verbose=False,
            input_names=["obs"],
            output_names=["actions"],
            dynamic_axes={},
        )
        print(f"[INFO] Policy exported to ONNX format at: {export_model_dir}/policy.onnx")

    termination_steps = torch.zeros(args_cli.num_envs, device=model_device)
    returns = torch.zeros(args_cli.num_envs, device=model_device)
    seen_dones = torch.zeros(args_cli.num_envs, dtype=torch.bool, device=model_device)

    # Main simulation loop
    while simulation_app.is_running():
        with torch.inference_mode():
            # Agent stepping
            actions = one_policy_runner.infer(one_policy_observation)

            # Environment stepping
            obs, rewards, dones, extra = env.step(actions)
            dones = dones.bool()

            if curr_timestep == 0:
                reward_extras = {key: torch.zeros_like(value, device=model_device) for key, value in extra["log_detailed"].items() if key != "reward_info/undesired_contacts"}
            for key, value in extra["log_detailed"].items():
                if key == "reward_info/undesired_contacts":
                    continue
                else:
                    reward_extras[key] += value * (1 - seen_dones.float())

            one_policy_observation = extra["observations"]["urma_obs"]

            # Update the returns
            returns += rewards * (1 - seen_dones.float())
            termination_steps[(~seen_dones) & dones] = curr_timestep + 1

            seen_dones = seen_dones | dones

            curr_timestep += 1
            if curr_timestep % 100 == 0:
                print(f"[INFO] Timestep: {curr_timestep}")
            
            if seen_dones.all():
                break

    env.close()
    del env

    avg_return = returns.mean().item()
    avg_steps = termination_steps.mean().item()
    avg_reward_extras = {key: value.mean().item() for key, value in reward_extras.items()}
    print(f"[INFO] Average return: {avg_return}, average steps: {avg_steps}")

    # log average return to file
    import json
    if args_cli.log_file is not None:
        if not os.path.exists(args_cli.log_file):
            with open(args_cli.log_file, 'w') as f:
                json.dump({}, f)
        
        # update the log file
        with open(args_cli.log_file, 'r') as f:
            log_data = json.load(f)
        log_data[args_cli.task] = {"average_return": avg_return, "average_steps": avg_steps,
                                   "returns": returns.tolist(), "steps": termination_steps.tolist()}
        log_data[args_cli.task].update({"reward_extras": {key: value.tolist() for key, value in reward_extras.items()}})
        with open(args_cli.log_file, 'w') as f:
            json.dump(log_data, f)
            print(f"[INFO] Save reward information of {args_cli.task} into {args_cli.log_file}")

if __name__ == "__main__":
    main()
    simulation_app.close()
