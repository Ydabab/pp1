def f(array2D):
    value = []
    for i in range(len(array2D[0])):
        suma = 0 
        for j in range(len(array2D)):
            suma = suma + array2D[j][i]
        value.append(suma)
    return value

print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) )