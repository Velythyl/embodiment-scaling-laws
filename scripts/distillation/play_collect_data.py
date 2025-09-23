"""Script to play and collect data from a checkpoint."""

"""Launch Isaac Sim Simulator first."""
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import cli_args

from omni.isaac.lab.app import AppLauncher

# add argparse arguments
parser = argparse.ArgumentParser(description="Collect demonstration data for policy distillation.")
parser.add_argument("--video", action="store_true", default=False, help="Record videos during training.")
parser.add_argument("--video_length", type=int, default=20, help="Length of the recorded video (in steps).")
parser.add_argument(
    "--disable_fabric", action="store_true", default=False, help="Disable fabric and use USD I/O operations."
)
parser.add_argument("--num_envs", type=int, default=4096, help="Number of environments to simulate.")
parser.add_argument("--task", type=str, default=None, help="Name of the task.")
parser.add_argument("--seed", type=int, default=0, help="Seed used for the environment")
parser.add_argument("--min_ckpt_iter", type=int, default=None, help="The minimum checkpoint pt iteration for collecting data")
parser.add_argument("--steps", type=int, default=1000, help="Number of steps per environment stored as dataset")
parser.add_argument("--reward_log_file", type=str, default=None, help="Indicator and directory for storing return information")
parser.add_argument("--resume_path", type=str, default=None, help="Additionally specify the wanted policy. If set, ignore task set policy path.")

# append RSL-RL cli arguments
cli_args.add_rsl_rl_args(parser)
# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)

"""Rest everything follows."""

args_cli = parser.parse_args()
# always enable cameras to record video
if args_cli.video:
    args_cli.enable_cameras = True

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app


import gymnasium as gym
import os
import torch
import tqdm
import json

from rsl_rl.runners import OnPolicyRunner

# Import extensions to set up environment tasks
import embodiment_scaling_laws.tasks  # noqa: F401

from omni.isaac.lab.utils.dict import print_dict
from omni.isaac.lab_tasks.utils import get_checkpoint_path, parse_env_cfg
from omni.isaac.lab_tasks.utils.wrappers.rsl_rl import RslRlOnPolicyRunnerCfg, RslRlVecEnvWrapper, export_policy_as_onnx
from dataset_functions import DatasetSaver  #
from utility_functions import RewardDictLogger


def main():
    # parse configuration
    env_cfg = parse_env_cfg(
        args_cli.task, num_envs=args_cli.num_envs, use_fabric=not args_cli.disable_fabric
    )
    agent_cfg: RslRlOnPolicyRunnerCfg = cli_args.parse_rsl_rl_cfg(args_cli.task, args_cli)

    # specify resume_path for loading customized policy
    # [INFO]: The args_cli.task still decides which environment to make
    if args_cli.resume_path != parser.get_default("resume_path"):
        resume_path = args_cli.resume_path
        print(f"[INFO] Loading policy file from directory: {resume_path}")
    else:
        # specify directory for logging experiments
        log_root_path = os.path.join("logs", "rsl_rl", agent_cfg.experiment_name)
        log_root_path = os.path.abspath(log_root_path)
        print(f"[INFO] Loading experiment from directory: {log_root_path}")
        resume_path = get_checkpoint_path(log_root_path, agent_cfg.load_run, agent_cfg.load_checkpoint)
        # If use  policy corresponding to the task, then check the epoch number to be at least args_cli.min_ckpt_iter
        # otherwise, directly exit
        if args_cli.min_ckpt_iter != None:
            from utility_functions import extract_epoch
            epoch_number = extract_epoch(resume_path)
            if epoch_number < args_cli.min_ckpt_iter:
                print(f"[WARNING] {agent_cfg.experiment_name} maximum checkpoint epoch is {epoch_number}. "
                      f"Does not satisfy the required min_ckpt_iter of {args_cli.min_ckpt_iter}.")
                return

    log_dir = os.path.dirname(resume_path)

    # create isaac environment
    env = gym.make(args_cli.task, cfg=env_cfg, render_mode="rgb_array" if args_cli.video else None)
    env.unwrapped.env_curriculum_eval = True

    # wrap for video recording
    if args_cli.video:
        video_kwargs = {
            "video_folder": os.path.join(log_dir, "videos", "play"),
            "step_trigger": lambda step: step == 0,
            "video_length": args_cli.video_length,
            "disable_logger": True,
        }
        print("[INFO] Recording videos during training.")
        print_dict(video_kwargs, nesting=4)
        env = gym.wrappers.RecordVideo(env, **video_kwargs)

    # wrap around environment for rsl-rl
    env = RslRlVecEnvWrapper(env)

    print(f"[INFO]: Loading model checkpoint from: {resume_path}")
    model_device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # load previously trained model
    ppo_runner = OnPolicyRunner(env, agent_cfg.to_dict(), log_dir=None, device=agent_cfg.device)
    ppo_runner.load(resume_path)

    # obtain the trained policy for inference
    policy = ppo_runner.get_inference_policy(device=env.unwrapped.device)

    # Initialize DatasetManager
    data_record_path = os.path.join(log_dir, "h5py_record")
    dataset_manager = DatasetSaver(
        record_path=data_record_path,
        max_steps_per_file=100,
        env=env
    )

    # Reset environment and start simulation
    obs, observations = env.get_observations()
    one_policy_observation = observations["observations"]["urma_obs"]
    curr_timestep = 0
    actions_std = None

    # Initialize a manual tqdm progress bar
    pbar = tqdm.tqdm(total=args_cli.steps)

    reward_dict_logger = RewardDictLogger(args_cli.num_envs)
    termination_steps = torch.zeros(args_cli.num_envs, device=model_device)
    returns = torch.zeros(args_cli.num_envs, device=model_device)
    seen_dones = torch.zeros(args_cli.num_envs, dtype=torch.bool, device=model_device)
    
    # Main simulation loop
    while simulation_app.is_running():
        with torch.inference_mode():

            # Break when current step exceed the number of data collect steps
            if curr_timestep > args_cli.steps:
                if args_cli.reward_log_file is None:
                    break
                else:
                    # If reward_log_file is needed, then break when data collect finishes and all robots done.
                    # If needed, reward_log_file should be set to "reward_log_file.yaml"
                    if seen_dones.all().item() is True:
                        break
            
            # Agent stepping
            actions = policy(obs)

            if curr_timestep < args_cli.steps:
                # Reshape and save data
                dataset_manager.save_data(
                    one_policy_observation=one_policy_observation.cpu().numpy(),
                    actions=actions.cpu().numpy(),
                )
                # print(f"[INFO] Save one_policy_observation to {data_record_path}")
                pbar.update(1)  # Manually update the progress bar
            
            curr_timestep += 1 # Manually update the curr_timestep due to while instead of for loop

            # To expand the training data distribution, we should inject noise when rolling out teacher policy
            # Please don't use randomized actions as ground truth!

            # First, record action std
            if actions_std is None:
                actions_std = actions.std(0)       # compute std for every joint
                print(f'[INFO] Action std recorded: {actions_std}')

            # Apply strong randomization 1/20 of the time so there is still quite some clean data
            # if np.random.randn() < 0.05:
            #     # actions = actions * (torch.randn_like(actions) * actions_std + 1)
            #     actions += torch.randn_like(actions) * actions_std.unsqueeze(0).repeat(args_cli.num_envs, 1) * 0.9

            # Stepping the environment
            obs, rewards, dones, extra = env.step(actions)
            dones = dones.bool()

            if curr_timestep == 1:
                reward_extras = {key: torch.zeros_like(value, device=model_device) for key, value in extra["log_detailed"].items() if key != "reward_info/undesired_contacts"}
            for key, value in extra["log_detailed"].items():
                if key == "reward_info/undesired_contacts":
                    continue
                else:
                    reward_extras[key] += value * (1 - seen_dones.float())

            one_policy_observation = extra["observations"]["urma_obs"]
            if args_cli.reward_log_file is not None:
                # log reward
                reward_dict_logger.update(env, rewards, dones, seen_dones)
                if not seen_dones.all().item():
                    returns += rewards * (1 - seen_dones.float())
                    termination_steps[(~seen_dones) & dones] = curr_timestep
                    seen_dones = seen_dones | dones

                    if curr_timestep % 100 == 0:
                        print(f"[INFO] Timestep: {curr_timestep}")
                        print(f"[INFO] Number of done robots: {seen_dones.sum()}")
                        
    if args_cli.reward_log_file is not None:
        # Sanity check that all robots are done
        print(f"[INFO] Timestep: {curr_timestep}")
        print(f"[INFO] Number of done robots: {seen_dones.sum()}")

    # log reward statistics
    reward_dict_logger.write_to_yaml(os.path.join(data_record_path, "reward_dict.yaml"))

    # close the simulator
    env.close()
    del env

    avg_return = returns.mean().item()
    avg_steps = termination_steps.mean().item()
    # avg_reward_extras = {key: value.mean().item() for key, value in reward_extras.items()}
    print(f"[INFO] Average return: {avg_return}, average steps: {avg_steps}")

    if args_cli.reward_log_file is not None:
        # log average return to file
        reward_log_file = os.path.join(data_record_path, args_cli.reward_log_file)
        if not os.path.exists(reward_log_file):
            with open(reward_log_file, 'w') as f:
                json.dump({}, f)
        
        # update the log file
        with open(reward_log_file, 'r') as f:
            log_data = json.load(f)

        log_data[args_cli.task] = {"average_return": avg_return, "average_steps": avg_steps,
                                   "returns": returns.tolist(), "steps": termination_steps.tolist()}
        log_data[args_cli.task].update({"reward_extras": {key: value.tolist() for key, value in reward_extras.items()}})

        with open(reward_log_file, 'w') as f:
            print(f"[INFO] Log reward value: average_return into {reward_log_file}")
            json.dump(log_data, f)


if __name__ == "__main__":
    # run the main execution
    main()
    # close sim app
    simulation_app.close()
