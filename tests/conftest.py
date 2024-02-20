import pytest
import os


@pytest.fixture(scope="session")
def excel_file_path():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_dir, '..', 'Sprint3Data.xlsx')
