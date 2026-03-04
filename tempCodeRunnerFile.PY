import functools as ft
num = [5,8,2,10,9]
result = ft.reduce(lambda a,b: a+b, num)
print(result)