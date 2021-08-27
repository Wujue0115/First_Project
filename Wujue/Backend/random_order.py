import random as rd


# class Order:
#     def __init__(self, name: str = "", time: str = "", commodity: str = "", price: int = 0, status: str = ""):
#         self.name = name
#         self.time = time
#         self.commodity = commodity
#         self.price = price
#         self.status = status

#     def show_order(self):
#         print("{")
#         print(f"  \"name\": {self.name}")
#         print(f"  \"time\": {self.time}")
#         print(f"  \"commodity\": {self.commodity}")
#         print(f"  \"price\": {self.price}")
#         print(f"  \"status\": {self.status}")
#         print("}")

#     def get_json(self, i, n) -> str:
#         res = "  {\n"
#         res += f"    \"_id\": {i + 1},\n"
#         res += f"    \"name\": \"{self.name}\",\n"
#         res += f"    \"time\": \"{self.time}\",\n"
#         res += f"    \"commodity\": \"{self.commodity}\",\n"
#         res += f"    \"price\": {self.price},\n"
#         res += f"    \"status\": \"{self.status}\"\n"
#         res += "  }"
#         if i != n - 1: res += ","
#         res += "\n"
#         return res


def data_to_names(path: str) -> list[str]:
    res = []
    with open(path, "r") as rf:
        for name in rf.readlines():
            name = name[:-1]
            if name.encode("utf-8").isalpha(): 
                res.append(name)
    return res
names = data_to_names(path = "data/names_data.txt")

def get_random_name() -> str:
    return names[rd.randint(0, len(names) - 1)]

def get_random_time(min_year = 2000, max_year = 2020) -> str:
    max_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = rd.randint(min_year, max_year)
    month = rd.randint(1, 12)

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: max_day[2] = 29
    else: max_day[2] = 28
    day = rd.randint(1, max_day[month])

    hour = rd.randint(0, 23)
    minute = rd.randint(0, 59)
    second = rd.randint(0, 59)

    return f"{year}/{month}/{day} {hour}:{minute}:{second}"

def get_random_commodity() -> str:
    commodities = ["shirt", "polo shirt", "jacket", "coat", "short pants", "jeans", "tie", "chain"]
    return commodities[rd.randint(0, len(commodities) - 1)]

def get_random_price(min_price = 1, max_price = 1000) -> str:
    return rd.randint(min_price, max_price)

def get_random_status() -> str:
    return ["已付款", "送貨中", "已送達", "已取貨"][rd.randint(0, 3)]

def data_to_json(i, n, name, time, commodity, price, status) -> str:
    res = "  {\n"
    res += f"    \"_id\": {i + 1},\n"
    res += f"    \"name\": \"{name}\",\n"
    res += f"    \"time\": \"{time}\",\n"
    res += f"    \"commodity\": \"{commodity}\",\n"
    res += f"    \"price\": {price},\n"
    res += f"    \"status\": \"{status}\"\n"
    res += "  }"
    if i != n - 1: res += ","
    res += "\n"
    return res


n = int(1e5)
# orders = []
# for i in range(n): 
#     name = get_random_name()
#     time = get_random_time()
#     commodity = get_random_commodity()
#     price = get_random_price()
#     status = get_random_status()
#     orders.append(Order(name, time, commodity, price, status))

with open("data/orders.json", "w") as wf:
    wf.write("[\n")
    for i in range(0, n):
        name = get_random_name()
        time = get_random_time()
        commodity = get_random_commodity()
        price = get_random_price()
        status = get_random_status()

        wf.write(data_to_json(i, n, name, time, commodity, price, status))
    wf.write("]")

