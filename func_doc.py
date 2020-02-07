#!/usr/bin/python3
def printMax(x, y):
    '''Выводит максимальное
    оба значения                 '''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


printMax(3, 5)
print(printMax.__doc__)