import json

student = {
    "name": "Krystian",
    "surname": "Byrgiel",
    "age": 20,
    "university": "UEK",
    "gender": "male",
    "adult": True
}

file = open("student.json", "w")
json.dump(student, file, indent= 2)
file.close()