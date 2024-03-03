"""File to configure all project tests."""

import pytest
import os


@pytest.fixture(scope="session")
def excel_file_path():
    """Tests are in subdirectory. Let them read Excel file from parent directory."""
    base_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_dir, '..', 'Sprint3Data.xlsx')
