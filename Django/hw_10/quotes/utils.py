from pymongo import MongoClient
from conf import settings

def get_mongodb():
    client = MongoClient(settings.MongoClient)
    db = client[settings.MongoDB]
    return db