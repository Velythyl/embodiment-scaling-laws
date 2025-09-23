#!/bin/bash

# Check if tasks are provided
if [[ "$#" -lt 2 ]]; then
  echo "Usage: bash train_batch.sh --tasks task1 task2 ... [additional arguments]"
  exit 1
fi

# Parse tasks and additional arguments
if [[ "$1" == "--tasks" ]]; then
  shift
  # Collect tasks until the first non-task flag
  while [[ "$#" -gt 0 && "$1" != --* ]]; do
    tasks+=("$1")
    shift
  done
else
  echo "Expected --tasks flag"
  exit 1
fi

# Remaining arguments are treated as additional keyword arguments
kwargs=("$@")

# Print the tasks to be executed and additional arguments
echo "Tasks to be executed: ${tasks[@]}"
echo "Additional arguments: ${kwargs[@]}"

# Function to handle interrupt and exit
function stop_execution {
  echo "Training interrupted. Exiting."
  exit 1
}

# Trap SIGINT (Ctrl+C) and call stop_execution
trap stop_execution SIGINT

# Execute training for each specified task
for task in "${tasks[@]}"; do
  echo "Starting training for task: $task"
  python scripts/rsl_rl/train.py --task "$task" --headless "${kwargs[@]}" || stop_execution
  echo "Completed training for task: $task"
done
