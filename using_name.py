if __name__ == '__main__':
    print("Эта программа  запущена  сама по себе ")
else:
    print("Меня  импортировали  в  другой модуль")

    name = __name__
    print(name)