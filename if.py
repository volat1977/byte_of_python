number = 23
guess = int(input('Введите целое число: '))

if guess == number:
    print('Поздравляю вы  угадали,')
    print('(Хотя и  не  выйграли никакого приза!)')
elif guess < number:
    print('Нет, загаданное  число немного больше  этого')
else:
    print('Нет, загаданное  число  немного  больше  этого.')

print('завершено')

