array = [1,2,3,4,5]
print("start", array)
array[0] -= 1
print("-1", array)
array[-1] += 4
print("+4", array)
array[len(array)//2] *= 2
print("multiplied", array)