def f(c):
    cards = {
        "A": 10,
        "K": 10,
        "Q": 10,
        "J": 10,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }
    sum = 0
    for i in c:
        if i in cards.keys():
            sum += cards[f"{i}"]
    return sum

print(f("2K9"))
print(f("AJ58K"))