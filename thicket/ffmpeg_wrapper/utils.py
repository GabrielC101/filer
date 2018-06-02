#!/usr/bin/env python
import os
from os.path import isfile


import magic


def is_video(path):
    
    if isfile(path):
        abspath = os.path.abspath(path)
        tipe = tuple(magic.from_file(abspath, mime=True).split('/'))[0]
        if tipe == 'video':
            return True

    return False
