#!/bin/bash

# Grant execute permission to this script
chmod +x "$0"

# Initialize git
git init
wait

# Check if Poetry is installed, if not, download it
if ! command -v poetry &> /dev/null
then
    make poetry-download
fi
wait

# Initialize Poetry and install pre-commit hooks
make install
wait
make pre-commit-install
wait

# Run the codestyle
make codestyle
wait

# Upload initial code to GitHub
git add .
wait
git commit -m ":tada: Initial commit"
wait
git branch -M master
wait
git remote add origin https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}.git
wait

# Delete both scripts
rm "$0" init.cmd
