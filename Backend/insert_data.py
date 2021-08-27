import random as rd
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.test_collection
collection.drop()


n = int(1e4)
orders = []
for i in range(0, n):
    name = get_random_name()
    time = get_random_time()
    commodity = get_random_commodity()
    price = get_random_price()
    status = get_random_status()
    orders.append(data_to_dict(name, time, commodity, price, status))

collection.insert_many(orders)

