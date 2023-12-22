def f(array2D):
    for i in range(len(array2D)):
        suma = 0
        for rows in array2D:
            suma = suma + rows[i]
        if suma != sum(array2D[i]):
            return False
    return True

print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))