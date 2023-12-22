def f(d,v):
    sum = 0
    for key, value in d.items():
        if value is not v:
            sum += 1
    return sum

print(f({"a":True, "b":False, "c": True, "d": True, "e": True}, True))
print(f({"a": True, "b": False, "c": True, "d": True, "e": True}, False))