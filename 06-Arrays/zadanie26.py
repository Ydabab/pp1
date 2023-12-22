names = ["Genowefa", "Onfury", "Celestyna", "Alojzy", "Pankracy"]
word = 0
longest_name = ""
for i in names:
    if len(i) > len(longest_name):
        longest_name = i
        word = len(longest_name)
        
print(f"{longest_name} is the longest name with lenght of: {word}")