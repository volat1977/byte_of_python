while True:
    s = input('Введите что-нибуть : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введенная строка достаточной  длинны')