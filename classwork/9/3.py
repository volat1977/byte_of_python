class Rectangle:
    def __init__(self, a, b):
        print("INIT")
        self.a = a
        self.b = b
    def perimetr(self):
        return (self.a + self.b)


       
rec = Rectangle(10,5)

print(rec.perimetr())