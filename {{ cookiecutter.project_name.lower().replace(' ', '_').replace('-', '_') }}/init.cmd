@echo off

REM Initialize git
git init

REM Check if Poetry is installed, if not, download it
where poetry >nul 2>nul
if %errorlevel% neq 0 (
    make poetry-download
)

REM Initialize Poetry and install pre-commit hooks
make install
make pre-commit-install

REM Run the codestyle
make codestyle

REM Upload initial code to GitHub
git add .
git commit -m ":tada: Initial commit"
git branch -M master
git remote add origin https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}.git

REM Delete both scripts
del %0 init.sh
