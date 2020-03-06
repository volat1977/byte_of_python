class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name)
        print(bases)
        print(namespace)
        namespace["atata"] = "asdasd"
        return super().__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):

    def foo(self):
        print("foo")

    def bar(self):
        print("bar")

    @classmethod
    def set_atata(cls, val):
        cls.atata = val


print(A.atata)
A.set_atata(1)
print(A.atata)
