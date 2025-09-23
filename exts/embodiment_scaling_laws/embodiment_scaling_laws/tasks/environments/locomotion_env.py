from __future__ import annotations
import torch
import math

from omni.isaac.lab.assets import Articulation
from omni.isaac.lab.envs import DirectRLEnv, DirectRLEnvCfg
import omni.isaac.lab.envs.mdp as mdp
from omni.isaac.lab.sensors import ContactSensor
import omni.isaac.lab.sim as sim_utils
import omni.isaac.lab.utils.math as math_utils
import os
import json


class LocomotionEnv(DirectRLEnv):
    cfg: DirectRLEnvCfg

    def __init__(self, cfg: DirectRLEnvCfg, render_mode: str | None = None, **kwargs):
        super().__init__(cfg, render_mode, **kwargs)
        self.action_dt = self.cfg.action_dt

        self.all_bodies_cfg = self.cfg.all_bodies_cfg
        self.all_bodies_cfg.resolve(self.scene)
        self.all_joints_cfg = self.cfg.all_joints_cfg
        self.all_joints_cfg.resolve(self.scene)
        self.trunk_cfg = self.cfg.trunk_cfg
        self.trunk_cfg.resolve(self.scene)
        self.trunk_contact_cfg = self.cfg.trunk_contact_cfg
        self.all_contact_cfg = self.cfg.all_contact_cfg
        self.all_contact_cfg.resolve(self.scene)
        self.feet_contact_cfg = self.cfg.feet_contact_cfg
        self.feet_contact_cfg.resolve(self.scene)

        # Set up a default termination condition
        if self.trunk_contact_cfg is None:
            self.all_body_ids_for_contact_termination = [body_id for body_id in self.all_contact_cfg.body_ids if body_id not in self.feet_contact_cfg.body_ids]
        else:
            self.trunk_contact_cfg.resolve(self.scene)
            self.all_body_ids_for_contact_termination = self.trunk_contact_cfg.body_ids

        # Set up undesired contact
        self.undesired_contact_cfg = self.cfg.undesired_contact_cfg
        self.undesired_contact_cfg.resolve(self.scene)

        self.nr_joints = self.robot.data.default_joint_pos.shape[1]
        self.nr_feet = self.cfg.nr_feet

        self.joint_nominal_positions = self.robot.data.default_joint_pos
        self.default_joint_limit = self.robot.data.default_joint_limits[:, :, :].clone()
        self.action_scaling_factor = self.cfg.action_scaling_factor

        # Lock the joint; Specify lock joint index and lock scale factor
        if self.cfg.lock_joint_cfg is None:
            self.lock_joint_ids = []
            assert self.cfg.lock_joint_factor == 1, \
                f'when self.cfg.lock_joint_cfg is None, lock_joint_factor = {self.cfg.lock_joint_factor} is not 1'
            self.lock_joint_factor = 1
        else:
            self.lock_joint_cfg = self.cfg.lock_joint_cfg
            self.lock_joint_cfg.resolve(self.scene)
            self.lock_joint_ids = self.lock_joint_cfg.joint_ids
            self.lock_joint_factor = self.cfg.lock_joint_factor

        if 'all' in self.robot.actuators:
            robot_actuators = self.robot.actuators["all"] # this should use the same order as self.robot.data.joint_names
            self.joint_max_velocity = robot_actuators.velocity_limit
            self.joint_max_torque = robot_actuators.effort_limit
            self.p_gains = robot_actuators.stiffness
            self.d_gains = robot_actuators.damping
        elif 'base_legs' in self.robot.actuators:
            robot_actuators = self.robot.actuators["base_legs"]
            self.joint_max_velocity = robot_actuators.velocity_limit
            self.joint_max_torque = robot_actuators.effort_limit
            self.p_gains = robot_actuators.stiffness
            self.d_gains = robot_actuators.damping
        else:
            raise NotImplementedError()

        self.hard_joint_lower_limits = self.default_joint_limit[:, :, 0].clone()
        self.hard_joint_lower_limits[:, self.lock_joint_ids] = self.lock_joint_factor * self.hard_joint_lower_limits[:, self.lock_joint_ids] + (1 - self.lock_joint_factor) * self.joint_nominal_positions[:, self.lock_joint_ids]
        self.hard_joint_upper_limits = self.default_joint_limit[:, :, 1].clone()
        self.hard_joint_upper_limits[:, self.lock_joint_ids] = self.lock_joint_factor * self.hard_joint_upper_limits[:, self.lock_joint_ids] + (1 - self.lock_joint_factor) * self.joint_nominal_positions[:, self.lock_joint_ids]

        self.trunk_too_low_percentage = self.cfg.trunk_too_low_percentage

        self.step_sampling_probability = self.cfg.step_sampling_probability

        self.goal_velocities = torch.rand((self.num_envs, 3), device=self.sim.device).uniform_(-1.0, 1.0)
        self.target_global_goal = False  # Used for play_collect_replay_trajectory.py
        self.previous_actions = torch.zeros((self.num_envs, self.nr_joints), dtype=torch.float32, device=self.sim.device)
        self.previous_previous_actions = torch.zeros((self.num_envs, self.nr_joints), dtype=torch.float32, device=self.sim.device)
        self.previous_feet_air_times = torch.zeros((self.num_envs, self.nr_feet), dtype=torch.float32, device=self.sim.device)

        self.env_curriculum_nr_levels = self.cfg.env_curriculum_nr_levels
        self.env_curriculum_level_success_episode_length = self.cfg.env_curriculum_level_success_episode_length
        self.env_curriculum_level_success_avg_xy_velocity_diff_abs_percentage = self.cfg.env_curriculum_level_success_avg_xy_velocity_diff_abs_percentage
        self.env_curriculum_eval = False
        self.env_curriculum_coeff = torch.zeros((self.num_envs,), dtype=torch.float32, device=self.sim.device)
        self.max_command_velocity = 1.0
        self.episode_total_xy_velocity_diff_abs = torch.zeros((self.num_envs,), dtype=torch.float32, device=self.sim.device)
        self.last_episode_length = torch.zeros((self.num_envs,), dtype=torch.float32, device=self.sim.device)

        self.tracking_xy_velocity_command_coeff = self.cfg.tracking_xy_velocity_command_coeff
        self.tracking_yaw_velocity_command_coeff = self.cfg.tracking_yaw_velocity_command_coeff
        self.z_velocity_coeff = self.cfg.z_velocity_coeff
        self.pitch_roll_vel_coeff = self.cfg.pitch_roll_vel_coeff
        self.pitch_roll_pos_coeff = self.cfg.pitch_roll_pos_coeff

        self.actuator_joint_nominal_diff_coeff = self.cfg.actuator_joint_nominal_diff_coeff
        actuator_joint_nominal_diff_joints_cfg = self.cfg.actuator_joint_nominal_diff_joints_cfg
        if actuator_joint_nominal_diff_joints_cfg is not None:
            actuator_joint_nominal_diff_joints_cfg.resolve(self.scene)
            self.actuator_joint_nominal_diff_joints = actuator_joint_nominal_diff_joints_cfg.joint_ids
        else:
            # dummy to first joint to avoid tensor indexing error -> in that case make sure the coeff is 0.0
            self.actuator_joint_nominal_diff_joints = [0,]  
            self.actuator_joint_nominal_diff_coeff = 0.0

        self.joint_position_limit_coeff = self.cfg.joint_position_limit_coeff
        self.joint_velocity_limit_coeff = self.cfg.joint_velocity_limit_coeff
        self.soft_joint_velocity_limit = self.cfg.soft_joint_velocity_limit
        self.joint_acceleration_coeff = self.cfg.joint_acceleration_coeff
        self.joint_torque_coeff = self.cfg.joint_torque_coeff
        self.action_rate_coeff = self.cfg.action_rate_coeff
        self.action_smoothness_coeff = self.cfg.action_smoothness_coeff
        self.base_height_coeff = self.cfg.base_height_coeff
        self.air_time_coeff = self.cfg.air_time_coeff
        self.feet_force_coeff = self.cfg.feet_force_coeff
        self.symmetry_air_coeff = self.cfg.symmetry_air_coeff
        self.feet_symmetry_pairs = torch.tensor(self.cfg.feet_symmetry_pairs, dtype=torch.int32, device=self.sim.device)
        self.feet_y_distance_coeff = self.cfg.feet_y_distance_coeff
        self.stand_still_coeff = self.cfg.stand_still_coeff
        self.calculated_feet_y_distance_target = False

        self.max_nr_action_delay_steps = self.cfg.max_nr_action_delay_steps
        self.mixed_action_delay_chance = self.cfg.mixed_action_delay_chance
        self.action_current_mixed = torch.zeros((self.num_envs,), dtype=torch.bool, device=self.sim.device)
        self.action_history = torch.zeros((self.num_envs, self.max_nr_action_delay_steps + 1, self.nr_joints), dtype=torch.float32, device=self.sim.device)

        self.motor_strength_min = self.cfg.motor_strength_min
        self.motor_strength_max = self.cfg.motor_strength_max
        self.p_gain_factor_min = self.cfg.p_gain_factor_min
        self.p_gain_factor_max = self.cfg.p_gain_factor_max
        self.d_gain_factor_min = self.cfg.d_gain_factor_min
        self.d_gain_factor_max = self.cfg.d_gain_factor_max
        self.p_law_position_offset_min = self.cfg.p_law_position_offset_min
        self.p_law_position_offset_max = self.cfg.p_law_position_offset_max
        self.extrinsic_motor_strength = torch.ones((self.num_envs, self.nr_joints), dtype=torch.float32, device=self.sim.device)
        self.extrinsic_p_gain_factor = torch.ones((self.num_envs, self.nr_joints), dtype=torch.float32, device=self.sim.device)
        self.extrinsic_d_gain_factor = torch.ones((self.num_envs, self.nr_joints), dtype=torch.float32, device=self.sim.device)
        self.extrinsic_position_offset = torch.zeros((self.num_envs, self.nr_joints), dtype=torch.float32, device=self.sim.device)

        self.initial_state_roll_angle_factor = self.cfg.initial_state_roll_angle_factor
        self.initial_state_pitch_angle_factor = self.cfg.initial_state_pitch_angle_factor
        self.initial_state_yaw_angle_factor = self.cfg.initial_state_yaw_angle_factor
        self.initial_state_joint_nominal_position_factor = self.cfg.initial_state_joint_nominal_position_factor
        self.initial_state_joint_velocity_factor = self.cfg.initial_state_joint_velocity_factor
        self.initial_state_joint_velocity_clip = self.cfg.initial_state_joint_velocity_clip
        self.initial_state_max_linear_velocity = self.cfg.initial_state_max_linear_velocity
        self.initial_state_max_angular_velocity = self.cfg.initial_state_max_angular_velocity

        self.joint_position_noise = self.cfg.joint_position_noise
        self.joint_velocity_noise = self.cfg.joint_velocity_noise
        self.trunk_angular_velocity_noise = self.cfg.trunk_angular_velocity_noise
        self.ground_contact_noise_chance = self.cfg.ground_contact_noise_chance
        self.contact_time_noise_chance = self.cfg.contact_time_noise_chance
        self.contact_time_noise_factor = self.cfg.contact_time_noise_factor
        self.gravity_vector_noise = self.cfg.gravity_vector_noise

        self.joint_and_feet_dropout_chance = self.cfg.joint_and_feet_dropout_chance

        self.static_friction_min = self.cfg.static_friction_min
        self.static_friction_max = self.cfg.static_friction_max
        self.dynamic_friction_min = self.cfg.dynamic_friction_min
        self.dynamic_friction_max = self.cfg.dynamic_friction_max
        self.restitution_min = self.cfg.restitution_min
        self.restitution_max = self.cfg.restitution_max
        self.added_trunk_mass_min = self.cfg.added_trunk_mass_min
        self.added_trunk_mass_max = self.cfg.added_trunk_mass_max
        self.added_gravity_min = self.cfg.added_gravity_min
        self.added_gravity_max = self.cfg.added_gravity_max
        self.joint_friction_min = self.cfg.joint_friction_min
        self.joint_friction_max = self.cfg.joint_friction_max
        self.joint_armature_min = self.cfg.joint_armature_min
        self.joint_armature_max = self.cfg.joint_armature_max
        event_term_config = mdp.EventTermCfg()
        event_term_config.params = {
            "env": self,
            "static_friction_range": (self.static_friction_min, self.static_friction_max),
            "dynamic_friction_range": (self.dynamic_friction_min, self.dynamic_friction_max),
            "restitution_range": (self.restitution_min, self.restitution_max),
            "num_buckets": 64,
            "asset_cfg": self.all_bodies_cfg,
        }
        self.randomize_rigid_body_material = mdp.randomize_rigid_body_material(event_term_config, self)

        self.perturb_velocity_x_min = self.cfg.perturb_velocity_x_min
        self.perturb_velocity_x_max = self.cfg.perturb_velocity_x_max
        self.perturb_velocity_y_min = self.cfg.perturb_velocity_y_min
        self.perturb_velocity_y_max = self.cfg.perturb_velocity_y_max
        self.perturb_velocity_z_min = self.cfg.perturb_velocity_z_min
        self.perturb_velocity_z_max = self.cfg.perturb_velocity_z_max
        self.perturb_add_chance = self.cfg.perturb_add_chance
        self.perturb_additive_multiplier = self.cfg.perturb_additive_multiplier

        self.set_observation_indices()

        # initialize URMA-related attributs
        self.urma_initialized = False
        self._setup_urma_obs_params()

        self.handle_domain_randomization(all_envs=True)

    def _setup_urma_obs_params(self):
        """
        Migrated from branch isaac-v2.1. Initializing some attributes needed to generate urma observation.
        """
        self._read_robot_description_vec()

        self.joint_names = self.robot.data.joint_names
        self.foot_names = self.robot.data.body_names

        self.name_to_description_vector = self.get_name_to_description_vector()
        self.initial_observation = self._initialize_urma_observations()
        self.observation_name_to_id = self._get_observation_space()

        # Idx that need to be updated every step
        self.joint_positions_update_obs_idx = [self.observation_name_to_id[joint_name + "_position"] for joint_name in self.joint_names]
        self.joint_velocities_update_obs_idx = [self.observation_name_to_id[joint_name + "_velocity"] for joint_name in self.joint_names]
        self.joint_previous_actions_update_obs_idx = [self.observation_name_to_id[joint_name + "_previous_action"] for joint_name in self.joint_names]
        self.trunk_angular_vel_update_obs_idx = [self.observation_name_to_id["trunk_" + observation_name] for observation_name in ["roll_velocity", "pitch_velocity", "yaw_velocity"]]
        self.goal_velocity_update_obs_idx = [self.observation_name_to_id["goal_" + observation_name] for observation_name in ["x_velocity", "y_velocity", "yaw_velocity"]]
        self.projected_gravity_update_obs_idx = [self.observation_name_to_id["projected_gravity_" + observation_name] for observation_name in ["x", "y", "z"]]

        self.urma_initialized = True
        print("LocomotionEnv init done")

    def _get_observation_space(self):
        observation_names = []

        # Dynamic observations
        self.nr_dynamic_joint_observations = len(self.joint_names)
        self.single_dynamic_joint_observation_length = self.dynamic_joint_description_size + 3
        self.dynamic_joint_observation_length = self.single_dynamic_joint_observation_length * self.nr_dynamic_joint_observations
        for joint_name in self.joint_names:
            observation_names.extend([joint_name + "_description_" + str(i) for i in range(self.dynamic_joint_description_size)])
            observation_names.extend([
                joint_name + "_position", joint_name + "_velocity", joint_name + "_previous_action",
            ])

        # General observations
        observation_names.extend([
            "trunk_roll_velocity", "trunk_pitch_velocity", "trunk_yaw_velocity",
        ])

        observation_names.extend(["goal_x_velocity", "goal_y_velocity", "goal_yaw_velocity"])
        observation_names.extend(["projected_gravity_x", "projected_gravity_y", "projected_gravity_z"])

        # General robot context
        observation_names.extend(["p_gain", "d_gain", "action_scaling_factor"])
        observation_names.append("mass")
        observation_names.extend(["robot_length", "robot_width", "robot_height"])

        name_to_idx = {name: idx for idx, name in enumerate(observation_names)}

        self.one_policy_observation_length = len(name_to_idx)

        return name_to_idx

    def _read_robot_description_vec(self, file_name: str = "robot_description_vec.json"):
        # Construct the path to the JSON file
        json_path = os.path.join(
            os.path.dirname(
                os.path.dirname(self.cfg.robot.spawn.usd_path)
            ),
            file_name
        )

        if not os.path.exists(json_path):
            raise FileNotFoundError(
                f"Could not find the robot description JSON file at {json_path}. Did you generate it?"
            )

        # Open and load the JSON file
        with open(json_path, "r") as f:
            self.robot_description_vec_json = json.load(f)

    def _setup_scene(self):
        self.robot = Articulation(self.cfg.robot)
        self.robot._apply_actuator_model = lambda: None
        self.cfg.terrain.num_envs = self.scene.cfg.num_envs
        self.cfg.terrain.env_spacing = self.scene.cfg.env_spacing
        self.terrain = self.cfg.terrain.class_type(self.cfg.terrain)
        self.contact_sensor = ContactSensor(self.cfg.contact_sensor)
        self.scene.sensors["contact_sensor"] = self.contact_sensor

        self.scene.clone_environments(copy_from_source=False)
        self.scene.filter_collisions(global_prim_paths=[self.cfg.terrain.prim_path])
        self.scene.articulations["robot"] = self.robot

        light_cfg = sim_utils.DomeLightCfg(intensity=2000.0, color=(0.75, 0.75, 0.75))
        light_cfg.func("/World/Light", light_cfg)

    def get_name_to_description_vector(self):
        name_to_description_vector = {}

        bbox_corner_0, bbox_corner_1 = torch.tensor(self.robot_description_vec_json['bbox'][0],
                                                    device=self.sim.device), torch.tensor(
            self.robot_description_vec_json['bbox'][1], device=self.sim.device)
        original_bbox_min_z = bbox_corner_0[2].clone()
        bbox_corner_1[2] -= original_bbox_min_z
        bbox_corner_0[2] = 0.0
        robot_dimensions = torch.abs(bbox_corner_0 - bbox_corner_1)
        robot_bbox_center = (bbox_corner_0 + bbox_corner_1) / 2
        self.robot_dimensions = robot_dimensions.unsqueeze(0).repeat(self.num_envs, 1)

        self.gains_and_action_scaling_factor = torch.tensor([self.p_gains[0, 0], self.d_gains[0, 0],
                                                             self.cfg.action_scaling_factor], device=self.sim.device)
        self.mass = torch.sum(self.robot.data.default_mass, dim=1).unsqueeze(1).to(self.sim.device)

        # Compute normalized joint positions and axes
        for i, joint_name in enumerate(self.joint_names):
            relative_joint_position = torch.tensor(
                self.robot_description_vec_json['joint_info'][joint_name]['position'],
                device=self.sim.device).unsqueeze(0).repeat(self.num_envs, 1)
            relative_joint_position[:, 2] -= original_bbox_min_z
            relative_joint_position -= robot_bbox_center  # noisy center estimate as an approximation
            relative_joint_position_normalized = (relative_joint_position - (bbox_corner_0 - robot_bbox_center)) / (
                        self.robot_dimensions + 1e-8)  # note the mins are based on links

            relative_joint_axis_local = torch.tensor(self.robot_description_vec_json['joint_info'][joint_name]['axis'],
                                                     device=self.sim.device).unsqueeze(0).repeat(self.num_envs, 1)

            # Append joint description vector
            name_to_description_vector[joint_name] = torch.cat([
                (relative_joint_position_normalized / 0.5) - 1.0,
                relative_joint_axis_local,
                self.joint_nominal_positions[:, i].unsqueeze(1) / 4.6,
                (self.joint_max_torque[:, i].unsqueeze(1) / 500.0) - 1.0,
                (self.joint_max_velocity[:, i].unsqueeze(1) / 17.5) - 1.0,
                self.hard_joint_lower_limits[:, i].unsqueeze(1) / 4.6,
                self.hard_joint_upper_limits[:, i].unsqueeze(1) / 4.6,
                ((self.gains_and_action_scaling_factor / torch.tensor([50.0, 1.0, 0.4], device=self.sim.device)) - 1.0).repeat((self.num_envs, 1)),
                (self.mass / 85.0) - 1.0,
                (self.robot_dimensions / 1.0) - 1.0,
            ], dim=1)
        
        self.dynamic_joint_description_size = name_to_description_vector[self.joint_names[0]].shape[1]

        return name_to_description_vector

    def _reset_idx(self, env_ids: torch.Tensor):
        if not self.calculated_feet_y_distance_target:
            self.robot.write_joint_state_to_sim(self.robot.data.default_joint_pos[env_ids], 0.0 * self.joint_max_velocity[env_ids], None, env_ids)
            feet_indices, _ = self.robot.find_bodies(self.feet_contact_cfg.body_names, True)
            global_feet_pos = self.robot.data.body_pos_w[:, feet_indices]
            local_feet_pos = math_utils.quat_rotate_inverse(self.robot.data.root_quat_w[:, None, :], global_feet_pos - self.robot.data.root_state_w[:, None, :3])
            feet_y_distance = torch.abs(local_feet_pos[:, self.feet_symmetry_pairs[:, 0], 1] - local_feet_pos[:, self.feet_symmetry_pairs[:, 1], 1]).mean(dim=1)
            self.feet_y_distance_target = feet_y_distance.mean().item()
            self.calculated_feet_y_distance_target = True
            self.nominal_trunk_z = self.robot.data.root_state_w[0, 2] - (global_feet_pos[:, :, 2].min().item() / 2.0)
            self.starting_y_position = self.robot.data.root_state_w[:, 1]
        
        if env_ids is None or len(env_ids) == self.num_envs:
            env_ids = self.robot._ALL_INDICES
        self.robot.reset(env_ids)
        super()._reset_idx(env_ids)

        nr_reset_envs = env_ids.shape[0]

        self.env_curriculum_coeff[env_ids] = torch.clamp(
            torch.where((self.last_episode_length[env_ids] >= self.env_curriculum_level_success_episode_length) &
                        ((self.episode_total_xy_velocity_diff_abs[env_ids] / torch.maximum(self.last_episode_length[env_ids], torch.tensor(1.0, device=self.episode_total_xy_velocity_diff_abs.device))) <= (self.max_command_velocity * self.env_curriculum_level_success_avg_xy_velocity_diff_abs_percentage)),
                self.env_curriculum_coeff[env_ids] + (1.0 / self.env_curriculum_nr_levels),
                self.env_curriculum_coeff[env_ids] - (1.0 / self.env_curriculum_nr_levels)),
            min=0.0,
            max=1.0
        )

        self.episode_total_xy_velocity_diff_abs[env_ids] *= 0.0

        if self.env_curriculum_eval:
            curriculum_coeff = self.env_curriculum_coeff[env_ids] * 0.0 + 1.0
        else:
            curriculum_coeff = self.env_curriculum_coeff[env_ids]
        curriculum_coeff_1 = curriculum_coeff.reshape(-1, 1)


        roll_angle = ((torch.rand((nr_reset_envs,), device=self.sim.device) * 2) - 1.0) * math.pi * self.initial_state_roll_angle_factor * curriculum_coeff
        pitch_angle = ((torch.rand((nr_reset_envs,), device=self.sim.device) * 2) - 1.0) * math.pi * self.initial_state_pitch_angle_factor * curriculum_coeff
        yaw_angle = ((torch.rand((nr_reset_envs,), device=self.sim.device) * 2) - 1.0) * math.pi * self.initial_state_yaw_angle_factor * curriculum_coeff
        quaternion = axis_angle_to_quaternion(torch.stack([roll_angle, pitch_angle, yaw_angle], dim=1))
        joint_positions = self.robot.data.default_joint_pos[env_ids] * (1.0 + ((torch.rand((nr_reset_envs, self.nr_joints), device=self.sim.device) * 2) - 1.0) * self.initial_state_joint_nominal_position_factor * curriculum_coeff_1)

        # note that the randomization strength below line is dependent on the joint velocity range
        # some robots are very sensitive to the initial velocities, such as very tall humanoids
        # and the randomization could be overly strong for robots with super large joint_max_velocity
        # so it's good to clip the range to a constant, which is a hyper parameter
        joint_velocities = (self.joint_max_velocity[env_ids] * ((torch.rand((nr_reset_envs, self.nr_joints),
                                                                           device=self.sim.device) * 2) - 1.0)
                            * self.initial_state_joint_velocity_factor * curriculum_coeff_1)
        joint_velocities = joint_velocities.clip(-self.initial_state_joint_velocity_clip, self.initial_state_joint_velocity_clip)

        linear_velocity = ((torch.rand((nr_reset_envs, 3), device=self.sim.device) * 2) - 1.0) * self.initial_state_max_linear_velocity * curriculum_coeff_1
        angular_velocity = ((torch.rand((nr_reset_envs, 3), device=self.sim.device) * 2) - 1.0) * self.initial_state_max_angular_velocity * curriculum_coeff_1

        default_root_state = self.robot.data.default_root_state[env_ids]
        default_root_state[:, :3] += self.scene.env_origins[env_ids]
        default_root_state[:, 3:7] = quaternion
        default_root_state[:, 7:10] = linear_velocity
        default_root_state[:, 10:] = angular_velocity

        self.robot.write_root_pose_to_sim(default_root_state[:, :7], env_ids)
        self.robot.write_root_velocity_to_sim(default_root_state[:, 7:], env_ids)
        self.robot.write_joint_state_to_sim(joint_positions, joint_velocities, None, env_ids)

        feet_indices, _ = self.robot.find_bodies(self.feet_contact_cfg.body_names, True)
        global_feet_pos = self.robot.data.body_pos_w[env_ids][:, feet_indices, :]
        lowest_feet = global_feet_pos[:, :, 2].min(dim=1).values
        root_state = self.robot.data.root_state_w[env_ids]
        root_state[:, 2] -= (lowest_feet / 2.0)
        self.robot.write_root_pose_to_sim(root_state[:, :7], env_ids)

        self.previous_actions[env_ids] *= 0.0
        self.previous_previous_actions[env_ids] *= 0.0
        self.previous_feet_air_times[env_ids] *= 0.0

        self.action_history[env_ids] *= 0.0


    def _pre_physics_step(self, actions: torch.Tensor):
        self.actions = actions

        # Action delay
        self.action_history = torch.roll(self.action_history, -1, dims=1)
        self.action_history[:, -1] = self.actions
        current_nr_delay_steps = torch.zeros((self.num_envs,), dtype=torch.int32, device=self.sim.device)
        current_nr_delay_steps[self.action_current_mixed] = torch.randint(0, self.max_nr_action_delay_steps + 1, (int(self.action_current_mixed.sum().item()),), dtype=torch.int32, device=self.sim.device)
        chosen_actions = self.action_history[torch.arange(self.num_envs, device=self.sim.device), -1 - current_nr_delay_steps]

        # PD control
        scaled_actions = chosen_actions * self.action_scaling_factor
        target_joint_positions = self.joint_nominal_positions + scaled_actions
        
        ## Test locked joint
        # Determine the joint lower upper bound around the nominal joint position
        # original lower limits < hard lower limits < nominal positions < hard upper limits < original upper limits
        hard_lock_ids = self.lock_joint_ids

        # The real position of joint read from the simulator
        actual_joint_position = self.robot.data.joint_pos.clone()

        # Compute violation differences for the locked joints
        hard_lower_diff = - (actual_joint_position[:, hard_lock_ids] - self.hard_joint_lower_limits[:, hard_lock_ids])
        hard_upper_diff = actual_joint_position[:, hard_lock_ids] - self.hard_joint_upper_limits[:, hard_lock_ids]

        # Check if any locked joint in each robot exceeds the bounds
        # Shaped in locked joints
        hard_out_of_lower_limits = (hard_lower_diff > 0)
        hard_out_of_upper_limits = (hard_upper_diff > 0)
        hard_out_of_limits = hard_out_of_lower_limits | hard_out_of_upper_limits

        # Define normal p_gain, d_gain
        # Shaped in all joints
        normal_p_gain = self.p_gains.clone()
        normal_d_gain = self.d_gains.clone()

        # Define high p_gain, d_gain
        # Shaped in all joints
        high_p_gain = torch.ones(normal_p_gain.shape, device=self.sim.device) * 60
        high_d_gain = torch.ones(normal_d_gain.shape, device=self.sim.device) * 1

        #  Apply high p_gain, d_gain only for locked joints of robots that exceed bounds
        # Shaped in locked joints
        normal_p_gain[:, hard_lock_ids] = torch.where(
            hard_out_of_limits,  # Shape: [4096, 3]
            high_p_gain[:, hard_lock_ids],    # High p_gain where condition is True
            normal_p_gain[:, hard_lock_ids]  # Keep original value otherwise
        )
        normal_d_gain[:, hard_lock_ids] = torch.where(
            hard_out_of_limits,  # Shape: [4096, 3]
            high_d_gain[:, hard_lock_ids],    # High d_gain where condition is True
            normal_d_gain[:, hard_lock_ids]  # Keep original value otherwise
        )

        # Clip the locked joint
        target_joint_positions[:, hard_lock_ids] = torch.clamp(target_joint_positions[:, hard_lock_ids], min=self.hard_joint_lower_limits[:, hard_lock_ids], max=self.hard_joint_upper_limits[:, hard_lock_ids])

        # Compute torques with the updated p_gain and d_gain
        self.torques = normal_p_gain * self.extrinsic_p_gain_factor * (target_joint_positions - self.robot.data.joint_pos + self.extrinsic_position_offset) \
                    - normal_d_gain * self.extrinsic_d_gain_factor * self.robot.data.joint_vel
        ## Test locked joint end

        # Clip torque based on maximum torque limit; Normal practice
        self.torques = torch.clamp(self.torques * self.extrinsic_motor_strength, -self.joint_max_torque, self.joint_max_torque)

    def _apply_action(self):
        self.robot._joint_effort_target_sim = self.torques

    def get_undesired_contacts(self, sensor_cfg, threshold) -> torch.Tensor:
        """Penalize undesired contacts as the number of violations that are above a threshold."""
        contact_sensor = self.scene.sensors[sensor_cfg.name]
        net_contact_forces = contact_sensor.data.net_forces_w_history[:, :, sensor_cfg.body_ids]  # (envs, T, n links, 3)
        is_contact = net_contact_forces.norm(dim=-1).max(dim=1)[0] > threshold  # shape (num_envs, num_links)
        return is_contact.float()

    def handle_domain_randomization(self, all_envs=False):
        if not all_envs:
            env_randomization_mask = torch.rand((self.num_envs,), device=self.sim.device) < self.step_sampling_probability
        else:
            env_randomization_mask = torch.zeros((self.num_envs,), device=self.sim.device) < self.step_sampling_probability  # ugly, to avoid linting error
        nr_randomized_envs = env_randomization_mask.sum()

        if self.env_curriculum_eval:
            all_curriculum_coeff = self.env_curriculum_coeff * 0.0 + 1.0
            curriculum_coeff = self.env_curriculum_coeff[env_randomization_mask]
        else:
            all_curriculum_coeff = self.env_curriculum_coeff
            curriculum_coeff = self.env_curriculum_coeff[env_randomization_mask]
        curriculum_coeff_1 = curriculum_coeff.reshape(-1, 1)
        curriculum_coeff_1_cpu = curriculum_coeff_1.cpu()
        curriculum_coeff_mean_cpu = all_curriculum_coeff.mean().item()


        # Action delay
        self.action_current_mixed[env_randomization_mask] = torch.rand((nr_randomized_envs,), device=self.sim.device) < self.mixed_action_delay_chance * curriculum_coeff
        
        # Control
        default_motor_stength = 1.0
        motor_strength_min = curriculum_coeff_1 * self.motor_strength_min + (1.0 - curriculum_coeff_1) * default_motor_stength
        motor_strength_max = curriculum_coeff_1 * self.motor_strength_max + (1.0 - curriculum_coeff_1) * default_motor_stength
        self.extrinsic_motor_strength[env_randomization_mask] = torch.rand((nr_randomized_envs, self.nr_joints), device=self.sim.device) * (motor_strength_max - motor_strength_min) + motor_strength_min
        
        default_p_gain_factor = 1.0
        p_gain_factor_min = curriculum_coeff_1 * self.p_gain_factor_min + (1.0 - curriculum_coeff_1) * default_p_gain_factor
        p_gain_factor_max = curriculum_coeff_1 * self.p_gain_factor_max + (1.0 - curriculum_coeff_1) * default_p_gain_factor
        self.extrinsic_p_gain_factor[env_randomization_mask] = torch.rand((nr_randomized_envs, self.nr_joints), device=self.sim.device) * (p_gain_factor_max - p_gain_factor_min) + p_gain_factor_min
        
        default_d_gain_factor = 1.0
        d_gain_factor_min = curriculum_coeff_1 * self.d_gain_factor_min + (1.0 - curriculum_coeff_1) * default_d_gain_factor
        d_gain_factor_max = curriculum_coeff_1 * self.d_gain_factor_max + (1.0 - curriculum_coeff_1) * default_d_gain_factor
        self.extrinsic_d_gain_factor[env_randomization_mask] = torch.rand((nr_randomized_envs, self.nr_joints), device=self.sim.device) * (d_gain_factor_max - d_gain_factor_min) + d_gain_factor_min
        
        p_law_position_offset_min = curriculum_coeff_1 * self.p_law_position_offset_min
        p_law_position_offset_max = curriculum_coeff_1 * self.p_law_position_offset_max
        self.extrinsic_position_offset[env_randomization_mask] = torch.rand((nr_randomized_envs, self.nr_joints), device=self.sim.device) * (p_law_position_offset_max - p_law_position_offset_min) + p_law_position_offset_min

        # Model
        env_randomization_indices = torch.nonzero(env_randomization_mask).flatten()
        middle_static_friction = (self.static_friction_min + self.static_friction_max) / 2.0
        static_friction_min = curriculum_coeff_1 * self.static_friction_min + (1.0 - curriculum_coeff_1) * middle_static_friction
        static_friction_max = curriculum_coeff_1 * self.static_friction_max + (1.0 - curriculum_coeff_1) * middle_static_friction
        middle_dynamic_friction = (self.dynamic_friction_min + self.dynamic_friction_max) / 2.0
        dynamic_friction_min = curriculum_coeff_1 * self.dynamic_friction_min + (1.0 - curriculum_coeff_1) * middle_dynamic_friction
        dynamic_friction_max = curriculum_coeff_1 * self.dynamic_friction_max + (1.0 - curriculum_coeff_1) * middle_dynamic_friction
        middle_restitution = (self.restitution_min + self.restitution_max) / 2.0
        restitution_min = curriculum_coeff_1 * self.restitution_min + (1.0 - curriculum_coeff_1) * middle_restitution
        restitution_max = curriculum_coeff_1 * self.restitution_max + (1.0 - curriculum_coeff_1) * middle_restitution
        self.randomize_rigid_body_material(self, env_randomization_indices, (static_friction_min, static_friction_max), (dynamic_friction_min, dynamic_friction_max), (restitution_min, restitution_max), 64, self.all_bodies_cfg)
        
        mdp.randomize_rigid_body_mass(self, env_randomization_indices, self.trunk_cfg, (self.added_trunk_mass_min * curriculum_coeff_1_cpu, self.added_trunk_mass_max * curriculum_coeff_1_cpu), "add")
        
        mdp.randomize_physics_scene_gravity(self, env_randomization_indices, (self.added_gravity_min * curriculum_coeff_mean_cpu, self.added_gravity_max * curriculum_coeff_mean_cpu), "add")
        
        middle_joint_friction = (self.joint_friction_min + self.joint_friction_max) / 2.0
        joint_friction_min = curriculum_coeff_1 * self.joint_friction_min + (1.0 - curriculum_coeff_1) * middle_joint_friction
        joint_friction_max = curriculum_coeff_1 * self.joint_friction_max + (1.0 - curriculum_coeff_1) * middle_joint_friction
        
        middle_joint_armature = (self.joint_armature_min + self.joint_armature_max) / 2.0
        joint_armature_min = curriculum_coeff_1 * self.joint_armature_min + (1.0 - curriculum_coeff_1) * middle_joint_armature
        joint_armature_max = curriculum_coeff_1 * self.joint_armature_max + (1.0 - curriculum_coeff_1) * middle_joint_armature
        mdp.randomize_joint_parameters(self, env_randomization_indices, self.all_joints_cfg, (joint_friction_min, joint_friction_max), (joint_armature_min, joint_armature_max), None, None, "abs")

        # Perturbations
        if not all_envs:
            env_perturbation_mask = torch.rand((self.num_envs,), device=self.sim.device) < self.step_sampling_probability
        else:
            env_perturbation_mask = torch.ones((self.num_envs,), device=self.sim.device) < self.step_sampling_probability  # ugly, to avoid linting error
        if self.env_curriculum_eval:
            curriculum_coeff = self.env_curriculum_coeff[env_perturbation_mask] * 0.0 + 1.0
        else:
            curriculum_coeff = self.env_curriculum_coeff[env_perturbation_mask]
        nr_perturbed_envs = env_perturbation_mask.sum()
        perturb_velocity_x_min, perturb_velocity_x_max = self.perturb_velocity_x_min * curriculum_coeff, self.perturb_velocity_x_max * curriculum_coeff
        perturb_velocity_y_min, perturb_velocity_y_max = self.perturb_velocity_y_min * curriculum_coeff, self.perturb_velocity_y_max * curriculum_coeff
        perturb_velocity_z_min, perturb_velocity_z_max = self.perturb_velocity_z_min * curriculum_coeff, self.perturb_velocity_z_max * curriculum_coeff
        perturb_velocity_x = torch.rand((nr_perturbed_envs,), device=self.sim.device) * (perturb_velocity_x_max - perturb_velocity_x_min) + perturb_velocity_x_min
        perturb_velocity_y = torch.rand((nr_perturbed_envs,), device=self.sim.device) * (perturb_velocity_y_max - perturb_velocity_y_min) + perturb_velocity_y_min
        perturb_velocity_z = torch.rand((nr_perturbed_envs,), device=self.sim.device) * (perturb_velocity_z_max - perturb_velocity_z_min) + perturb_velocity_z_min
        current_global_velocity = self.robot.data.root_state_w[env_perturbation_mask, 7:]
        current_global_velocity[:, 0] = torch.where(torch.rand((nr_perturbed_envs,), device=self.sim.device) < self.perturb_add_chance, perturb_velocity_x + current_global_velocity[:, 0] * self.perturb_additive_multiplier, perturb_velocity_x)
        current_global_velocity[:, 1] = torch.where(torch.rand((nr_perturbed_envs,), device=self.sim.device) < self.perturb_add_chance, perturb_velocity_y + current_global_velocity[:, 1] * self.perturb_additive_multiplier, perturb_velocity_y)
        current_global_velocity[:, 2] = torch.where(torch.rand((nr_perturbed_envs,), device=self.sim.device) < self.perturb_add_chance, perturb_velocity_z + current_global_velocity[:, 2] * self.perturb_additive_multiplier, perturb_velocity_z)
        env_perturbed_indices = torch.nonzero(env_perturbation_mask).flatten()
        self.robot.write_root_velocity_to_sim(current_global_velocity, env_perturbed_indices)


    def _get_dones(self) -> tuple[torch.Tensor, torch.Tensor]:
        self.handle_domain_randomization()

        all_contact_sensor = self.scene.sensors[self.all_contact_cfg.name]
        contact_for_termination = torch.any(torch.norm(all_contact_sensor.data.net_forces_w[:, self.all_body_ids_for_contact_termination], dim=-1) > 1.0, dim=1)
        trunk_too_low = self.robot.data.root_state_w[:, 2] < self.nominal_trunk_z * self.trunk_too_low_percentage
        terminated = contact_for_termination | trunk_too_low

        truncated = self.episode_length_buf >= self.max_episode_length
        self.last_episode_length = self.episode_length_buf.clone()

        return terminated, truncated


    def _get_rewards(self) -> torch.Tensor:
        if self.env_curriculum_eval:
            curriculum_coeff = self.env_curriculum_coeff * 0.0 + 1.0
        else:
            curriculum_coeff = self.env_curriculum_coeff


        feet_contact_sensors = self.scene.sensors[self.feet_contact_cfg.name]
        feet_contacts = torch.norm(feet_contact_sensors.data.net_forces_w[:, self.feet_contact_cfg.body_ids], dim=-1) > 1.0
        feet_forces_norm = torch.norm(feet_contact_sensors.data.net_forces_w[:, self.feet_contact_cfg.body_ids], dim=-1)

        feet_indices, _ = self.robot.find_bodies(self.feet_contact_cfg.body_names, True)
        global_feet_pos = self.robot.data.body_pos_w[:, feet_indices]
        local_feet_pos = math_utils.quat_rotate_inverse(self.robot.data.root_quat_w[:, None, :], global_feet_pos - self.robot.data.root_state_w[:, None, :3])

        undesired_contacts = self.get_undesired_contacts(self.undesired_contact_cfg, threshold=1.0)

        reward, extras, extras_detailed = compute_rewards(
            curriculum_coeff,
            self.tracking_xy_velocity_command_coeff,
            self.tracking_yaw_velocity_command_coeff,
            self.z_velocity_coeff,
            self.pitch_roll_vel_coeff,
            self.pitch_roll_pos_coeff,
            self.actuator_joint_nominal_diff_coeff,
            self.actuator_joint_nominal_diff_joints,
            self.joint_position_limit_coeff,
            self.joint_velocity_limit_coeff,
            self.soft_joint_velocity_limit,
            self.joint_acceleration_coeff,
            self.joint_torque_coeff,
            self.action_rate_coeff,
            self.action_smoothness_coeff,
            self.base_height_coeff,
            self.air_time_coeff,
            self.feet_force_coeff,
            self.symmetry_air_coeff,
            self.feet_y_distance_coeff,
            self.stand_still_coeff,
            self.robot.data.root_lin_vel_b,
            self.robot.data.root_ang_vel_b,
            self.robot.data.root_state_w[:, :3],
            self.robot.data.root_state_w[:, 3:7],
            self.robot.data.joint_pos,
            self.robot.data.joint_vel,
            self.joint_max_velocity,
            self.joint_nominal_positions,
            self.robot.data.default_joint_limits[0, :, 0],
            self.robot.data.default_joint_limits[0, :, 1],
            self.actions,
            self.previous_actions,
            self.previous_previous_actions,
            self.robot.data.joint_acc,
            self.torques,
            self.goal_velocities,
            self.nominal_trunk_z,
            feet_contacts,
            feet_forces_norm,
            self.previous_feet_air_times,
            self.feet_symmetry_pairs,
            local_feet_pos,
            self.feet_y_distance_target,
            self.max_command_velocity,
            undesired_contacts
        )

        self.extras = {"log": extras, "log_detailed": extras_detailed}

        self.previous_previous_actions = self.previous_actions.clone()
        self.previous_actions = self.actions.clone()
        self.previous_feet_air_times = feet_contact_sensors.data.current_air_time[:, self.feet_contact_cfg.body_ids].clone()

        # Curriculum
        self.episode_total_xy_velocity_diff_abs += self.extras["log"]["env_info/xy_vel_diff_abs"]

        return reward
    

    def set_observation_indices(self):
        current_observation_idx = 0

        self.joint_positions_obs_idx = [current_observation_idx + i for i in range(self.nr_joints)]
        current_observation_idx += self.nr_joints

        self.joint_velocities_obs_idx = [current_observation_idx + i for i in range(self.nr_joints)]
        current_observation_idx += self.nr_joints

        self.joint_previous_actions_obs_idx = [current_observation_idx + i for i in range(self.nr_joints)]
        current_observation_idx += self.nr_joints

        self.feet_contact_obs_idx = [current_observation_idx + i for i in range(self.nr_feet)]
        current_observation_idx += self.nr_feet

        self.feet_air_time_obs_idx = [current_observation_idx + i for i in range(self.nr_feet)]
        current_observation_idx += self.nr_feet

        self.trunk_linear_velocity_obs_idx = [current_observation_idx + i for i in range(3)]
        current_observation_idx += 3

        self.trunk_angular_velocity_obs_idx = [current_observation_idx + i for i in range(3)]
        current_observation_idx += 3

        self.goal_velocities_obs_idx = [current_observation_idx + i for i in range(3)]
        current_observation_idx += 3

        self.projected_gravity_vector_obs_idx = [current_observation_idx + i for i in range(3)]
        current_observation_idx += 3

        self.height_obs_idx = [current_observation_idx]
        current_observation_idx += 1

    def update_goal_velocities(self):
        """
        Sample some robots and update the target velocities.
        This function should only be called by _get_observations function.
        """
        if not self.target_global_goal:
            should_sample_new_goal_velocities = torch.rand((self.num_envs,), device=self.sim.device) < self.step_sampling_probability
            new_goal_velocities = torch.rand((should_sample_new_goal_velocities.sum(), 3), device=self.sim.device).uniform_(-1.0, 1.0)
            new_goal_velocities = torch.where(torch.abs(new_goal_velocities) < 0.02, 0.0, new_goal_velocities)
            new_goal_velocities = torch.where(torch.rand_like(new_goal_velocities) < 0.05, torch.zeros_like(new_goal_velocities), new_goal_velocities)
            self.goal_velocities[should_sample_new_goal_velocities] = new_goal_velocities
        else:
            orientation_quat = self.robot.data.root_state_w[:, 3:7]
            orientation_euler = quaternion_to_axis_angle(orientation_quat)
            global_heading_angle = orientation_euler[:, 2]
            self.goal_velocities[:, 2] = torch.clamp(-global_heading_angle, -self.max_command_velocity, self.max_command_velocity)
            self.goal_velocities[:, 1] = torch.clamp(self.starting_y_position - self.robot.data.root_state_w[:, 1], -self.max_command_velocity, self.max_command_velocity)
        return self.goal_velocities

    def _get_observations(self) -> dict:
        # Joint-specific observations
        joint_positions = self.robot.data.joint_pos - self.joint_nominal_positions
        joint_velocities = self.robot.data.joint_vel
        joint_previous_actions = self.actions

        # Feet-specific observations
        feet_contact_sensors = self.scene.sensors[self.feet_contact_cfg.name]
        feet_contacts = (torch.norm(feet_contact_sensors.data.net_forces_w[:, self.feet_contact_cfg.body_ids], dim=-1) > 1.0).float()
        feet_air_times = feet_contact_sensors.data.current_air_time[:, self.feet_contact_cfg.body_ids]

        # General observations
        trunk_linear_velocity = self.robot.data.root_lin_vel_b
        trunk_angular_velocity = self.robot.data.root_ang_vel_b

        goal_velocities = self.update_goal_velocities()

        projected_gravity_vector = self.robot.data.projected_gravity_b
        height = self.robot.data.root_state_w[:, [2]]

        observation = torch.cat(
            [
                joint_positions,
                joint_velocities,
                joint_previous_actions,
                feet_contacts,
                feet_air_times,
                trunk_linear_velocity,
                trunk_angular_velocity,
                goal_velocities,
                projected_gravity_vector,
                height,
            ],
            dim=1,
        )
        
        # Add noise
        if self.env_curriculum_eval:
            curriculum_coeff = self.env_curriculum_coeff * 0.0 + 1.0
        else:
            curriculum_coeff = self.env_curriculum_coeff
        curriculum_coeff_1 = curriculum_coeff.reshape(-1, 1)

        observation[:, self.joint_positions_obs_idx] += ((torch.rand_like(observation[:, self.joint_positions_obs_idx]) * 2) - 1) * self.joint_position_noise * curriculum_coeff_1
        observation[:, self.joint_velocities_obs_idx] += ((torch.rand_like(observation[:, self.joint_velocities_obs_idx]) * 2) - 1) * self.joint_velocity_noise * curriculum_coeff_1
        observation[:, self.trunk_angular_velocity_obs_idx] += ((torch.rand_like(observation[:, self.trunk_angular_velocity_obs_idx]) * 2) - 1) * self.trunk_angular_velocity_noise * curriculum_coeff_1
        observation[:, self.projected_gravity_vector_obs_idx] += ((torch.rand_like(observation[:, self.projected_gravity_vector_obs_idx]) * 2) - 1) * self.gravity_vector_noise * curriculum_coeff_1
        observation[:, self.feet_contact_obs_idx] = torch.where(torch.rand_like(observation[:, self.feet_contact_obs_idx]) < self.ground_contact_noise_chance * curriculum_coeff_1, 1.0 - observation[:, self.feet_contact_obs_idx], observation[:, self.feet_contact_obs_idx])
        observation[:, self.feet_air_time_obs_idx] = torch.where(torch.rand_like(observation[:, self.feet_air_time_obs_idx]) < self.contact_time_noise_chance * curriculum_coeff_1, observation[:, self.feet_air_time_obs_idx] + (((torch.rand_like(observation[:, self.feet_air_time_obs_idx]) * 2) - 1.0) * self.contact_time_noise_factor * curriculum_coeff_1 * self.action_dt), observation[:, self.feet_air_time_obs_idx])

        # Dropout
        joint_dropout_mask = torch.rand((self.num_envs, self.nr_joints), device=self.sim.device) < self.joint_and_feet_dropout_chance * curriculum_coeff_1
        feet_dropout_mask = torch.rand((self.num_envs, self.nr_feet), device=self.sim.device) < self.joint_and_feet_dropout_chance * curriculum_coeff_1
        observation[:, self.joint_positions_obs_idx][joint_dropout_mask] = 0.0
        observation[:, self.joint_velocities_obs_idx][joint_dropout_mask] = 0.0
        observation[:, self.joint_previous_actions_obs_idx][joint_dropout_mask] = 0.0
        observation[:, self.feet_contact_obs_idx][feet_dropout_mask] = 0.0
        observation[:, self.feet_air_time_obs_idx][feet_dropout_mask] = 0.0

        # Normalize & Clip
        observation[:, self.joint_positions_obs_idx] /= 4.6
        observation[:, self.joint_velocities_obs_idx] /= 35.0
        observation[:, self.joint_previous_actions_obs_idx] /= 10.0
        observation[:, self.feet_contact_obs_idx] = (observation[:, self.feet_contact_obs_idx] / 0.5) - 1.0
        observation[:, self.feet_air_time_obs_idx] = torch.clamp((observation[:, self.feet_air_time_obs_idx] / (5.0 / 2)) - 1.0, -1.0, 1.0)
        observation[:, self.trunk_linear_velocity_obs_idx] = torch.clamp(observation[:, self.trunk_linear_velocity_obs_idx] / 10.0, -1.0, 1.0)
        observation[:, self.trunk_angular_velocity_obs_idx] = torch.clamp(observation[:, self.trunk_angular_velocity_obs_idx] / 50.0, -1.0, 1.0)
        observation[:, self.height_obs_idx] = torch.clamp((observation[:, self.height_obs_idx] / 1.0) - 1.0, -1.0, 1.0)

        policy_observation = observation[:,
            self.joint_positions_obs_idx + \
            self.joint_velocities_obs_idx + \
            self.joint_previous_actions_obs_idx + \
            self.trunk_angular_velocity_obs_idx + \
            self.goal_velocities_obs_idx + \
            self.projected_gravity_vector_obs_idx
        ]

        if self.urma_initialized:
            urma_obs = self._get_urma_observations(observation)
            return {"policy": policy_observation, "critic": observation, "urma_obs": urma_obs}

        return {"policy": policy_observation, "critic": observation}


    def _initialize_urma_observations(self):
        # Dynamic observations
        dynamic_joint_observations = torch.empty((self.num_envs, 0), device=self.sim.device)
        for i, joint_name in enumerate(self.joint_names):
            desc_vector = self.name_to_description_vector[joint_name]
            joint_pos_rel = torch.zeros((self.num_envs, 1), device=self.sim.device)
            joint_vel_rel = torch.zeros((self.num_envs, 1), device=self.sim.device)
            action = torch.zeros((self.num_envs, 1), device=self.sim.device)
            current_observation = torch.cat((desc_vector, joint_pos_rel, joint_vel_rel, action), dim=1)
            dynamic_joint_observations = torch.cat((dynamic_joint_observations, current_observation), dim=1)

        # General observations
        trunk_angular_velocity = torch.zeros((self.num_envs, 3), device=self.sim.device)
        goal_velocity = torch.zeros((self.num_envs, 3), device=self.sim.device)
        projected_gravity_vector = torch.zeros((self.num_envs, 3), device=self.sim.device)

        # General robot context
        gains_and_action_scaling_factor = ((self.gains_and_action_scaling_factor / torch.tensor(
            [100.0 / 2, 2.0 / 2, 0.8 / 2], device=self.sim.device)) - 1.0).repeat((self.num_envs, 1))
        mass = (self.mass / (170.0 / 2)) - 1.0
        robot_dimensions = ((self.robot_dimensions / (2.0 / 2)) - 1.0)
        nr_joints = torch.tensor([(self.nr_joints / (30 / 2)) - 1.0], device=self.sim.device).repeat((self.num_envs, 1))

        # compute foot size
        foot_info = self.robot_description_vec_json['foot_info']
        random_foot_bbox = next(iter(foot_info.values()))['bbox']
        foot_size = (torch.tensor(random_foot_bbox[0]) - torch.tensor(random_foot_bbox[1])).abs()
        foot_size = ((foot_size / (0.5 / 2)) - 1).to(self.sim.device).repeat((self.num_envs, 1))     # assuming 0.5 is the max

        observation = torch.cat([
            dynamic_joint_observations,
            trunk_angular_velocity,
            goal_velocity,
            projected_gravity_vector,
            gains_and_action_scaling_factor,
            mass,
            robot_dimensions,
            nr_joints,
            foot_size
        ], dim=1)

        return observation

    def _get_urma_observations(self, expert_observation: torch.Tensor) -> torch.Tensor:
        """
        Returns the observations for the URMA.
        """
        urma_obs = self.initial_observation.clone()

        # Update observations every step
        urma_obs[:, self.joint_positions_update_obs_idx] = expert_observation[:, self.joint_positions_obs_idx]
        urma_obs[:, self.joint_velocities_update_obs_idx] = expert_observation[:, self.joint_velocities_obs_idx]
        urma_obs[:, self.joint_previous_actions_update_obs_idx] = expert_observation[:, self.joint_previous_actions_obs_idx]
        urma_obs[:, self.trunk_angular_vel_update_obs_idx] = expert_observation[:, self.trunk_angular_velocity_obs_idx]
        urma_obs[:, self.goal_velocity_update_obs_idx] = expert_observation[:, self.goal_velocities_obs_idx]
        urma_obs[:, self.projected_gravity_update_obs_idx] = expert_observation[:, self.projected_gravity_vector_obs_idx]

        return urma_obs


### JIT compiled helper functions ###
@torch.jit.script
def quaternion_to_axis_angle(quaternions: torch.Tensor) -> torch.Tensor:
    # From: https://github.com/facebookresearch/pytorch3d/blob/main/pytorch3d/transforms/rotation_conversions.py#L530

    norms = torch.norm(quaternions[..., 1:], p=2, dim=-1, keepdim=True)
    half_angles = torch.atan2(norms, quaternions[..., :1])
    angles = 2 * half_angles
    eps = 1e-6
    small_angles = angles.abs() < eps
    sin_half_angles_over_angles = torch.empty_like(angles)
    sin_half_angles_over_angles[~small_angles] = (
        torch.sin(half_angles[~small_angles]) / angles[~small_angles]
    )
    # for x small, sin(x/2) is about x/2 - (x/2)^3/6
    # so sin(x/2)/x is about 1/2 - (x*x)/48
    sin_half_angles_over_angles[small_angles] = (
        0.5 - (angles[small_angles] * angles[small_angles]) / 48
    )

    return quaternions[..., 1:] / sin_half_angles_over_angles


@torch.jit.script
def axis_angle_to_quaternion(axis_angle: torch.Tensor) -> torch.Tensor:
    # From: https://github.com/facebookresearch/pytorch3d/blob/main/pytorch3d/transforms/rotation_conversions.py#L498

    angles = torch.norm(axis_angle, p=2, dim=-1, keepdim=True)
    half_angles = angles * 0.5
    eps = 1e-6
    small_angles = angles.abs() < eps
    sin_half_angles_over_angles = torch.empty_like(angles)
    sin_half_angles_over_angles[~small_angles] = (
        torch.sin(half_angles[~small_angles]) / angles[~small_angles]
    )
    # for x small, sin(x/2) is about x/2 - (x/2)^3/6
    # so sin(x/2)/x is about 1/2 - (x*x)/48
    sin_half_angles_over_angles[small_angles] = (
        0.5 - (angles[small_angles] * angles[small_angles]) / 48
    )
    quaternions = torch.cat(
        [torch.cos(half_angles), axis_angle * sin_half_angles_over_angles], dim=-1
    )
    return quaternions


@torch.jit.script
def compute_rewards(
    curriculum_coeff: torch.Tensor,
    tracking_xy_velocity_command_coeff: float,
    tracking_yaw_velocity_command_coeff: float,
    z_velocity_coeff: float,
    pitch_roll_vel_coeff: float,
    pitch_roll_pos_coeff: float,
    actuator_joint_nominal_diff_coeff: float,
    actuator_joint_nominal_diff_joints: list[int],
    joint_position_limit_coeff: float,
    joint_velocity_limit_coeff: float,
    soft_joint_velocity_limit: float,
    joint_acceleration_coeff: float,
    joint_torque_coeff: float,
    action_rate_coeff: float,
    action_smoothness_coeff: float,
    base_height_coeff: float,
    air_time_coeff: float,
    feet_force_coeff: float,
    symmetry_air_coeff: float,
    feet_y_distance_coeff: float,
    stand_still_coeff: float,
    current_local_linear_velocity: torch.Tensor,
    current_local_angular_velocity: torch.Tensor,
    linear_position: torch.Tensor,
    orientation_quat: torch.Tensor,
    joint_positions: torch.Tensor,
    joint_velocities: torch.Tensor,
    joint_max_velocity: torch.Tensor,
    joint_nominal_positions: torch.Tensor,
    joint_position_soft_lower_limits: torch.Tensor,
    joint_position_soft_upper_limits: torch.Tensor,
    actions: torch.Tensor,
    previous_actions: torch.Tensor,
    previous_previous_actions: torch.Tensor,
    joint_accelerations: torch.Tensor,
    joint_torques: torch.Tensor,
    goal_velocities: torch.Tensor,
    nominal_trunk_z: float,
    feet_contacts: torch.Tensor,
    feet_forces: torch.Tensor,
    feet_air_times: torch.Tensor,
    feet_symmetry_pairs: torch.Tensor,
    local_feet_pos: torch.Tensor,
    feet_y_distance_target: float,
    max_command_velocity: float,
    undesired_contacts: torch.Tensor
) -> tuple[torch.Tensor, dict[str, torch.Tensor], dict[str, torch.Tensor]]:
    
    # Tracking xy velocity command reward
    current_local_linear_velocity_xy = current_local_linear_velocity[:, :2]
    desired_local_linear_velocity_xy = goal_velocities[:, :2]
    xy_difference = desired_local_linear_velocity_xy - current_local_linear_velocity_xy
    xy_velocity_difference_norm = torch.sum(torch.square(xy_difference), dim=1)
    tracking_xy_velocity_command_reward = tracking_xy_velocity_command_coeff * torch.exp(-xy_velocity_difference_norm / 0.25)

    # Tracking angular velocity command reward
    current_local_yaw_velocity = current_local_angular_velocity[:, 2]
    desired_local_yaw_velocity = goal_velocities[:, 2]
    yaw_velocity_difference_norm = torch.square(current_local_yaw_velocity - desired_local_yaw_velocity)
    tracking_yaw_velocity_command_reward = tracking_yaw_velocity_command_coeff * torch.exp(-yaw_velocity_difference_norm / 0.25)

    # Linear velocity reward
    z_velocity_squared = torch.square(current_local_linear_velocity[:, 2])
    linear_velocity_reward = curriculum_coeff * z_velocity_coeff * -z_velocity_squared

    # Angular velocity reward
    angular_velocity_norm = torch.sum(torch.square(current_local_angular_velocity[:, :2]), dim=1)
    angular_velocity_reward = curriculum_coeff * pitch_roll_vel_coeff * -angular_velocity_norm

    # Angular position reward
    orientation_euler = quaternion_to_axis_angle(orientation_quat)
    pitch_roll_position_norm = torch.sum(torch.square(orientation_euler[:, :2]), dim=1)
    angular_position_reward = curriculum_coeff * pitch_roll_pos_coeff * -pitch_roll_position_norm

    # Joint nominal position difference reward
    actuator_joint_nominal_diff_norm = torch.square(
        joint_positions[:, actuator_joint_nominal_diff_joints] - joint_nominal_positions[:, actuator_joint_nominal_diff_joints]
    ).mean(dim=1)
    actuator_joint_nominal_diff_reward = curriculum_coeff * actuator_joint_nominal_diff_coeff * -actuator_joint_nominal_diff_norm

    # Joint position limit reward
    lower_limit_penalty = -torch.minimum(joint_positions - joint_position_soft_lower_limits, torch.tensor(0.0, device=joint_positions.device)).mean(dim=1)
    upper_limit_penalty = torch.maximum(joint_positions - joint_position_soft_upper_limits, torch.tensor(0.0, device=joint_positions.device)).mean(dim=1)
    joint_position_limit_reward = curriculum_coeff * joint_position_limit_coeff * -(lower_limit_penalty + upper_limit_penalty)

    # Joint velocity limit reward
    joint_abs_velocities = torch.abs(joint_velocities)
    soft_joint_velocites_limit = joint_max_velocity * soft_joint_velocity_limit
    joint_velocity_limit_penalty = torch.maximum(joint_abs_velocities - soft_joint_velocites_limit, torch.tensor(0.0, device=joint_velocities.device)).mean(dim=1)
    joint_velocity_limit_reward = curriculum_coeff * joint_velocity_limit_coeff * -joint_velocity_limit_penalty

    # Joint acceleration reward
    acceleration_norm = torch.mean(torch.square(joint_accelerations), dim=1)
    acceleration_reward = curriculum_coeff * joint_acceleration_coeff * -acceleration_norm

    # Joint torque reward
    torque_norm = torch.mean(torch.square(joint_torques), dim=1)
    torque_reward = curriculum_coeff * joint_torque_coeff * -torque_norm

    # Action rate reward
    action_rate_norm = torch.mean(torch.square(actions - previous_actions), dim=1)
    action_rate_reward = curriculum_coeff * action_rate_coeff * -action_rate_norm

    # Action smoothness reward
    action_smoothness_norm = torch.mean(torch.square(actions - 2 * previous_actions + previous_previous_actions), dim=1)
    action_smoothness_reward = curriculum_coeff * action_smoothness_coeff * -action_smoothness_norm

    # Walking height reward
    trunk_z = linear_position[:, 2]
    height_difference_squared = (trunk_z - nominal_trunk_z) ** 2
    base_height_reward = curriculum_coeff * base_height_coeff * -height_difference_squared

    # Air time reward
    is_standing_command = torch.all(goal_velocities == 0.0, dim=1)
    air_time_reward = torch.sum(feet_contacts.float() * (feet_air_times - 0.5), dim=1)
    air_time_reward *= ~is_standing_command
    air_time_reward = curriculum_coeff * air_time_coeff * air_time_reward

    # Symmetry air reward
    symmetry_air_violations = torch.sum(~feet_contacts[:, feet_symmetry_pairs[:, 0]] & ~feet_contacts[:, feet_symmetry_pairs[:, 1]], dim=1)
    symmetry_air_reward = curriculum_coeff * symmetry_air_coeff * -symmetry_air_violations

    # Feet-ground contact forces reward
    force_norm_mean = torch.mean(feet_forces, dim=1)
    feet_force_reward = -force_norm_mean * feet_force_coeff * curriculum_coeff

    # Feet y distance reward
    feet_y_distance = torch.abs(local_feet_pos[:, feet_symmetry_pairs[:, 0], 1] - local_feet_pos[:, feet_symmetry_pairs[:, 1], 1]).mean(dim=1)
    feet_y_distance_from_target_norm = (feet_y_distance - feet_y_distance_target) ** 2
    feet_y_distance_reward = curriculum_coeff * feet_y_distance_coeff * -feet_y_distance_from_target_norm

    # Stand still reward
    stand_still_position_diff_norm = is_standing_command * torch.mean(torch.square(joint_positions - joint_nominal_positions), dim=1)
    stand_still_reward = curriculum_coeff * stand_still_coeff * -stand_still_position_diff_norm

    # undesired contact
    undesired_contact_reward = curriculum_coeff * 1.0 * -undesired_contacts.sum(dim=1)

    # Total reward
    tracking_reward = tracking_xy_velocity_command_reward + tracking_yaw_velocity_command_reward
    reward_penalty = (linear_velocity_reward + angular_velocity_reward + angular_position_reward + actuator_joint_nominal_diff_reward + \
                     joint_position_limit_reward + joint_velocity_limit_reward + acceleration_reward + torque_reward + \
                     action_rate_reward + action_smoothness_reward + \
                     base_height_reward + air_time_reward + symmetry_air_reward + feet_y_distance_reward + stand_still_reward)

    reward = tracking_reward + reward_penalty
    reward = torch.maximum(reward, torch.tensor(0.0, device=reward.device))

    extras_detailed = {
        "reward/track_xy_vel_cmd": tracking_xy_velocity_command_reward,
        "reward/track_yaw_vel_cmd": tracking_yaw_velocity_command_reward,
        "reward/linear_velocity": linear_velocity_reward,
        "reward/angular_velocity": angular_velocity_reward,
        "reward/angular_position": angular_position_reward,
        "reward/joint_nominal_diff": actuator_joint_nominal_diff_reward,
        "reward/joint_position_limit": joint_position_limit_reward,
        "reward/joint_velocity_limit": joint_velocity_limit_reward,
        "reward/joint_acceleration": acceleration_reward,
        "reward/joint_torque": torque_reward,
        "reward/action_rate": action_rate_reward,
        "reward/action_smoothness": action_smoothness_reward,
        "reward/base_height": base_height_reward,
        "reward/air_time": air_time_reward,
        "reward/feet_force": feet_force_reward,
        "reward/symmetry_air": symmetry_air_reward,
        "reward/feet_y_distance": feet_y_distance_reward,
        "reward/stand_still": stand_still_reward,
        "reward/undesired_contact": undesired_contact_reward,
        "reward_info/xy_velocity_difference_norm": xy_velocity_difference_norm,
        "reward_info/yaw_velocity_difference_norm": yaw_velocity_difference_norm,
        "reward_info/z_velocity_squared": z_velocity_squared,
        "reward_info/angular_velocity_norm": angular_velocity_norm,
        "reward_info/pitch_roll_position_norm": pitch_roll_position_norm,
        "reward_info/actuator_joint_nominal_diff_norm": actuator_joint_nominal_diff_norm,
        "reward_info/joint_position_limit_penalty": lower_limit_penalty + upper_limit_penalty,
        "reward_info/joint_velocity_limit_penalty": joint_velocity_limit_penalty,
        "reward_info/acceleration_norm": acceleration_norm,
        "reward_info/torque_norm": torque_norm,
        "reward_info/action_rate_norm": action_rate_norm,
        "reward_info/action_smoothness_norm": action_smoothness_norm,
        "reward_info/height_difference_squared": height_difference_squared,
        "reward_info/feet_y_distance_from_target_norm": feet_y_distance_from_target_norm,
        "reward_info/feet_force_norm_mean": force_norm_mean,
        "reward_info/stand_still_position_diff_norm": stand_still_position_diff_norm,
        "reward_info/undesired_contacts": undesired_contacts,
        "env_info/xy_vel_diff_abs": torch.mean(torch.minimum(torch.abs(xy_difference), torch.tensor(2 * max_command_velocity, device=xy_difference.device)), dim=1),
        "env_info/curriculum_coeff": curriculum_coeff,
    }

    return reward, {k: v.mean() for k, v in extras_detailed.items()}, extras_detailed
