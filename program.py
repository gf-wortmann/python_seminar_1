# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

from curses.ascii import isdigit

def IntCheckedInput (message:str) :
    while True:
        res = input(f'{message}: ')
        if res.isdigit():
            return int(res)
        print('Enter digits only, please!')

def IntCheckedInputLtd (message:str, max:int) :
    while True:
        res = input(f'{message}: ')
        if res.isdigit():
            if int(res)<int(max):
                return int(res)
            else:
                print(f'number must be less than {max}')
        else:
            print('Enter digits only, please!')              

rows_in_bar = IntCheckedInput('Enter count of rows in the bar')
slices_in_row = IntCheckedInput('Enter count of slices in a row of the bar')
slices_brokenout = IntCheckedInputLtd(
    f'Enter count of slices broken out, not more than {rows_in_bar * slices_in_row // 2}',
     rows_in_bar * slices_in_row // 2)

if slices_brokenout % slices_in_row == 0 or slices_brokenout % rows_in_bar == 0:
    print(f'There is possible to brake out {slices_brokenout} slices by one break.')
else:
    print(f'No, there is impossible to brake out {slices_brokenout} slices in one row.')
    