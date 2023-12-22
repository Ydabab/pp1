file = open("allproducts.txt", "w")
meat = open("MeatAndFish.txt", "r")
grains = open("GrainsAndBread.txt", "r")

meat_content = meat.read()
grains_content = grains.read()

file.write(meat_content + "\n" + grains_content)

file.close()
meat.close()
grains.close()