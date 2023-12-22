dist = 70
hr = 1
min = 23
avg_speed = lambda dist, hr, min : dist / (hr + (min/60))


print(f"Enter distance in km: {dist}")
print(f"Enter number of travel hours: {hr}")
print(f"Enter number of travel in minutes: {min}")
print(f"Average speed: {avg_speed(dist,hr,min)} km/h")