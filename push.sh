#!/bin/bash

if [[ -z $1 ]]; then
    echo Please provide the commit message.
else
    pipenv requirements >requirements.txt

    # git config --local user.name "Jamison Chen"
    # git config --local user.email "106208004@g.nccu.edu.tw"

    git add .
    git commit -m "$1"

    # ssh-add -D
    # ssh-add ~/.ssh/id_rsa

    git push origin master
fi
