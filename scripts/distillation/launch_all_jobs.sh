#!/bin/bash
# Launch all distillation jobs (excluding data_scaling) via SLURM multirun.
# Usage: bash distillation/launch_all_jobs.sh [extra hydra overrides...]
# Example: bash distillation/launch_all_jobs.sh dataloading.max_files_in_memory=256

set -euo pipefail
cd "$(dirname "$0")/.."  # cd to scripts/

CONFIGS=(
  all_robot_jobs_v7_allrobots_0.05
  all_robot_jobs_v7_allrobots_0.1
  all_robot_jobs_v7_allrobots_0.2
  all_robot_jobs_v7_allrobots_0.4
  all_robot_jobs_v7_allrobots_0.6
  all_robot_jobs_v7_allrobots_0.8
  all_robot_jobs_v7_allrobots_1.0
  all_robot_jobs_v7_allrobots_test_set
  hexapod_jobs_v7_hexapod_distillation_0.05
  hexapod_jobs_v7_hexapod_distillation_0.1
  hexapod_jobs_v7_hexapod_distillation_0.2
  hexapod_jobs_v7_hexapod_distillation_0.4
  hexapod_jobs_v7_hexapod_distillation_0.6
  hexapod_jobs_v7_hexapod_distillation_0.8
  hexapod_jobs_v7_hexapod_distillation_1.0
  hexapod_jobs_v7_hexapod_test_set
  humanoid_jobs_v7_humanoid_distillation_0.05
  humanoid_jobs_v7_humanoid_distillation_0.1
  humanoid_jobs_v7_humanoid_distillation_0.2
  humanoid_jobs_v7_humanoid_distillation_0.4
  humanoid_jobs_v7_humanoid_distillation_0.6
  humanoid_jobs_v7_humanoid_distillation_0.8
  humanoid_jobs_v7_humanoid_distillation_1.0
  humanoid_jobs_v7_humanoid_test_set
  quadruped_jobs_v7_quadruped_0.025
  quadruped_jobs_v7_quadruped_0.05
  quadruped_jobs_v7_quadruped_0.1
  quadruped_jobs_v7_quadruped_0.2
  quadruped_jobs_v7_quadruped_0.4
  quadruped_jobs_v7_quadruped_0.6
  quadruped_jobs_v7_quadruped_0.8
  quadruped_jobs_v7_quadruped_1.0
  quadruped_jobs_v7_quadruped_test_set
)

SLURM_ARGS=(
  --multirun
  hydra/launcher=firsbatch
  +hydra/sweep=sbatch
  hydra.launcher._target_=hydra_plugins.packed_launcher.packedlauncher.SlurmLauncher
  hydra.launcher.tasks_per_node=1
  +hydra.launcher.timeout_min=10000
  hydra.launcher.cpus_per_task=6
  hydra.launcher.mem_gb=128
  hydra.launcher.array_parallelism=300
)

for cfg in "${CONFIGS[@]}"; do
  echo "=== Launching: $cfg ==="
  python3 distillation/run_distillation.py \
    --config-name "$cfg" \
    "${SLURM_ARGS[@]}" \
    "$@"
done
