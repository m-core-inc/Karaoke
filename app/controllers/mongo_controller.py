from pymongo import MongoClient, errors
from app.models.song import Song


class MongoController(MongoClient):

    # Constants
    CONST_DB_NAME = "karaoke"
    CONST_PROPERTY_ID = "_id"
    CONST_PROPERTY_TITLE = "title"
    CONST_PROPERTY_ARTIST = "artist"
    CONST_PROPERTY_YOUTUBE = "youtube"

    def __init__(self, db_host, db_port, db_username, db_password):
        super().__init__()
        self.dbHost = db_host
        self.dbPort = db_port
        self.dbUsername = db_username
        self.dbPassword = db_password

        try:
            connection_string = "mongodb://{0}:{1}@{2}:{3}".format(db_username, db_password, db_host, db_port)
            self.client = MongoClient(connection_string)[self.CONST_DB_NAME]
            self.songsCollections = self.client.songs
            self.songsCollections.create_index([(self.CONST_PROPERTY_TITLE, 1),
                                                (self.CONST_PROPERTY_ARTIST, 1)], default_language='english')

        except errors.ServerSelectionTimeoutError as e:
            print("Error connecting to mongo")
            print(e)

    def get_all_songs(self):

        songs = self.songsCollections.find()[:50]
        song_list = []

        for item in songs:
            convert = Song(item[self.CONST_PROPERTY_TITLE], item[self.CONST_PROPERTY_ARTIST],
                           item[self.CONST_PROPERTY_YOUTUBE])
            song_list.append(convert)

        return song_list

    def get_song(self, title, artist):

        return self.songsCollections.find_one({self.CONST_PROPERTY_TITLE: title, self.CONST_PROPERTY_ARTIST: artist})

    def insert_song(self, title, artist, youtube):

        song = {self.CONST_PROPERTY_TITLE: title,
                self.CONST_PROPERTY_ARTIST: artist,
                self.CONST_PROPERTY_YOUTUBE: youtube}

        return self.songsCollections.update({self.CONST_PROPERTY_TITLE: title, self.CONST_PROPERTY_ARTIST: artist},
                                            song, True)

    def insert_song_obj(self, song):

        title = song.get_title()
        artist = song.get_artist()
        youtube = song.get_link()

        return self.insert_song(title, artist, youtube)

    def remove_song(self, title, artist):

        return self.songsCollections.remove({self.CONST_PROPERTY_TITLE: title, self.CONST_PROPERTY_ARTIST: artist},
                                            True)
