'''
17.	Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. 
Then, write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. 
The program repeats displaying the next five lines from the file, waiting for the Enter key to be pressed each time.
'''
file = open("data.txt", "r")
i = 1
for line in file:
    print(line, end="")
    if i%5 == 0 and i != 0:
        x = input()
        if x == "":
            i += 1
            continue
        else:
            break
    else:
        i += 1
file.close()