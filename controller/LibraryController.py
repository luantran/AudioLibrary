from model import album
from model import artist
from model import file
from model import folder
from model import library
from model import song
import os, sys

class LibraryController(object):

    ########################################################################
    #       ARTIST
    ########################################################################

    def initArtist(self, folderpath):
        folder_object = folder.Folder(folderpath)
        artist_name = folder_object.foldername
        newArtist = artist.Artist(artist_name, folder_object)

        lib = library.Library()
        lib.artists.append(newArtist)

        #TODO: SQL QUERY

    def createArtist(self, name):
        if name == "" or name is None:
            raise ValueError('name given is empty')
        lib = library.Library()
        artistsExists = False
        artist_element = None
        for artists in lib.artists:
            if artists.name == name:
                artistsExists = True
                artist_element = artists
                break

        if not artistsExists:
            folderpath = os.path.join(os.environ['MEDIA_PATH'], name)
            if not os.path.exists(folderpath):
                os.mkdir(folderpath)
            folder_object = folder.Folder(folderpath)

            newArtist = artist.Artist(name, folder_object)
            lib = library.Library()
            lib.artists.append(newArtist)

            #TODO: SQL QUERY
            return newArtist
        else:
            return artist_element

    ########################################################################
    #       ALBUM
    ########################################################################

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
        #TODO: SQL QUERY

    def createAlbum(self, name, release_date, artist_object, num_tracks):
        error = ""
        if name == "" or name is None:
            error += "Album name cannot be empty! "
        # if release_date is None:
        #     error += "Album release date cannot be null! "
        if artist_object is None:
            error += "Album artist cannot be null! "
        # if num_tracks < 0:
        #     error += "Album number of tracks cannot be less than zero! "
        if len(error) > 0:
            raise ValueError(error)

        lib = library.Library()
        albumExists = False
        album_element = None
        for albums in lib.albums:
            if albums.name == name and albums.artist == artist_object:
                albumExists = True
                album_element = albums
        if not albumExists:
            folderpath = os.path.join(artist_object.folder.folderpath, name)
            if not os.path.exists(folderpath):
                os.mkdir(folderpath)
            folder_object = folder.Folder(folderpath)

            newAlbum = album.Album(name, release_date, artist_object, num_tracks, folder_object)
            artist_object.listOfArtistsAlbums.append(newAlbum)
            lib = library.Library()
            lib.albums.append(newAlbum)
            return newAlbum

             #TODO : SQL QUERY
        else:
            return album_element

    ########################################################################
    #       SONG
    ########################################################################

    def initSong(self, album_folderpath, artist_folderpath, filepath):
        file_object = file.File(filepath)
        albumname_folder = album_folderpath.rsplit('/', 1)[1]
        if albumname_folder != file_object.getAlbumName():
            raise ValueError("Album name in file path does not match album folder name!")

        artistname_folder = artist_folderpath.rsplit('/', 1)[1]
        if artistname_folder != file_object.getArtistName():
            raise ValueError("Artist name in file path does not match artist folder name!")

        lib = library.Library()
        album_artist = None
        for artist_element in lib.artists:
            if artist_folderpath == artist_element.folder.folderpath:
                album_artist = artist_element
                break
        songs_album = None
        for album_element in lib.albums:

            if album_folderpath == album_element.folder.folderpath:
                songs_album = album_element
                break

        if album_artist is None:
            raise ValueError("Could not find album_artist")
        if songs_album is None:
            raise ValueError("Could not find songs_album")

        newSong = song.Song(file_object.getSongTitle(), int(file_object.getDuration()), int(file_object.getTrackNum()), songs_album, int(file_object.getYear()), file_object)
        songs_album.listOfAlbumSongs.append(newSong)
        if int(songs_album.num_tracks) < int(file_object.getTracks()):
            songs_album.num_tracks = int(file_object.getTracks())
        lib.songs.append(newSong)


    def importSong(self, filepath):
        lib = library.Library()
        file_object = file.File(filepath)
        songs_artist = self.createArtist(file_object.getArtistName())
        songs_album = self.createAlbum(file_object.getAlbumName(), file_object.getYear(), songs_artist,
                                       file_object.getTracks())
        if file_object.getYear() != '' and file_object.getTracks() != '':
            if int(songs_album.num_tracks) < int(file_object.getTracks()):
                songs_album.num_tracks = file_object.getTracks()
            if int(songs_album.release_date) < int(file_object.getYear()):
                songs_album.release_date = file_object.getYear()

        file_object.moveFile(os.path.join(songs_album.folder.folderpath, file_object.getSongTitle()))

        newSong = song.Song(file_object.getSongTitle(), file_object.getDuration(), file_object.getTrackNum(),
                            songs_album, file_object.getYear(), file_object)
        songs_album.listOfAlbumSongs.append(newSong)
        lib.songs.append(newSong)

        return newSong







