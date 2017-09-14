import os, sys
class Folder(object):

    def __init__(self, folderpath):
        self.folderpath = folderpath
        self.foldername = folderpath.rsplit('/', 1)[1]

    def __del__(self):
        folderpath = self.__class__.__name__
        # print(folderpath + " " + self.folderpath + " destroyed")
