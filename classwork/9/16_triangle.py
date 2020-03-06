class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Client(Person):
    pass




