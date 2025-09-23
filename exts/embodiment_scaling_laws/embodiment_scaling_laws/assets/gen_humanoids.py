import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ActuatorNetMLPCfg, DCMotorCfg, ImplicitActuatorCfg
from omni.isaac.lab.assets.articulation import ArticulationCfg
from omni.isaac.lab.utils.assets import ISAACLAB_NUCLEUS_DIR

from embodiment_scaling_laws.assets import ISAAC_ASSET_DIR


activate_contact_sensors = True
rigid_props = sim_utils.RigidBodyPropertiesCfg(
    disable_gravity=False,
    retain_accelerations=False,
    linear_damping=0.0,
    angular_damping=0.0,
    max_linear_velocity=1000.0,
    max_angular_velocity=1000.0,
    max_depenetration_velocity=1.0,
)
articulation_props = sim_utils.ArticulationRootPropertiesCfg(
    enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=4 # note the value 4 not 0
)
soft_joint_pos_limit_factor = 0.9
prim_path = "/World/envs/env_.*/Robot"

"""
The above is shared across all humanoids, but below we have two types of actuators
"""

actuators_without_knee = {
    "all": DCMotorCfg(
        joint_names_expr=[
            '.*_hip_yaw_joint', '.*_hip_roll_joint', '.*_hip_pitch_joint', 'torso_joint',
            '.*_ankle_joint',
            '.*_shoulder.*joint', '.*_elbow_joint',
        ],
        effort_limit={
            '.*_hip_yaw_joint': 200,
            '.*_hip_roll_joint': 200,
            '.*_hip_pitch_joint': 200,
            'torso_joint': 200,
            '.*_ankle_joint': 40,
            '.*_shoulder.*joint': 40,
            '.*_elbow_joint': 18,
        },
        saturation_effort={
            '.*_hip_yaw_joint': 200,
            '.*_hip_roll_joint': 200,
            '.*_hip_pitch_joint': 200,
            'torso_joint': 200,
            '.*_ankle_joint': 40,
            '.*_shoulder.*joint': 40,
            '.*_elbow_joint': 18,
        },
        velocity_limit={
            '.*_hip_yaw_joint': 23,
            '.*_hip_roll_joint': 23,
            '.*_hip_pitch_joint': 23,
            'torso_joint': 23,
            '.*_ankle_joint': 9,
            '.*_shoulder.*joint': 9,
            '.*_elbow_joint': 20,
        },
        stiffness=60.0,
        damping=2.0,
        armature=0.01,
    ),
}

actuators_with_knee = {
    "all": DCMotorCfg(
        joint_names_expr=[
            '.*_hip_yaw_joint', '.*_hip_roll_joint', '.*_hip_pitch_joint', '.*_knee.*joint', 'torso_joint',
            '.*_ankle_joint',
            '.*_shoulder.*joint', '.*_elbow_joint',
        ],
        effort_limit={
            '.*_hip_yaw_joint': 200,
            '.*_hip_roll_joint': 200,
            '.*_hip_pitch_joint': 200,
            '.*_knee.*joint': 300,
            'torso_joint': 200,
            '.*_ankle_joint': 40,
            '.*_shoulder_pitch_joint': 40,
            '.*_shoulder_roll_joint': 40,
            '.*_shoulder_yaw_joint': 18,
            '.*_elbow_joint': 18,
        },
        saturation_effort={
            '.*_hip_yaw_joint': 200,
            '.*_hip_roll_joint': 200,
            '.*_hip_pitch_joint': 200,
            '.*_knee.*joint': 300,
            'torso_joint': 200,
            '.*_ankle_joint': 40,
            '.*_shoulder_pitch_joint': 40,
            '.*_shoulder_roll_joint': 40,
            '.*_shoulder_yaw_joint': 18,
            '.*_elbow_joint': 18,
        },
        velocity_limit={
            '.*_hip_yaw_joint': 23,
            '.*_hip_roll_joint': 23,
            '.*_hip_pitch_joint': 23,
            '.*_knee.*joint': 14,
            'torso_joint': 23,
            '.*_ankle_joint': 9,
            '.*_shoulder_pitch_joint': 9,
            '.*_shoulder_roll_joint': 9,
            '.*_shoulder_yaw_joint': 9,
            '.*_elbow_joint': 20,
        },
        stiffness=60.0,
        damping=2.0,
        armature=0.01,
    ),
}

"""
Customized Cfgs
"""


GEN_HUMANOID_0_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_0_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.73420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_100_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_100_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_101_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_101_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_102_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_102_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_103_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_103_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_104_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_104_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_105_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_105_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_106_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_106_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_107_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_107_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.28105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_108_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_108_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_109_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_109_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.26042),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_10_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_10_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.73420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_110_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_110_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.88168),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_111_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_111_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_112_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_112_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_113_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_113_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_114_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_114_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_115_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_115_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_116_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_116_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_117_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_117_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_118_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_118_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_119_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_119_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_11_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_11_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_120_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_120_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_121_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_121_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_122_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_122_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_123_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_123_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.28105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_124_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_124_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_125_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_125_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.48147),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_126_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_126_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.02905),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_127_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_127_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_128_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_128_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_129_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_129_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_12_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_12_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_130_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_130_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_131_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_131_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_132_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_132_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_133_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_133_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_134_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_134_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_135_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_135_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_136_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_136_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_137_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_137_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_138_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_138_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_139_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_139_KneeNum_l2_r2__ScaleJointLimit_l0_r0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.46526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_13_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_13_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.26042),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_140_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_140_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_141_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_141_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.48147),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_142_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_142_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.02905),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_143_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_143_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_144_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_144_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_145_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_145_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_146_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_146_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_147_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_147_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_148_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_148_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_149_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_149_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_14_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_14_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.88168),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_150_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_150_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_151_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_151_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_152_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_152_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_153_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_153_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_154_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_154_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_155_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_155_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.46526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_156_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_156_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_157_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_157_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.48147),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_158_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_158_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.02905),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_159_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_159_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_15_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_15_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_160_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_160_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_161_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_161_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_162_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_162_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_163_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_163_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_164_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_164_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_165_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_165_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_166_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_166_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_167_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_167_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_168_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_168_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_169_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_169_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_16_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_16_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_170_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_170_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_171_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_171_KneeNum_l2_r2__ScaleJointLimit_l1_r0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.46526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_172_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_172_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_173_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_173_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.48147),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_174_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_174_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.02905),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_175_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_175_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_176_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_176_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_177_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_177_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_178_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_178_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_179_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_179_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_17_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_17_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_180_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_180_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_181_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_181_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_182_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_182_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_183_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_183_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_184_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_184_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_185_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_185_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_186_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_186_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_187_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_187_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.46526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_188_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_188_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_189_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_189_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.48147),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_18_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_18_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_190_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_190_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.02905),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_191_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_191_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_192_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_192_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_193_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_193_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_194_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_194_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_195_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_195_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_196_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_196_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_197_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_197_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_198_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_198_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_199_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_199_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_19_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_19_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_1_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_1_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.85620),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_200_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_200_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_201_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_201_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_202_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_202_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_203_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_203_KneeNum_l2_r2__ScaleJointLimit_l1_r1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.46526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_204_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_204_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_205_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_205_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.48147),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_206_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_206_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.02905),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_207_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_207_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_208_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_208_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_209_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_209_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_20_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_20_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_210_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_210_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_211_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_211_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_212_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_212_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_213_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_213_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_214_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_214_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_215_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_215_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_216_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_216_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_217_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_217_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_218_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_218_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_219_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_219_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.46526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_21_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_21_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_220_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_220_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_221_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_221_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.48147),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_222_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_222_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.02905),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_223_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_223_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_224_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_224_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_225_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_225_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_226_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_226_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_227_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_227_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.36579),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_228_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_228_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.29210),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_229_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_229_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.21842),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_22_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_22_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_230_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_230_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.14473),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_231_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_231_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_232_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_232_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_233_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_233_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_234_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_234_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.25526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_235_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_235_KneeNum_l2_r2__ScaleJointLimit_l0_r1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.46526),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_236_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_236_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_237_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_237_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.70253),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_238_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_238_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.17642),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_239_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_239_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_23_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_23_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_240_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_240_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_241_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_241_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_242_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_242_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_243_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_243_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_244_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_244_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_245_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_245_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_246_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_246_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_247_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_247_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_248_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_248_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_249_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_249_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_24_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_24_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_250_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_250_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_251_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_251_KneeNum_l3_r3__ScaleJointLimit_l0_r0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.64947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_252_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_252_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_253_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_253_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.70253),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_254_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_254_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.17642),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_255_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_255_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_256_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_256_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_257_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_257_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_258_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_258_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_259_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_259_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_25_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_25_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_260_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_260_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_261_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_261_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_262_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_262_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_263_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_263_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_264_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_264_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_265_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_265_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_266_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_266_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_267_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_267_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.64947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_268_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_268_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_269_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_269_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.70253),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_26_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_26_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_270_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_270_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.17642),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_271_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_271_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_272_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_272_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_273_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_273_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_274_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_274_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_275_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_275_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_276_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_276_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_277_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_277_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_278_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_278_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_279_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_279_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_27_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_27_KneeNum_l1_r1__ScaleJointLimit_l0_r0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.28105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_280_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_280_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_281_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_281_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_282_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_282_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_283_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_283_KneeNum_l3_r3__ScaleJointLimit_l1_r0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.64947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_284_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_284_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_285_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_285_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.70253),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_286_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_286_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.17642),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_287_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_287_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_288_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_288_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_289_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_289_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_28_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_28_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_290_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_290_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_291_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_291_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_292_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_292_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_293_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_293_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_294_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_294_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_295_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_295_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_296_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_296_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_297_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_297_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_298_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_298_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_299_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_299_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.64947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_29_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_29_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.26042),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_2_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.61220),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_300_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_300_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_301_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_301_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.70253),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_302_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_302_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.17642),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_303_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_303_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_304_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_304_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_305_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_305_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_306_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_306_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_307_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_307_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_308_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_308_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_309_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_309_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_30_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_30_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.88168),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_310_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_310_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_311_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_311_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_312_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_312_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_313_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_313_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_314_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_314_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_315_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_315_KneeNum_l3_r3__ScaleJointLimit_l1_r1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.64947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_316_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_316_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_317_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_317_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.70253),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_318_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_318_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.17642),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_319_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_319_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_31_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_31_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_320_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_320_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_321_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_321_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_322_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_322_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_323_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_323_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_324_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_324_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_325_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_325_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_326_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_326_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_327_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_327_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_328_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_328_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_329_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_329_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_32_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_32_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_330_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_330_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_331_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_331_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.64947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_332_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_332_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_333_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_333_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.70253),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_334_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_334_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.17642),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_335_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_335_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_336_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_336_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_337_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_337_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_338_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_338_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_339_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_339_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.55000),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_33_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_33_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_340_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_340_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.47632),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_341_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_341_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.40263),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_342_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_342_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.32895),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_343_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_343_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_344_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_344_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_345_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_345_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_346_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_346_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.43947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_347_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_347_KneeNum_l3_r3__ScaleJointLimit_l0_r1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.64947),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*_knee_joint": 0.80000,
            ".*_knee_.*_joint": 0.00000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_34_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_34_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_35_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_35_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_36_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_36_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_37_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_37_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_38_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_38_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_39_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_39_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_3_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_3_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.85420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_40_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_40_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_41_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_41_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_42_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_42_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_43_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_43_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.28105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_44_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_44_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_45_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_45_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.26042),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_46_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_46_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.88168),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_47_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_47_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_48_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_48_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_49_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_49_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_4_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_4_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.77420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_50_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_50_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_51_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_51_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_52_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_52_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_53_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_53_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_54_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_54_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_55_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_55_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_56_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_56_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_57_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_57_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_58_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_58_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_59_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_59_KneeNum_l1_r1__ScaleJointLimit_l1_r0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.28105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_5_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_5_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.69420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_60_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_60_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_61_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_61_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.26042),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_62_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_62_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.88168),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_63_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_63_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_64_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_64_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_65_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_65_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_66_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_66_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_67_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_67_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_68_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_68_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_69_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_69_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_6_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_6_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.61420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_70_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_70_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_71_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_71_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_72_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_72_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_73_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_73_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_74_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_74_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_75_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_75_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.28105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_76_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_76_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_77_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_77_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.26042),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_78_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_78_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.88168),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_79_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_79_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_7_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_7_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.73420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_80_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_80_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_81_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_81_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_82_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_82_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_83_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_83_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_84_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_84_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_85_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_85_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_86_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_86_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_87_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_87_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_88_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_88_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_89_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_89_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_8_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_8_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.73420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)

GEN_HUMANOID_90_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_90_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_scale_torso_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_91_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_91_KneeNum_l1_r1__ScaleJointLimit_l1_r1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.28105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_92_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_92_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.07105),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_93_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_93_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.26042),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_94_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_94_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.88168),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_95_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_95_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_96_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_96_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.10789),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_97_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_97_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.03421),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_98_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_98_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.96052),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_99_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_99_KneeNum_l1_r1__ScaleJointLimit_l0_r1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18158),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": -0.40000,
            ".*knee.*": 0.80000,
            ".*ankle.*": -0.40000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_with_knee,
    prim_path=prim_path
)

GEN_HUMANOID_9_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_humanoids/genhumanoid_9_KneeNum_l0_r0__ScaleJointLimit_l0_r0_1_0__Geo_scale_torso_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.73420),
        joint_pos={
            ".*torso.*": 0.00000,
            ".*_shoulder_pitch_joint": 0.00000,
            ".*_shoulder_roll_joint": 0.00000,
            ".*_shoulder_yaw_joint": 0.00000,
            ".*elbow.*": 0.00000,
            ".*_hip_yaw_joint": 0.00000,
            ".*_hip_roll_joint": 0.00000,
            ".*_hip_pitch_joint": 0.00000,
            ".*ankle.*": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators_without_knee,
    prim_path=prim_path
)
