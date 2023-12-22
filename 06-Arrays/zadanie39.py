array = [1, 2, 4, 5, 7, 9, 12, 3, 6, 8]
even = []
odd = []
result = []
for i in array:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
for j in even:
    result.append(j)
for k in odd:
    result.append(k)
print(result)