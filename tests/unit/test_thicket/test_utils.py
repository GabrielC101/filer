#!/usr/bin/env python

import datetime

from mock import patch

from thicket.utils import (get_atime, get_ctime, get_folder_size, get_inode, get_mtime, get_path_type, get_size,
                           is_image, remove_nondigits)

# pylint: disable=unused-argument


def test_remove_non_digits_pass():
    string_data = 'aa11bb22cc33'
    result = remove_nondigits(string_data)
    assert result == '112233'


def test_remove_non_digits_fail():
    string_data = 'aa11bb22cc33'
    result = remove_nondigits(string_data)
    assert result != 'aabbcc'


@patch('thicket.utils.isfile', return_value=True)
@patch('thicket.utils.isdir', return_value=False)
@patch('thicket.utils.exists', return_value=True)
def test_path_type_file_pass(mock_exists, mock_is_dir, mock_is_file):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert tipe == 'file'


def test_path_type_dummy_pass():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    tipe = get_path_type(path)
    assert tipe == 'file'


@patch('thicket.utils.isfile', return_value=False)
@patch('thicket.utils.isdir', return_value=True)
@patch('thicket.utils.exists', return_value=True)
def test_path_type_file_fail(mock_exists, mock_is_dir, mock_is_file):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert tipe != 'file'


def test_path_type_file_dummy_fail():
    path = './tests/fixtures/test_dir_01'
    tipe = get_path_type(path)
    assert tipe != 'file'


@patch('thicket.utils.isfile', return_value=False)
@patch('thicket.utils.isdir', return_value=True)
@patch('thicket.utils.exists', return_value=True)
def test_path_type_dir_pass(mock_exists, mock_is_dir, mock_is_file):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert tipe == 'directory'


def test_path_type_dir_no_mock_pass():
    path = './tests/fixtures/test_dir_01'
    tipe = get_path_type(path)
    assert tipe == 'directory'


@patch('thicket.utils.isfile', return_value=True)
@patch('thicket.utils.isdir', return_value=False)
@patch('thicket.utils.exists', return_value=True)
def test_path_type_dir_fail(mock_exists, mock_is_dir, mock_is_file):
    path = '/home/username/file'
    tipe = get_path_type(path)
    assert not tipe == 'directory'


def test_path_type_dir_no_mock_fail():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    tipe = get_path_type(path)
    assert not tipe == 'directory'


@patch('thicket.utils.get_mimetype', return_value='image/jpeg')
@patch('thicket.utils.isfile', return_value=True)
def test_is_image_true_pass(mock_is_file, mock_magic_from_file):
    path = '/home/username/image_file.jpg'
    result = is_image(path)
    assert result


def test_is_image_true_no_mock_pass():
    path = './tests/fixtures/test_dir_01/random.png'
    result = is_image(path)
    assert result


@patch('thicket.utils.get_mimetype', return_value='application/pdf')
@patch('thicket.utils.isfile', return_value=True)
def test_is_image_true_fail(mock_is_file, mock_magic_from_file):
    path = '/home/username/image_file.jpg'
    result = is_image(path)
    assert not result


def test_is_image_true_no_mock_fail():
    path = './tests/fixtures/test_dir_01/dummy_file_001'
    result = is_image(path)
    assert not result


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_size': 1}))
def test_get_size_pass(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_size(path)
    assert result == 1


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_size': 2}))
def test_get_size_fail(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_size(path)
    assert result != 1


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_ino': 1}))
def test_get_inode_pass(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_inode(path)
    assert result == 1


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_ino': 2}))
def test_get_inode_fail(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_inode(path)
    assert result != 1


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_atime': 1507390145}))
def test_get_atime_pass(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_atime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_atime': 15073901111}))
def test_get_atime_fail(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_atime(path)
    assert result != datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_mtime': 1507390145}))
def test_get_mtime_pass(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_mtime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_mtime': 15073901111}))
def test_get_mtime_fail(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_mtime(path)
    assert result != datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass', (), {'st_ctime': 1507390145}))
def test_get_ctime_pass(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_ctime(path)
    assert result == datetime.datetime.fromtimestamp(1507390145)


@patch('thicket.utils.os.stat', return_value=type('TestClass1', (), {'st_ctime': 15073901111}))
def test_get_ctime_fail(mock_st_size):
    path = '/home/username/nonfile.txt'
    result = get_ctime(path)
    assert result != datetime.datetime.fromtimestamp(1507390145)


def test_folder_size():
    path = './tests/fixtures/test_dir_01'
    result = get_folder_size(path)
    assert result == 355618
    assert result != 106006
