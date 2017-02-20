from pymongo import MongoClient, errors, TEXT


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
                                           (self.CONST_PROPERTY_ARTIST, 1)],
                                          default_language='english')

    def insert_song(self, title, artist, youtube):

        self.songsCollections.insert_one({self.CONST_PROPERTY_TITLE: title,
                                          self.CONST_PROPERTY_ARTIST: artist,
                                          self.CONST_PROPERTY_YOUTUBE: youtube})


mongo = MongoController("localhost", "27017", "admin", "pa55word")

mongo.insert_song("Capital Cites", "Safe and sound", "http://www.youtube.com/watch?v=47dtFZ8CFo8")
