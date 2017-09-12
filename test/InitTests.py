import unittest
import os
from controller import LibraryController
from model import library

class InitTests(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        lib = library.Library()
        lib.artists = []
        lib.albums = []
        lib.songs = []

    def test1_init_artist(self):
        print("test1 starting...")
        rootDirectory = "/home/luantran/Music/InitTests/"
        # print(rootDirectory)
        for files in os.listdir(rootDirectory):
            print(files)
            if os.path.isdir(os.path.join(rootDirectory, files)):
                lc = LibraryController.LibraryController()
                lc.initArtist(os.path.join(rootDirectory, files))
        lib = library.Library()
        self.assertEqual(1, len(lib.artists))
        for artist in lib.artists:
            # print(artist.name)
            self.assertEqual("Artist1", artist.name)
        print("test1 passed")

    def test2_init_abum(self):
        print("test2 starting...")
        lib = library.Library()
        artist_folder = lib.artists[0].folder.folderpath
        for files in os.listdir(artist_folder):
            print(files)
            if os.path.isdir(os.path.join(artist_folder, files)):
                lc = LibraryController.LibraryController()
                lc.initAlbum(os.path.join(artist_folder, files), artist_folder)
        self.assertEqual(1, len(lib.albums))
        self.assertEqual("Album1", lib.albums[0].name)
        self.assertEqual("Artist1", lib.albums[0].artist.name)
        print("test2 passed")




if __name__ == '__main__':
    unittest.main()
