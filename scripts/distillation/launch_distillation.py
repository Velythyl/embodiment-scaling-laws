"""Lightweight Hydra entry point for submitit job submission.

This file intentionally avoids importing torch, CUDA, or any heavy ML
libraries so that cloudpickle can serialise the submitit job on a login
node that has no GPU.  The actual training code is imported lazily inside
``hydra_main`` only when execution reaches a compute node.
"""

import os
import sys
import shlex

import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="conf", config_name="config", version_base=None)
def hydra_main(cfg: DictConfig):
    """Hydra entry point."""
    # If HYDRA_SPOOF is set, we're in a submitit-unpickled process where sys.path
    # is wrong. Re-launch ourselves as a fresh subprocess from the correct directory.
    spoof_dir = os.environ.pop("HYDRA_SPOOF", None)
    if spoof_dir:
        import subprocess
        from hydra.core.hydra_config import HydraConfig

        hc = HydraConfig.get()
        overrides = list(hc.overrides.task)
        config_name = hc.job.config_name

        activate = os.path.normpath(os.path.join(spoof_dir, "..", "env_isaaclab", "bin", "activate"))
        script = os.path.join("distillation", "launch_distillation.py")
        cmd_parts = ["python", script, "--config-name", config_name] + overrides
        bash_cmd = f"source {shlex.quote(activate)} && cd {shlex.quote(spoof_dir)} && {shlex.join(cmd_parts)}"

        print(f"[INFO] HYDRA_SPOOF active, re-launching from {spoof_dir}")
        print(f"[INFO] bash -c {bash_cmd}")
        sys.stdout.flush()

        result = subprocess.run(["bash", "-c", bash_cmd], cwd=spoof_dir)
        sys.exit(result.returncode)

    # Store sys.argv in meta for reproducibility
    OmegaConf.update(cfg, "meta.sys_argv", " ".join(sys.argv), force_add=True)

    try:
        print("[INFO] hydra_main: importing and calling main()...")
        sys.stdout.flush()
        from run_distillation import main
        main(cfg)
        print("[INFO] hydra_main: main() completed successfully")
        sys.stdout.flush()
    except Exception as e:
        print(f"[ERROR] hydra_main: main() raised exception: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise


if __name__ == "__main__":
    print("[INFO] Script starting, calling hydra_main...")
    sys.stdout.flush()
    try:
        hydra_main()
    except Exception as e:
        print(f"[ERROR] Top-level exception: {e}")
        import traceback
        traceback.print_exc()
        sys.stdout.flush()
        raise


"""
# debugging
ln -s /home/mila/c/charlie.gauthier/embodiment-scaling-laws/ /tmp
python3 distillation/launch_distillation.py --config-name all_robot_jobs_v7_allrobots_1.0

# override dataloading at CLI
python3 distillation/launch_distillation.py --config-name all_robot_jobs_v7_allrobots_1.0 dataloading.max_files_in_memory=256

# override optim group
python3 distillation/launch_distillation.py --config-name all_robot_jobs_v7_allrobots_1.0 optim=e60_lr3e-4_acc8

# multirun with SLURM
python3 distillation/launch_distillation.py --config-name all_robot_jobs_v7_allrobots_1.0 --multirun hydra/launcher=firsbatch +hydra/sweep=sbatch hydra.launcher._target_=hydra_plugins.packed_launcher.packedlauncher.SlurmLauncher hydra.launcher.tasks_per_node=1 +hydra.launcher.timeout_min=10000 hydra.launcher.cpus_per_task=6 hydra.launcher.mem_gb=128 hydra.launcher.array_parallelism=300

optim.gradient_acc_steps=1 dataloading.h5_repeat_factor=3  dataloading.batch_size=8192 optim.lr=4.8e-3 optim.warmup_pct=0.05



## exps

python3 distillation/launch_distillation.py --config-name all_robot_jobs_v7_allrobots_1.0 --multirun hydra/launcher=firsbatch +hydra/sweep=sbatch hydra.launcher._target_=hydra_plugins.packed_launcher.packedlauncher.SlurmLauncher hydra.launcher.tasks_per_node=1 +hydra.launcher.timeout_min=4319 hydra.launcher.cpus_per_task=6 hydra.launcher.mem_gb=128 hydra.launcher.array_parallelism=300 optim.gradient_acc_steps=1 dataloading.h5_repeat_factor=3  dataloading.batch_size=8192 optim.lr=4.8e-3 optim.warmup_pct=0.05 ablation=no_bboxes,bboxes


"""
