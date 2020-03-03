l = [1, 2, 3, 4, 5]
def func(a):
    a.append(100)
    a =  [1, 2, 3]
print(l)

func(l)

print(l)