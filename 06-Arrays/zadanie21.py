array = [15, 8, 31, 47, 2, 19]
reversed_array = []
print(array)
for i in range(len(array)):
    reversed_array.append(array[-i - 1])
print(reversed_array)