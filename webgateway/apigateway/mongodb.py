import pymongo

def get_post_collection():
    client = pymongo.MongoClient('mongodb://mongosir:mongopass@185.104.112.241:27017/')
    return client
