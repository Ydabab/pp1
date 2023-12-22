icao = {
    "a":"Alfa",
    "b":"Bravo",
    "c":"Charlie",
    "d":"Delta",
    "e":"Echo",
    "f":"Foxtrot",
    "g":"Golf",
    "h":"Hotel",
    "i":"India",
    "j":"Juliett",
    "k":"Kilo",
    "l":"Lima",
    "m":"Mike",
    "n":"November",
    "o":"Oscar",
    "p":"Papa",
    "q":"Quebec",
    "r":"Romeo",
    "s":"Sierra",
    "t":"Tango",
    "u":"Uniform",
    "v":"Vector",
    "w":"Whiskey",
    "x":"Xray",
    "y":"Yankee",
    "z":"Zulu"
    }

text = str(input("Enter text: "))
for letter in text:
    for key,value in icao.items():
        if letter == key:
            print(value, end=" ")