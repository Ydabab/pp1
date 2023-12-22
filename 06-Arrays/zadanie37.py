array = [7, 3, 8, 5, 2]
def second_largest(arr):
    x = 0
    for i in arr:
        if i > x and i < max(arr):
            x = i
    return x

print(second_largest(array))

def difference(arr):
    value = max(arr) - min(arr)
    return value

print(difference(array))

def smallest_biggest(arr):
    numbers = [min(arr), max(arr)]
    return numbers

print(smallest_biggest(array))

def string(arr):
    x = str("")
    for i in arr:
        x = x + "-" + f"{i}"
    return x[1:]

print(string(array))

