class A:
    def __init__(self, a):
        self.a = a

    @property
    def a(self):
        return self._a


a = A(100)
print(a.a)
