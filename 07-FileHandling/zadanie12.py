name = "Krystian Byrgiel"
university = "Krakow University of Economics"
field = "Applied informatics"

file = open("student.txt", "w")
file.write(name + "\n" + university + "\n" + field + "\n")
file.close()