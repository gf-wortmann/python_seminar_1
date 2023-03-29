# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
from curses.ascii import isdigit
import math


while True:
    s = input('Enter how many paper cranes have made all the kids? (Number must be natural) :')
    try:
        s = int(s)
        if s > 0:
            if s % 6 == 0:
                print (f'Katya has made {s//3*2} paper cranes and every boy by {s//6} ones')
                break
            else: 
                print ('Sorry, number of paper cranes must be a multiple of six')
        else: 
            print(f'Sorry, {s} isn\'t a natural number')
    except :
        print(f'Sorry, you\'ve entered incorrect number or not a number..')
