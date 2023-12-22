
def f(e):
    sum = int(e[0])
    i = 0
    for znak in e:
        if znak == "+":
            sum = sum + int(e[i+1])
        if znak == "-":
            sum = sum - int(e[i+1])
        i = i+1
    return sum

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))       