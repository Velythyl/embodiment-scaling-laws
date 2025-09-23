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

from embodiment_scaling_laws.tasks.configs.environment.h1_cfg import H1EnvCfg
from embodiment_scaling_laws.assets.gen_humanoids import *

@configclass
class Genhumanoid0Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_0_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid100Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_100_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid101Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_101_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid102Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_102_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid103Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_103_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid104Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_104_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid105Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_105_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid106Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_106_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid107Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_107_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid108Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_108_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid109Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_109_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid10Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_10_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid110Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_110_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid111Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_111_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid112Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_112_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid113Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_113_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid114Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_114_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid115Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_115_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid116Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_116_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid117Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_117_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid118Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_118_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid119Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_119_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid11Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_11_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid120Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_120_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid121Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_121_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid122Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_122_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid123Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_123_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid124Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_124_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid125Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_125_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid126Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_126_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid127Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_127_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid128Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_128_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid129Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_129_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid12Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_12_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid130Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_130_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid131Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_131_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid132Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_132_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid133Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_133_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid134Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_134_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid135Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_135_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid136Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_136_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid137Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_137_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid138Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_138_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid139Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_139_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid13Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_13_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid140Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_140_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid141Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_141_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid142Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_142_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid143Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_143_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid144Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_144_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid145Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_145_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid146Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_146_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid147Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_147_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid148Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_148_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid149Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_149_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid14Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_14_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid150Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_150_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid151Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_151_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid152Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_152_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid153Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_153_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid154Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_154_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid155Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_155_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid156Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_156_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid157Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_157_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid158Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_158_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid159Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_159_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid15Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_15_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid160Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_160_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid161Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_161_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid162Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_162_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid163Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_163_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid164Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_164_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid165Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_165_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid166Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_166_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid167Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_167_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid168Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_168_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid169Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_169_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid16Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_16_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid170Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_170_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid171Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_171_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid172Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_172_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid173Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_173_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid174Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_174_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid175Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_175_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid176Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_176_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid177Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_177_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid178Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_178_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid179Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_179_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid17Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_17_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid180Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_180_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid181Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_181_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid182Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_182_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid183Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_183_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid184Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_184_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid185Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_185_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid186Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_186_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid187Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_187_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid188Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_188_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid189Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_189_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid18Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_18_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid190Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_190_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid191Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_191_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid192Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_192_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid193Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_193_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid194Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_194_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid195Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_195_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid196Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_196_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid197Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_197_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid198Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_198_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid199Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_199_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid19Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_19_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid1Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_1_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid200Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_200_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid201Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_201_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid202Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_202_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid203Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_203_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid204Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_204_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid205Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_205_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid206Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_206_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid207Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_207_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid208Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_208_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid209Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_209_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid20Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_20_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid210Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_210_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid211Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_211_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid212Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_212_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid213Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_213_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid214Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_214_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid215Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_215_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid216Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_216_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid217Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_217_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid218Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_218_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid219Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_219_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid21Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_21_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid220Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_220_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid221Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_221_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid222Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_222_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid223Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_223_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid224Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_224_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid225Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_225_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid226Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_226_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid227Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_227_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid228Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_228_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid229Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_229_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid22Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_22_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid230Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_230_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid231Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_231_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid232Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_232_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid233Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_233_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid234Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_234_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid235Cfg(H1EnvCfg):
    action_space = 21
    robot: ArticulationCfg = GEN_HUMANOID_235_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid236Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_236_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid237Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_237_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid238Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_238_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid239Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_239_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid23Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_23_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid240Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_240_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid241Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_241_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid242Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_242_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid243Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_243_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid244Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_244_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid245Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_245_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid246Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_246_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid247Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_247_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid248Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_248_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid249Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_249_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid24Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_24_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid250Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_250_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid251Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_251_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid252Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_252_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid253Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_253_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid254Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_254_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid255Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_255_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid256Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_256_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid257Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_257_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid258Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_258_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid259Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_259_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid25Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_25_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid260Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_260_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid261Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_261_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid262Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_262_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid263Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_263_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid264Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_264_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid265Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_265_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid266Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_266_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid267Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_267_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid268Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_268_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid269Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_269_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid26Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_26_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid270Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_270_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid271Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_271_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid272Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_272_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid273Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_273_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid274Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_274_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid275Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_275_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid276Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_276_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid277Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_277_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid278Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_278_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid279Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_279_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid27Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_27_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid280Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_280_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid281Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_281_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid282Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_282_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid283Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_283_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid284Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_284_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid285Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_285_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid286Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_286_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid287Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_287_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid288Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_288_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid289Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_289_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid28Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_28_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid290Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_290_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid291Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_291_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid292Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_292_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid293Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_293_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid294Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_294_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid295Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_295_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid296Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_296_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid297Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_297_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid298Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_298_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid299Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_299_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid29Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_29_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid2Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_2_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid300Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_300_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid301Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_301_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid302Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_302_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid303Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_303_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid304Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_304_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid305Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_305_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid306Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_306_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid307Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_307_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid308Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_308_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid309Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_309_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid30Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_30_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid310Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_310_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid311Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_311_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid312Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_312_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid313Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_313_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid314Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_314_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid315Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_315_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid316Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_316_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid317Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_317_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid318Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_318_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid319Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_319_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid31Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_31_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid320Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_320_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid321Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_321_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid322Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_322_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid323Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_323_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid324Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_324_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid325Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_325_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid326Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_326_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid327Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_327_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid328Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_328_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid329Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_329_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid32Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_32_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid330Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_330_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid331Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_331_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid332Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_332_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid333Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_333_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid334Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_334_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid335Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_335_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid336Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_336_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid337Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_337_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid338Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_338_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid339Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_339_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid33Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_33_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid340Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_340_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid341Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_341_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid342Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_342_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid343Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_343_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid344Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_344_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid345Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_345_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid346Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_346_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid347Cfg(H1EnvCfg):
    action_space = 23
    robot: ArticulationCfg = GEN_HUMANOID_347_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid34Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_34_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid35Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_35_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid36Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_36_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid37Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_37_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid38Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_38_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid39Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_39_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid3Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_3_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid40Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_40_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid41Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_41_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid42Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_42_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid43Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_43_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid44Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_44_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid45Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_45_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid46Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_46_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid47Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_47_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid48Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_48_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid49Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_49_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid4Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_4_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid50Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_50_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid51Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_51_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid52Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_52_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid53Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_53_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid54Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_54_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid55Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_55_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid56Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_56_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid57Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_57_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid58Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_58_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid59Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_59_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid5Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_5_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid60Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_60_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid61Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_61_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid62Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_62_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid63Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_63_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid64Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_64_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid65Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_65_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid66Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_66_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid67Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_67_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid68Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_68_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid69Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_69_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid6Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_6_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid70Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_70_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid71Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_71_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid72Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_72_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid73Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_73_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid74Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_74_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid75Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_75_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid76Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_76_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid77Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_77_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid78Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_78_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid79Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_79_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid7Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_7_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid80Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_80_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid81Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_81_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid82Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_82_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid83Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_83_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid84Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_84_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid85Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_85_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid86Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_86_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid87Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_87_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid88Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_88_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid89Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_89_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid8Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_8_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

@configclass
class Genhumanoid90Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_90_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid91Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_91_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['left_knee_joint', 'right_knee_joint'])
    lock_joint_factor = 0.2

@configclass
class Genhumanoid92Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_92_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid93Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_93_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid94Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_94_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid95Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_95_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid96Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_96_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid97Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_97_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid98Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_98_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid99Cfg(H1EnvCfg):
    action_space = 19
    robot: ArticulationCfg = GEN_HUMANOID_99_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = SceneEntityCfg("robot", joint_names=['right_knee_joint'])
    lock_joint_factor = 0.6

@configclass
class Genhumanoid9Cfg(H1EnvCfg):
    action_space = 17
    robot: ArticulationCfg = GEN_HUMANOID_9_CFG
    trunk_cfg = SceneEntityCfg("robot", body_names="pelvis")
    trunk_contact_cfg = None
    feet_contact_cfg = SceneEntityCfg("contact_sensor", body_names=".*foot")
    lock_joint_cfg = None
    lock_joint_factor = 1.0

