from model import album
from model import artist
from model import file
from model import folder
from model import library
from model import song
import os, sys

class LibraryController(object):

    ### ARTIST ###

    def editArtist(self, name):
        if name == "" or name is None:
            raise ValueError('name given is empty')

        folderpath = os.path.join(os.environ['MEDIA_PATH'], name)
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
        folder_object = folder.Folder(folderpath)

        newArtist = artist.Artist(name, folder_object)
        lib = library.Library
        lib.artists.add(newArtist)

        #TODO: SQL QUERY

    ### ALBUM ###

    def editAlbum(self, name, release_date, artist_object, num_tracks):
        error = ""
        if name == "" or name is None:
            error = error + "Album name cannot be empty!"
        if release_date == "" or release_date is None:
            error = error + "Album release date cannot be null!"
        if artist_object is None:
            error = error + "Album artist cannot be null!"
        if num_tracks < 0:
            error = error + "Album number of tracks cannot be less than zero!"
        if len(error) > 0:
            raise ValueError(error)

        folderpath = os.path.join(os.environ['MEDIA_PATH'], name)
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
        folder_object = folder.Folder(folderpath)

        newAlbum = album.Album(name, release_date, artist_object, num_tracks, folder_object)
        lib = library.Library
        lib.albums.add(newAlbum)

        #TODO : SQL QUERY

    def editSong(self, name, duration, track_num, album_object, year):
        return None





