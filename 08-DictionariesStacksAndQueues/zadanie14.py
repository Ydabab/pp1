winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

hours = 0
for key, value in winter_semester.items():
    hours += value

print(f"Total number of hours is {hours}")