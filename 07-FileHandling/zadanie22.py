file = open("random.txt", "w")
import random
for i in range(50):
    file.write(f"{random.randrange(100,999)}")
    if i != 49:
        file.write("\n")
file.close()