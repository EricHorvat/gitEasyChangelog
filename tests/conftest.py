import os
import random
import string
import pytest


@pytest.fixture(scope="function")
def working_folder():
    tmp_folder_name = (''.join(
      random.choices(string.ascii_uppercase + string.digits, k=6)
    ))
    full_folder_name = '/tmp/{name}'.format(name=tmp_folder_name)
    os.mkdir(full_folder_name)
    os.mkdir('{folder}/CHANGELOG/'.format(folder=full_folder_name))
    os.chdir(full_folder_name)
    yield full_folder_name
    os.system('rm -fr {folder}'.format(folder=full_folder_name))
