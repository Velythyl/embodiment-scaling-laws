#!/bin/bash

# Check if tasks are provided
if [[ "$#" -lt 2 ]]; then
  echo "Usage: bash play_collect_data_batch.sh --tasks task1 task2 ... [additional arguments]"
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
  echo "Simulation interrupted. Exiting."
  exit 1
}

# Trap SIGINT (Ctrl+C) and call stop_execution
trap stop_execution SIGINT

total_elapsed=0
task_count=0
start_all=$(date +%s)

# Execute training for each specified task
for task in "${tasks[@]}"; do
  echo "Starting simulation for task: $task at $(date "+%T")"
  start_time=$(date +%s)

  python scripts/distillation/play_collect_data.py --task "$task" --reward_log_file reward_log_file.json --headless "${kwargs[@]}" || stop_execution

  end_time=$(date +%s)
  duration=$((end_time - start_time))
  total_elapsed=$((total_elapsed + duration))
  task_count=$((task_count + 1))
  avg_per_task=$((total_elapsed / task_count))
  est_total=$((avg_per_task * ${#tasks[@]}))
  remaining=$((est_total - total_elapsed))

  end_timestamp=$(date "+%T")
  finish_timestamp=$(date -d "+$remaining seconds" "+%T")

  # Convert total elapsed and estimated total time to HH:MM:SS
  format_time() { printf "%02d:%02d:%02d" $(($1/3600)) $((($1%3600)/60)) $(($1%60)); }

  echo "Completed task: $task at $end_timestamp (duration: $(format_time $duration))"
  echo "→ Total elapsed: $(format_time $total_elapsed), Estimated total: $(format_time $est_total), ETA: ~$finish_timestamp"
done
