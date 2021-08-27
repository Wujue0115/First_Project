import pprint
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.test_collection

find_data = collection.update_one({"_id": 10}, {"$set": {"price": -1}})