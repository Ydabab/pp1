def f(enter):
    number_of_people = 0
    for i in enter:
        if i == "+":
            number_of_people += 1
        elif i == "-":
            number_of_people -= 1
    return number_of_people

print(f("+-+++-+---"))
print(f("+-+++++-"))