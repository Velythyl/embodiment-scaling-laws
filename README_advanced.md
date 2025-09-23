# Design your own robot 

## Understanding the codebase
1. `exts/embodiment_scaling_laws/embodiment_scaling_laws/assets`: place where the robot USD files are placed, and the entry for importing
robots. Every robot is treated as an articulation, and its associated properties, such as initial state, joint limit, joint type, 
are defined in `ArticulationCfg` in the files there. 
2. `exts/embodiment_scaling_laws/embodiment_scaling_laws/tasks/environments/locomotion_env.py`: the core simulation logic. The observation space
defined in  `_get_observations` and the reward function is `_get_rewards`. 
3. `exts/embodiment_scaling_laws/embodiment_scaling_laws/tasks/configs/environment`: place where parameters of the environments 
(for different robots), such as scene, ground, velocity command parameters, are defined.
4. `generation`: scripts for generating nautilus training job scripts, articulation configs, PPO configs, in batch, among many others. 

## Generate customized GenBot1K
To follow our robot generation pipeline and design your own customized GenBot1K, check code under `generation/embodiment_generation`.

To only generate URDF files:
```
python main_color.py
```
To simultaneously generate .usd files:
First, change the Isaac path in Line 9 in main_color.py
Then run:
```
python main_color.py --gen_usd
```

## Adding configurations for customized GenBot1K
Taking quadruped as an example, but the specific file names could differ for different robots: 

0. Copy file `scripts/utility/convert_urdf.py` to `${ISAAC_LAB_PATH}/source/standalone/tools/convert_urdf.py`.
Covner URDF to USD using `scripts/utility/urdf_to_usd.sh` or `scripts/utility/urdf_to_usd_batch.sh`. Here are the example commands:
```angular2html
sh urdf_to_usd.sh ~/Downloads/gen_dog_3_variants/gen_dog_1.urdf ~/Downloads/gen_dog_3_variants/usd/gen_dog_1.usd
sh urdf_to_usd_batch.sh ~/Downloads/gen_dog_3_variants ~/Downloads/gen_dog_3_variants_us    # specify folder 
```

0.1. Update initial height via 
```aiignore
python generation/update_init_height_sapien.py 
```
You will see `train_cfg_v2.json` in all folders. Please install `sapien===2.2.2` for this. It uses SAPIEN to determine the most suitable initial height for each robot. 

0.2. (Optional) Generate description vector via
```aiignore
python generation/get_description_vector_sapien.py 
```
You will see an additional file in all folders, useful for URMA training.

1. Place USD files under `exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/Robots`. 
For large robot dataset like `GenBot1K`, we could store the folder somewhere else and create a soft link in the directory pointing to the folder, e.g.
```angular2html
ln -s /folder_absolute_path /absolute_path/exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/Robots/GenBot1K-v7
```

2. Add PPO configs to `exts/embodiment_scaling_laws/embodiment_scaling_laws/tasks/direct/humanoid/agents/gen_quadruped_1k_ppo_cfg.py`, following the pattern in the file. For adding a large number of robots, run `generation/gen_ppo_cfg.py` to generate these lines automatically:
```angular2html
python generation/gen_ppo_cfg.py 
```
but remember to modify the paths in the file. 

3. Add robot configs to `exts/embodiment_scaling_laws/embodiment_scaling_laws/assets/gen_quadrupeds.py`. Note that the configs here might be highly relevant for sim-to-real transfer, e.g., actuator parameters. For adding a large number of robots, run `generation/gen_articulation_cfg.py` to generate these lines automatically:
```angular2html
python generation/gen_articulation_cfg.py
```
but also remember to modify the paths in the file.

4. Add training env configs to `exts/embodiment_scaling_laws/embodiment_scaling_laws/tasks/direct/humanoid/gen_quadrupeds_env.py`. For adding a large number of robots, run `generation/gen_quadruped_env.py` to generate these lines automatically.

5. Register training envs at `exts/embodiment_scaling_laws/embodiment_scaling_laws/tasks/configs/environment/__init__.py`. For adding a large number of robots, run `generation/gen_init_registry.py` to generate these lines automatically.

NOTE: For newly generated robots, please run `generation/update_init_height_sapien.py` and `generation/get_description_vector_sapien.py` so that the robot folder contains all necessary information for training and distillation. For the latter, please see the section on `Use SAPIEN` for more details.

## Use SAPIEN
We use SAPIEN to compute description vector, initial robot height, etc. To use these scripts, we first install SAPIEN 2.2.2:
```aiignore
pip install sapien==2.2.2
conda install -y networkx">=2.5"
```
Then we can run `generation/get_description_vector_sapien.py` or `generation/update_init_height_sapien.py`. These
scripts don't have any args, but you need to adjust the paths in the code yourself.

P.S.The following error is okay. Just ignore it:
```aiignore
[2024-12-17 20:39:12.722] [SAPIEN] [error] Cylinder collision is not supported. Replaced with a capsule
```

## Common errors
1. Initial state values are integers
```angular2html
self._data.default_joint_pos[:, indices_list] = torch.tensor(values_list, device=self.device)
RuntimeError: Index put requires the source and destination dtypes match, got Float for the destination and Long for the source
```
This is pretty likely due to using integers like `0` as the initial state -- please use `0.0` instead.
