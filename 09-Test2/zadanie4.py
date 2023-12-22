def f(arr):
    support = []
    blacklist = []
    for i in arr:
        if i not in blacklist:
            if i in support:
                support.remove(i)
                blacklist.append(i)
            else:
                support.append(i)
    return len(support)

print(f([11,22,33,11]))
print(f([11,22,11,11,22,35,27,11,22,14]))