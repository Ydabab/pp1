grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

positive_grades = list(filter(lambda x: x >= 3.0, grades))
mean = sum(positive_grades) / len(positive_grades)

print(mean)