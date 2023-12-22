import random
array = []
for i in range(8):
    array.append(random.randint(1,999))
print("-----------------------------------------")
for j in array:
    if len(str(j)) == 1:
        print(f"|   {j}", end="")
    elif len(str(j)) == 2:
        print(f"|  {j}", end="")
    elif len(str(j)) == 3:
        print(f"| {j}", end="")
    if j == array[-1]:
        print("|", end="\n")
print("-----------------------------------------")