import random
import numpy as np

employees = ['Odd 1', 'Even 2', 'Odd 3', 'Even 4', 'Odd 5', 'Even 6', 'Odd 7', 'Even 8']

employees_d = [
    employee.split(' ')[1]
    for employee in employees
]
n = [1,2,3,4,5]
def test(*n):
    n = int(n)
    for i in range(n):
         n = int(n)
         lst = np.random_integers(-10, 10, n)
    return lst


print(test(n))