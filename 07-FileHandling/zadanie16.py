x = input("Enter file name:")
file = open(x, "r")
counter = 0
for line in file:
    counter += 1
print(f"File name: {x}")
print(f"Number of lines: {counter}")
file.close()