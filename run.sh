#! /bin/bash

. "$(dirname $0)/env.sh"

cd $DEEPDIVE_HOME

prosodic_array=( 0 1 2 )
meta_array=( 0 1 2 )
textual_array=( 0 2 )

folder_array=( 0 1 2 3 4 )


for i in "${folder_array[@]}"
do
	export DATA_DIR=$APP_HOME/data/cross_validation/Male/$i

	for p in "${prosodic_array[@]}"
	do
		for m in "${meta_array[@]}"
		do
			for t in "${textual_array[@]}"
			do
				export prosodic=$p
				export meta=$m
				export textual=$t

				sbt "run -c $APP_HOME/application.conf" > /dev/null

				file="$APP_HOME/output/male_3buckets_midis50_threshold50/output_${i}_${m}_${p}_${t}.out"
				
				sh evaluate.sh > $file
				cat $file
			done
		done
	done
done