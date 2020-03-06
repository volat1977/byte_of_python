class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __eq__(self, other):
        return (self.name, self.lastname) == (other.name, other.lastname)


from dataclasses import dataclass

@dataclass
class Person2:
    name: str
    lastname: str

    middlename: str = None


p1 = Person2(name="Ivan", lastname="Ivanov")
print(p1)
p2 = Person2("Ivan", "Ivanov")
print(p2)
print(p1 == p2)

print(p1.name)
print(p1.middlename)





