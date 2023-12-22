'''
16.	Write a program that calculates the number of lines for any text file. 
The user enters the name of the file from the keyboard. 
Display the result of the calculation (the file name and the number of lines). 
Do not display the contents of the file. Sample result:
File name: countries.txt
Number of lines: 14
'''
file_name = input("File name: ")
file = open(file_name, "r")
counter = 0
for line in file:
    counter += 1
print(f"File name: {file_name}" + "\n" + f"Number of lines: {counter}")
file.close()