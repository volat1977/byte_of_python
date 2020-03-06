from time import time
from functools import wraps

@wraps # декоратор
def time_me(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        stop = time()
        delta = stop -start
        print("time: ", delta)
        return result
    return wrapper

@time_me # декоратор
def pow(m, n):
    return m **n

print(pow(100, 10))
print(pow(100, 1000))
print(pow(10000, 10000))
