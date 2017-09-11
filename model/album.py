from model import folder
from model import artist

class Album:

    def __init__(self, name, release_date, artist_object, num_tracks, folder_object):
        self.name = name
        self.num_tracks = num_tracks
        self.release_date = release_date
        self.listOfAlbumSongs = []
        self.artist = artist_object
        self.folder = folder_object

    def __del__(self):
        album_name = self.__class__.__name__
        print(album_name + " " + self.name + " destroyed")

    def delete(self):
        for i in range(len(self.listOfAlbumSongs), 0, -1):
            song = self.listOfAlbumSongs[i - 1]
            song.delete()
        placeholderArtist = self.artist
        self.artist = None
        placeholderArtist.listOfArtistsAlbums.remove(self)
        del self
