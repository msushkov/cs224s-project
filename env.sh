#! /bin/bash

export APP_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export DEEPDIVE_HOME=/Users/msushkov/Dropbox/Stanford/deepdive

# Machine Configuration
export MEMORY="4g"
export PARALLELISM=4

# Database Configuration
export DBNAME=cs224s_speeddate
export PGUSER=${PGUSER:-`whoami`}
export PGPASSWORD=${PGPASSWORD:-}
export PGPORT=${PGPORT:-5432}
export PGHOST=${PGHOST:-localhost}

# SBT Options
export SBT_OPTS="-Xmx$MEMORY"

# Using ddlib
export PYTHONPATH=$DEEPDIVE_HOME/ddlib:$PYTHONPATH

# Need these environment variables for the sampler
export LD_LIBRARY_PATH=$DEEPDIVE_HOME/lib/dw_mac/lib/protobuf/lib:$DEEPDIVE_HOME/lib/dw_mac/lib
export DYLD_LIBRARY_PATH=$DEEPDIVE_HOME/lib/dw_mac

# The data
export DATA_DIR=$APP_HOME/data

# Prosodic feature file
export PROSODIC_FEATURES=$DATA_DIR/FINAL_Prosodic.csv

# Metadata features per person
export METADATA=$DATA_DIR/FINAL_Metadata.csv

# The output labels
export OUTPUT=$DATA_DIR/FINAL_Output.csv

# The textual features
export TEXTUAL=$DATA_DIR/FINAL_Textual.csv