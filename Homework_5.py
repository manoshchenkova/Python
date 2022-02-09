# Дано число из отрезка (10,99). Показать наибольшую цифру числа

from random import randint


initialNumber = randint(10,99)
print(f'Initial number is {initialNumber}')

firstDigit = int(initialNumber/10)
secondDigit = int(initialNumber%10)

if firstDigit >= secondDigit:
    print(f'The largest digit in the initial number is {firstDigit}')
else:
    print(f'The largest digit in the initial number is {secondDigit}')
    