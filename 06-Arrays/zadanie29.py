array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]
result = []
for i in array1:
    if i not in array2:
        result.append(i)
    else:
        continue

print(result)