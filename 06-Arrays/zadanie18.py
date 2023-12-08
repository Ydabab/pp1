array = [
    [True, False],
    [True, True],
    [False, False]
]
i = 0
for row in array:
    j = 0
    for element in row:
        if element == True:
            array[i][j] = False
        else:
            array[i][j] = True
        j += 1
    i += 1
print(array)