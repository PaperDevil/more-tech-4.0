import pymongo

def get_post_collection():
    client = pymongo.MongoClient('mongodb://mongosir:mongopass@localhost:27017/')
    collection = client['posts']
    return collection
