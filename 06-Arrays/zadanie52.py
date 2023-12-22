array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print(array)

for rows in array:
    support = rows[0]
    rows[0] = rows[-1]
    rows[-1] = support

print(array)