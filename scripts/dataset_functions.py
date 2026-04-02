import os
import random
import time
import h5py
import numpy as np
import torch
import yaml
import json
import warnings
from torch.utils.data import Dataset, DataLoader
from torch.utils.data import TensorDataset
from itertools import chain

from thread_safe_dict import ThreadSafeDict, ThreadSafeSingleEntryDict
from utility_functions import AverageMeter


class DatasetSaver:
    # List of attribute names to retrieve from the environment
    ENV_ATTRS = [
        "nr_dynamic_joint_observations",
        "single_dynamic_joint_observation_length",
        "dynamic_joint_observation_length",
        "dynamic_joint_description_size",
        "joint_positions_update_obs_idx",
        "joint_velocities_update_obs_idx",
        "joint_previous_actions_update_obs_idx",
        "trunk_angular_vel_update_obs_idx",
        "goal_velocity_update_obs_idx",
        "projected_gravity_update_obs_idx",
    ]

    def __init__(self, record_path, env, max_steps_per_file, buffer_size=1):
        """
        Initialize the DatasetSaver to handle HDF5 datasets.

        Args:
            record_path (str): Directory to store HDF5 files.
            max_steps_per_file (int): Maximum number of steps per HDF5 file.
            buffer_size (int): Number of HDF5 files to accumulate before saving.
            env: Instance of the locomotion environment.
        """
        self.record_path = record_path
        self.max_steps_per_file = max_steps_per_file
        self.buffer_size = buffer_size
        self.current_file_index = 0

        # Buffers for accumulating data
        self.obs_buffer = []
        self.actions_buffer = []

        # Ensure the record directory exists
        os.makedirs(self.record_path, exist_ok=True)
        print(f"Recording path set to: {self.record_path}")

        # Save environment metadata, including the number of samples and parallel environments
        self._save_environment_metadata(env)

    def _save_environment_metadata(self, env):
        """
        Save specific environment metadata as a YAML file.

        Args:
            env: Instance of the locomotion environment.
        """
        # Dynamically retrieve attribute values
        metadata = {attr: getattr(env.unwrapped, attr, None) for attr in self.ENV_ATTRS}

        # Add additional metadata for sample and environment counts
        metadata["steps_per_file"] = self.max_steps_per_file
        metadata["parallel_envs"] = env.num_envs  # Assuming `num_envs` is an attribute of the environment

        # Save metadata to a YAML file
        metadata_file_path = os.path.join(self.record_path, "metadata.yaml")
        with open(metadata_file_path, "w") as metadata_file:
            yaml.dump(metadata, metadata_file, default_flow_style=False)

        print(f"Environment metadata saved to: {metadata_file_path}")

    def _save_to_files(self):
        """
        Save the accumulated data in the buffers to multiple HDF5 files,
        checking for None/NaN values before saving.
        """
        num_files = len(self.obs_buffer) // self.max_steps_per_file

        for i in range(num_files):
            # Prepare file-specific data
            start_idx = i * self.max_steps_per_file
            end_idx = (i + 1) * self.max_steps_per_file
            obs_data = np.array(self.obs_buffer[start_idx:end_idx])
            action_data = np.array(self.actions_buffer[start_idx:end_idx])

            # Check for None or NaN values
            if np.any(obs_data == None) or np.any(action_data == None):  # Check for None
                raise ValueError(f"Found None values in observation or action data for file {i}")
            if np.isnan(obs_data).any() or np.isnan(action_data).any():  # Check for NaN
                raise ValueError(f"Found NaN values in observation or action data for file {i}")

            # Save to a new HDF5 file
            file_name = f"obs_actions_{self.current_file_index:05d}.h5"
            file_path = os.path.join(self.record_path, file_name)
            with h5py.File(file_path, "w") as file:
                file.create_dataset("one_policy_observation", data=obs_data, dtype="float32")
                file.create_dataset("actions", data=action_data, dtype="float32")

            print(f"[INFO]: Saved {len(obs_data)} steps to {file_path}")
            self.current_file_index += 1

        # Remove saved data from buffers
        self.obs_buffer = self.obs_buffer[num_files * self.max_steps_per_file:]
        self.actions_buffer = self.actions_buffer[num_files * self.max_steps_per_file:]

    def save_data(self, one_policy_observation, actions):
        """
        Accumulate data in buffers and save to multiple files when buffer is full.

        Args:
            one_policy_observation (np.ndarray): Observation data.
            actions (np.ndarray): Action data.
        """
        # Append data to buffers
        self.obs_buffer.append(one_policy_observation)
        self.actions_buffer.append(actions)

        # Check if we need to save files
        total_steps = len(self.obs_buffer)
        if total_steps >= self.buffer_size * self.max_steps_per_file:
            self._save_to_files()

    def close(self):
        """
        Save any remaining data in the buffers to files.
        """
        if self.obs_buffer or self.actions_buffer:
            print("[INFO]: Flushing remaining data to files.")
            self._save_to_files()

    def __del__(self):
        """
        Destructor to ensure proper cleanup.
        """
        self.close()


class LocomotionDataset(Dataset):
    GENERAL_POLICY_STATE_LEN = 11

    def __init__(self, folder_paths, max_files_in_memory, train_mode, val_ratio, h5_repeat_factor,
                 max_parallel_envs_per_file, max_envs_per_file_in_memory,
                 description_filename: str = None, asset_base_path: str = None):
        """
        Initialize the LocomotionDataset.

        The dataset uses memoization for data loading, i.e., once a data file is loaded it will also be stored in cache.
        Note that DataLoader spawns num_workers DataSet classes, each for one thread, so the cache will not be shared across multiple threads.
        We attempted to implement a cache sharable across all threads to avoid duplicate IO and memory usage, but it was 100x slower due to multi-thread communication.

        The dataset sampler also ensures that the samples in one batch are all from one .h5 file, which may reduce randomness in data but increases reading speed and ease implementation.
        Thus, an implicit assumption is that one .h5 file contains at least one batch of data.

        Args:
            - folder_paths (list): List of paths to dataset folders.
            max_files_in_memory (int): Maximum number of .h5 files to keep in memory. This helps reduce IO bottlenecks.
            - max_files_in_memory: Maximum number of .h5 files to keep in memory. This trades off between IO and RAM usage.
            - train_mode: whether to use the training set or the validation set.
            - val_ratio: ratio of validation set to training set.
            - h5_repeat_factor: Number of times we repeat one h5 file consecutively in one epoch. This gives us more batches without additional IO, but may alter the training dynamics a bit.
            - max_parallel_envs_per_file: Maximum number of parallel environments to load from one .h5 file. This canbe used to control the portion of data we want to use for training.
            - max_envs_per_file_in_memory: Maximum number of environments to load from one .h5 file into memory. This is useful when the number of environments in one .h5 file is larger than the number of environments we can load into memory. This trades off between IO and RAM usage.
            - description_filename: Name of robot description JSON file to load from each robot's asset folder.
                                   If None, uses baseline 18-dim description (no limb bboxes).
                                   Examples: "robot_description_vec_with_bboxes.json", "robot_description_vec_custom.json"
            - asset_base_path: Base path to robot assets (required if description_filename is provided)
        """
        
        self.folder_paths = np.array(folder_paths)
        self.max_files_in_memory = max_files_in_memory
        self.metadata_list = np.array([self._load_metadata(folder_path) for folder_path in folder_paths])   # use numpy to avoid copy-on-write behavior of python list
        # self.metadata_list = [self._load_metadata(folder_path) for folder_path in folder_paths]
        self.max_parallel_envs_per_file = max_parallel_envs_per_file
        self.max_envs_per_file_in_memory = max_envs_per_file_in_memory
        # assert self.max_envs_per_file_in_memory <= self.max_parallel_envs_per_file, \
        #     (f"max_envs_per_file_in_memory {self.max_envs_per_file_in_memory} should not be larger "
        #      f"than max_parallel_envs_per_file {self.max_parallel_envs_per_file}")

        self.train_mode = train_mode
        self.val_ratio = val_ratio
        self.h5_repeat_factor = h5_repeat_factor
        self.total_samples = 0

        # Robot description parameters for limb shape conditioning
        self.description_filename = description_filename
        self.asset_base_path = asset_base_path
        self.robot_desc_cache = {}  # Cache for robot description JSONs
        self.use_limb_bboxes = False  # Will be set to True if descriptions contain bbox data

        # Thread-safe cache for loaded files
        # global global_cache    # we must use global reference, otherwise every thread will spawn its own cache
        self.cache = ThreadSafeDict(max_size=max_files_in_memory)
        # self.cache = ThreadSafeSingleEntryDict(max_size=max_files_in_memory)

        # Map file indices and prepare dataset structure
        self._prepare_file_indices()

        # Preload robot descriptions if a custom description file is specified
        if self.description_filename is not None:
            if self.asset_base_path is None:
                raise ValueError("asset_base_path is required when description_filename is provided")
            self._preload_robot_descriptions()

        # Compute hit rate for caching, for debugging purpose
        # self.cache_hit_count = AverageMeter()
        # self.cache_query_time = AverageMeter()
        # self.transform_data_time = AverageMeter()

        # record the number of times the data index is not in the worker's scope
        # self.counter_not_in_scope = 0

        # for debugging
        # self.get_count = 0

        # Verbose output
        print(f"[INFO]: Initialized dataset with {len(self)} samples from {len(self.folder_paths)} folders. "
              f"\n\tGot {len(self.folder_idx_to_file_name)} robots" # : {list(self.folder_idx_to_file_name.values())}
              f"\n\th5_repeat_factor={self.h5_repeat_factor}"
              f"\n\tdescription_filename={self.description_filename}"
              f"\n\tuse_limb_bboxes={self.use_limb_bboxes}")

    def _load_metadata(self, folder_path):
        """
        Load metadata from the YAML file in a dataset folder.

        Args:
            folder_path (str): Path to the folder.

        Returns:
            dict: Metadata containing environment parameters.
        """
        metadata_path = os.path.join(folder_path, "metadata.yaml")
        if not os.path.exists(metadata_path):
            raise FileNotFoundError(f"[ERROR]: Metadata file not found at {metadata_path}")

        with open(metadata_path, "r") as metadata_file:
            metadata = yaml.safe_load(metadata_file)
        return metadata

    def _robot_name_to_asset_folder(self, robot_name: str) -> str:
        """Convert h5py folder name to robot asset folder path.
        
        Example: Gendog10_gendog_10_KneeNum_... -> gen_dogs/gendog_10_KneeNum_...
        """
        robot_name_lower = robot_name.lower()
        if robot_name_lower.startswith("gendog"):
            # Find where the actual robot folder name starts
            # Format: Gendog{N}_gendog_{N}_...
            parts = robot_name.split("_", 1)
            if len(parts) > 1:
                return f"gen_dogs/{parts[1]}"
            else:
                raise ValueError(f"Could not parse robot name: {robot_name}")
        elif robot_name_lower.startswith("genhexapod"):
            parts = robot_name.split("_", 1)
            if len(parts) > 1:
                return f"gen_hexapods/{parts[1]}"
            else:
                raise ValueError(f"Could not parse robot name: {robot_name}")
        elif robot_name_lower.startswith("genhumanoid"):
            parts = robot_name.split("_", 1)
            if len(parts) > 1:
                return f"gen_humanoids/{parts[1]}"
            else:
                raise ValueError(f"Could not parse robot name: {robot_name}")
        else:
            raise ValueError(f"Unknown robot type: {robot_name}")

    def _preload_robot_descriptions(self):
        """Load robot description JSON files for all robots in dataset.
        
        The JSON file specified by self.description_filename is loaded from each robot's asset folder.
        If the JSON contains 'link_info' and 'joint_to_child_link' fields, limb bbox injection is enabled.
        
        Expected JSON structure (extends robot_description_vec.json):
        {
            "joint_info": {
                "joint_name": {
                    "joint_index": int,
                    "joint_lower_limit": float,
                    "joint_upper_limit": float,
                    ... (other joint properties)
                },
                ...
            },
            "link_info": {  # NEW: required for limb bbox injection
                "link_name": {
                    "bbox": <any structure, will be flattened via np.array().flatten()>,
                    "mass": float
                },
                ...
            },
            "joint_to_child_link": {  # NEW: required for limb bbox injection
                "joint_name": "child_link_name",
                ...
            }
        }
        
        Supported bbox formats (all flattened automatically):
          - Nested: [[min_x, min_y, min_z], [max_x, max_y, max_z]] -> 6 dims
          - Flat: [data1, data2, data3, ...] -> N dims
          - Any nested structure that np.array().flatten() can handle
        
        Generate with: python generation/get_description_vector_sapien.py --root_dir <robot_type> --output_suffix <suffix>
        """
        print(f"[INFO]: Preloading robot descriptions from '{self.description_filename}' for {len(self.folder_idx_to_file_name)} robots...")
        
        has_bbox_data = None  # Track whether all robots have bbox data
        
        for folder_idx, robot_name in self.folder_idx_to_file_name.items():
            if robot_name in self.robot_desc_cache:
                continue  # Already loaded
            try:
                asset_folder = self._robot_name_to_asset_folder(robot_name)
                json_path = os.path.join(
                    self.asset_base_path, asset_folder, self.description_filename
                )
                if not os.path.exists(json_path):
                    raise FileNotFoundError(
                        f"Robot description file not found: {json_path}\n"
                        f"Please generate with: python generation/get_description_vector_sapien.py --root_dir <robot_type> --output_suffix <suffix>"
                    )
                with open(json_path, 'r') as f:
                    desc = json.load(f)
                
                # Check if this description has limb bbox data
                robot_has_bbox = 'link_info' in desc and 'joint_to_child_link' in desc
                
                if has_bbox_data is None:
                    has_bbox_data = robot_has_bbox
                elif has_bbox_data != robot_has_bbox:
                    raise ValueError(
                        f"Inconsistent robot descriptions: some have link_info/joint_to_child_link, some don't. "
                        f"Robot '{robot_name}' has bbox data: {robot_has_bbox}, expected: {has_bbox_data}"
                    )
                
                self.robot_desc_cache[robot_name] = desc
            except Exception as e:
                raise RuntimeError(f"Failed to load robot description for {robot_name}: {e}")
        
        # Set flag for whether to inject limb bboxes
        self.use_limb_bboxes = has_bbox_data if has_bbox_data is not None else False
        
        # Determine extra description dimension by sampling actual data
        self.extra_des_dim = 0
        if self.use_limb_bboxes and self.robot_desc_cache:
            # Sample one robot to determine the bbox dimension
            sample_robot = next(iter(self.robot_desc_cache.keys()))
            sample_desc = self.robot_desc_cache[sample_robot]
            sample_link = next(iter(sample_desc['link_info'].keys()))
            sample_bbox = sample_desc['link_info'][sample_link]['bbox']
            # Flatten any nested structure (e.g., [[min], [max]] or [data1, data2, ...])
            self.extra_des_dim = len(np.array(sample_bbox).flatten())
            
            # Validate bbox dimension consistency across ALL robots and links
            for robot_name, desc in self.robot_desc_cache.items():
                for link_name, link_data in desc['link_info'].items():
                    bbox = link_data['bbox']
                    bbox_dim = len(np.array(bbox).flatten())
                    if bbox_dim != self.extra_des_dim:
                        raise ValueError(
                            f"Inconsistent bbox dimensions in robot '{robot_name}', link '{link_name}': "
                            f"got {bbox_dim} dims, expected {self.extra_des_dim}. "
                            f"All robots and links must have identical bbox format after flattening. "
                            f"Regenerate all descriptions with: "
                            f"python generation/get_description_vector_sapien.py --root_dir <robot_type>"
                        )
            
            # Pre-compute per-robot bbox arrays keyed by robot_name.
            # This avoids rebuilding tensors from Python dicts on every batch.
            # Shape: (nr_dynamic_joint_observations, extra_des_dim) as a float32 np.ndarray.
            self.robot_bbox_np_cache = {}
            for folder_idx, robot_name in self.folder_idx_to_file_name.items():
                if robot_name in self.robot_bbox_np_cache:
                    continue
                desc = self.robot_desc_cache[robot_name]
                nr_joints = self.metadata_list[folder_idx]["nr_dynamic_joint_observations"]
                all_joint_names = list(desc['joint_info'].keys())
                joint_names = all_joint_names[:nr_joints]
                rows = []
                for joint_name in joint_names:
                    child_link = desc['joint_to_child_link'][joint_name]
                    rows.append(np.array(desc['link_info'][child_link]['bbox']).flatten())
                self.robot_bbox_np_cache[robot_name] = np.stack(rows).astype(np.float32)

            print(f"[INFO]: Limb bbox injection ENABLED - extra_des_dim={self.extra_des_dim}, "
                  f"pre-cached bbox arrays for {len(self.robot_bbox_np_cache)} robots")
        else:
            self.robot_bbox_np_cache = {}
            print(f"[INFO]: Limb bbox injection DISABLED - descriptions do not contain bbox data")

    def _get_limb_bbox_for_batch(self, robot_name: str, joint_names: list) -> torch.Tensor:
        """Get limb bboxes for all joints in a robot.

        Returns CPU tensor of shape (nr_joints, extra_des_dim).
        Uses pre-computed numpy cache built in _preload_robot_descriptions for zero
        per-batch Python overhead (torch.from_numpy is a zero-copy view).
        """
        cached = self.robot_bbox_np_cache.get(robot_name)
        if cached is None:
            return torch.zeros((len(joint_names), self.extra_des_dim), dtype=torch.float32)
        return torch.from_numpy(cached)

    def _prepare_file_indices(self):
        """
        Create a mapping of file indices to (folder_idx, file_idx).
        Segregates files into train/validation sets based on val_ratio.
        """
        self.file_indices = {}
        self.folder_idx_to_file_name = {}
        for folder_idx, folder_path in enumerate(self.folder_paths):
            # example path: 'logs/rsl_rl/Gendog10_gendog__KneeNum_fl0_fr0_rl0_rr0__ScaleJointLimit_fl0_fr0_rl0_rr0_1_0__Geo_lengthen_calf_0_4/2024-12-15_15-19-08/h5py_record'
            self.folder_idx_to_file_name[folder_idx] = folder_path.split("/")[-3]
            metadata = self.metadata_list[folder_idx]
            hdf5_files = sorted(
                [
                    f.decode("utf-8") if isinstance(f, bytes) else f
                    for f in os.listdir(folder_path)
                    if (isinstance(f, bytes) and f.endswith(b".h5")) or (isinstance(f, str) and f.endswith(".h5"))
                ],
                key=lambda x: int(x.split('_')[-1].split('.')[0])
            )
            total_files = len(hdf5_files)
            num_val_files = int(total_files * self.val_ratio)
            if num_val_files == 0:
                num_val_files = 1

            # Choose files based on train/val mode
            if self.train_mode:
                selected_files = hdf5_files[:-num_val_files]  # First files for training
            else:
                selected_files = hdf5_files[-num_val_files:]  # Remaining files for validation

            # Process selected files
            for file_idx, file_name in enumerate(selected_files):
                key = (folder_idx, file_idx)
                steps_per_file = metadata["steps_per_file"]
                parallel_envs = metadata["parallel_envs"]
                if self.max_parallel_envs_per_file is not None:
                    assert parallel_envs >= self.max_parallel_envs_per_file, \
                        f"actual parallel envs {parallel_envs} smaller than {self.max_parallel_envs_per_file}"
                    parallel_envs = self.max_parallel_envs_per_file

                assert self.max_envs_per_file_in_memory <= parallel_envs, \
                    (f"self.max_envs_per_file_in_memory = {self.max_envs_per_file_in_memory} "
                     f"should be <= parallel_envs = {parallel_envs}")
                index = np.random.randint(0, parallel_envs - self.max_envs_per_file_in_memory + 1)
                slice_key = key + (index,)
                self.file_indices[slice_key] = (folder_path, file_name, steps_per_file, parallel_envs)
                self.total_samples += steps_per_file * parallel_envs

        for k, v in self.file_indices.items():
            h5_path = os.path.join(v[0], v[1])
            assert os.path.exists(h5_path)

    def __len__(self):
        """
        Get the total number of samples in the dataset.
        """
        print("[INFO] You are trying to get the number of samples in the dataset, "
              "which might not reflect the actual samples used in one epoch due to resampling")
        return self.total_samples

    def _load_file(self, folder_idx, file_idx, env_start_idx):
        """
        Load a specific HDF5 file into memory.

        Args:
            folder_idx (int): Index of the folder.
            file_idx (int): Index of the file within the folder.

        Returns:
            tuple: (inputs, targets) from the HDF5 file.
        """
        # print('loading', (folder_idx, file_idx, env_start_idx))
        folder_path, file_name, steps_per_file, parallel_envs = self.file_indices[(folder_idx, file_idx, env_start_idx)]
        file_path = os.path.join(folder_path, file_name)
        # print(f"[INFO]: Loading file {file_path}")

        with h5py.File(file_path, "r") as data_file:
            inputs = np.array(data_file["one_policy_observation"][:, env_start_idx:env_start_idx+self.max_envs_per_file_in_memory])
            targets = np.array(data_file["actions"][:, env_start_idx:env_start_idx+self.max_envs_per_file_in_memory])

        # Validate shapes
        if inputs.shape != (steps_per_file, self.max_envs_per_file_in_memory, inputs.shape[-1]):
            raise ValueError(f"[ERROR]: Input shape mismatch in file {file_path}.")
        if targets.shape != (steps_per_file, self.max_envs_per_file_in_memory, targets.shape[-1]):
            raise ValueError(f"[ERROR]: Target shape mismatch in file {file_path}.")

        del folder_path, file_name, steps_per_file, parallel_envs

        return inputs, targets

    def _cache_file(self, folder_idx, file_idx, env_start_idx):
        """
        Cache a specific file, loading it if not already cached.

        Args:
            folder_idx (int): Folder index.
            file_idx (int): File index within the folder.

        Returns:
            tuple: (inputs, targets) from the file.
        """
        cache_key = (folder_idx, file_idx, env_start_idx)
        # print(f"[INFO]: Caching file {cache_key}... keys = {self.cache.keys()}")
        cached_file = self.cache.get(cache_key)
        if cached_file is None:
            # print(f"can't find cached file for {cache_key}, only got {self.cache.keys()}")
            inputs, targets = self._load_file(folder_idx, file_idx, env_start_idx)
            self.cache.put(cache_key, (inputs, targets))
            return inputs, targets
            # self.cache_hit_count.update(0, 1)
        # else:
            # self.cache_hit_count.update(1, 1 / self.batch_size)
            # print(f"[INFO]: Cached file found {cache_key}")
            # if self.cache_hit_count.count % 1000000:
            #     print(f"[INFO]: Cache hit rate: {self.cache_hit_count.avg}")
        return cached_file

    def __getitem__(self, index):
        """
        Get a sample from the dataset.

        Args:
            index (tuple): A four-tuple (folder_idx, file_idx, step, env) specifying the sample.

        Returns:
            tuple: Transformed input and target for the sample.
        """

        folder_idx, file_idx, env_start_idx, step, env = index

        # Load data from cache or file
        start_time = time.time()
        inputs, targets = self._cache_file(folder_idx, file_idx, env_start_idx)
        io_time = time.time() - start_time

        # Retrieve specific sample within the file
        input_sample = inputs[step, env]
        target_sample = targets[step, env]
        del inputs, targets

        # Get metadata for transformation
        metadata = self.metadata_list[folder_idx]  # potential copy-on-write behavior if using native python list

        return input_sample, target_sample, metadata, self.folder_idx_to_file_name[folder_idx], torch.tensor(io_time)

    def _transform_samples(self, input_samples, target_samples, metadata_list, robot_name=None):
        """
        Transform a single input and target sample into its components.

        Args:
            input_samples (np.ndarray): The input sample (shape: [B, D]).
            target_samples (np.ndarray): The target sample (shape: [B, T]).
            metadata (dict): Metadata list for samples.
            robot_name (str): Robot name for limb shape lookup (optional).

        Returns:
            tuple: Transformed components.
        """
        assert all(metadata == metadata_list[0] for metadata in metadata_list), \
            "the metadata for all samples in batch should be identical"
        metadata = metadata_list[0]

        batch_size = len(target_samples)

        # Returns CPU tensors; the training loop moves them to CUDA. This is required
        # for safe use with num_workers > 0 (CUDA cannot be initialised in worker processes).
        state = torch.from_numpy(np.stack(input_samples, axis=0)).to(dtype=torch.float32)  # Shape: (B, D)
        target = torch.from_numpy(np.stack(target_samples, axis=0)).to(dtype=torch.float32)  # Shape: (B, A)

        # Dynamic Joint Data Transformation
        dynamic_joint_observation_length = metadata["dynamic_joint_observation_length"]
        nr_dynamic_joint_observations = metadata["nr_dynamic_joint_observations"]
        single_dynamic_joint_observation_length = metadata["single_dynamic_joint_observation_length"]
        dynamic_joint_description_size = metadata["dynamic_joint_description_size"]

        dynamic_joint_combined_state = state[..., :dynamic_joint_observation_length]  # Focus only on last dim
        dynamic_joint_combined_state = dynamic_joint_combined_state.view(
            batch_size, nr_dynamic_joint_observations, single_dynamic_joint_observation_length
        )
        dynamic_joint_description = dynamic_joint_combined_state[..., :dynamic_joint_description_size]
        dynamic_joint_state = dynamic_joint_combined_state[..., dynamic_joint_description_size:]

        # Inject limb shape information if enabled
        if self.use_limb_bboxes and robot_name is not None:
            # Get joint names from robot description
            desc = self.robot_desc_cache.get(robot_name)
            if desc is not None and 'joint_info' in desc:
                all_joint_names = list(desc['joint_info'].keys())
                
                # Validate joint count
                if len(all_joint_names) < nr_dynamic_joint_observations:
                    raise ValueError(
                        f"Robot '{robot_name}' has {len(all_joint_names)} joints in description file, "
                        f"but dataset metadata expects {nr_dynamic_joint_observations}. "
                        f"Please check: (1) robot URDF joint count, (2) dataset metadata"
                    )
                
                joint_names = all_joint_names[:nr_dynamic_joint_observations]
                limb_bboxes = self._get_limb_bbox_for_batch(robot_name, joint_names)
                limb_bboxes = limb_bboxes.unsqueeze(0).expand(batch_size, -1, -1)  # CPU; moves to CUDA in training loop
                
                # Note: limb bboxes are NOT normalized (raw values in meters)
                # This differs from foot_size in locomotion_env.py which is normalized.
                # Raw values preserve scale information across different robot sizes.
                
                # Concatenate to description vector: 18 -> 24 dims
                dynamic_joint_description = torch.cat([
                    dynamic_joint_description, limb_bboxes
                ], dim=-1)
                
                # Validate expected shape after concatenation
                expected_dim = dynamic_joint_description_size + self.extra_des_dim
                assert dynamic_joint_description.shape[-1] == expected_dim, \
                    f"Shape mismatch after bbox concat: got {dynamic_joint_description.shape[-1]}, expected {expected_dim}"

        # General Policy State Transformation
        trunk_angular_vel_update_obs_idx = metadata["trunk_angular_vel_update_obs_idx"]
        goal_velocity_update_obs_idx = metadata["goal_velocity_update_obs_idx"]
        projected_gravity_update_obs_idx = metadata["projected_gravity_update_obs_idx"]
        general_policy_state = state[..., trunk_angular_vel_update_obs_idx+goal_velocity_update_obs_idx+projected_gravity_update_obs_idx]
        general_policy_state = torch.cat((general_policy_state, state[..., -self.GENERAL_POLICY_STATE_LEN:]), dim=-1) # gains_and_action_scaling_factor; mass; robot_dimensions; nr_joints; foot dimension

        del dynamic_joint_observation_length, nr_dynamic_joint_observations, single_dynamic_joint_observation_length, \
            dynamic_joint_description_size, trunk_angular_vel_update_obs_idx, goal_velocity_update_obs_idx, \
            projected_gravity_update_obs_idx

        # add a small Gaussian noise to improve model robustness
        # dynamic_joint_description += torch.randn_like(dynamic_joint_description) * 0.005
        # dynamic_joint_state += torch.randn_like(dynamic_joint_state) * 0.005    # already randomized during data collection
        # general_policy_state += torch.randn_like(general_policy_state) * 0.005

        # Return transformed inputs and target
        return (
            dynamic_joint_description,  # Shape: (nr_dynamic_joint_observations, dynamic_joint_description_size) or (nr_dynamic_joint_observations, dynamic_joint_description_size + extra_des_dim) if bbox mode
            dynamic_joint_state,  # Shape: (nr_dynamic_joint_observations, remaining_length)
            general_policy_state,  # Shape: (<concatenated_dim>)
            target  # Shape: (12,)
        )

    def collate_fn(self, batch):
        """
        Collate function to combine samples into a batch.

        Args:
            batch (list): List of samples, where each sample is a 2-tuple:
                          (inputs, target).

        Returns:
            tuple: A 2-tuple where:
                - The first element is a tuple of batched inputs (stacked by component).
                - The second element is the batched target tensor.
        """
        # Split batch into inputs and targets
        inputs, targets, metadata_list, robot_names, io_times = zip(*batch)  # inputs: list of tuples, targets: list of tensors
        assert len(set(robot_names)) == 1, f"got different robot names in a batch: {set(robot_names)}"

        # batch transform these samples (pass robot_name for limb shape conditioning)
        st = time.time()
        transformed_sample = self._transform_samples(inputs, targets, metadata_list, robot_name=robot_names[0])
        inputs, targets = transformed_sample[:-1], transformed_sample[-1]
        processing_times = time.time() - st

        # # Transpose the inputs to group by component
        # inputs_by_component = zip(*inputs)  # Converts list of tuples into tuples of components
        batched_inputs = inputs

        # # Stack each component of the inputs
        # batched_inputs = tuple(torch.stack(components) for components in inputs_by_component)

        # # Stack the targets
        # batched_targets = torch.stack(targets)
        batched_targets = targets

        return batched_inputs, batched_targets, robot_names[0], torch.stack(io_times), torch.tensor(processing_times)

    def get_batch_indices(self, batch_size, shuffle=True, num_workers=1):
        """
        Generate all indices for the dataset, ensuring (1) batches are interleaved across workers,
        (2) each worker processes batches from a specific file in sequence, and (3) adjacent batches
        for one worker come from the same file.

        The expectation is:
        Worker 1: [batch from K1.h5] [batch from K1.h5] ... [batch from K3.h5] [batch from K3.h5]
        Worker 2: [batch from K2.h5] [batch from K2.h5] ... [batch from K4.h5] [batch from K4.h5]
        This way, workers won't process the same .h5 and every .h5 won't be read from disk more than once.
        This way, workers won't process the same .h5 and every .h5 won't be read from disk more than once.

        Args:
            batch_size (int): The size of each batch.
            shuffle (bool): Whether to shuffle the dataset.
            num_workers (int): Number of workers in the DataLoader.

        Returns:
            list: A list of indices, interleaved for workers, where each sublist contains indices for a batch.
        """
        num_workers = max(num_workers, 1)

        self.batch_size = batch_size
        file_samples = {}  # Dictionary to hold batches per file

        # Collect batches for each file
        for (folder_idx, file_idx, env_start_idx), (_, _, steps_per_file, parallel_envs) in self.file_indices.items():
            # Get the index list
            # Repeat the list by the given times as if this were a longer file
            # so that we get more data from every .h5 file without additional IO
            indices = [(folder_idx, file_idx, env_start_idx, step, env)
                       for step in range(steps_per_file)
                       for env in range(self.max_envs_per_file_in_memory)] * self.h5_repeat_factor
            if shuffle:
                np.random.shuffle(indices)  # Shuffle indices within the file

            # Split indices into batches and store in file_batches
            file_samples[(folder_idx, file_idx, env_start_idx)] = [
                indices[i:i + batch_size] for i in range(0, len(indices), batch_size)
            ]

        # Get a shuffled list of file keys for iteration later
        file_keys = list(file_samples.keys())
        if shuffle:
            np.random.shuffle(file_keys)

        if len(file_keys) < num_workers:
            print(f'we only have {len(file_keys)} files for {num_workers} workers. we will repeat some files '
                  f'so that every worker at at least one .h5')
            file_keys += [random.choice(file_keys) for _ in range(num_workers - len(file_keys))]

        # Distribute batches across workers in an interleaved manner
        # samples_per_worker will be a list of lists, where the inner list contains lists of samples, with
        # each list from one file
        # also record the mapping between worker and file keys
        file_sample_lists_per_worker = [[] for _ in range(num_workers)]
        self.worker_idx_to_folder_file_idx = {worker_idx: set() for worker_idx in range(num_workers)}
        for i, key in enumerate(file_keys):
            file_sample_lists_per_worker[i % num_workers].append(file_samples[key])
            self.worker_idx_to_folder_file_idx[i % num_workers].add(key)

        # assert 0 not in [len(x) for x in file_sample_lists_per_worker], \
        #     (f"Zero exists in file_sample_lists_per_worker: {file_sample_lists_per_worker}, "
        #      f"meaning that we don't have enough .h5 files for workers")

        # Duplicate samples so that every worker has the same number of samples
        # otherwise the workers that finish their job earlier will be assigned to join
        # other worker's job queue, which may create the condition where multiple workers
        # read the same file from the disk, making the system incredibly slow
        duplicates = 0
        max_files_per_worker = max(len(worker_batches) for worker_batches in file_sample_lists_per_worker)
        for worker_idx, worker_samples in enumerate(file_sample_lists_per_worker):
            while len(worker_samples) < max_files_per_worker:
                sampled_file_samples = random.choice(file_sample_lists_per_worker[worker_idx])  # sample a file sample list
                worker_samples.append(sampled_file_samples)
                duplicates += len(sampled_file_samples)     # record number of duplicates for logging
            file_sample_lists_per_worker[worker_idx] = worker_samples

        # flatten the inner 2-layer nested lists into one 1-layer list
        samples_per_worker = [list(chain(*worker_sample_lists)) for worker_sample_lists in file_sample_lists_per_worker]
        assert all(len(samples) == len(samples_per_worker[0]) for samples in samples_per_worker), \
            (f"the number of samples for workers differ: {[len(samples) for samples in samples_per_worker]}"
             f"This function assumes all files have the same number of samples. Is this true?")

        # Interleave batches from all workers to form the final sequence
        final_samples = []
        max_samples_per_worker = max(len(worker_samples) for worker_samples in samples_per_worker)
        for i in range(max_samples_per_worker):
            cycle_samples = []
            for worker_idx, samples in enumerate(samples_per_worker):
                cycle_samples.append(samples[i])
            
            # shuffle the samples in one cycle, if desirable
            random.shuffle(cycle_samples)

            final_samples.extend(cycle_samples)

        print(f'[INFO]: h5_repeat_factor = {self.h5_repeat_factor}. '
              f'additional duplicates due to resample: {duplicates} out of {len(final_samples)} samples '
              f'({duplicates/len(final_samples)*100:.2f}%)')

        return final_samples

    def get_data_loader(self, batch_size, shuffle=True, num_workers=16, **kwargs):
        """
        Create a DataLoader for the dataset.

        Args:
            batch_size (int): Batch size for the DataLoader.
            shuffle (bool): Whether to shuffle the dataset.

        Returns:
            DataLoader: The configured DataLoader instance.
        """

        if num_workers > len(self.file_indices):
            warnings.warn(f"num_workers={num_workers} should not exceed the number of files to read={len(self.file_indices)}, "
             f"as this would cause torch DataLoader to be extremely slow with our dataset implementation. "
             f"This is likely due to multiple threads reading the same file. "
             f"I will set num_workers to {min(num_workers, len(self.file_indices))}")
            num_workers = min(num_workers, len(self.file_indices))        # 2 is a safe number, tested

        if num_workers > 0:
            print(f"[INFO]: Using num_workers={num_workers}. "
                  f"num_workers=1 keeps cache RAM identical to num_workers=0 (one worker, one cache). "
                  f"num_workers>1 multiplies cache RAM by num_workers. "
                  f"Each worker maintains its own h5py handles and file cache (max_files={self.max_files_in_memory}).")

        assert self.max_files_in_memory > 0, "max_files_in_memory must be > 0"

        self._prepare_file_indices()  # re-sample the dataset

        # When using real workers, distribute batches across num_workers slots so each worker
        # stays on its own subset of files and the per-worker cache stays hot.
        # When num_workers=0 the main process handles everything; use max_files_in_memory as
        # the virtual-worker count so the cache-friendly access pattern is preserved.
        n_batch_slots = num_workers if num_workers > 0 else self.max_files_in_memory

        return DataLoader(
            self,
            batch_sampler=self.get_batch_indices(batch_size, shuffle, n_batch_slots),
            collate_fn=self.collate_fn,
            num_workers=num_workers,
            pin_memory=(num_workers > 0),   # pin_memory speeds up CPU->GPU transfers when using workers
            # NOTE: persistent_workers is intentionally False — a new DataLoader is created each
            # epoch so workers are destroyed anyway; setting True here can cause stale-state bugs.
            persistent_workers=False,
            prefetch_factor=4 if num_workers > 0 else None,
            # **kwargs
        )
