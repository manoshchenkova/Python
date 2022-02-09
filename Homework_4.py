# Показать последнюю цифру трехзначного числа

from random import randint


initialNumber = randint(100,999)
print(f'The initial number is {initialNumber}')

print(f'The last digit of the initial number is {initialNumber%10}')