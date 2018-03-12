#!/usr/bin/env python

from __future__ import absolute_import, print_function

import datetime

from mock import patch

from forest.utils import remove_nondigits, get_path_type, is_image, get_size, get_inode, atime, mtime, ctime, \
    get_folder_size, get_mime_from_extension


def test_remove_nondigits_pass():
    string_data = 'aa11bb22cc33'
    result = remove_nondigits(string_data)
    assert result == '112233'


def test_remove_nondigits_fail():
    string_data = 'aa11bb22cc33'
    result = remove_nondigits(string_data)
    assert not result == 'aabbcc'


@patch('forest.utils.isfile', return_value=True)
@patch('forest.utils.isdir', return_value=False)
@patch('forest.utils.exists', return_value=True)
def test_get_path_type_file_pass(MockExists, MockIsDir, MockIsFile):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert tipe == 'file'


def test_get_path_type_file_no_mock_pass():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    tipe = get_path_type(path)
    assert tipe == 'file'


@patch('forest.utils.isfile', return_value=False)
@patch('forest.utils.isdir', return_value=True)
@patch('forest.utils.exists', return_value=True)
def test_get_path_type_file_fail(MockExists, MockIsDir, MockIsFile):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert not tipe == 'file'


def test_get_path_type_file_no_mock_fail():
    path = './tests/fixtures/test_dir_01'
    tipe = get_path_type(path)
    assert not tipe == 'file'


@patch('forest.utils.isfile', return_value=False)
@patch('forest.utils.isdir', return_value=True)
@patch('forest.utils.exists', return_value=True)
def test_get_path_type_dir_pass(MockExists, MockIsDir, MockIsFile):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert tipe == 'directory'


def test_get_path_type_dir_no_mock_pass():
    path = './tests/fixtures/test_dir_01'
    tipe = get_path_type(path)
    assert tipe == 'directory'


@patch('forest.utils.isfile', return_value=True)
@patch('forest.utils.isdir', return_value=False)
@patch('forest.utils.exists', return_value=True)
def test_get_path_type_dir_fail(MockExists, MockIsDir, MockIsFile):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert not tipe == 'directory'


def test_get_path_type_dir_no_mock_fail():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    tipe = get_path_type(path)
    assert not tipe == 'directory'


@patch('forest.utils.magic.from_file', return_value='image/jpeg')
@patch('forest.utils.isfile', return_value=True)
def test_is_image_true_pass(MockIsFile, MockMagicFromFile):
    path = '/home/username/image_file.jpg'
    result = is_image(path)
    assert result == True


def test_is_image_true_no_mock_pass():
    path = './tests/fixtures/test_dir_01/random.png'
    result = is_image(path)
    assert result == True


@patch('forest.utils.magic.from_file', return_value='application/pdf')
@patch('forest.utils.isfile', return_value=True)
def test_is_image_true_fail(MockIsFile, MockMagicFromFile):
    path = '/home/username/image_file.jpg'
    result = is_image(path)
    assert result == False


def test_is_image_true_no_mock_fail():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    result = is_image(path)
    assert not result == True


@patch('forest.utils.os.stat', return_value=type('TestClass', (), {'st_size': 1}))
def test_get_size_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_size(path)
    assert result == 1


@patch('forest.utils.os.stat', return_value=type('TestClass1', (), {'st_size': 2}))
def test_get_size_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_size(path)
    assert not result == 1


@patch('forest.utils.os.stat', return_value=type('TestClass', (), {'st_ino': 1}))
def test_get_inode_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_inode(path)
    assert result == 1


@patch('forest.utils.os.stat', return_value=type('TestClass1', (), {'st_ino': 2}))
def test_get_inode_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_inode(path)
    assert not result == 1


@patch('forest.utils.os.stat', return_value=type('TestClass', (), {'st_atime': 1507390145}))
def test_get_atime_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = atime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('forest.utils.os.stat', return_value=type('TestClass1', (), {'st_atime': 15073901111}))
def test_get_atime_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = atime(path)
    assert not result == datetime.datetime.fromtimestamp(1507390145)


@patch('forest.utils.os.stat', return_value=type('TestClass', (), {'st_mtime': 1507390145}))
def test_get_mtime_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = mtime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('forest.utils.os.stat', return_value=type('TestClass1', (), {'st_mtime': 15073901111}))
def test_get_mtime_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = mtime(path)
    assert not result == datetime.datetime.fromtimestamp(1507390145)


@patch('forest.utils.os.stat', return_value=type('TestClass', (), {'st_ctime': 1507390145}))
def test_get_ctime_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = ctime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('forest.utils.os.stat', return_value=type('TestClass1', (), {'st_ctime': 15073901111}))
def test_get_ctime_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = ctime(path)
    assert not result == datetime.datetime.fromtimestamp(1507390145)


def test_folder_size_pass():
    path = './tests/fixtures/test_dir_01'
    result = get_folder_size(path)
    assert result == 352615


def test_folder_size_fail():
    path = './tests/fixtures/test_dir_01'
    result = get_folder_size(path)
    assert not result == 106006


def test_get_mime_from_extension_group_pass():
    result = get_mime_from_extension('jpg')
    assert result[0] == 'image'


def test_get_mime_from_extension_type_pass():
    result = get_mime_from_extension('jpg')
    assert result[1] == 'jpeg'


def test_get_mime_from_extension_group_fail():
    result = get_mime_from_extension('not-a-valid-extension')
    assert not result[0] == 'image'


def test_get_mime_from_extension_type_fail():
    result = get_mime_from_extension('not-a-valid-extension')
    assert not result[1] == 'jpeg'