#!/bin/bash

# Install pyenv
pyenv local {{ cookiecutter.minimal_python_version }}
pycharm .

# Delete this file
rm "$0"
