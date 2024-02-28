#!/usr/bin/env bash

set -e

# Pull code
git checkout master
git pull origin master

# Install the latest dependencies if necessary
requirements="~/trade-smartly-backend/requirements.txt"
if git diff HEAD^ HEAD -- "$requirements" | grep -qE '^\+|^\-'; then
    pip install -r "$requirements"

    # If the `pip install` command above has actually caused any changes in the dependencies, all the gunicorn proccesses will get killed.
    gunicorn_process_count=$(ps aux | grep gunicorn | awk '{ print $2 }' | wc -l)
    if [ $gunicorn_process_count -eq 1 ]; then
        # Why -eq 1? This is because the command that count the process itself is a proccess that will be counted.
        gunicorn --daemon
    fi
fi

# Crontab
## Transform the content of the crontab file of this project
python ~/trade-smartly-backend/scripts/prod/transform_crontab.py

## Update the real crontab
crontab ~/trade-smartly-backend/main/crontab/crontab

## Undo the transform
git reset HEAD --hard

set +e
