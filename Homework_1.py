# По двум заданным числам проверить, является ли первое квадратом второго

print(f'Enter first number:')
number1 = float(input())

print(f'Enter second number:')
number2 = float(input())

if number1 == number2**2:
    print(f"Number {number1} is a square of {number2}")
else:
    print(f"Number {number1} is NOT a square of {number2}")