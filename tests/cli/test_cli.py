#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `giteasychangelog` package."""

import pytest

from click.testing import CliRunner

from giteasychangelog import cli


def test_command_line_interface(working_folder):
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '' in result.output
    with open('{folder}/RELEASE.md'
              .format(folder=working_folder)) as release_file:
        assert release_file.readline() == ''
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

