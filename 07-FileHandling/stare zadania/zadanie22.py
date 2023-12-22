'''
22.	Create a program that writes 50 random integers between 100 and 999 to a text file, each number on a separate line.
'''
import random
file = open("randomintegers.txt", "w")
for i in range(50):
    file.write(f"{random.randrange(100,999)}" + "\n")

file.close()