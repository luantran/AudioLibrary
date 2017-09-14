from model import file


class Song:

    def __init__(self, name, duration, track_num, album_object, year, file_object):
        self.name = name
        self.duration = duration
        self.track_num = track_num
        self.album = album_object
        self.year = year
        self.file = file_object

    def __del__(self):
        song_name = self.__class__.__name__
        # print(song_name + " " + self.name + " destroyed")