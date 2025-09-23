from __future__ import annotations

from embodiment_scaling_laws.tasks.environments.locomotion_env import LocomotionEnv
# from embodiment_scaling_laws.tasks.environments.locomotion_env_multi_embodi import LocomotionEnvMultiEmbodiment


class GenDirectEnv(LocomotionEnv):
    cfg: GenDogEnvCfg

    def __init__(self, cfg: GenDogEnvCfg, render_mode: str | None = None, **kwargs):
        super().__init__(cfg, render_mode, **kwargs)