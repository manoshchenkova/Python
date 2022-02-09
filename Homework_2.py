# По заданному номеру дня недели вывести его номер

from pickle import NONE


week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print('Please enter the day number')
userDay = int(input())

if userDay > 7 or userDay <= 0:
    print('There are 7 days a week')
else:
    print(f'This day is {week[userDay-1]}')
