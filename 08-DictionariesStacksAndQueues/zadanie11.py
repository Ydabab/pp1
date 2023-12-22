movie = {
    "title":"asd",
    "year": 1234,
    "actor": {"leading": "Tim", "supporting": "Tom"},
    "oscar": False,
    "director": "Christopher Nolan"
}

import json

file = open("favourite.json", "w")
json.dump(movie, file , indent=4)
file.close()