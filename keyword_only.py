def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
        print(count)
    count += keywords[key]
    print(count)

total(10, 1, 2, 3, vegetables=50, fruits=100)