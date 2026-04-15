#!/bin/bash
# Launch suite of distillation jobs across different data fractions
# Copy and paste this entire script into a terminal

cd /home/mila/c/charlie.gauthier/embodiment-scaling-laws/scripts

# ============================================================
# EDIT YOUR COMMAND TEMPLATE HERE
# ============================================================
# Base command (everything except --config-name)
CMD_TEMPLATE='python3 launch_distillation.py --config-name CONFIG_PLACEHOLDER --multirun hydra/launcher=firsbatch +hydra/sweep=sbatch hydra.launcher._target_=hydra_plugins.packed_launcher.packedlauncher.SlurmLauncher hydra.launcher.tasks_per_node=1 +hydra.launcher.timeout_min=179 hydra.launcher.cpus_per_task=6 hydra.launcher.mem_gb=128 hydra.launcher.array_parallelism=300 meta=auto optim.gradient_acc_steps=1 dataloading.h5_repeat_factor=3 dataloading.num_workers=5 dataloading.batch_size=1024 optim.lr=0.0006 ablation=vme_full meta.project=esl_apr10_requeue meta.seed=-1,-1,-1,-1,-1 hydra.launcher.name=esl_requeue'

# ============================================================
# Data fractions to loop over
# ============================================================
FRACTIONS=(0.05 0.1 0.2 0.4 0.6 0.8 1.0)

# ============================================================
# How long to wait for job submission (seconds)
# Increase if submission takes longer
# ============================================================
WAIT_FOR_SUBMISSION=60
CHECK_INTERVAL=2

for FRAC in "${FRACTIONS[@]}"; do
    CONFIG_NAME="all_robot_jobs_v7_allrobots_${FRAC}"
    echo ""
    echo "============================================================"
    echo "Launching config: ${CONFIG_NAME}"
    echo "============================================================"
    
    # Build the actual command
    CMD="${CMD_TEMPLATE//CONFIG_PLACEHOLDER/${CONFIG_NAME}}"
    
    echo "Running: ${CMD}"
    echo ""
    
    # Launch in background and capture PID
    eval "$CMD" &
    PID=$!
    
    echo "Started process with PID: ${PID}"
    
    # Wait for jobs to be submitted
    # We detect this by checking if new SLURM jobs appear with our name
    INITIAL_JOBS=$(squeue -u $USER -h | wc -l)
    ELAPSED=0
    SUBMITTED=false
    
    while [ $ELAPSED -lt $WAIT_FOR_SUBMISSION ]; do
        sleep $CHECK_INTERVAL
        ELAPSED=$((ELAPSED + CHECK_INTERVAL))
        
        # Check if process is still running
        if ! kill -0 $PID 2>/dev/null; then
            echo "Process exited on its own after ${ELAPSED}s"
            SUBMITTED=true
            break
        fi
        
        # Check if new jobs appeared in SLURM queue
        CURRENT_JOBS=$(squeue -u $USER -h | wc -l)
        if [ $CURRENT_JOBS -gt $INITIAL_JOBS ]; then
            echo "Detected new SLURM jobs (${INITIAL_JOBS} -> ${CURRENT_JOBS}) after ${ELAPSED}s"
            SUBMITTED=true
            break
        fi
        
        echo "  Waiting... (${ELAPSED}s elapsed, jobs: ${CURRENT_JOBS})"
    done
    
    # Kill the background process if still running
    if kill -0 $PID 2>/dev/null; then
        echo "Killing launcher process (PID: ${PID})"
        kill $PID 2>/dev/null
        wait $PID 2>/dev/null
    fi
    
    if [ "$SUBMITTED" = true ]; then
        echo "Jobs submitted for ${CONFIG_NAME}"
    else
        echo "WARNING: Timed out waiting for job submission for ${CONFIG_NAME}"
    fi
    
    # Small delay before next iteration
    sleep 2
done

echo ""
echo "============================================================"
echo "All configs launched! Check your jobs with: squeue -u \$USER"
echo "============================================================"
