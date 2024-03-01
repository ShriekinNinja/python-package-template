"""This module is called after project is created."""
from typing import List

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
CREATE_EXAMPLE_TEMPLATE = "{{ cookiecutter.create_example_template }}"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

# Values to generate github repository
GITHUB_USER = "{{ cookiecutter.github_name }}"

licences_dict = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "Apache Software License 2.0": "apache",
}


def generate_license(directory: Path, licence: str) -> None:
    """Generate license file for the project.

    Args:
        directory: path to the project directory
        licence: chosen licence
    """
    move(str(directory / "_licences" / f"{licence}.txt"), str(directory / "LICENSE"))
    rmtree(str(directory / "_licences"))


def remove_unused_files(directory: Path, module_name: str, need_to_remove_cli: bool) -> None:
    """Remove unused files.

    Args:
        directory: path to the project directory
        module_name: project module name
        need_to_remove_cli: flag for removing CLI related files
    """
    files_to_delete: List[Path] = []

    def _cli_specific_files() -> List[Path]:
        return [directory / module_name / "__main__.py"]

    if need_to_remove_cli:
        files_to_delete.extend(_cli_specific_files())

    for path in files_to_delete:
        path.unlink()


def print_futher_instuctions(project_name: str, github: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_name: current project name
        github: GitHub username
    """
    message = f"""
    #############################################################
    ##  Your project {project_name} is created.                ##
    ##  Run init script BEFORE opening the project in Pycharm  ##
    #############################################################

    $ cd {project_name}
    $ chmod +x init.sh
    $ run init.sh or init.bat depending on your OS
    """
    print(textwrap.dedent(message))


def main() -> None:
    generate_license(directory=PROJECT_DIRECTORY, licence=licences_dict[LICENSE])
    remove_unused_files(
        directory=PROJECT_DIRECTORY,
        module_name=PROJECT_MODULE,
        need_to_remove_cli=CREATE_EXAMPLE_TEMPLATE != "cli",
    )
    print_futher_instuctions(project_name=PROJECT_NAME, github=GITHUB_USER)


if __name__ == "__main__":
    main()
