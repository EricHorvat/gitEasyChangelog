import os
import pytest
import tempfile


@pytest.fixture(scope="function")
def working_folder():
  with tempfile.TemporaryDirectory() as full_folder_name:
    os.mkdir('{folder}/CHANGELOG/'.format(folder=full_folder_name))
    os.chdir(full_folder_name)
    yield full_folder_name
