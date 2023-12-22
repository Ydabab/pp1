'''
18.	Find any text file on the Internet and download it to your computer. 
Then write a program that copies the contents of this file to the copy.txt file. 
Copy the contents of the file as a whole. Finally, open both files in any text editor and check that their contents are the same.
'''
original = open("data.txt", "r")
file = original.read()
copy = open("copy.txt", "w")
copy.write(file)

original.close()
copy.close()