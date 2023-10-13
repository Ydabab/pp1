import random
x = random.randrange(1,7)
y = int(input("Zgadnij jaką liczbę wyrzuciłem "))
if y == x:
    print("Gratuluję!")
else:
    print("Nie tym razem! Spróbuj jeszcze raz! Moja liczba to: ", x)