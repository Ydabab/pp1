array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]
x = 0
sum = 0
for rows in array:
    for elements in rows:
        if elements == array[x][-1]:
            sum += elements
    x += 1
print(sum)