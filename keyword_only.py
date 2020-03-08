def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
        print(count)
    count += extra_number
    print(count)

total(10, 1, 2, 3, 4, extra_number=10)