#!/bin/bash

# Grant execute permission to this script
chmod +x "$0"

# Initialize git
git init

# Check if Poetry is installed, if not, download it
if ! command -v poetry &> /dev/null
then
    make poetry-download
fi

# Initialize Poetry and install pre-commit hooks
make install
make pre-commit-install

# Run the codestyle
make codestyle

# Upload initial code to GitHub
git add .
git commit -m ":tada: Initial commit"
git branch -M master
git remote add origin https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}.git

# Delete both scripts
rm "$0" init.cmd
