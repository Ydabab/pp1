employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter"),("Johnson","Rick"),("Lewis","Terry"),("Clarke","Robin")]

capitalized = list(map(lambda x: x[0].upper() + ", " + x[1], employees))

print(capitalized)