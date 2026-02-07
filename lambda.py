
'''A one-line anonymous (nameless) function that can take any number of arguments but has only one expression.'''

'''Basic Syntax is:
# lambda arguments: expression'''

double = lambda x: x*2
print(double(5))

cal = lambda x,y=10: x+y
print(cal(5))

'''lambda → keyword that says “I’m creating a function”
x → input (just like function parameter)
: → separates input from logic
x * 2 → what to return (NO return keyword)
Lambda always returns automatically
A lambda can only contain ONE expression, not statements.'''

square = lambda x: x*x
print(square(5))

cube = lambda x: x*x*x
print(cube(3))

avg = lambda x,y : x+y/2
print(avg(10,15))

# incrementing number
incr = lambda n: n+1
print(incr(5))

# uppercase string conversion
upper= lambda str: str.upper()
print(upper("saqib"))

# celcius to fh
fahrenheit = lambda c: c*9/5 + 32
print(fahrenheit(37))

# Multiple statement are not allowed
# add_sub= lambda x,y: x+y , x-y
# print(add_sub(5,5))

# Multiple statement are allowed while passing as tuple 
add_sub= lambda x,y: (x+y , x-y)
print(add_sub(5,5))

x =lambda: print("Hello world")
x()

check_number = lambda x: "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
print(check_number(9))

'''why we used lambda function instead of named function
1- lambda function can be used as parameter for functions that accept function as parameter
2-very small expression and less code required
3-mostly used in higher order functions'''


print(sorted([10,5,6,20,78,98,24,12,98,76]))

print(sorted(['Saqib', 'Aqib', 'Talha', 'Ali']))

print(sorted(['Jawad Saqib ', 'Behzad Aqib', 'Rehman Talha', 'Zafar Ali'],key= len))
data = ['Jawad Saqib ', 'Behzad Aqib', 'Rehman Talha', 'Zafar Ali']
print(sorted (data,key = len))


print("jawad saqib".split()[1]) # saqib
# print("jawad saqib".split()[::-1])  # ['saqib', 'jawad']


def func(nm):
    names = nm.split()
    first_names = names[1]
    return first_names  
    # return nm.split()[1] 

data = ['Jawad Saqib ', 'Behzad Aqib', 'Rehman Talha', 'Zafar Ali']
print(sorted(data, key = lambda nm: nm.split()[1]))


# Nested Lambda function

def outer():
    def add(num1,num2):
        return num1 + num2
    return add

add = outer()
print(add(2,3))

def outer():
    return lambda num1,num2: num1 + num2
add = outer()
print(add(3,3))


# lambda function with list comprehension

num1 = int(input(f'Enter num1 = '))
num2 = int(input(f'Enter num2 = '))

max1 = lambda n1,n2 : n1 if n1>=n2 else n2

print(max1(num1, num2))


nums = [3,4,5,6]
square = lambda lst: [i*i for i in nums]
print(square(nums))

square = lambda: [i*i for i in [3,4,5,6]]
print(square())


# IIFE concepts of JAVASCRIPTS

result = (lambda a,b: a+b)(4,5)
print(result)

'''First class Functions'''

properties:
# they are instance of some class
# can be stored in dat Structures
# can be assigned to variables
# can perform operation on these objects
# can be passed as arguments to functions
# can be returned

