basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

person = {}
person.update(basic_data.items())
person.update(advanced_data.items())

print(person)