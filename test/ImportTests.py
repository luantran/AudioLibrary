import unittest
import os
from controller import LibraryController
from model import library
import shutil

class ImportTests(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        lib = library.Library()
        lib.artists = []
        lib.albums = []
        lib.songs = []
        for files in os.listdir('/home/luantran/Music/ImportTests'):
            if os.path.isdir(os.path.join('/home/luantran/Music/ImportTests', files)):
                shutil.rmtree(os.path.join('/home/luantran/Music/ImportTests', files))
            else:
                os.remove(os.path.join('/home/luantran/Music/ImportTests',files))
    def test1_import_song(self):
        lib = library.Library()
        lc = LibraryController.LibraryController()
        lc.importSong("/home/luantran/Smack That.mp3")
        self.assertEqual(True, os.path.exists('/home/luantran/Music/ImportTests/Akon/Akon/Smack That.mp3'))
        self.assertEqual(1, len(lib.artists))
        self.assertEqual('Akon', lib.artists[0].name)
        self.assertEqual(1, len(lib.artists[0].listOfArtistsAlbums))

if __name__ == '__main__':
    unittest.main()
