import pprint
from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.test_collection


app = Flask(__name__)
CORS(app, supports_credentials = True)
@app.route("/find_order", methods = ["POST"])
def find_order():
    data = request.get_json()
    find_data = collection.find({"_id": {"$lt": int(data["id"])}})
    res = []
    for i in find_data:
        print(type(i))
        print(i)
        res.append(i)
    return {"orders": res}

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 3000, debug = True)



# pprint.pprint(collection.find({"time": "2020/5/1 5:49:10"}))

# find_data = collection.find({"price": {"$eq": 1}})
# for data in find_data:
#     print(data)

# find_data = collection.find({"_id": {"$lte": 10}})
# print(find_data)
# for data in find_data:
#     print(data)