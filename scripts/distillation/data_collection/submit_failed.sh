#!/bin/bash
# Submit data collection scripts for failed experiments

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for script in "$SCRIPT_DIR"/collect_data_failed_*.sh; do
    script_name=$(basename "$script" .sh)
    
    sbatch <<EOF
#!/bin/bash
#SBATCH --job-name=${script_name}
#SBATCH --partition=main
#SBATCH --gres=gpu:rtx8000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=24G
#SBATCH --time=2-00:00:00
#SBATCH --output=logs/slurm/%x_%j.out
#SBATCH --error=logs/slurm/%x_%j.err

cd "$SCRIPT_DIR/../../.."
source env_isaaclab/bin/activate

bash "$script"
EOF

    echo "Submitted: $script_name"
done
