import random as rd
from pymongo import MongoClient
from flask import Flask
from flask_cors import CORS


def data_to_names(path: str) -> list[str]:
    res = []
    with open(path, "r") as rf:
        for name in rf.readlines():
            name = name[:-1]
            if name.encode("utf-8").isalpha(): 
                res.append(name)
    return res


def get_random_name() -> str:
    return names[rd.randint(0, len(names) - 1)]


def get_random_time(min_year = 2000, max_year = 2020) -> str:
    max_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = rd.randint(min_year, max_year)
    month = rd.randint(1, 12)
    month_space = "0" * (2 - len(str(month)))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: max_day[2] = 29
    else: max_day[2] = 28
    day = rd.randint(1, max_day[month])
    day_space = "0" * (2 - len(str(day)))

    time1 = f"{year}/{month_space}{month}/{day_space}{day}"

    
    hour = rd.randint(0, 23)
    hour_space = "0" * (2 - len(str(hour)))
    minute = rd.randint(0, 59)
    minute_space = "0" * (2 - len(str(minute)))
    second = rd.randint(0, 59)
    second_space = "0" * (2 - len(str(second)))

    time2 = f"{hour_space}{hour}:{minute_space}{minute}:{second_space}{second}"

    space = 19 - (len(time1) + len(time2))

    return time1 + " " + time2


def get_random_commodity() -> str:
    commodities = ["shirt", "polo shirt", "jacket", "coat", "short pants", "jeans", "tie", "chain"]
    return commodities[rd.randint(0, len(commodities) - 1)]


def get_random_price(min_price = 1, max_price = 1000) -> str:
    return rd.randint(min_price, max_price)


def get_random_status() -> str:
    return ["已付款", "送貨中", "已送達", "已取貨"][rd.randint(0, 3)]


def data_to_dict(name, time, commodity, price, status) -> dict:
    res = {}
    res["_id"] = i + 1
    res["name"] = name
    res["time"] = time
    res["commodity"] = commodity
    res["price"] = price
    res["status"] = status
    return res


client = MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.test_collection
collection.drop()


names = data_to_names(path = "data/names_data.txt")
n = int(1e5)
orders = []
for i in range(0, n):
    name = get_random_name()
    time = get_random_time()
    commodity = get_random_commodity()
    price = get_random_price()
    status = get_random_status()
    orders.append(data_to_dict(name, time, commodity, price, status))
    
collection.insert_many(orders)

