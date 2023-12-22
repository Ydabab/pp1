def f(arr):
    support = []
    blacklist = []
    for i in arr:
        if i not in blacklist:
            if i in support:
                blacklist.append(i)
                support.remove(i)
            elif i not in support:
                support.append(i)
    return support[0]

print(f([7,7,7,7,5,7,7]))
print(f([2,2,2,2,2,2,3,2,2]))