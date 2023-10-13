a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
p = (a+b+c)/2
area1 = (p*(p-a)*(p-b)*(p-c))
area2 = area1**0.5
circumference = a+b+c
print(f'''
      a = {a} 
      b = {b} 
      c = {c} 
      area = {area2} 
      circumference = {circumference}''')
