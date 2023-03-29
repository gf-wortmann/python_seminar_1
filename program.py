#Задача 2: Найдите сумму цифр трехзначного числа.

import math

number = input('Enter a 3-digit number: ')
result : int = 0
if number.isdigit() and (len(number) == 3) :
    for i in number :
        result += int(i)
    print(f'Sum of the digits of the the entered number is equal to: {result}')
else:
    print('It seems to me you\'ve entered an incorrect number...')
    