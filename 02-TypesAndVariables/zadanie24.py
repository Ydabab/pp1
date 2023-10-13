reg_number = input('Enter vehicle registration number: ')
if 'KR' in reg_number[0:2] or 'KK' in reg_number[0:2]:
    print('Car from Kraków: True')
else:
    print('Car from Kraków: False')
