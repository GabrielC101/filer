#!/usr/bin/env python

from __future__ import absolute_import, print_function
from os.path import isfile, isdir


class Collection(list):

    def items(self):
        return self

    def tolist(self):
        return list(self)

    def num_items(self):
        return len(self)

    def files(self, tolist=False):
        if not tolist:
            return Collection([item for item in self.items() if isfile(item.abspath())])
        else:
            return [item for item in self.items() if isfile(item.abspath())]

    def dirs(self, tolist=False):
        if not tolist:
            return Collection([item for item in self.items() if isdir(item.abspath())])
        else:
            return [item for item in self.items() if isdir(item.abspath())]

    def images(self, tolist=False):
        if not tolist:
            return Collection([item for item in self.files().items() if item.mime()[0] == 'image'])
        else:
            return [item for item in self.files().items() if item.mime()[0] == 'image']

    def pngs(self, tolist=False):
        if not tolist:
            return Collection([item for item in self.images().items() if item.mime()[1] == 'png'])
        else:
            return [item for item in self.images().items() if item.mime()[1] == 'png']

    def jpgs(self, tolist=False):
        if not tolist:
            return Collection([item for item in self.images().items() if item.mime()[1] == 'jpg' or item.mime()[1] == 'jpeg'])
        else:
            return [item for item in self.images().items() if item.mime()[1] == 'jpg' or item.mime()[1] == 'jpeg']

    def gifs(self, tolist=False):
        if not tolist:
            return Collection([item for item in self.get_files().get_items() if item.get_mime()[0] == 'gif'])
        else:
            return [item for item in self.get_files().get_items() if item.get_mime()[0] == 'gif']

    def get_tiffs(self, tolist=False):
        if not tolist:
            return Collection([item for item in self.get_files().get_items() if item.get_mime()[0] == 'tiff'])
        else:
            return [item for item in self.get_files().get_items() if item.get_mime()[0] == 'tiff']

    def copy_files(self, file_path_string):
        for item in self.get_files().get_items():
            item.copy_file(file_path_string, hard_link=False, symbolic_link=False, preserve_attributes=True)


