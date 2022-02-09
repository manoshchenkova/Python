# Выяснить, кратно ли число заданному, если нет, вывести остаток

from ast import Return


print('Please enter the initial number')
initialNumber = int(input())

print('Please enter the number you would like to check for multiplicity')
multNumber = int(input())

def CheckDivision(number1, number2):
    if number2 == 0:
        print("We can't divide by 0")
        return
    if number1 % number2 == 0:
        print(f'Number {number1} is divisible to number {number2}')
    else:
        print(f'Number {number1} is divisible to number {number2} and the remainder of division is {number1 % number2}')

CheckDivision(initialNumber, multNumber)