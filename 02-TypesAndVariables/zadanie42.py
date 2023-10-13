a = (input("Wprowadź liczbę binarną: "))
b = a[0:1] * 2**3 + a[1:2] * 2**2 + a[2:3] * 2**1 + a[3:4] * 2**0
print(b)