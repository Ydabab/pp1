i = 1
sum = 0
for i in range(1,10):
    if i % 2 == 0:
        sum = sum + i
        i = i + 1
    else:
        i = i + 1
print(f"Sum is {sum}")