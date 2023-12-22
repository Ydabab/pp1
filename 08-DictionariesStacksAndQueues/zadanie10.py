import json

with open("favourite.json") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key} : {value}")