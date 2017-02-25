from pymongo import MongoClient, errors, TEXT
from app.models.song import Song


class MongoController(MongoClient):

    # Constants
    CONST_DB_NAME = "karaoke"
    CONST_PROPERTY_ID = "_id"
    CONST_PROPERTY_TITLE = "title"
    CONST_PROPERTY_ARTIST = "artist"
    CONST_PROPERTY_YOUTUBE = "youtube"

    def __init__(self, dbHost, dbPort, dbUsername, dbPassword):
        self.dbHost = dbHost
        self.dbPort = dbPort
        self.dbUsername = dbUsername
        self.dbPassword = dbPassword
        connectionString = "mongodb://{0}:{1}@{2}:{3}".format(dbUsername, dbPassword, dbHost, dbPort)
        self.client = MongoClient(connectionString)[self.CONST_DB_NAME]
        self.songsCollections = self.client.songs
        self.songsCollections.create_index([(self.CONST_PROPERTY_TITLE, 1),
                                           (self.CONST_PROPERTY_ARTIST, 1)], default_language='english')

    def get_song(self, title, artist):

        space = []

    def insert_song(self, title, artist, youtube):

        song = {self.CONST_PROPERTY_TITLE: title,
                self.CONST_PROPERTY_ARTIST: artist,
                self.CONST_PROPERTY_YOUTUBE: youtube}

        return self.songsCollections.update({self.CONST_PROPERTY_TITLE: title, self.CONST_PROPERTY_ARTIST: artist},
                                     song,
                                     True)

    def insert_song_obj(self, song):

        title = song.get_title()
        artist = song.get_artist()
        youtube = song.get_link()

        return self.insert_song(title, artist, youtube)

    def remove_song(self, title, artist):

        song = {}


mongo = MongoController("localhost", "27017", "admin", "pa55word")

mongo.insert_song("Safe and sound", "Capital Cites", "http://www.youtube.com/watch?v=47dtFZ8CFo8")

song = Song("In The End", "Linkin Park", "www.youtube.com/watch?v=eVTXPUF4Oz4")

mongo.insert_song_obj(song)