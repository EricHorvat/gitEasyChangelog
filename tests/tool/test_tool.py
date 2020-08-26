#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `giteasychangelog` package."""

import os
import pytest

from giteasychangelog import giteasychangelog


def default_release_filename(working_folder):
    return '{folder}/RELEASE.md'.format(folder=working_folder)


def compare_final_file_with_expected(release_file_name, expected_text):
    with open(release_file_name, 'r') as release_file:
        content = release_file.read()
        assert content == expected_text


def test_header_footer(working_folder):
    HEADER_CONTENT = "THIS IS HEADER\nAND HAVE 2 LINES"
    FOOTER_CONTENT = "THIS IS FOOTER\nAND\nHAVE 3 LINES"
    expeted_final = '{header}\n{footer}'.format(header=HEADER_CONTENT,
                                                footer=FOOTER_CONTENT)
    with open('{folder}/header.md'.format(
                                  folder=working_folder), 'w+') as header_file:
        header_file.write(HEADER_CONTENT)
    with open('{folder}/footer.md'.format(
                                  folder=working_folder), 'w+') as footer_file:
        footer_file.write(FOOTER_CONTENT)
    giteasychangelog.main()
    release_filename = default_release_filename(working_folder)
    compare_final_file_with_expected(release_filename,expeted_final)


def test_versions(working_folder):
    preversion = 0.1
    version = 0.2
    preversion_folder = '{folder}/{version}'.format(folder=working_folder,
                                                    version=preversion)
    version_folder = '{folder}/{version}'.format(folder=working_folder,
                                                 version=version)
    content = 'SOME_{version}\n_CONTENT'
    preversion_content = content.format(version=preversion)
    version_content = content.format(version=version)
    os.mkdir(preversion_folder)
    os.mkdir(version_folder)
    with open('{folder}/some.md'.format(
      folder=preversion), 'w+') as preversion_file:
        preversion_file.write(preversion_content)
    with open('{folder}/other.md'.format(
      folder=version), 'w+') as version_file:
        version_file.write(version_content+"\n")

    giteasychangelog.main()
    expected_text = "0.2:\n---\n * {version_content}\n\n0.1:\n---\n" \
                    " * {preversion_content}\n\n"\
                    .format(version_content=version_content,
                            preversion_content=preversion_content)
    compare_final_file_with_expected(default_release_filename(working_folder),
                                     expected_text)


def test_date(working_folder):
    version = '{folder}/0.2'.format(folder=working_folder)
    version_content = '{folder}/0.2'
    date_content = '12/12/2012'
    os.mkdir(version)
    with open('{folder}/date.md'.format(
      folder=version), 'w+') as date_file:
        date_file.write(date_content)
    with open('{folder}/other.md'.format(
      folder=version), 'w+') as version_file:
        version_file.write(version_content)
    with open('{folder}/other_rev.md'.format(
      folder=version), 'w+') as version_file:
        version_file.write(version_content[::-1])

    giteasychangelog.main()
    expected_text = "0.2 [{date_content}]:\n---\n * {version_content}\n" \
                    " * {rev_version_content}\n\n" \
                    .format(version_content=version_content,
                            rev_version_content=version_content[::-1],
                            date_content=date_content)
    compare_final_file_with_expected(default_release_filename(working_folder),
                                     expected_text)

