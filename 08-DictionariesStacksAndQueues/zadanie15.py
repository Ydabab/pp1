basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": "false",
    "interest": ["reading", "swimming"]
}
person = basic_data
person.update(advanced_data)
print(person)
