array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 5]

counter = 0
for i in array2:
    if i in array1:
        counter += 1
if counter == len(array2):
    print(True)
else:
    print(False)