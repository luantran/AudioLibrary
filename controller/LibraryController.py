from model import album
from model import artist
from model import file
from model import folder
from model import library
from model import song
import os, sys

class LibraryController(object):

    ### ARTIST ###
    def initArtist(self, folderpath):
        print("initializing artist: " + folderpath)
        folder_object = folder.Folder(folderpath)
        artist_name = folder_object.foldername
        newArtist = artist.Artist(artist_name, folder_object)

        lib = library.Library()
        lib.artists.append(newArtist)

        #TODO: SQL QUERY


    def editArtist(self, name):
        if name == "" or name is None:
            raise ValueError('name given is empty')

        folderpath = os.path.join(os.environ['MEDIA_PATH'], name)
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
        folder_object = folder.Folder(folderpath)

        newArtist = artist.Artist(name, folder_object)
        lib = library.Library()
        lib.artists.append(newArtist)

        #TODO: SQL QUERY

    ### ALBUM ###

    def initAlbum(self, album_folderpath, artist_folderpath):
        folder_object = folder.Folder(album_folderpath)
        album_name = folder_object.foldername
        lib = library.Library()
        album_artist = None
        for artist_element in lib.artists:
            if artist_folderpath == artist_element.folder.folderpath:
                album_artist = artist_element
                break
        newAlbum = album.Album(album_name, None, album_artist, 0, folder_object)
        album_artist.listOfArtistsAlbums.append(newAlbum)

        # lib = library.Library
        lib.albums.append(newAlbum)


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
        lib = library.Library()
        lib.albums.append(newAlbum)

        #TODO : SQL QUERY

    def editSong(self, name, duration, track_num, album_object, year):
        return None





