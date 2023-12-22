text = "I completely agree with you"
arr = text.split()

result = map(lambda x : len(x),arr)

print(result)