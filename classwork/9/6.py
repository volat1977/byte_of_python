class Person:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        return 1