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
ORGANIZATION = "{{ cookiecutter.organization }}"

# Values to generate github repository
GITHUB_USER = "{{ cookiecutter.github_name }}"
GITHUB_ACCESS_TOKEN = "{{ cookiecutter.github_access_token }}"


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
    ###################################
    ##  {project_name} is created.   ##
    ##  Open in Pycharm to continue  ##
    ###################################
    $ cd {project_name} && pycharm .
    """
    print(textwrap.dedent(message))


def main() -> None:
    remove_unused_files(
        directory=PROJECT_DIRECTORY,
        module_name=PROJECT_MODULE,
        need_to_remove_cli=CREATE_EXAMPLE_TEMPLATE != "cli",
    )
    print_futher_instuctions(project_name=PROJECT_NAME, github=GITHUB_USER)


if __name__ == "__main__":
    main()
