array1 = [
    [2,3],
    [1,5]
]
array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]
array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]
def two_into_one(arr):
    arr_1d = []
    for rows in arr:
        for elements in rows:
            arr_1d.append(elements)
    return arr_1d

print(two_into_one(array1))
print(two_into_one(array2))
print(two_into_one(array3))