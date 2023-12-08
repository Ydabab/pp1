names = ["Genowefa", "Onfury", "Celestyna", "Alojzy", "Pankracy"]
length = 0
longest_name = None
for i in names:
    if len(i) > length:
        lenght = len(i)
        longest_name = i

print(f"{longest_name} is the longest name with lenght of: {lenght}")