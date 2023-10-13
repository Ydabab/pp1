buy = float(input("Wprowadź cenę kupna Euro: "))
buy = round(buy, 4)
sell = float(input("Wprowadź cenę sprzedaży Euro: "))
sell = round(sell, 4)
spread = sell - buy
spread = round(spread, 4)
print(f"Euro zostało kupione za cenę {buy}, następnie sprzedane za {sell}. Zysk wynosi {spread}")