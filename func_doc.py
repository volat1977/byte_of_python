def printMax(x, y):
    '''Выводит  максимальное  из  2 х чисел
    Оба значения  должны  быть  целыми  числами '''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printMax(3, 5)
print(printMax.__doc__)

