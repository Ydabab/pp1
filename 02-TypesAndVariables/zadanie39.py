price = float(input("Podaj cenę "))
discount = int(input("Podaj % zniżki "))
price_disc = price * (1 - (discount/100))
reduction = price - price_disc
price = round(price, 2)
discount = round(discount, 2)
price_disc = round(price_disc, 2)
reduction = round(reduction, 2)
print(f"Cena początkowa: {price}, obniżka: {discount}, cena po obniżce: {price_disc}, wartość obniżki: {reduction}")