countries = [
    {"name": "Polska",
    "population": 38000000},
    {"name": "Niemcy",
     "population": 83000000},
    {"name": "Czechy",
     "population": 10500000},
    {"name": "Wielka Brytania",
     "population": 67000000},
    {"name": "Francja",
     "population": 67000000}
]

i = 0
while i < len(countries):
    print(countries[i]["name"], " ", countries[i]["population"])
    i += 1