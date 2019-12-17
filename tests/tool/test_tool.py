#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `giteasychangelog` package."""

import os
import pytest

from giteasychangelog import giteasychangelog


def default_release_filename(working_folder):
    return f'{working_folder}/RELEASE.md'


def compare_final_file_with_expected(release_file_name,expected_text):
    with open(release_file_name, 'r') as release_file:
        for line in expected_text.split('\n'):
            assert line == release_file.readline().strip('\n')


def test_header_footer(working_folder):
    HEADER_CONTENT = "THIS IS HEADER\nAND HAVE 2 LINES"
    FOOTER_CONTENT = "THIS IS FOOTER\nAND\nHAVE 3 LINES"
    expeted_final = f'{HEADER_CONTENT}\n{FOOTER_CONTENT}'
    with open(f'{working_folder}/header.md', 'w+') as header_file:
        header_file.write(HEADER_CONTENT)
    with open(f'{working_folder}/footer.md', 'w+') as footer_file:
        footer_file.write(FOOTER_CONTENT)
    giteasychangelog.main()
    release_filename = default_release_filename(working_folder)
    compare_final_file_with_expected(release_filename,expeted_final)


def test_versions(working_folder):
    preversion = f'{working_folder}/0.1'
    version = f'{working_folder}/0.2'
    preversion_content = '{folder}/0.1'
    version_content = '{folder}/0.2'
    os.mkdir(preversion)
    os.mkdir(version)
    with open(f'{preversion}/some.md', 'w+') as preversion_file:
        preversion_file.write(preversion_content)
    with open(f'{version}/other.md', 'w+') as version_file:
        version_file.write(version_content)

    giteasychangelog.main()
    expected_text= f"0.2:\n---\n * {version_content}\n\n0.1:\n---\n" \
                   f" * {preversion_content}\n"
    compare_final_file_with_expected(default_release_filename(working_folder),
                                     expected_text)


def test_date(working_folder):
    version = f'{working_folder}/0.2'
    version_content = '{folder}/0.2'
    date_content = '12/12/2012'
    os.mkdir(version)
    with open(f'{version}/date.md', 'w+') as date_file:
        date_file.write(date_content)
    with open(f'{version}/other.md', 'w+') as version_file:
        version_file.write(version_content)
    with open(f'{version}/other_rev.md', 'w+') as version_file:
        version_file.write(version_content[::-1])

    giteasychangelog.main()
    expected_text = f"0.2 [{date_content}]:\n---\n * {version_content}\n" \
                    f" * {version_content[::-1]}\n"
    compare_final_file_with_expected(default_release_filename(working_folder),
                                     expected_text)

