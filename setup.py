#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('RELEASE.md') as release_file:
    release = release_file.read()

requirements = ['Click>=6.0', 'packaging>=18.0']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

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
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + release,
    include_package_data=True,
    keywords='giteasychangelog',
    name='giteasychangelog',
    packages=find_packages(include=['giteasychangelog']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/EricHorvat/giteasychangelog',
    version='0.1.0',
    zip_safe=False,
)
