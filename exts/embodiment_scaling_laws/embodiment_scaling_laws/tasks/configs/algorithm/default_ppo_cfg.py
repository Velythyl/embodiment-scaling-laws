# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from omni.isaac.lab.utils import configclass

@configclass
class PolicyCfg:
    class_name = "ActorCritic"
    init_noise_std = 1.0
    actor_hidden_dims = [512, 256, 128]
    critic_hidden_dims = [512, 256, 128]
    activation = "elu"


@configclass
class AlgorithmCfg:
    class_name = "PPO"
    value_loss_coef = 1.0
    use_clipped_value_loss = True
    clip_param = 0.2
    entropy_coef = 0.002
    num_learning_epochs = 5
    num_mini_batches = 4
    learning_rate = 1.0e-3
    schedule = "adaptive"
    gamma = 0.99
    lam = 0.95
    desired_kl = 0.01
    max_grad_norm = 1.0


@configclass
class DefaultPPORunnerCfg:
    seed = 42
    device = "cuda:0"
    num_steps_per_env = 24

    # 7000 is minimally sufficient to see if the training is on the right track;
    # 15k needed for sim-to-real for quadrupeds, and 35k needed for humanoids
    max_iterations = 17500

    empirical_normalization = False
    policy = PolicyCfg()
    algorithm = AlgorithmCfg()
    save_interval = 1000
    experiment_name = "standard"
    run_name = ""
    logger = "tensorboard"
    neptune_project = "isaaclab"
    wandb_project = "isaaclab"
    resume = False
    load_run = ".*"
    load_checkpoint = "model_.*.pt"


@configclass
class Go2PPORunnerCfg(DefaultPPORunnerCfg):
    experiment_name = "Go2"


@configclass
class H1PPORunnerCfg(DefaultPPORunnerCfg):
    experiment_name = "H1"

