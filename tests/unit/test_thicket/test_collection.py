from collections.abc import MutableSequence

from thicket.collection import Collection


def test_instantiation():
    collection = Collection()
    assert isinstance(collection, Collection)
    assert isinstance(collection, list)
    assert isinstance(collection, MutableSequence)


def test_items():
    collection = Collection()
    assert isinstance(collection.items, list)


def test_tolist():
    collection = Collection()
    assert isinstance(collection.tolist, list)


def test_num_items():
    collection = Collection()
    assert collection.num_items == 0
