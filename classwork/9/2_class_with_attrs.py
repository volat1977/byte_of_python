class MyList:

    def append(self, item, item2):
        self.attr1 = item
        self.attr2 = item2

l = MyList()
l.append(1, 2)

print(l.attr1)
print(l.attr2)

l.append(3, 4)

print(l.attr1)
print(l.attr2)

l2 = MyList()
l2.append(5, 6)
print(l2.attr1)
print(l2.attr2)
