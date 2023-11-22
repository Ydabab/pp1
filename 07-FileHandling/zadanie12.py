'''
12.	Create a program that saves in the student.txt file, in three separate lines, your name and surname, university name and field of study.  
Tip: open a file in writing mode and use the write() method. Sample result:
# define personal data
name = "Anna May"
university = "Krakow University of Economics"
field = "Applied Informatics"

# write to a file
file = open("student.txt",…)
file.write(name+"\n")
...
file.close()
'''
name = "Krystian Byrgiel"
university = "Krakow University of Economics"
field = "Applied Informatics"


student = open("student.txt", "w")
student.write(name + "\n")
student.write(university + "\n")
student.write(field + "\n")

student.close()