def f(player1, player2):
    cards = {
    "A": 10,
    "K": 10,
    "Q": 10,
    "J": 10,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
    }
    player1_sum = 0
    player2_sum = 0
    for i in player1:
        if i in cards:
            player1_sum += cards[f"{i}"]
    for i in player2:
        if i in cards:
            player2_sum += cards[f"{i}"]
    if player1_sum > player2_sum:
        return True
    else:
        return False
    
print(f("AJ972","AQT72"))
print(f("9532","K8"))