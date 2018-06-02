#!/usr/bin/env python

from __future__ import absolute_import, print_function

import datetime

from mock import patch

from thicket.utils import remove_nondigits, get_path_type, is_image, get_size, get_inode, get_atime, get_mtime, get_ctime, \
    get_folder_size


def test_remove_nondigits_pass():
    string_data = 'aa11bb22cc33'
    result = remove_nondigits(string_data)
    assert result == '112233'


def test_remove_nondigits_fail():
    string_data = 'aa11bb22cc33'
    result = remove_nondigits(string_data)
    assert not result == 'aabbcc'


@patch('thicket.utils.isfile', return_value=True)
@patch('thicket.utils.isdir', return_value=False)
@patch('thicket.utils.exists', return_value=True)
def test_get_path_type_file_pass(MockExists, MockIsDir, MockIsFile):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert tipe == 'file'


def test_get_path_type_file_no_mock_pass():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    tipe = get_path_type(path)
    assert tipe == 'file'


@patch('thicket.utils.isfile', return_value=False)
@patch('thicket.utils.isdir', return_value=True)
@patch('thicket.utils.exists', return_value=True)
def test_get_path_type_file_fail(MockExists, MockIsDir, MockIsFile):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert not tipe == 'file'


def test_get_path_type_file_no_mock_fail():
    path = './tests/fixtures/test_dir_01'
    tipe = get_path_type(path)
    assert not tipe == 'file'


@patch('thicket.utils.isfile', return_value=False)
@patch('thicket.utils.isdir', return_value=True)
@patch('thicket.utils.exists', return_value=True)
def test_get_path_type_dir_pass(MockExists, MockIsDir, MockIsFile):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert tipe == 'directory'


def test_get_path_type_dir_no_mock_pass():
    path = './tests/fixtures/test_dir_01'
    tipe = get_path_type(path)
    assert tipe == 'directory'


@patch('thicket.utils.isfile', return_value=True)
@patch('thicket.utils.isdir', return_value=False)
@patch('thicket.utils.exists', return_value=True)
def test_get_path_type_dir_fail(MockExists, MockIsDir, MockIsFile):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert not tipe == 'directory'


def test_get_path_type_dir_no_mock_fail():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    tipe = get_path_type(path)
    assert not tipe == 'directory'


@patch('thicket.utils.get_mimetype', return_value='image/jpeg')
@patch('thicket.utils.isfile', return_value=True)
def test_is_image_true_pass(MockIsFile, MockMagicFromFile):
    path = '/home/username/image_file.jpg'
    result = is_image(path)
    assert result == True


def test_is_image_true_no_mock_pass():
    path = './tests/fixtures/test_dir_01/random.png'
    result = is_image(path)
    assert result == True


@patch('thicket.utils.get_mimetype', return_value='application/pdf')
@patch('thicket.utils.isfile', return_value=True)
def test_is_image_true_fail(MockIsFile, MockMagicFromFile):
    path = '/home/username/image_file.jpg'
    result = is_image(path)
    assert result == False


def test_is_image_true_no_mock_fail():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    result = is_image(path)
    assert not result == True


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_size': 1}))
def test_get_size_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_size(path)
    assert result == 1


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_size': 2}))
def test_get_size_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_size(path)
    assert not result == 1


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_ino': 1}))
def test_get_inode_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_inode(path)
    assert result == 1


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_ino': 2}))
def test_get_inode_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_inode(path)
    assert not result == 1


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_atime': 1507390145}))
def test_get_atime_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_atime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_atime': 15073901111}))
def test_get_atime_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_atime(path)
    assert not result == datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_mtime': 1507390145}))
def test_get_mtime_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_mtime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_mtime': 15073901111}))
def test_get_mtime_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_mtime(path)
    assert not result == datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_ctime': 1507390145}))
def test_get_ctime_pass(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_ctime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_ctime': 15073901111}))
def test_get_ctime_fail(MockStSize):
    path = '/home/username/nonfile.txt'
    result = get_ctime(path)
    assert not result == datetime.datetime.fromtimestamp(1507390145)


def test_folder_size_pass():
    path = './tests/fixtures/test_dir_01'
    result = get_folder_size(path)
    assert result == 352615


def test_folder_size_fail():
    path = './tests/fixtures/test_dir_01'
    result = get_folder_size(path)
    assert not result == 106006
