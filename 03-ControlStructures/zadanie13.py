num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 >= 0 or num2 >=0:
    print(f"At least one of entered numbers {num1} and {num2} is not negative")
else:
    print("Both numbers are negative")