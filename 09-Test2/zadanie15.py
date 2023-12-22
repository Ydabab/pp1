def f(human_age):
    if human_age > 2:
        return 20 + 4*(human_age-2)
    else:
        return 10*human_age

print(f(15))
print(f(2))