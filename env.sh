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

# The data
export DATA_DIR=$APP_HOME/data