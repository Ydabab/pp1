Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    h_list = ""
    for i in hotels:
        h_list = h_list + i["name"] + ","
    return h_list[0:-1]

print(hotel_list(Hotels_in_Krakow))

def avg_price(hotels):
    h_price = 0
    counter = 0
    for i in hotels:
        h_price = h_price + i["price"]
        counter += 1
    return h_price/counter

x = avg_price(hotels_in_Sopot)
y = avg_price(Hotels_in_Krakow)

if x > y:
    print("Hotels in Krakow are cheaper")
else:
    print("Hotels in Sopot are cheaper")

