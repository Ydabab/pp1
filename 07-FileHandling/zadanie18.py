file = open("text.txt", "r", encoding="utf8")
file_content = file.read()

copy = open("copy.txt", "w", encoding="utf8")
copy.write(file_content)

file.close()
copy.close()