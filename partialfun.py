'''In Python, a partial function lets you fix (pre-fill) some arguments of another function, 
creating a new function with fewer parameters. 
This is very useful for cleaner, reusable code.
synatx partial(func, arg1, arg2, arg3)'''

from functools import partial

'''Original function:
-------power(base, exponent)
Partial function:
-------square(base) = power(base, 2)'''

# Step 1 - Original Function
def power(base,exponent):
    return base ** exponent
# Step 2 - You can create a new function with exponent fixed to 2.
square = partial(power, exponent = 2)

# Now square() behaves like:
# square(x) = power(x, 2)
print(square(3))
print(square(4))

# Step 1 — Original Function
def add(n1,n2,n3,n4):
    return n1 + n2 + n3 + n4

# Step 2 - Creating the Partial Function with fixed arguments as n3,n4
sum = partial(add, n3= 2, n4=3)
print(sum(10,20))



# Original function: -------power(base, exponent) 
# Partial function: -------square(base) = power(base, 2) 
# vs -------power(base, exponent=2) difference behave same?


# Partial functions help create pipeline steps.
from functools import partial
def add(a, b):
    return a + b

add10 = partial(add, 10)
# add10(10+b)
numbers = [1,2,3]
result = list(map(add10,numbers))
print(result)


# partial function is commonly used in dependecy injection in fastapi e.g database connection
