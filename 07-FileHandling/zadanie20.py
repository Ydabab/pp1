'''
20.	Using any text editor, create the following two text files:
MeatAndFish.txt
Skinless white meat
Tuna fish
Luncheon meat
Lean cuts of red meat
GrainsAndBread.txt
Bread
Rice
All purpose flour
Breakfast cereal
Pasta 
Then, write a program that creates the allproducts.txt file, 
in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.
'''
file = open("allproducts.txt", "w")
meat = open("MeatAndFish.txt", "r")
x = meat.read()
file.write(x)
file.close()

file2 = open("allproducts.txt", "a")
grains = open("GrainsAndBread.txt", "r")
y = grains.read()
file2.write(y)

file2.close()
meat.close()
grains.close()
