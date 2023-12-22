dist = 70
hr = 1
min = 23

def avg_speed(distance, hours, minutes):
    time = hours + (minutes/60)
    speed = distance/time
    return speed

print(f"Enter distance in km: {dist}")
print(f"Enter number of travel hours: {hr}")
print(f"Enter number of travel in minutes: {min}")
print(f"Average speed: {avg_speed(dist,hr,min)} km/h")