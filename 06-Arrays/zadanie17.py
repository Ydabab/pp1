array = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
i = 0
for row in array:
    j = 0
    for element in row:
        if j == i:
            array[i][j] = 1
        j += 1
    i += 1

print(array)