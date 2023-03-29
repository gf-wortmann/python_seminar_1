#Задача 6: Вы пользуетесь общественным транспортом?
#Вероятно, вы расплачивались за проезд и получали билет с номером.
#Счастливым билетом называют такой билет с шестизначным номером,
#где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.


from curses.ascii import isdigit
import math

def half (entered, head:bool):
    res = 0
    if head:
        countRange = [0,3]
    else:
        countRange = [3,6]

    for i in entered[ countRange[0] : countRange[1] ]:        
        res+=int(i)
    return res


while True:
    ticket_id = input ("enter the ticket id: ")
    if len(ticket_id) != 6:
        print("count of digits must be equal to six!")
    else:
        if ticket_id.isdigit():
            break
    print("ticket id must contain only digits!")

if half (ticket_id, True) == half (ticket_id, False):
    print('Your ticket is happy')
else:
    print('Your ticket is NOT happy, sorry... Try another.')

