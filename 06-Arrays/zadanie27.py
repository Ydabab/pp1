array = [12, 6, 4, 9, 10]

def star(n):
    return (n*"*")

for i in array:
    print(f"{i}: {star(i)}")