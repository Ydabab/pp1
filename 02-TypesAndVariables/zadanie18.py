x = 7
y = 34
z = int(input('Żeby wykonać zamianę wciśnij 1: '))
if z == 1:
 z = x 
 x = y
 y = z
else:
 x = x
 y = y
print(f'x = {x}, y = {y}')