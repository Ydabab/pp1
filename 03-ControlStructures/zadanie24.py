price = 200
reduced = 140
if reduced <= price * 0.9:
    print("Buy the product!")
    x = reduced*100/price
    print(f"Product price reduced by {100 - x}%") 