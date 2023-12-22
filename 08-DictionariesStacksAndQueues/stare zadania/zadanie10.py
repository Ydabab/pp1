import json
with open("data.json") as file:
    data = json.load(file)

for key, value in data[0].items():
    print(f"{key} : {value}")