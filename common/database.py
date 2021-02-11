import pymongo
import os

class Database(object):
    
    Uri = "mongodb://127.0.0.1:27017"
    uri = "mongodb://ithollie:hawaibrahB1a@ds023478.mlab.com:23478/full_stack?retryWrites=true&w=majority"
    online = "mongodb+srv://new_user_12:hawaibrahB1a1@cluster0.jdn8r.mongodb.net/full_stack?retryWrites=true&w=majority"
    
    DATABASE = None

    def __init(self):
        pass

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.connectUrl(Database.Uri, Database.online))
        Database.DATABASE = client['full_stack']

    @staticmethod
    def connectUrl(uri_connection, online_connection):
        if online_connection is not None:
            return online_connection

    @staticmethod
    def collectionexists(collection):
        if Database.DATABASE[collection]:
            return True
        else:
            return False

    @staticmethod
    def dropCollection(collection):
        Database.DATABASE[collection].drop()


    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    # @staticmethod
    # def createCollections(collectionOne, collectionTwo):
    #     Database.DATABASE.create_collection(collectionOne)
    #     Database.DATABASE.create_collection(collectionTwo)
        
    @staticmethod
    def updates(collection, data, data1):
        Database.DATABASE[collection].update(data, data1)

    @staticmethod
    def delete(collection, data):
        Database.DATABASE[collection].remove(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
