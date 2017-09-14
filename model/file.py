#!/usr/bin/python
from tinytag import TinyTag
import os, shutil

class File:
    nextId = 1

    def __init__(self, filepath):

        self.filepath = filepath
        self.filename = filepath.rsplit('/', 1)[1]

    def __del__(self):
        filename = self.__class__.__name__
        # print(filename + " " + self.filename + " destroyed")

    def moveFile(self, new_filepath):
        filetype = self.filepath.rsplit('.', 1)[1]
        new_filepath += '.'
        new_filepath += filetype
        if os.path.exists(new_filepath):
            raise Exception("There already exists a file with that name")
        else:
            shutil.copy(self.filepath, new_filepath)
            self.filepath = new_filepath
            self.filename = self.filepath.rsplit('/', 1)[1]



###############################
# GETTERS
###############################

    def getAlbumName(self):
        tag = TinyTag.get(self.filepath)
        return tag.album

    def getArtistName(self):
        tag = TinyTag.get(self.filepath)
        return tag.albumartist

    def getDuration(self):
        tag = TinyTag.get(self.filepath)
        return tag.duration

    def getYear(self):
        tag = TinyTag.get(self.filepath)
        return tag.year

    def getTrackNum(self):
        tag = TinyTag.get(self.filepath)
        return tag.track

    def getTracks(self):
        tag = TinyTag.get(self.filepath)
        return tag.track_total

    def getGenre(self):
        tag = TinyTag.get(self.filepath)
        return tag.genre

    def getSongTitle(self):
        tag = TinyTag.get(self.filepath)
        return tag.title

###############################
# SETTERS
###############################

    def setAlbumName(self, albumname):
        tag = TinyTag.get(self.filepath)
        tag.album = albumname

    def setArtistName(self, artistname):
        tag = TinyTag.get(self.filepath)
        tag.albumartist = artistname

    def setDuration(self, duration):
        tag = TinyTag.get(self.filepath)
        tag.duration = duration

    def setYear(self, year):
        tag = TinyTag.get(self.filepath)
        tag.year = year

    def setTrackNum(self, tracknum):
        tag = TinyTag.get(self.filepath)
        tag.track = tracknum

    def setTracks(self, totaltracks):
        tag = TinyTag.get(self.filepath)
        tag.track_total = totaltracks

    def setGenre(self, genre):
        tag = TinyTag.get(self.filepath)
        tag.genre = genre

    def setSongTitle(self, title):
        tag = TinyTag.get(self.filepath)
        tag.title = title






