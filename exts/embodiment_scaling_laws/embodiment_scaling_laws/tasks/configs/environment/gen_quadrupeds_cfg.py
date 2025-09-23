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

from embodiment_scaling_laws.assets.gen_quadrupeds import *
from .go2_cfg import Go2EnvCfg


@configclass
class Gendog0Cfg(Go2EnvCfg):
    action_space = 8
    robot: ArticulationCfg = GEN_DOG_0_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog100Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_100_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog101Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_101_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog102Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_102_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog103Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_103_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog104Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_104_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog105Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_105_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog106Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_106_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog107Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_107_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog108Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_108_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog109Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_109_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog10Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_10_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog110Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_110_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog111Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_111_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog112Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_112_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog113Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_113_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog114Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_114_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog115Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_115_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog116Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_116_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog117Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_117_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog118Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_118_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog119Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_119_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog11Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_11_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog120Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_120_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog121Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_121_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog122Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_122_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog123Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_123_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog124Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_124_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog125Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_125_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog126Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_126_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog127Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_127_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog128Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_128_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog129Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_129_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog12Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_12_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog130Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_130_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog131Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_131_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog132Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_132_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog133Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_133_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog134Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_134_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog135Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_135_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog136Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_136_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog137Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_137_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog138Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_138_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog139Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_139_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog13Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_13_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog140Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_140_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog141Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_141_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog142Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_142_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog143Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_143_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog144Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_144_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog145Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_145_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog146Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_146_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog147Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_147_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog148Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_148_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog149Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_149_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog14Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_14_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog150Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_150_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog151Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_151_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog152Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_152_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog153Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_153_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog154Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_154_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog155Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_155_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog156Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_156_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog157Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_157_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog158Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_158_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog159Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_159_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog15Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_15_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog160Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_160_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog161Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_161_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog162Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_162_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog163Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_163_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog164Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_164_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog165Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_165_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog166Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_166_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog167Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_167_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog168Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_168_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog169Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_169_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog16Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_16_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog170Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_170_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog171Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_171_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog172Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_172_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog173Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_173_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog174Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_174_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog175Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_175_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog176Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_176_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog177Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_177_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog178Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_178_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog179Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_179_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog17Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_17_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog180Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_180_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog181Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_181_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog182Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_182_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog183Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_183_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog184Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_184_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog185Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_185_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog186Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_186_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog187Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_187_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog188Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_188_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog189Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_189_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog18Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_18_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog190Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_190_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog191Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_191_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog192Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_192_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog193Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_193_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog194Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_194_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog195Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_195_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog196Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_196_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog197Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_197_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog198Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_198_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog199Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_199_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog19Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_19_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog1Cfg(Go2EnvCfg):
    action_space = 8
    robot: ArticulationCfg = GEN_DOG_1_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog200Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_200_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog201Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_201_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog202Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_202_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog203Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_203_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog204Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_204_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog205Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_205_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog206Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_206_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog207Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_207_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog208Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_208_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog209Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_209_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog20Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_20_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog210Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_210_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog211Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_211_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog212Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_212_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog213Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_213_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog214Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_214_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog215Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_215_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog216Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_216_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog217Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_217_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog218Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_218_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog219Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_219_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog21Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_21_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog220Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_220_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog221Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_221_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog222Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_222_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog223Cfg(Go2EnvCfg):
    action_space = 16
    robot: ArticulationCfg = GEN_DOG_223_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog224Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_224_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog225Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_225_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog226Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_226_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog227Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_227_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog228Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_228_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog229Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_229_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog22Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_22_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog230Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_230_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog231Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_231_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog232Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_232_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog233Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_233_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog234Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_234_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog235Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_235_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog236Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_236_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog237Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_237_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog238Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_238_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog239Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_239_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog23Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_23_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog240Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_240_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog241Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_241_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog242Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_242_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog243Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_243_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog244Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_244_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog245Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_245_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog246Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_246_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog247Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_247_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog248Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_248_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog249Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_249_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog24Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_24_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog250Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_250_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog251Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_251_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog252Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_252_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog253Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_253_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog254Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_254_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog255Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_255_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog256Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_256_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog257Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_257_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog258Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_258_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog259Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_259_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog25Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_25_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog260Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_260_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog261Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_261_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog262Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_262_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog263Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_263_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog264Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_264_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog265Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_265_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog266Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_266_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog267Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_267_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog268Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_268_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog269Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_269_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog26Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_26_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog270Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_270_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog271Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_271_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog272Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_272_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog273Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_273_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog274Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_274_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog275Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_275_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog276Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_276_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog277Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_277_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog278Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_278_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog279Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_279_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog27Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_27_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog280Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_280_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog281Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_281_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog282Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_282_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog283Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_283_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog284Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_284_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog285Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_285_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog286Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_286_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog287Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_287_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog288Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_288_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog289Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_289_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog28Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_28_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog290Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_290_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog291Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_291_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog292Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_292_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog293Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_293_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog294Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_294_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog295Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_295_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog296Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_296_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog297Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_297_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog298Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_298_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog299Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_299_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog29Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_29_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog2Cfg(Go2EnvCfg):
    action_space = 8
    robot: ArticulationCfg = GEN_DOG_2_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog300Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_300_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog301Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_301_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog302Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_302_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog303Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_303_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog304Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_304_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog305Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_305_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog306Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_306_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog307Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_307_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog308Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_308_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog309Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_309_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog30Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_30_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog310Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_310_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog311Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_311_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog312Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_312_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog313Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_313_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog314Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_314_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog315Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_315_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog316Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_316_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog317Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_317_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog318Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_318_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog319Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_319_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog31Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_31_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog320Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_320_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog321Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_321_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog322Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_322_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog323Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_323_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog324Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_324_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog325Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_325_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog326Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_326_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog327Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_327_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog328Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_328_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog329Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_329_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog32Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_32_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog330Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_330_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog331Cfg(Go2EnvCfg):
    action_space = 20
    robot: ArticulationCfg = GEN_DOG_331_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog33Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_33_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog34Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_34_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog35Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_35_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog36Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_36_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog37Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_37_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog38Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_38_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog39Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_39_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog3Cfg(Go2EnvCfg):
    action_space = 8
    robot: ArticulationCfg = GEN_DOG_3_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog40Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_40_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog41Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_41_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog42Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_42_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog43Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_43_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog44Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_44_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog45Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_45_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog46Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_46_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog47Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_47_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog48Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_48_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog49Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_49_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog4Cfg(Go2EnvCfg):
    action_space = 8
    robot: ArticulationCfg = GEN_DOG_4_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog50Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_50_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog51Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_51_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog52Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_52_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog53Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_53_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog54Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_54_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog55Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_55_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog56Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_56_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog57Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_57_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog58Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_58_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog59Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_59_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog5Cfg(Go2EnvCfg):
    action_space = 8
    robot: ArticulationCfg = GEN_DOG_5_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog60Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_60_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog61Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_61_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog62Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_62_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog63Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_63_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog64Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_64_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog65Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_65_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog66Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_66_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog67Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_67_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['front_right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog68Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_68_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog69Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_69_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog6Cfg(Go2EnvCfg):
    action_space = 8
    robot: ArticulationCfg = GEN_DOG_6_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog70Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_70_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog71Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_71_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog72Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_72_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog73Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_73_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog74Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_74_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog75Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_75_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog76Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_76_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog77Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_77_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog78Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_78_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog79Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_79_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog7Cfg(Go2EnvCfg):
    action_space = 8
    robot: ArticulationCfg = GEN_DOG_7_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog80Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_80_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog81Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_81_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog82Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_82_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog83Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_83_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog84Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_84_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog85Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_85_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog86Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_86_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog87Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_87_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog88Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_88_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog89Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_89_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog8Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_8_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Gendog90Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_90_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog91Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_91_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Gendog92Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_92_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog93Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_93_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog94Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_94_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog95Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_95_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog96Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_96_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog97Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_97_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog98Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_98_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog99Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_99_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['rear_right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Gendog9Cfg(Go2EnvCfg):
    action_space = 12
    robot: ArticulationCfg = GEN_DOG_9_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="trunk")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

