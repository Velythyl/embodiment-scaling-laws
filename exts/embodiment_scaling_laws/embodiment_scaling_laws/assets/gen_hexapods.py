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
    enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=4
)
soft_joint_pos_limit_factor = 0.9
prim_path = "/World/envs/env_.*/Robot"

"""
===================================breakline=======================================
The above do not quite differ for different categories of robots, but the below do
"""

init_state_dog = ArticulationCfg.InitialStateCfg(
    pos=(0.0, 0.0, 0.5),
    # joint_pos={".*": 0.0},
    joint_pos={
        ".*_left_hip_pitch_joint": 0.1,
        ".*_right_hip_pitch_joint": -0.1,
        "front_left_thigh_joint": 0.8,
        "front_right_thigh_joint": 0.8,
        "rear_left_thigh_joint": 1.0,
        "rear_right_thigh_joint": 1.0,
        ".*_knee_joint": -1.5,
    },
    # joint_pos={
    #     ".*hip.*joint": 0.0,
    #     ".*knee.*joint": 1.0,
    #     ".*thigh.*joint": -0.3
    # },
    joint_vel={".*": 0.0},
)
actuators = {
    # "base_legs": DCMotorCfg(
    #     joint_names_expr=[".*joint"],
    #     effort_limit=23.5,
    #     saturation_effort=23.5,
    #     velocity_limit=30.0,
    #     stiffness=25.0,
    #     damping=0.5,
    #     friction=0.0,
    # ),
    "all": DCMotorCfg(
        joint_names_expr=[".*joint"],
        effort_limit=23.5,
        saturation_effort=23.5,
        velocity_limit=30.0,
        stiffness=25.0,
        damping=0.5,
        friction=0.0,
    ),
}

"""
GenHexapod
"""


GEN_HEXAPOD_0_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_0_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_100_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_100_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_101_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_101_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_102_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_102_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_103_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_103_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_104_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_104_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_105_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_105_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_106_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_106_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_107_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_107_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_108_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_108_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_109_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_109_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_10_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_10_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_110_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_110_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_111_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_111_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_112_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_112_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_113_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_113_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_114_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_114_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_115_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_115_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_116_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_116_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_117_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_117_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_118_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_118_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_119_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_119_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_11_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_11_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_120_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_120_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_121_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_121_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_122_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_122_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_123_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_123_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_124_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_124_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_125_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_125_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_126_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_126_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_127_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_127_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_128_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_128_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_129_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_129_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_12_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_12_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_130_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_130_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_131_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_131_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_132_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_132_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_133_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_133_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_134_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_134_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_135_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_135_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_136_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_136_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_137_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_137_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_138_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_138_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_139_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_139_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_13_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_13_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_140_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_140_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_141_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_141_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_142_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_142_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_143_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_143_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_144_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_144_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_145_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_145_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_146_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_146_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_147_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_147_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_148_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_148_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_149_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_149_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_14_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_14_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_150_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_150_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_151_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_151_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_152_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_152_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_153_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_153_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_154_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_154_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_155_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_155_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_156_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_156_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_157_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_157_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_158_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_158_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_159_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_159_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_15_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_15_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_160_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_160_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_161_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_161_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_162_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_162_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_163_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_163_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_164_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_164_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_165_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_165_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_166_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_166_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_167_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_167_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_168_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_168_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_169_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_169_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_16_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_16_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_170_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_170_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_171_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_171_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_172_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_172_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_173_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_173_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_174_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_174_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_175_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_175_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_176_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_176_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_177_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_177_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_178_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_178_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_179_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_179_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_17_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_17_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_180_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_180_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_181_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_181_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_182_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_182_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_183_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_183_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_184_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_184_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_185_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_185_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_186_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_186_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_187_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_187_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_188_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_188_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_189_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_189_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_18_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_18_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_190_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_190_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_191_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_191_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_192_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_192_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_193_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_193_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_194_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_194_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_195_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_195_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_196_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_196_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_197_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_197_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_198_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_198_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_199_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_199_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_19_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_19_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_1_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_1_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_200_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_200_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_201_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_201_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_202_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_202_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_203_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_203_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_204_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_204_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_205_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_205_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_206_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_206_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_207_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_207_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_208_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_208_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_209_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_209_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_20_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_20_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_210_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_210_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_211_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_211_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_212_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_212_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.62653),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_213_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_213_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75184),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_214_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_214_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50123),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_215_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_215_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.72030),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_216_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_216_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65779),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_217_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_217_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.59528),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_218_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_218_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53277),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_219_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_219_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.89052),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_21_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_21_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_220_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_220_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_221_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_221_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_222_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_222_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_223_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_223_KneeNum_l1-2_l2-2_l3-2_l4-2_l5-2_l6-2__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.65681),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_224_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_224_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_225_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_225_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_226_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_226_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_227_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_227_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_228_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_228_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_229_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_229_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_22_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_22_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_230_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_230_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_231_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_231_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_232_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_232_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_233_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_233_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_234_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_234_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_235_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_235_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_236_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_236_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_237_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_237_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_238_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_238_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_239_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_239_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_23_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_23_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_240_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_240_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_241_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_241_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_242_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_242_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_243_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_243_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_244_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_244_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_245_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_245_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_246_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_246_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_247_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_247_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_248_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_248_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_249_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_249_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_24_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_24_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_250_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_250_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_251_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_251_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_252_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_252_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_253_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_253_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_254_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_254_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_255_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_255_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_256_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_256_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_257_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_257_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_258_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_258_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_259_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_259_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_25_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_25_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_260_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_260_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_261_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_261_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_262_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_262_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_263_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_263_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_264_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_264_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_265_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_265_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_266_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_266_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_267_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_267_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_268_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_268_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_269_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_269_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_26_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_26_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_270_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_270_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_271_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_271_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_272_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_272_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_273_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_273_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_274_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_274_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_275_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_275_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_276_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_276_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_277_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_277_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_278_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_278_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_279_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_279_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_27_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_27_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_280_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_280_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_281_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_281_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_282_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_282_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_283_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_283_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_284_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_284_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_285_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_285_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_286_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_286_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_287_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_287_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_288_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_288_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_289_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_289_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_28_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_28_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_290_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_290_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_291_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_291_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_292_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_292_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_293_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_293_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_294_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_294_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_295_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_295_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_296_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_296_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_297_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_297_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_298_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_298_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_299_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_299_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_29_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_29_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_2_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_300_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_300_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_301_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_301_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_302_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_302_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_303_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_303_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_304_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_304_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_305_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_305_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_306_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_306_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_307_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_307_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_308_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_308_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_309_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_309_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_30_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_30_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_310_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_310_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_311_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_311_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_312_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_312_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_313_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_313_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_314_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_314_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_315_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_315_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_316_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_316_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_317_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_317_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_318_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_318_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_319_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_319_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_31_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_31_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_320_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_320_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.84652),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_321_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_321_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.01583),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_322_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_322_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.67722),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_323_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_323_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.94029),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_324_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_324_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87778),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_325_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_325_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.81527),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_326_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_326_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.75276),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_327_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_327_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.24251),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_328_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_328_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.97852),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_329_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_329_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71453),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_32_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_32_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_330_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_330_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_331_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_331_KneeNum_l1-3_l2-3_l3-3_l4-3_l5-3_l6-3__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.87680),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_33_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_33_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_34_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_34_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_35_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_35_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_36_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_36_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_37_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_37_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_38_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_38_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_39_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_39_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_3_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_3_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_40_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_40_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_41_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_41_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_42_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_42_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_43_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_43_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-1_l2-0_l3-0_l4-0_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_44_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_44_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_45_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_45_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_46_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_46_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_47_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_47_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_48_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_48_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_49_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_49_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_4_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_4_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_50_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_50_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_51_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_51_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_52_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_52_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_53_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_53_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_54_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_54_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_55_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_55_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_56_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_56_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_57_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_57_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_58_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_58_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_59_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_59_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_5_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_5_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_60_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_60_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_61_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_61_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_62_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_62_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_63_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_63_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_64_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_64_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_65_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_65_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_66_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_66_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_67_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_67_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-1_l4-0_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_68_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_68_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_69_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_69_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_6_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_6_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_70_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_70_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_71_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_71_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_72_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_72_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_73_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_73_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_74_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_74_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_75_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_75_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_76_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_76_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_77_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_77_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_78_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_78_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_79_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_79_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_7_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_7_KneeNum_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_80_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_80_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_81_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_81_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_82_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_82_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_83_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_83_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_84_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_84_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_85_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_85_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_86_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_86_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_87_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_87_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_88_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_88_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45054),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_89_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_89_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_8_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_8_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_90_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_90_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_91_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_91_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-1_l5-0_l6-0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43682),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_92_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_92_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40654),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_93_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_93_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_94_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_94_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32523),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_95_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_95_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50031),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_96_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_96_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.43780),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_97_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_97_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_98_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_98_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40000),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_99_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_99_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.53854),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_HEXAPOD_9_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_hexapods/genhexapod_9_KneeNum_l1-1_l2-1_l3-1_l4-1_l5-1_l6-1__ScaleJointLimit_l1-0_l2-0_l3-0_l4-0_l5-0_l6-0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48785),
        joint_pos={
            ".*_hip_joint": 0.00000,
            ".*_thigh_joint": 0.79000,
            ".*_knee_joint": 0.79000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)
