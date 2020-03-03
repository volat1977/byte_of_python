class ADescr:
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, type=None):
        print(self)
        print(obj)
        print(type)
        return self.value

    def __set__(self, obj, value):
        pass

class A:
    b = ADescr(100)

a = A()
print(a.b)
a.b = 500
print(a.b)
