def func2(a):
    if not isinstance(a,int):
        print(a**2)

def func1(a):
    try:
        func2(a)
    except ValueError:
        func2(int(a))



a = int(input())

out = func2(a)

print(out)

