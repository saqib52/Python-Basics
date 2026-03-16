from functools import partial
def add(a, b):
    return a + b

add10 = partial(add, 10)
# add10(10+b)
numbers = [1,2,3]
result = list(map(add10,numbers))
print(result)