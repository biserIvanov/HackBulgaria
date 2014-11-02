from __future__ import print_function
from pprint import pprint
from mutagen.mp3 import MP3
import json
import glob
import os
#from jsonweb.encode import to_object, dumper


class Song(object):

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def __repr__(self):
        return json.dumps(self.__dict__)

    def rate(self, rating):
        if rating in [1, 2, 3, 4, 5]:
            self.rating = rating
        else:
            return "invalid rating"


class Playlist(object):

    def __init__(self, collection, name):
        self.collection = collection
        self.name = name

    def add_song(self, song):
        if isinstance(song, Song):
            self.collection.append(song)

    def remove_song(self, songInstance):
        if isinstance(songInstance, Song):
            for song in self.collection:
                if song.title == songInstance.title:
                    self.collection.remove(song)

    def total_length(self):
        result = 0
        for song in self.collection:
            result += song.length
        return result

    def remove_disrated(self, rating):
        toRemove = []
        if rating in [1, 2, 3, 4, 5]:
            for song in self.collection:
                if song.rating < rating:
                    toRemove.append(song.title)
        for songName in toRemove:
            for song in self.collection:
                if songName == song.title:
                    self.collection.remove(song)

    def remove_bad_quality(self):
        toRemove = []
        minBitRate = 200
        for song in self.collection:
            if song.bitrate < minBitRate:
                toRemove.append(song.title)
        for songName in toRemove:
            for song in self.collection:
                if songName == song.title:
                    self.collection.remove(song)

    def show_artist(self):
        toReturn = []
        for song in self.collection:
            if not song.artist in toReturn:
                toReturn.append(song.artist)
        return toReturn

    def str(self):
        toReturn = ""
        for song in self.collection:
            toReturn += song.artist + " " + song.title + \
                " - " + str(song.length) + "\n"
        return toReturn

    def save(self, file_name):
        songs = []
        fd = open(file_name, 'w+')
        for each_song in self.collection:
            songs.append({"title": each_song.title,
                "artist": each_song.artist,
                "album": each_song.album,
                "rating": each_song.rating,
                "length": each_song.length,
                "bitrate": each_song.bitrate})
        jsondata = {
        "name": self.name,
        "songs": songs
        }
        fd.write(json.dumps(jsondata) + "\n")
        fd.close()

    @staticmethod
    def load(file_name):
        with open(file_name) as data_file:
            data = json.load(data_file)
        defoultCollection = []
        for song in data['songs']:
            album = song['album']
            rating = song['rating']
            title = song['title']
            artist = song['artist']
            length = song['length']
            bitrate = song['bitrate']
            newSong = Song(title, artist, album, rating, length, bitrate)
            defoultCollection.append(newSong)
        defoultPlayList = Playlist(defoultCollection, data['name'])


class MusicCrawler(object):

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def generate_playlist(self):
        collection = []
        os.chdir(self.dir_path)
        for fileName in glob.glob("*.mp3"):
            audio = MP3(self.dir_path + "/" + fileName)
            newSong = Song(audio['TIT2'], audio['TPE1'], audio['TALB'], 0, audio.info.length, audio.info.bitrate/1000)
            collection.append(newSong)
        playList4 = Playlist(collection, "Default_name")
        return playList4
