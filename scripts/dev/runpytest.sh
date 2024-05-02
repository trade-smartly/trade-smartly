#!/usr/bin/env bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RESET='\033[0m'

set -e

if [ ! -e "manage.py" ]; then
    printf "${RED}You should run this command under the root directory of this project.${RESET}\n"
    exit 1
fi

# Activate virtual Python environment
source $(pipenv --venv)/bin/activate

# Load all environment variables from .env file
set -o allexport
source .env set

pytest

deactivate

set +e
