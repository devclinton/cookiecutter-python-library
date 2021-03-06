#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script for the {{ cookiecutter.library_name }}"""
import sys

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

# Load our Requirements files
extra_require_files = dict()
for file_prefix in ['', 'dev_', 'build_']:
    filename = f'{file_prefix}requirements'
    with open(f'{filename}.txt') as requirements_file:
        fk = file_prefix.strip("_") if file_prefix else filename
        extra_require_files[fk] = [r for r in requirements_file.read().split("\n") if not r.startswith("--")]

extras = dict(
    test=extra_require_files['build'] + extra_require_files['dev'],
    dev=extra_require_files['build'] + extra_require_files['dev'],
    build=extra_require_files['build'],
    packaging=extra_require_files['build']
)

# TODO review
authors = [
    ("{{cookiecutter.full_name}}", "{{cookiecutter.email}}"),
]

setup(
    author=[author[0] for author in authors],
    author_email=[author[1] for author in authors],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=extra_require_files['requirements'],
    long_description=readme,
    include_package_data=True,
    keywords='modeling, IDM',
    name='{{ cookiecutter.library_name }}',
    packages=find_packages(),
    setup_requires=[],
    python_requires='>=3.6.*, !=3.7.0, !=3.7.1, !=3.7.2',
    test_suite='tests',
    extras_require=extras,
    version='0.0.1.dev'
)