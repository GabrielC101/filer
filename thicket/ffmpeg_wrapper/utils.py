#!/usr/bin/env python
import os
from os.path import isfile

import mimetypes
from thicket.utils import get_media_type

def is_video(path):

    if not path:
        return False
    
    if isfile(path):
        abspath = os.path.abspath(path)
        media_type = get_media_type(path)
        if media_type == 'video':
            return True

    return False
