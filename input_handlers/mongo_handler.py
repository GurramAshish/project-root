from pymongo import MongoClient

def load_mongo_data():
    client = MongoClient('localhost', 27017)
    db = client['your_database']
    collection = db['your_collection']
    return list(collection.find())
