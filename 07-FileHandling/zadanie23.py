file = open("power.txt", "w")
for i in range(1,11):
    file.write(f"{i} {i**2} {i**3}")
    if i != 10:
        file.write("\n")
file.close()