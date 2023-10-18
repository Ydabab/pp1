number = int(input("Enter number of products purchased: "))
price = float(input("Enter price of the product: "))
if number > 2:
    amount = 2*price + (number-2)*(0.75*price)
else:
    amount = number*price
print(f"Amount to pay: {amount}")

