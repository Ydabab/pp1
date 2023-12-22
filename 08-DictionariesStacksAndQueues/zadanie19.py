import json
file = open("students.json", "r")
full_json = json.load(file)

file2 = open("limited.json", "w")
limited = []
for i in full_json:
    x = {"name": i["name"],
         "surname": i["surname"],
         "student id": i["student id"]}
    limited.append(x)
json.dump(limited, file2, indent=2)

file.close()
file2.close()