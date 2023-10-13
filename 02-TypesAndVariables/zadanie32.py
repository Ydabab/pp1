amount = float(input("Wprowadź wartość "))
vat = 0.23 * amount
amount = round(amount, 2)
vat = round(vat, 2)
print("Wartość: ", amount)
print("Vat: ", vat)