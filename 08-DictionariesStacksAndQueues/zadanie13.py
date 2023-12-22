dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
counter = 0
for key, value in dictionary.items():
    counter += 1

print(f"Number of key: value pairs is: {counter}")