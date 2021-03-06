![Staging: {{ cookiecutter.library_name }}]

# {{ cookiecutter.library_name }}

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# User Installation

```bash
pip install {{ cookiecutter.library_name }} --index-url={{ cookiecutter.pypi_server }}
```

## Pre-requisites
- Python 3.6/3.7 x64


# Development Environment Setup

When setting up your environment for the first time, you can use the following instructions

## First Time Setup
1) Clone the repository:
   ```bash
   > git clone https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.repo_name }}.git
   ```
2) Create a virtualenv. On Windows, please use venv to create the environment
   `python -m venv {{ cookiecutter.library_name }}`
   On Unix(Mac/Linux) you can use venv or virtualenv
3) Activate the virtualenv
4) If you are on windows, run `pip install py-make --upgrade --force-reinstall`
5) Then run `python ./.dev_scripts/bootstrap.py`. This will install all the tools. 

## Development Tips

There is a Makefile file available for most common development tasks. Here is a list of commands
```bash
clean       -   Clean up temproary files
lint        -   Lint package and tests
test        -   Run All tests
coverage    -   Run tests and generate coverage report that is shown in browser
```
On Windows, you can use `pymake` instead of `make`


## Building docs

```make docs```