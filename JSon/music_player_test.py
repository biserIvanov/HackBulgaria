import unittest
from music_player import Song, Playlist, MusicCrawler



class music_player_test(unittest.TestCase):

    def setUp(self):
        self.song = Song(
            "Thunderstruck", "ACDC", "Back in black", 5, 4.24, 256)
        self.collection = []
        self.collection2 = []
        self.collection.append(self.song)
        self.playList1 = Playlist(self.collection, "rock")
        self.playList2 = Playlist(self.collection2, "pop")

    def test_Song_constructor(self):
        self.assertEqual("Thunderstruck", self.song.title)
        self.assertEqual("ACDC", self.song.artist)
        self.assertEqual("Back in black", self.song.album)
        self.assertEqual(5, self.song.rating)
        self.assertEqual(4.24, self.song.length)
        self.assertEqual(256, self.song.bitrate)

    def test_Song_rate_func(self):
        self.song.rate(4)
        self.assertEqual(4, self.song.rating)

    def test_Song_rate_func_invalid_rating(self):
        self.assertEqual("invalid rating", self.song.rate(16))
        self.assertEqual(5, self.song.rating)

    def test_Playlist_constructor(self):
        self.assertEqual(
            self.collection[0].title, self.playList1.collection[0].title)

    def test_add_song(self):
        self.song1 = Song(
            "Shoot to thrill", "ACDC", "Back in black", 4, 4.44, 256)
        self.playList1.add_song(self.song1)
        self.assertEqual("Shoot to thrill", self.playList1.collection[1].title)

    def test_remove_song(self):
        self.song1 = Song(
            "Shoot to thrill", "ACDC", "Back in black", 4, 4.44, 256)
        self.playList1.add_song(self.song1)
        self.playList1.remove_song(self.song)
        self.assertEqual(1, len(self.playList1.collection))
        self.assertEqual("Shoot to thrill", self.playList1.collection[0].title)

    def test_total_length(self):
        self.song1 = Song(
            "Shoot to thrill", "ACDC", "Back in black", 4, 4.44, 256)
        self.playList1.add_song(self.song1)
        self.assertEqual(8.68, self.playList1.total_length())

    def test_remove_disrated_songs(self):
        self.song1 = Song(
            "Shoot to thrill", "ACDC", "Back in black", 4, 4.44, 128)
        self.playList1.add_song(self.song1)
        self.song2 = Song(
            "TNT", "ACDC", "Bon Scott baby", 3, 4.44, 256)
        self.playList1.add_song(self.song2)
        self.playList1.remove_disrated(5)
        self.assertEqual(1, len(self.playList1.collection))
        self.assertEqual("Thunderstruck", self.playList1.collection[0].title)

    def test_remove_bad_quality(self):
        flag1 = False
        self.song1 = Song(
            "Shoot to thrill", "ACDC", "Back in black", 4, 4.44, 128)
        self.playList1.add_song(self.song1)
        self.song2 = Song(
            "TNT", "ACDC", "Bon Scott baby", 3, 4.44, 256)
        self.playList1.add_song(self.song2)
        self.playList1.remove_bad_quality()
        if self.song1 in self.playList1.collection:
            flag1 = True
        self.assertFalse(flag1)

    def test_show_artists(self):
        self.song1 = Song(
            "Shoot to thrill", "ACDC", "Back in black", 4, 4.44, 128)
        self.playList1.add_song(self.song1)
        self.song2 = Song(
            "sweet child o mine", "GnR", "Apetite for destruction", 5, 6.44, 256)
        a = ["ACDC", "GnR"]
        self.playList1.add_song(self.song2)
        self.assertEqual(a, self.playList1.show_artist())

    def test_playlist_str(self):
        self.song1 = Song(
            "Shoot to thrill", "ACDC", "Back in black", 4, 4.44, 128)
        self.playList1.add_song(self.song1)
        self.song2 = Song(
            "sweet child o mine", "GnR", "Apetite for destruction", 5, 6.44, 256)
        a = ["ACDC", "GnR"]
        self.playList1.add_song(self.song2)
        a = "ACDC Thunderstruck - 4.24\nACDC Shoot to thrill - 4.44\nGnR sweet child o mine - 6.44\n"
        self.assertEqual(a, self.playList1.str())

    def test_JSON_save(self):
        self.song1 = Song(
            "Shoot to thrill", "ACDC", "Back in black", 4, 4.44, 128)
        self.playList1.add_song(self.song1)
        self.song2 = Song(
            "sweet child o mine", "GnR", "Apetite for destruction", 5, 6.44, 256)
        a = ["ACDC", "GnR"]
        self.playList1.add_song(self.song1)
        self.playList1.save("/home/biser/JSon/json1.json")
        self.song3 = Song(
            "Give in to me", "Jackson and Slash", "Best", 4, 4.44, 256)
        self.song4 = Song(
            "Cant stop", "RHCP", "blqblq", 4, 4.44, 128)
        self.playList2.add_song(self.song3)
        self.playList2.add_song(self.song4)
        self.playList2.save("/home/biser/JSon/json2.json")

    def test_JSON_load(self):
        Playlist.load("/home/biser/JSon/json1.json")
        pass


class MusicCrowler_test(unittest.TestCase):

    def test_music_crowler(self):
        crawler = MusicCrawler("/home/biser/Desktop/Music_Folder")
        playlist = crawler.generate_playlist()
        for song in playlist.collection:
            print(song.title)
            print(song.artist)
        print(playlist)
        pass
    #too lazy to finish this


if __name__ == '__main__':
    unittest.main()
