'''
10.	Find any text file on the Internet and download it to your computer. Then, write a program that displays its content.
'''
data = open('data.txt', 'r')
file = data.read()
print(file)
data.close()