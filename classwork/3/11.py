def run(a):

    if a % 2 == 0:
       raise TypeError('Mexcep')
    else:
       print(a)

try:
    run(44)
except (NameError, TypeError) as e:
    if isinstance(e, TypeError):
        print("error")
    else:
        print("name")