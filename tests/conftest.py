from os.path import dirname, join, realpath

import pytest


@pytest.fixture
def base_dir():
    return dirname(dirname(realpath(__file__)))


@pytest.fixture
def test_dir_01_path():
    return join(dirname(dirname(realpath(__file__))), 'tests', 'fixtures', 'test_dir_01')
