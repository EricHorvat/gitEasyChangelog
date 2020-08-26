#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import search

"""The setup script."""

from setuptools import setup, find_packages

with open('giteasychangelog/__init__.py', 'rt', encoding='utf8') as f:
    version = search(r'__version__ = \'(.*?)\'', f.read()).group(1)

with open('RELEASE.md') as release_file:
    release = release_file.read()

requirements = ['Click', 'packaging']

setup_requirements = ['pytest-runner', ]

extra_req = {
        'dev': [
            'giteasychangelog'
        ],
        'test': [
            'pytest',  # >= travis requirement
            'pytest-cov',
        ],
        'docs': [
            'mkdocs',
            'mkdocs-material',
        ]
    }

setup(
    author="Eric Horvat",
    author_email='eric.nahuel.horvat@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A python tool which helps whit changelog/release file "
                "conflicts with git",
    entry_points={
        'console_scripts': [
            'giteasychangelog=giteasychangelog.cli:main',
        ],
    },
    extras_require=extra_req,
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=release,
    include_package_data=True,
    keywords='giteasychangelog',
    name='giteasychangelog',
    packages=find_packages(include=['giteasychangelog']),
    setup_requires=setup_requirements,
    test_suite='tests',
    url='https://github.com/EricHorvat/giteasychangelog',
    version=version,
    zip_safe=False,
)
