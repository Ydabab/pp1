array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

for rows in array:
    for elements in rows:
        print(elements, "\t", end="")
    print("\n")