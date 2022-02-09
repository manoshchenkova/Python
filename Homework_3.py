# Показать числа от -N до N

from random import randint

N = randint(1,10)

print(f'Number N is {N}')

for numbers in range(N*-1,N+1):
    print (numbers, end = " ")