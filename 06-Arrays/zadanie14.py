array = [
    [2, 5, 4],
    [9, 0, 3]
]

print(array)
print(f"columns: {len(array)}, rows: {len(array[0])}")
print(array[0][1])
print(array[1][2])
for i in array[1]:
    print(i, end=" ")