scores = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
    return lambda pts: pts>=limit

min70 = list(filter(min_pts(70), scores))
min40 = list(filter(min_pts(40), scores))
min30 = list(filter(min_pts(30), scores))

print("Min 70 pts:", min70)
print("Min 40 pts:", min40)
print("Min 30 pts:", min30)