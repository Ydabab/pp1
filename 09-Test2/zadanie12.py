def f(first_letter, last_letter):
    import re
    with open("data.txt", "r") as file:
        file_content = file.read()
        lst = re.findall(f'\\b[{first_letter}]\\S*[{last_letter}]\\b', file_content)
        return len(lst)
    
print(f("t", "a"))