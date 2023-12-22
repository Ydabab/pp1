movie_titles = ["abc", "def", "ghi", "jkl", "mno"]
file = open("movies.txt", "w")
for i in movie_titles:
    file.write(i + "\n")