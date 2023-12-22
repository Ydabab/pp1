def f(arr):
    value = 0
    for row in arr:
        if row[1] == (row[0]**2):
            value += 1
    return value

print(f([[4,16],[3,9],[-3,9]]))
print(f([[4,15],[3,9],[-3,-9]]))