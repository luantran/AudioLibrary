from model import album
from model import folder

class Artist(object):

    def __init__(self, name, folder_object):
        self.name = name
        self.listOfArtistsAlbums = []
        self.folder = folder_object

    def __del__(self):
        artist_name = self.__class__.__name__
        # print(artist_name + " " + self.name + " destroyed")

    def delete(self):
        for i in range(len(self.listOfArtistsAlbums), 0, -1):
            album = self.listOfArtistsAlbums[i]
            album.delete()
        del self
