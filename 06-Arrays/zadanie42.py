import random
arr = [1, 2, 4, 9, 7, 3, 5, 7, 8, 12, 51, 75]

def rand_element(array):
    return array[random.randrange(0,len(array))]

print(rand_element(arr))