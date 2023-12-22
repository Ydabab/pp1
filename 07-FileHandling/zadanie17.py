file = open("text.txt", "r", encoding="utf8")
counter = 0
for line in file:
    if counter%5 != 0 or counter == 0:
        print(line)
        counter += 1
    if counter%5 == 0:
        x = input("Press enter to continue:")
        if x != "":
            break
        counter = 0
file.close()