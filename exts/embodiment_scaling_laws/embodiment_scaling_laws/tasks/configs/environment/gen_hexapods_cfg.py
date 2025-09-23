from __future__ import annotations

from dataclasses import MISSING

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.envs import DirectRLEnvCfg
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors import ContactSensorCfg
from omni.isaac.lab.sim import SimulationCfg
from omni.isaac.lab.terrains import TerrainImporterCfg
from omni.isaac.lab.utils import configclass

from embodiment_scaling_laws.assets.gen_hexapods import *


class GenHexapodEnvCfg(DirectRLEnvCfg):
    num_envs = 4096
    episode_length_s = 20.0
    dt = 0.005
    decimation = 4
    nr_feet = 6
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
    robot: ArticulationCfg = MISSING
    contact_sensor = ContactSensorCfg(prim_path="/World/envs/env_.*/Robot/.*", track_air_time=True)
    all_bodies_cfg = SceneEntityCfg("robot", body_names=".*")
    all_joints_cfg = SceneEntityCfg("robot", joint_names=".*")

    # robot-specific config
    trunk_cfg = SceneEntityCfg("robot", body_names="base")
    trunk_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*base.*")
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
    air_time_coeff = 0.1                        * action_dt
    feet_force_coeff = 8e-3                     * action_dt
    symmetry_air_coeff = 0.5                    * action_dt
    feet_symmetry_pairs = [(0, 5), (1, 4), (2, 3)]
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

    undesired_contact_cfg = SceneEntityCfg("contact_sensor", body_names=[])


@configclass
class Genhexapod0Cfg(GenHexapodEnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_HEXAPOD_0_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod100Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_100_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod101Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_101_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod102Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_102_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod103Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_103_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod104Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_104_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod105Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_105_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod106Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_106_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod107Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_107_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod108Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_108_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod109Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_109_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod10Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_10_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod110Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_110_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod111Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_111_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod112Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_112_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod113Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_113_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod114Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_114_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod115Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_115_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod116Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_116_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod117Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_117_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod118Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_118_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod119Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_119_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod11Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_11_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod120Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_120_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod121Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_121_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod122Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_122_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod123Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_123_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod124Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_124_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod125Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_125_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod126Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_126_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod127Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_127_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod128Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_128_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod129Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_129_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod12Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_12_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod130Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_130_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod131Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_131_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod132Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_132_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod133Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_133_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod134Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_134_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod135Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_135_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod136Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_136_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod137Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_137_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod138Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_138_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod139Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_139_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod13Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_13_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod140Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_140_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod141Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_141_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod142Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_142_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod143Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_143_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod144Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_144_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod145Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_145_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod146Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_146_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod147Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_147_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod148Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_148_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod149Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_149_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod14Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_14_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod150Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_150_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod151Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_151_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod152Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_152_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod153Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_153_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod154Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_154_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod155Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_155_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod156Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_156_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod157Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_157_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod158Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_158_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod159Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_159_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod15Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_15_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod160Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_160_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod161Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_161_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod162Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_162_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod163Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_163_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod164Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_164_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod165Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_165_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod166Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_166_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod167Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_167_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod168Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_168_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod169Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_169_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod16Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_16_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod170Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_170_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod171Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_171_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod172Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_172_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod173Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_173_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod174Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_174_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod175Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_175_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod176Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_176_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod177Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_177_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod178Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_178_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod179Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_179_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod17Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_17_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod180Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_180_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod181Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_181_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod182Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_182_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod183Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_183_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod184Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_184_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod185Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_185_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod186Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_186_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod187Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_187_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod188Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_188_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod189Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_189_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod18Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_18_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod190Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_190_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod191Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_191_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod192Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_192_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod193Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_193_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod194Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_194_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod195Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_195_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod196Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_196_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod197Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_197_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod198Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_198_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod199Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_199_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod19Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_19_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod1Cfg(GenHexapodEnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_HEXAPOD_1_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod200Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_200_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod201Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_201_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod202Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_202_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod203Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_203_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod204Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_204_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod205Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_205_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod206Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_206_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod207Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_207_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod208Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_208_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod209Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_209_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod20Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_20_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod210Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_210_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod211Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_211_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod212Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_212_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod213Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_213_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod214Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_214_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod215Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_215_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod216Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_216_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod217Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_217_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod218Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_218_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod219Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_219_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod21Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_21_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod220Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_220_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod221Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_221_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod222Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_222_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod223Cfg(GenHexapodEnvCfg):
    action_space = 24
    robot: ArticulationCfg = GEN_HEXAPOD_223_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod224Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_224_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod225Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_225_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod226Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_226_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod227Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_227_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod228Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_228_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod229Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_229_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod22Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_22_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod230Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_230_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod231Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_231_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod232Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_232_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod233Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_233_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod234Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_234_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod235Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_235_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod236Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_236_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod237Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_237_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod238Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_238_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod239Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_239_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod23Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_23_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod240Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_240_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod241Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_241_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod242Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_242_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod243Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_243_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod244Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_244_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod245Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_245_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod246Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_246_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod247Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_247_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod248Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_248_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod249Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_249_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod24Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_24_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod250Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_250_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod251Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_251_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod252Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_252_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod253Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_253_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod254Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_254_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod255Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_255_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod256Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_256_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod257Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_257_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod258Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_258_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod259Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_259_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod25Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_25_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod260Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_260_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod261Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_261_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod262Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_262_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod263Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_263_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod264Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_264_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod265Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_265_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod266Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_266_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod267Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_267_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod268Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_268_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod269Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_269_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod26Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_26_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod270Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_270_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod271Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_271_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod272Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_272_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod273Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_273_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod274Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_274_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod275Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_275_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod276Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_276_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod277Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_277_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod278Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_278_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod279Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_279_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod27Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_27_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod280Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_280_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod281Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_281_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod282Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_282_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod283Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_283_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod284Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_284_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod285Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_285_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod286Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_286_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod287Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_287_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod288Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_288_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod289Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_289_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod28Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_28_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod290Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_290_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod291Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_291_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod292Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_292_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod293Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_293_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod294Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_294_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod295Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_295_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod296Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_296_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod297Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_297_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod298Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_298_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod299Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_299_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod29Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_29_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod2Cfg(GenHexapodEnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_HEXAPOD_2_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod300Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_300_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod301Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_301_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod302Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_302_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod303Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_303_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod304Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_304_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod305Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_305_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod306Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_306_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod307Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_307_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod308Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_308_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod309Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_309_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod30Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_30_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod310Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_310_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod311Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_311_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod312Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_312_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod313Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_313_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod314Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_314_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod315Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_315_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod316Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_316_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod317Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_317_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod318Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_318_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod319Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_319_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod31Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_31_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod320Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_320_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod321Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_321_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod322Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_322_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod323Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_323_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod324Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_324_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod325Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_325_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod326Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_326_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod327Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_327_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod328Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_328_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod329Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_329_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod32Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_32_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod330Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_330_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod331Cfg(GenHexapodEnvCfg):
    action_space = 30
    robot: ArticulationCfg = GEN_HEXAPOD_331_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod33Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_33_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod34Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_34_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod35Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_35_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod36Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_36_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod37Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_37_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod38Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_38_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod39Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_39_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod3Cfg(GenHexapodEnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_HEXAPOD_3_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod40Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_40_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod41Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_41_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod42Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_42_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod43Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_43_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_1_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod44Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_44_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod45Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_45_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod46Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_46_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod47Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_47_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod48Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_48_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod49Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_49_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod4Cfg(GenHexapodEnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_HEXAPOD_4_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod50Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_50_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod51Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_51_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod52Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_52_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod53Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_53_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod54Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_54_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod55Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_55_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod56Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_56_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod57Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_57_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod58Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_58_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod59Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_59_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod5Cfg(GenHexapodEnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_HEXAPOD_5_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod60Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_60_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod61Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_61_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod62Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_62_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod63Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_63_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod64Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_64_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod65Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_65_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod66Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_66_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod67Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_67_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_3_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod68Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_68_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod69Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_69_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod6Cfg(GenHexapodEnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_HEXAPOD_6_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod70Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_70_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod71Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_71_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod72Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_72_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod73Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_73_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod74Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_74_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod75Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_75_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod76Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_76_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod77Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_77_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod78Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_78_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod79Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_79_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod7Cfg(GenHexapodEnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_HEXAPOD_7_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod80Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_80_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod81Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_81_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod82Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_82_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod83Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_83_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod84Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_84_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod85Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_85_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod86Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_86_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod87Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_87_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod88Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_88_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod89Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_89_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod8Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_8_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

@configclass
class Genhexapod90Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_90_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod91Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_91_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_4_knee_joint']) 
    lock_joint_factor = 0.2 

@configclass
class Genhexapod92Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_92_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod93Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_93_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod94Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_94_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod95Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_95_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod96Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_96_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod97Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_97_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod98Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_98_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod99Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_99_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['leg_6_knee_joint']) 
    lock_joint_factor = 0.6 

@configclass
class Genhexapod9Cfg(GenHexapodEnvCfg):
    action_space = 18
    robot: ArticulationCfg = GEN_HEXAPOD_9_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None 
    lock_joint_factor = 1.0 

