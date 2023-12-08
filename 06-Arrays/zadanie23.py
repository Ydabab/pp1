array = [-15, 8, -31, 47, -2, 19]
min_value = 0
max_value = 0

for i in array:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i 

print(min_value)
print(max_value)