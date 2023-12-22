student = {
    "name": "Krystian",
    "surname": "Byrgiel",
    "age": 20,
    "index": 230665,
    "gender": "male",
    "adult": True
}

import json
file = open("student.json", "w")
json.dump(student, file, indent= 2)
file.close()