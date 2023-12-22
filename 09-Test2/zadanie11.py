def f(subjects):
    suma = 0
    przedmiot = ""
    for key, value in subjects.items():
        if sum(value)/len(value) > suma:
            przedmiot = key
    return key

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))