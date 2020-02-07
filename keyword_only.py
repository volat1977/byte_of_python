def total(initial=5, *numbers, exstra_number):
    count = initial
    for number in numbers:
        count += number
        print(count)
    count += exstra_number
    print(count)

total(10, 1, 2, 3, exstra_number=50)