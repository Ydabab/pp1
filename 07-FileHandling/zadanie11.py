file = open("numbers.txt", "r")
sum = 0
for line in file:
    x = int(line)
    sum += x
print(f"Sum: {sum}")
file.close()
