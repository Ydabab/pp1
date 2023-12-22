def create_2d_arr(x,y):
    array = []
    for i in range(x):
        array.append([])
    for j in range(0,x):
        for k in range(y):
            array[j].append(0)
    return array

print(create_2d_arr(3,5))