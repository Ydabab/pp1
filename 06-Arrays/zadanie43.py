x = "An apple a day keeps the doctor away"

def number_of_words(text):
    counter = 1
    for i in text:
        if i == " ":
            counter += 1
    return counter

print(f"Number of words in text: {number_of_words(x)}")

def array_of_words(text):
    word = ""
    array = []
    for i in text:
        if i == " ":
            array.append(word)
            word = ""
        else:
            word = word + i
    array.append(word)
    array_ordered = sorted(array, key=len, reverse= True)
    return array_ordered
print(array_of_words(x))

def array_alphabetically(text):
    word = ""
    array = []
    for i in text:
        if i == " ":
            array.append(word)
            word = ""
        else:
            word = word + i
    array.append(word)
    array_alphabet = sorted(array)
    return array_alphabet

print(array_alphabetically(x))