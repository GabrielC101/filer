from collections.abc import MutableSequence

from thicket import collection
from thicket.collection import Collection


def test_import():
    assert collection


def test_instantiation():
    collect = Collection()
    assert isinstance(collect, Collection)
    assert isinstance(collect, list)
    assert isinstance(collect, MutableSequence)


def test_items():
    collect = Collection()
    assert isinstance(collect.items, list)


def test_tolist():
    collect = Collection()
    assert isinstance(collect.tolist, list)


def test_num_items():
    collect = Collection()
    assert collect.num_items == 0
