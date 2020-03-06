class Person():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def __eq__(self, other):
        return self.name == other.name

p1 = Person("John", "Doe")
p2 = Person("Mark", "Lutc")
p3 = Person("John", "Doe")


print(p1 == p2)
print(p1 == p3)