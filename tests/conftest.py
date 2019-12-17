import os
import random
import string
import pytest


@pytest.fixture(scope="function")
def working_folder():

    tmp_folder_name = ''.join(
      random.choice(string.ascii_uppercase + string.digits
                    ) for _ in range(6))
    full_folder_name = f'/tmp/{tmp_folder_name}'
    os.mkdir(full_folder_name)
    os.mkdir(f'{full_folder_name}/CHANGELOG/')
    os.chdir(full_folder_name)
    yield full_folder_name
    os.system(f'rm -fr {full_folder_name}')
