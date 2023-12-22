array = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
i = 1
for rows in array:
    j = 0
    for elements in rows:
        array[i-1][j] = i * (j+1)
        j += 1
    i += 1

print(array)