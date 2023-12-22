x = int(input())
array = [2, 5, 7, 1, 4, 9, 13]
greater = []

for i in array:
    if i > x:
        greater.append(i)

print(greater)