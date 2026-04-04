#!/usr/bin/env python3
"""Migrate old argparse-based Hydra configs to native structured Hydra configs.

Creates proper Hydra config group composition:
  conf/
    config.yaml                    # base with defaults
    meta/default.yaml              # shared meta (wandb, SLURM, etc.)
    ablation/default.yaml          # description vec ablation settings
    optim/<profile>.yaml           # distinct optim profiles
    dataloading/<profile>.yaml     # distinct dataloading profiles
    <job>.yaml                     # defaults list + train_set/test_set

Usage:
    python migrate_configs.py          # dry-run (prints to stdout)
    python migrate_configs.py --write  # overwrite configs in-place
"""
import argparse
import os
import sys
import shlex
import glob
import json
import hashlib
from collections import OrderedDict

import yaml


# --------------------------------------------------------------------------- #
# The SAME argparse parser that run_distillation.py defines
# --------------------------------------------------------------------------- #
def build_legacy_parser():
    parser = argparse.ArgumentParser(description="(legacy parser for migration)")
    parser.add_argument("--train_set", nargs="+", type=str, default=None)
    parser.add_argument("--test_set", nargs="+", type=str, default=None)
    parser.add_argument("--num_epochs", type=int, default=10)
    parser.add_argument("--batch_size", type=int, default=256)
    parser.add_argument("--exp_name", type=str, default=None)
    parser.add_argument("--checkpoint_interval", type=int, default=5)
    parser.add_argument("--log_dir", type=str, default="log_dir")
    parser.add_argument("--lr", type=float, default=3e-4)
    parser.add_argument("--num_workers", type=int, default=0)
    parser.add_argument("--max_files_in_memory", type=int, default=1)
    parser.add_argument("--val_ratio", type=float, default=0.15)
    parser.add_argument("--gradient_acc_steps", type=int, default=1)
    parser.add_argument("--h5_repeat_factor", type=int, default=1)
    parser.add_argument("--warmup_pct", type=float, default=0.0)
    parser.add_argument("--use_amp", type=int, default=0)
    parser.add_argument("--max_parallel_envs_per_file", type=int, default=2048)
    parser.add_argument("--max_envs_per_file_in_memory", type=int, default=512)
    parser.add_argument("--model", type=str, default="urma")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("--dataset_dir", type=str, default="logs/rsl_rl")
    parser.add_argument("--resume", type=str, default=None)
    parser.add_argument("--log_epoch_pct", type=float, default=2.0)
    parser.add_argument("--description_filename", type=str, default=None)
    parser.add_argument("--asset_base_path", type=str,
                        default=os.path.join(os.environ.get("SCRATCH", ""),
                                             "embodiment-scaling-laws/exts/embodiment_scaling_laws/"
                                             "embodiment_scaling_laws/assets/Robots/GenBot1K-v7"))
    parser.add_argument("--wandb", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--wandb_project", type=str, default="esl_apr2")
    parser.add_argument("--wandb_entity", type=str, default="velythyl")
    parser.add_argument("--wandb_name", type=str, default=None)
    return parser


# --------------------------------------------------------------------------- #
# YAML helpers
# --------------------------------------------------------------------------- #
def _none_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:null", "null")

yaml.add_representer(type(None), _none_representer)

def _block_list_representer(dumper, data):
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=False)

yaml.add_representer(list, _block_list_representer)


def yaml_dump(d):
    return yaml.dump(d, default_flow_style=False, sort_keys=False, width=200, allow_unicode=True)


def extract_comments(filepath):
    """Extract leading comment lines from a YAML file."""
    comments = []
    with open(filepath) as f:
        for line in f:
            if line.startswith("#"):
                comments.append(line.rstrip())
            else:
                break
    return "\n".join(comments) if comments else ""


def dict_hash(d):
    """Stable short hash for a dict (for dedup)."""
    s = json.dumps(d, sort_keys=True)
    return hashlib.md5(s.encode()).hexdigest()[:8]


# --------------------------------------------------------------------------- #
# Extract optim / dataloading dicts from parsed args
# --------------------------------------------------------------------------- #
def extract_optim(args):
    return OrderedDict([
        ("lr", args.lr),
        ("num_epochs", args.num_epochs),
        ("gradient_acc_steps", args.gradient_acc_steps),
        ("warmup_pct", args.warmup_pct),
        ("use_amp", bool(args.use_amp)),
        ("checkpoint_interval", args.checkpoint_interval),
        ("log_epoch_pct", args.log_epoch_pct),
    ])


def extract_dataloading(args):
    return OrderedDict([
        ("batch_size", args.batch_size),
        ("num_workers", args.num_workers),
        ("max_files_in_memory", args.max_files_in_memory),
        ("max_parallel_envs_per_file", args.max_parallel_envs_per_file),
        ("max_envs_per_file_in_memory", args.max_envs_per_file_in_memory),
        ("h5_repeat_factor", args.h5_repeat_factor),
        ("val_ratio", args.val_ratio),
        ("dataset_dir", args.dataset_dir),
    ])


def name_optim(d):
    """Generate a human-readable name for an optim profile."""
    lr_str = f"{d['lr']:.0e}".replace("+", "").replace("-0", "-")
    parts = [
        f"e{d['num_epochs']}",
        f"lr{lr_str}",
        f"acc{d['gradient_acc_steps']}",
    ]
    if d["warmup_pct"] > 0:
        parts.append(f"warmup{d['warmup_pct']}")
    if d["use_amp"]:
        parts.append("amp")
    return "_".join(parts)


def name_dataloading(d):
    """Generate a human-readable name for a dataloading profile."""
    parts = [
        f"bs{d['batch_size']}",
        f"mem{d['max_files_in_memory']}",
        f"env{d['max_envs_per_file_in_memory']}",
        f"rep{d['h5_repeat_factor']}",
    ]
    if d["max_parallel_envs_per_file"] != 2048:
        parts.append(f"par{d['max_parallel_envs_per_file']}")
    return "_".join(parts)


# --------------------------------------------------------------------------- #
# Build shared group configs
# --------------------------------------------------------------------------- #
def build_meta_default():
    return OrderedDict([
        ("project", "morphoaware"),
        ("run_name", "debuggingMetamorph"),
        ("tags", []),
        ("seed", -1),
        ("wandb_mode", "online"),
        ("SLURM_JOB_ID", "${oc.env:SLURM_JOB_ID,null}"),
        ("SLURM_ARRAY_JOB_ID", "${oc.env:SLURM_ARRAY_JOB_ID,null}"),
        ("SLURM_ARRAY_TASK_ID", "${oc.env:SLURM_ARRAY_TASK_ID,null}"),
        ("HYDRA_SWEEP_DIR", "${oc.env:HYDRA_SWEEP_DIR,null}"),
        ("SLURM_HYDRA_DIR", "${oc.env:HYDRA_SWEEP_DIR,null}/${oc.env:SLURM_ARRAY_TASK_ID,null}/.hydra"),
        ("SLURM_HYDRA_OVERRIDES", "${oc.env:HYDRA_SWEEP_DIR,null}/${oc.env:SLURM_ARRAY_TASK_ID,null}/.hydra/overrides.yaml"),
        ("SLURM_TMPDIR", "${oc.env:SLURM_TMPDIR,null}"),
        ("CUDA_VISIBLE_DEVICES", "${hwinfo:gpu}"),
        ("notes", ""),
        ("sys_argv", ""),
    ])


def build_ablation_default():
    return OrderedDict([
        ("description_filename", None),
        ("asset_base_path",
         "${oc.env:SCRATCH,}/embodiment-scaling-laws/exts/embodiment_scaling_laws/"
         "embodiment_scaling_laws/assets/Robots/GenBot1K-v7"),
    ])


# --------------------------------------------------------------------------- #
# Main migration logic
# --------------------------------------------------------------------------- #
def parse_all_configs(conf_dir, parser):
    """First pass: parse all configs, collect unique optim/dataloading profiles."""
    yaml_files = sorted(glob.glob(os.path.join(conf_dir, "*.yaml")))
    parsed = []

    for filepath in yaml_files:
        filename = os.path.basename(filepath)
        with open(filepath) as f:
            raw = yaml.safe_load(f)
        if raw is None or "argparse" not in raw:
            print(f"  SKIP (no argparse field): {filename}")
            continue

        full_str = raw["argparse"] + " " + raw.get("append_argparse", "")
        argv = shlex.split(full_str)
        args, unknown = parser.parse_known_args(argv)
        if unknown:
            print(f"  WARNING: unknown args in {filename}: {unknown}")

        comments = extract_comments(filepath)
        parsed.append((filepath, filename, args, comments))

    return parsed


def deduplicate_profiles(parsed):
    """Find unique optim and dataloading profiles across all configs."""
    # hash → (name, dict)
    optim_profiles = OrderedDict()
    dataloading_profiles = OrderedDict()

    # Also track which config maps to which profile name
    config_optim = {}      # filepath → optim_name
    config_dataloading = {}  # filepath → dataloading_name

    for filepath, filename, args, _ in parsed:
        od = dict(extract_optim(args))
        dd = dict(extract_dataloading(args))
        oh = dict_hash(od)
        dh = dict_hash(dd)

        if oh not in optim_profiles:
            oname = name_optim(od)
            # Disambiguate if name collision
            existing_names = {v[0] for v in optim_profiles.values()}
            if oname in existing_names:
                oname = f"{oname}_{oh}"
            optim_profiles[oh] = (oname, od)
        config_optim[filepath] = optim_profiles[oh][0]

        if dh not in dataloading_profiles:
            dname = name_dataloading(dd)
            existing_names = {v[0] for v in dataloading_profiles.values()}
            if dname in existing_names:
                dname = f"{dname}_{dh}"
            dataloading_profiles[dh] = (dname, dd)
        config_dataloading[filepath] = dataloading_profiles[dh][0]

    return optim_profiles, dataloading_profiles, config_optim, config_dataloading


def build_job_yaml(filename, args, comments, optim_name, dataloading_name):
    """Build the new job-level YAML string."""
    lines = []
    if comments:
        lines.append(comments)
        lines.append("")

    lines.append("defaults:")
    lines.append("  - meta: default")
    lines.append(f"  - optim: {optim_name}")
    lines.append(f"  - dataloading: {dataloading_name}")
    lines.append("  - ablation: default")
    lines.append("  - _self_")
    lines.append("  - secrets: secrets")
    lines.append("")

    # Job-specific overrides
    run_name = args.exp_name or filename.replace(".yaml", "")
    body = OrderedDict()
    body["meta"] = {"run_name": run_name}
    body["log_dir"] = args.log_dir
    body["resume"] = args.resume
    body["train_set"] = list(args.train_set) if args.train_set else []
    body["test_set"] = list(args.test_set) if args.test_set else []

    lines.append(yaml_dump(dict(body)))
    return "\n".join(lines)


def build_base_config_yaml():
    """Build the main config.yaml."""
    lines = []
    lines.append("# Base configuration for run_distillation.py")
    lines.append("# Override with: python run_distillation.py --config-name=<job>")
    lines.append("")
    lines.append("defaults:")
    lines.append("  - meta: default")
    lines.append("  - optim: default")
    lines.append("  - dataloading: default")
    lines.append("  - ablation: default")
    lines.append("  - _self_")
    lines.append("  - secrets: secrets")
    lines.append("")
    body = {
        "log_dir": "log_dir",
        "resume": None,
        "train_set": [],
        "test_set": [],
    }
    lines.append(yaml_dump(body))
    return "\n".join(lines)


def main():
    script_parser = argparse.ArgumentParser(
        description="Migrate argparse configs to structured Hydra config groups")
    script_parser.add_argument("--write", action="store_true",
                               help="Write changes (default: dry-run)")
    script_args = script_parser.parse_args()

    conf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conf")
    legacy_parser = build_legacy_parser()

    # --- Pass 1: parse everything ---
    parsed = parse_all_configs(conf_dir, legacy_parser)
    print(f"\nParsed {len(parsed)} config files")

    # --- Pass 2: deduplicate optim/dataloading ---
    optim_profiles, dataloading_profiles, config_optim, config_dataloading = \
        deduplicate_profiles(parsed)

    print(f"\nFound {len(optim_profiles)} distinct optim profiles:")
    for h, (name, d) in optim_profiles.items():
        print(f"  {name}: epochs={d['num_epochs']} lr={d['lr']} acc={d['gradient_acc_steps']}")

    print(f"\nFound {len(dataloading_profiles)} distinct dataloading profiles:")
    for h, (name, d) in dataloading_profiles.items():
        print(f"  {name}: bs={d['batch_size']} mem={d['max_files_in_memory']} "
              f"env={d['max_envs_per_file_in_memory']} rep={d['h5_repeat_factor']} "
              f"par={d['max_parallel_envs_per_file']}")

    # Pick the most common optim/dataloading as "default"
    from collections import Counter
    most_common_optim = Counter(config_optim.values()).most_common(1)[0][0]
    most_common_dl = Counter(config_dataloading.values()).most_common(1)[0][0]
    print(f"\nMost common optim → 'default': {most_common_optim}")
    print(f"Most common dataloading → 'default': {most_common_dl}")

    if not script_args.write:
        print("\n" + "=" * 60)
        print("DRY RUN — use --write to create files")
        print("=" * 60)

    # --- Write shared group configs ---
    files_to_write = {}

    # meta/default.yaml
    files_to_write[os.path.join(conf_dir, "meta", "default.yaml")] = \
        yaml_dump(dict(build_meta_default()))

    # ablation/default.yaml
    files_to_write[os.path.join(conf_dir, "ablation", "default.yaml")] = \
        yaml_dump(dict(build_ablation_default()))

    # optim/<name>.yaml  (also write "default.yaml" as alias for most common)
    for h, (name, d) in optim_profiles.items():
        files_to_write[os.path.join(conf_dir, "optim", f"{name}.yaml")] = yaml_dump(dict(d))
        if name == most_common_optim:
            files_to_write[os.path.join(conf_dir, "optim", "default.yaml")] = yaml_dump(dict(d))

    # dataloading/<name>.yaml
    for h, (name, d) in dataloading_profiles.items():
        files_to_write[os.path.join(conf_dir, "dataloading", f"{name}.yaml")] = yaml_dump(dict(d))
        if name == most_common_dl:
            files_to_write[os.path.join(conf_dir, "dataloading", "default.yaml")] = yaml_dump(dict(d))

    # config.yaml (base)
    files_to_write[os.path.join(conf_dir, "config.yaml")] = build_base_config_yaml()

    # --- Write job configs ---
    for filepath, filename, args, comments in parsed:
        optim_name = config_optim[filepath]
        dataloading_name = config_dataloading[filepath]
        content = build_job_yaml(filename, args, comments, optim_name, dataloading_name)
        files_to_write[filepath] = content

    # --- Output ---
    for fpath, content in sorted(files_to_write.items()):
        if script_args.write:
            os.makedirs(os.path.dirname(fpath), exist_ok=True)
            with open(fpath, "w") as f:
                f.write(content)
            print(f"  WROTE: {fpath}")
        else:
            # Show a preview for non-job configs (job configs are huge)
            is_job = fpath.endswith(".yaml") and os.path.dirname(fpath) == conf_dir and \
                     os.path.basename(fpath) != "config.yaml"
            print(f"\n{'='*80}")
            print(f"FILE: {fpath}")
            print(f"{'='*80}")
            if is_job:
                # Just show first 40 lines (defaults + meta override), skip robot lists
                preview_lines = content.split("\n")[:40]
                print("\n".join(preview_lines))
                if len(content.split("\n")) > 40:
                    print(f"  ... ({len(content.split(chr(10)))} lines total)")
            else:
                print(content)

    print(f"\n{'='*60}")
    print(f"Total files: {len(files_to_write)}")
    if not script_args.write:
        print("Re-run with --write to apply changes")
    print("Done!")


if __name__ == "__main__":
    main()
