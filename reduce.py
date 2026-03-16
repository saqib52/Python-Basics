# A higher order function
# Reduce is a higher order function that take two parameters a function and iterable 

import functools as ft
num = [5,8,2,10,9]
result = ft.reduce(lambda a,b: a+b, num)
print(result)

