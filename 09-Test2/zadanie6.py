def f(t):
    import re
    sum = 0
    x = re.findall('[0-9]+', t)
    for i in x:
        sum += int(i)
    return sum

print(f("11 and 4 is 15"))
