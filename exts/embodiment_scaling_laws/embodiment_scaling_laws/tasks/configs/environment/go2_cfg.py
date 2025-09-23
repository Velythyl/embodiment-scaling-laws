# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.envs import DirectRLEnvCfg
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors import ContactSensorCfg
from omni.isaac.lab.sim import SimulationCfg
from omni.isaac.lab.terrains import TerrainImporterCfg
from omni.isaac.lab.utils import configclass

from embodiment_scaling_laws.assets.unitree import GO2_CFG
# from embodiment_scaling_laws.assets.gen_quadrupeds import GO2_CFG

@configclass
class Go2EnvCfg(DirectRLEnvCfg):
    num_envs = 4096
    episode_length_s = 20.0
    dt = 0.005
    decimation = 4
    nr_feet = 4
    action_space = 12
    observation_space = 69

    action_dt = dt * decimation

    sim: SimulationCfg = SimulationCfg(
        dt=dt,
        render_interval=decimation,
        disable_contact_processing=True,
    )
    terrain = TerrainImporterCfg(
        prim_path="/World/ground",
        terrain_type="plane",
        collision_group=-1,
        physics_material=sim_utils.RigidBodyMaterialCfg(
            friction_combine_mode="average",
            restitution_combine_mode="average",
            static_friction=1.0,
            dynamic_friction=1.0,
            restitution=0.0,
        ),
        debug_vis=False,
    )

    asset_name = "robot"
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=num_envs, env_spacing=4.0, replicate_physics=True)
    robot: ArticulationCfg = GO2_CFG.replace(prim_path="/World/envs/env_.*/Robot")
    contact_sensor = ContactSensorCfg(prim_path="/World/envs/env_.*/Robot/.*", track_air_time=True)
    all_bodies_cfg = SceneEntityCfg("robot", body_names=".*")
    all_joints_cfg = SceneEntityCfg("robot", joint_names=".*")

    # robot-specific config
    trunk_cfg = SceneEntityCfg("robot", body_names="base")
    trunk_contact_cfg = SceneEntityCfg("contact_sensor", body_names=['.*base.*', '.*hip.*', '.*thigh.*'])
    all_contact_cfg = SceneEntityCfg("contact_sensor", body_names=['.*'])
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    trunk_too_low_percentage = 0.0

    step_sampling_probability = 0.002

    action_scaling_factor = 0.3

    # Curriculum
    env_curriculum_nr_levels = 100
    env_curriculum_level_success_episode_length = 1000
    env_curriculum_level_success_avg_xy_velocity_diff_abs_percentage = 0.4

    # Reward
    tracking_xy_velocity_command_coeff = 2.0    * action_dt
    tracking_yaw_velocity_command_coeff = 1.0   * action_dt
    z_velocity_coeff = 2.0                      * action_dt
    pitch_roll_vel_coeff = 0.05                 * action_dt
    pitch_roll_pos_coeff = 5.0                  * action_dt
    actuator_joint_nominal_diff_coeff = 0.0     * action_dt
    actuator_joint_nominal_diff_joints_cfg = None
    joint_position_limit_coeff = 120.0          * action_dt
    joint_velocity_limit_coeff = 10.0           * action_dt
    soft_joint_velocity_limit = 0.9
    joint_acceleration_coeff = 5e-6             * action_dt
    joint_torque_coeff = 2.4e-3                 * action_dt
    action_rate_coeff = 0.12                    * action_dt
    action_smoothness_coeff = 0.12              * action_dt
    base_height_coeff = 30.0                    * action_dt
    air_time_coeff = 0.2                        * action_dt
    feet_force_coeff = 8e-3                     * action_dt
    symmetry_air_coeff = 1.0                    * action_dt
    feet_symmetry_pairs = [(0, 1), (2, 3)]
    feet_y_distance_coeff = 2.0                 * action_dt
    stand_still_coeff = 5.0                     * action_dt

    # Domain randomization
    ## Action delay
    max_nr_action_delay_steps = 1
    mixed_action_delay_chance = 0.05
    ## Control
    motor_strength_min = 0.5
    motor_strength_max = 1.5
    p_gain_factor_min = 0.5
    p_gain_factor_max = 1.5
    d_gain_factor_min = 0.5
    d_gain_factor_max = 1.5
    p_law_position_offset_min = -0.05
    p_law_position_offset_max = 0.05
    ## Initial state
    initial_state_roll_angle_factor = 0.0625
    initial_state_pitch_angle_factor = 0.0625
    initial_state_yaw_angle_factor = 1.0
    initial_state_joint_nominal_position_factor = 0.5
    initial_state_joint_velocity_factor = 0.5
    initial_state_joint_velocity_clip = 1
    initial_state_max_linear_velocity = 0.5
    initial_state_max_angular_velocity = 0.5
    ## Observation noise
    joint_position_noise = 0.01
    joint_velocity_noise = 1.5
    trunk_angular_velocity_noise = 0.2
    ground_contact_noise_chance = 0.05
    contact_time_noise_chance = 0.05
    contact_time_noise_factor = 1.0
    gravity_vector_noise = 0.05
    ## Observation dropout
    joint_and_feet_dropout_chance = 0.05
    ## Model
    static_friction_min = 0.05
    static_friction_max = 2.0
    dynamic_friction_min = 0.05
    dynamic_friction_max = 1.5
    restitution_min = 0.0
    restitution_max = 1.0
    added_trunk_mass_min = -2.0
    added_trunk_mass_max = 2.0
    added_gravity_min = -1.0
    added_gravity_max = 1.0
    joint_friction_min = 0.0
    joint_friction_max = 0.01
    joint_armature_min = 0.0
    joint_armature_max = 0.01
    ## Perturbations
    perturb_velocity_x_min = -1.0
    perturb_velocity_x_max = 1.0
    perturb_velocity_y_min = -1.0
    perturb_velocity_y_max = 1.0
    perturb_velocity_z_min = -1.0
    perturb_velocity_z_max = 1.0
    perturb_add_chance = 0.5
    perturb_additive_multiplier = 1.5

    lock_joint_cfg = None
    lock_joint_factor = 1.0

    undesired_contact_cfg = SceneEntityCfg("contact_sensor", body_names=[])
