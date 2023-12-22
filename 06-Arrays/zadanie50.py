array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]
min = 0
max = 0
rmin = 0
rmax = 0
cmin = 0
cmin = 0
r = 0 #row
for rows in array:
    c = 0 #column
    for elements in rows:
        if elements > max:
            max = elements
            rmax = r
            cmax = c
        if elements < min:
            min = elements
            rmin = r
            cmax = c
        c += 1
    r += 1

print(f"Max value is {max} and its located in row {rmax} in column {cmax}. Min value is {min} and its located in row {rmin} in column {cmin}.")