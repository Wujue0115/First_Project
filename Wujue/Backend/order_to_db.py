import json
from pymongo import MongoClient

with open("data/orders.json", "r") as rf: data = json.load(rf)

client = MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.test_collection
collection.drop()
db.test_collection.insert_many(data)