height = int(input('How tall are you in cm: '))
inch = height / 2.54
foot = inch // 12
print(f'I am {height}cm tall, i.e. {foot} feet and {inch - foot * 12} inches')