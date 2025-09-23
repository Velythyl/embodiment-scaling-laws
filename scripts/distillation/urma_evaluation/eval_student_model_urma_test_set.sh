#!/bin/bash

# test set for Gendog dataset
tasks_dog=("Gendog0" "Gendog7" "Gendog8" "Gendog20" "Gendog31" "Gendog32" "Gendog37" "Gendog41" "Gendog46" "Gendog47" "Gendog48" "Gendog50" "Gendog51" "Gendog55" "Gendog71" "Gendog72" "Gendog75" "Gendog97" "Gendog104" "Gendog111" "Gendog113" "Gendog122" "Gendog124" "Gendog128" "Gendog132" "Gendog133" "Gendog144" "Gendog149" "Gendog154" "Gendog155" "Gendog158" "Gendog161" "Gendog163" "Gendog166" "Gendog169" "Gendog170" "Gendog181" "Gendog183" "Gendog197" "Gendog204" "Gendog207" "Gendog215" "Gendog222" "Gendog226" "Gendog229" "Gendog241" "Gendog244" "Gendog248" "Gendog250" "Gendog252" "Gendog258" "Gendog260" "Gendog261" "Gendog266" "Gendog272" "Gendog278" "Gendog280" "Gendog282" "Gendog286" "Gendog290" "Gendog298" "Gendog308" "Gendog312" "Gendog313" "Gendog316" "Gendog320" "Gendog327")

# test set for Genhexapod dataset
tasks_hexapod=("Genhexapod0" "Genhexapod7" "Genhexapod8" "Genhexapod20" "Genhexapod31" "Genhexapod32" "Genhexapod37" "Genhexapod41" "Genhexapod46" "Genhexapod47" "Genhexapod48" "Genhexapod50" "Genhexapod51" "Genhexapod55" "Genhexapod71" "Genhexapod72" "Genhexapod75" "Genhexapod97" "Genhexapod104" "Genhexapod111" "Genhexapod113" "Genhexapod122" "Genhexapod124" "Genhexapod128" "Genhexapod132" "Genhexapod133" "Genhexapod144" "Genhexapod149" "Genhexapod154" "Genhexapod155" "Genhexapod158" "Genhexapod161" "Genhexapod163" "Genhexapod166" "Genhexapod169" "Genhexapod170" "Genhexapod181" "Genhexapod183" "Genhexapod197" "Genhexapod204" "Genhexapod207" "Genhexapod215" "Genhexapod222" "Genhexapod226" "Genhexapod229" "Genhexapod241" "Genhexapod244" "Genhexapod248" "Genhexapod250" "Genhexapod252" "Genhexapod258" "Genhexapod260" "Genhexapod261" "Genhexapod266" "Genhexapod272" "Genhexapod278" "Genhexapod280" "Genhexapod282" "Genhexapod286" "Genhexapod290" "Genhexapod298" "Genhexapod308" "Genhexapod312" "Genhexapod313" "Genhexapod316" "Genhexapod320" "Genhexapod327")

# test set for Genhumanoid dataset
tasks_humanoid=("Genhumanoid0" "Genhumanoid7" "Genhumanoid12" "Genhumanoid20" "Genhumanoid31" "Genhumanoid32" "Genhumanoid37" "Genhumanoid41" "Genhumanoid46" "Genhumanoid47" "Genhumanoid48" "Genhumanoid50" "Genhumanoid51" "Genhumanoid55" "Genhumanoid63" "Genhumanoid71" "Genhumanoid72" "Genhumanoid75" "Genhumanoid97" "Genhumanoid104" "Genhumanoid111" "Genhumanoid113" "Genhumanoid122" "Genhumanoid124" "Genhumanoid128" "Genhumanoid132" "Genhumanoid133" "Genhumanoid144" "Genhumanoid149" "Genhumanoid154" "Genhumanoid155" "Genhumanoid158" "Genhumanoid161" "Genhumanoid163" "Genhumanoid166" "Genhumanoid169" "Genhumanoid170" "Genhumanoid181" "Genhumanoid183" "Genhumanoid197" "Genhumanoid204" "Genhumanoid207" "Genhumanoid215" "Genhumanoid222" "Genhumanoid226" "Genhumanoid229" "Genhumanoid241" "Genhumanoid244" "Genhumanoid248" "Genhumanoid250" "Genhumanoid252" "Genhumanoid258" "Genhumanoid260" "Genhumanoid261" "Genhumanoid266" "Genhumanoid272" "Genhumanoid276" "Genhumanoid278" "Genhumanoid280" "Genhumanoid282" "Genhumanoid286" "Genhumanoid290" "Genhumanoid298" "Genhumanoid308" "Genhumanoid312" "Genhumanoid313" "Genhumanoid316" "Genhumanoid320" "Genhumanoid327" "Genhumanoid342")

tasks=("${tasks_dog[@]}" "${tasks_hexapod[@]}" "${tasks_humanoid[@]}")

checkpoint_path="policy_directory/checkpoint.pt"
log_file="policy_directory/test_set_log_file.json"

trap "echo 'Process interrupted. Exiting...'; exit 1" SIGINT

total_time=0

for i in "${!tasks[@]}"; do
    task=${tasks[$i]}
    num_done=$((i + 1))
    num_tasks=${#tasks[@]}

    echo -n "Evaluating embodiment $num_done out of $num_tasks: $task ... "

    start_time=$(date +%s)

    python scripts/rsl_rl/eval_student_model_urma.py \
        --task "$task" \
        --ckpt_path "$checkpoint_path" \
        --model urma \
        --log_file "$log_file" \
        --headless

    end_time=$(date +%s)
    runtime=$((end_time - start_time))
    total_time=$((total_time + runtime))

    echo -n "Done. "

    average_time=$((total_time / num_done))
    tasks_left=$((num_tasks - num_done))

    if [ $tasks_left -gt 0 ]; then
        estimate=$((average_time * tasks_left))
        current_time=$(date +%s)
        finish_time=$((current_time + estimate))
        echo "→ Expected completion: $(LC_ALL=en_US.UTF-8 date -d @"${finish_time}" +"%I:%M %p")"
    fi
done

echo "→ Evaluation complete!"
