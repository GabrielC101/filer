from collections.abc import MutableSequence

from thicket.collection import Collection
from thicket.finders import list_files


def test_list_dir(test_dir_01_path):
    collection = list_files(test_dir_01_path)
    assert isinstance(collection, Collection)
    assert isinstance(collection, list)
    assert isinstance(collection, MutableSequence)


def test_result_length(test_dir_01_path):
    collection = list_files(test_dir_01_path)
    assert len(collection) == 8


def test_num_items(test_dir_01_path):
    collection = list_files(test_dir_01_path)
    assert collection.num_items == len(collection)
    assert collection.num_items == 8


def test_files(test_dir_01_path):
    collection = list_files(test_dir_01_path)
    assert collection.num_items == len(collection)
    assert collection.num_items == 8


def test_images(test_dir_01_path):
    collection = list_files(test_dir_01_path)
    assert len(collection.images) == 2


def test_pngs(test_dir_01_path):
    collection = list_files(test_dir_01_path)
    assert len(collection.pngs) == 1
