error = AttributeError("My custom excep")

def run(a):

    if a % 2 == 0:
       raise error
    else:
       print(a)

try:
    run(44)
except (NameError, TypeError):
    print("error")
except AttributeError:
    print("attrib")