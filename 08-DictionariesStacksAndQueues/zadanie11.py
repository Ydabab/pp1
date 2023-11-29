movie = {
    "title": "asdddsa",
    "year": 1994,
    "actor": {"leading": "prrrrrr", "supporting": "trrrrrrrr"},
    "oscar": True,
    "director": "aaaaa"
}
import json
file = open("favourite.json", "w")
json.dump(movie, file, indent= 4)
file.close()