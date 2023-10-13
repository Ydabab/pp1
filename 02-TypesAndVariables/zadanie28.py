height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))
bmi = weight/(height/100)**2
print('Your BMI index: ', bmi)
print('Correct weight: ', bmi >= 18.5 and bmi <= 24.9)
