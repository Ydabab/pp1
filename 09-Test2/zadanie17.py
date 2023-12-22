def f(dictionary,x,y):
    suma = 0
    for key,value in dictionary.items():
        for number in value:     
            if number in range(x,y+1):
                suma += number
    return suma

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6) )