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
    #     stiffness=20.0,
    #     damping=0.5,
    #     friction=0.0,
    # ),
    "all": DCMotorCfg(
        joint_names_expr=[".*joint"],
        effort_limit=23.5,
        saturation_effort=23.5,
        velocity_limit=30.0,
        stiffness=20.0,
        damping=0.5,
        friction=0.0,
    ),
}

"""
Sanity check: import Go2 here to see if the config makes sense 
"""

# GO2_CFG = ArticulationCfg(
#     spawn=sim_utils.UsdFileCfg(
#         usd_path=f"{ISAAC_ASSET_DIR}/Robots/Unitree/Go2/go2.usd",
#         activate_contact_sensors=activate_contact_sensors,
#         rigid_props=rigid_props,
#         articulation_props=articulation_props,
#     ),
#     init_state=ArticulationCfg.InitialStateCfg(
#         pos=(0.0, 0.0, 0.325),
#         joint_pos={
#             ".*L_hip_joint": 0.1,
#             ".*R_hip_joint": -0.1,
#             "F[L,R]_thigh_joint": 0.8,
#             "R[L,R]_thigh_joint": 1.0,
#             ".*_calf_joint": -1.5,
#         },
#         # joint_pos={".*": 0.0},
#         joint_vel={".*": 0.0},
#     ),
#     soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
#     actuators=actuators,
#     prim_path=prim_path
# )


GEN_DOG_0_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_0_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.32440),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.00000,
            "rear_.*_thigh_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_100_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_100_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_101_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_101_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_102_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_102_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_103_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_103_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_104_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_104_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_105_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_105_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_106_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_106_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_107_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_107_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_108_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_108_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_109_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_109_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_10_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_10_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_110_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_110_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_111_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_111_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_112_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_112_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_113_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_113_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_114_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_114_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_115_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_115_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_116_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_116_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_117_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_117_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_118_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_118_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_119_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_119_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_11_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_11_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_120_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_120_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_121_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_121_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_122_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_122_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_123_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_123_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_124_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_124_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_125_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_125_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_126_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_126_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_127_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_127_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_128_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_128_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_129_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_129_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_12_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_12_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_130_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_130_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_131_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_131_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_132_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_132_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_133_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_133_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_134_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_134_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_135_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_135_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_136_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_136_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_137_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_137_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_138_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_138_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_139_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_139_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_13_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_13_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_140_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_140_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_141_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_141_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_142_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_142_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_143_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_143_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_144_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_144_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_145_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_145_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_146_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_146_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_147_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_147_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_148_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_148_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_149_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_149_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_14_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_14_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_150_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_150_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_151_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_151_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_152_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_152_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_153_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_153_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_154_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_154_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_155_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_155_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_156_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_156_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_157_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_157_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_158_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_158_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_159_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_159_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_15_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_15_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_160_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_160_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_161_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_161_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_162_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_162_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_163_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_163_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_164_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_164_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_165_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_165_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_166_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_166_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_167_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_167_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_168_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_168_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_169_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_169_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_16_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_16_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_170_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_170_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_171_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_171_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_172_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_172_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_173_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_173_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_174_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_174_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_175_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_175_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_176_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_176_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_177_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_177_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_178_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_178_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_179_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_179_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_17_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_17_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_180_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_180_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_181_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_181_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_182_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_182_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_183_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_183_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_184_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_184_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_185_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_185_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_186_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_186_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_187_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_187_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_188_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_188_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_189_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_189_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_18_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_18_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_190_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_190_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_191_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_191_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_192_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_192_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_193_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_193_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_194_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_194_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_195_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_195_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_196_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_196_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_197_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_197_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_198_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_198_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_199_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_199_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_19_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_19_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_1_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_1_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39129),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.00000,
            "rear_.*_thigh_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_200_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_200_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_201_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_201_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_202_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_202_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_203_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_203_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_204_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_204_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_205_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_205_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_206_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_206_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_207_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_207_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_208_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_208_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_209_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_209_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_20_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_20_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_210_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_210_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_211_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_211_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_212_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_212_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42235),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_213_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_213_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51009),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_214_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_214_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33476),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_215_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_215_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.51095),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_216_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_216_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45188),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_217_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_217_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.39923),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_218_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_218_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35343),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_219_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_219_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54788),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_21_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_21_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_220_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_220_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_221_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_221_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_222_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_222_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_223_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_223_KneeNum_fl2_fr2_rl2_rr2__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.44983),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_224_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_224_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_225_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_225_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_226_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_226_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_227_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_227_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_228_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_228_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_229_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_229_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_22_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_22_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_230_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_230_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_231_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_231_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_232_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_232_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_233_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_233_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_234_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_234_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_235_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_235_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_236_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_236_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_237_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_237_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_238_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_238_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_239_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_239_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_23_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_23_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_240_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_240_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_241_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_241_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_242_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_242_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_243_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_243_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_244_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_244_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_245_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_245_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_246_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_246_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_247_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_247_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_248_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_248_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_249_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_249_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_24_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_24_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_250_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_250_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_251_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_251_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_252_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_252_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_253_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_253_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_254_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_254_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_255_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_255_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_256_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_256_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_257_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_257_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_258_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_258_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_259_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_259_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_25_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_25_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_260_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_260_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_261_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_261_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_262_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_262_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_263_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_263_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_264_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_264_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_265_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_265_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_266_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_266_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_267_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_267_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_268_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_268_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_269_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_269_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_26_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_26_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_270_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_270_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_271_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_271_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_272_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_272_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_273_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_273_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_274_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_274_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_275_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_275_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_276_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_276_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_277_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_277_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_278_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_278_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_279_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_279_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_27_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_27_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_280_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_280_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_281_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_281_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_282_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_282_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_283_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_283_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_284_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_284_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_285_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_285_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_286_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_286_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_287_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_287_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_288_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_288_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_289_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_289_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_28_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_28_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_290_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_290_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_291_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_291_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_292_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_292_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_293_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_293_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_294_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_294_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_295_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_295_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_296_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_296_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_297_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_297_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_298_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_298_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_299_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_299_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_29_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_29_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_2_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.25752),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.00000,
            "rear_.*_thigh_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_300_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_300_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_301_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_301_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_302_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_302_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_303_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_303_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_304_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_304_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_305_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_305_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_306_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_306_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_307_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_307_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_308_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_308_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_309_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_309_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_30_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_30_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_310_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_310_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_311_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_311_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_312_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_312_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_313_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_313_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_314_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_314_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_315_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_315_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_316_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_316_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_317_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_317_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_318_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_318_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_319_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_319_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_31_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_31_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_320_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_320_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52692),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_321_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_321_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.63525),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_322_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_322_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41859),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_323_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_323_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.60227),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_324_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_324_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.54982),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_325_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_325_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.50402),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_326_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_326_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45821),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_327_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_327_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.71553),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_328_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_328_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.58979),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_329_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_329_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.46405),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_32_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_32_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_330_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_330_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_331_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_331_KneeNum_fl3_fr3_rl3_rr3__ScaleJointLimit_fl0_fr0_rl0_rr1_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55165),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000,
            ".*_knee_.*_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_33_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_33_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_34_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_34_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_35_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_35_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_36_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_36_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_37_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_37_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_38_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_38_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_39_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_39_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_3_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_3_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.45156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.00000,
            "rear_.*_thigh_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_40_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_40_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_41_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_41_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_42_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_42_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_43_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_43_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl1_fr0_rl0_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_44_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_44_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_45_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_45_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_46_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_46_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_47_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_47_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_48_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_48_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_49_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_49_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_4_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_4_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36679),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.00000,
            "rear_.*_thigh_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_50_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_50_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_51_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_51_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_52_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_52_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_53_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_53_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_54_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_54_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_55_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_55_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_56_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_56_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_57_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_57_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_58_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_58_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_59_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_59_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_5_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_5_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.28202),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.00000,
            "rear_.*_thigh_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_60_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_60_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_61_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_61_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_62_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_62_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_63_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_63_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_64_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_64_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_65_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_65_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_66_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_66_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_67_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_67_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr1_rl0_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_68_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_68_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_69_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_69_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_6_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_6_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.19724),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.00000,
            "rear_.*_thigh_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_70_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_70_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_71_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_71_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_72_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_72_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_73_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_73_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_74_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_74_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_75_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_75_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_76_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_76_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_77_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_77_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_78_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_78_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_79_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_79_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_6__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_7_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_7_KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35655),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.00000,
            "rear_.*_thigh_joint": 0.00000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_80_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_80_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_81_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_81_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_82_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_82_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_83_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_83_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_84_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_84_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_85_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_85_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_86_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_86_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_87_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_87_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_88_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_88_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.34929),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_89_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_89_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.31276),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_8_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_8_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_90_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_90_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_lengthen_calf_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.27623),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_91_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_91_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl1_rr0_0_2__Geo_scale_foot_size_2_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35850),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_92_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_92_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_1_0/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.33103),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_93_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_93_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_94_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_94_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_scale_all_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.26156),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_95_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_95_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.41962),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_96_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_96_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.36056),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_97_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_97_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_0_8/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.30150),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_98_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_98_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_thigh_0_4/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24865),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_99_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_99_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr1_0_6__Geo_lengthen_calf_1_6/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38582),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)

GEN_DOG_9_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/Robots/GenBot1K-v7/gen_dogs/gendog_9_KneeNum_fl1_fr1_rl1_rr1__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_scale_all_1_2/usd_file/robot.usd",
        activate_contact_sensors=activate_contact_sensors,
        rigid_props=rigid_props,
        articulation_props=articulation_props,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40050),
        joint_pos={
            ".*_left_hip_pitch_joint": 0.10000,
            ".*_right_hip_pitch_joint": -0.10000,
            "front_.*_thigh_joint": 0.80000,
            "rear_.*_thigh_joint": 1.00000,
            ".*_knee_joint": -1.50000
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=soft_joint_pos_limit_factor,
    actuators=actuators,
    prim_path=prim_path
)
