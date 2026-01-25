# The eval() function takes a string and executes it as a Python expression, then returns the result.
# eval() only evaluates expressions (not statements like for loops or if blocks).
# Mutable default arguments
# concept of closure
# Closures allow functions to “remember” variables from their enclosing scope. 
# Lambdas are a concise way to write anonymous functions.

# Two types of function
# parameterized and non-parameterized functions

'''non-parameterized functions: A non-parameterized function does not take any input/arguments.
Performs a fixed task, simple and easy to understand.
'''
def greet():
    print("Hello World")
greet()

'''parameterized:take inputs'''
def add(a,b):
    print(a + b)
add(5,10)

# arguments = actual arguments
# parameters = fromal arguments

def simple_interest(p,n,r):
    print("principal amount is :",p)
    print("number of year is :",n)
    print("rate of interest :",r)
    si = (p*n*r)/100
    print("simple interest is: ",si)

simple_interest(10000,3,12.25)
simple_interest(2000,7,10.25)


# local, global, non_local,built_in identifier
'''identifier: An identifier is the name used to identify (refer to) 
a variable, function, class, object, or any other entity in a program.'''

# local identifier: not ACCESIBLE OUTSIDE OF A BLOCK OF CODE USUALLY a FUNCTION

x = 20
def display(name):

    age = 29 #localvariable
    # x = 20
    print(f"{name}: has age {age}.")
    print(locals())    # Use to check local variable 
    # variable = locals() 
    # print(len(variable))
    # print(variable['x']) 
    # print(len(locals()))
    print(age)

display("Saqib") 

# global identifier: an identifier not define inside funcions 

country = "pakistan"
def display():
    name = "saqib"
    print(name)
    print(country)

display()

# if local vs global identifier are same
num = 10
def display():
    num = 20
    print("inside:",num)
display()

print("outside:", num)
print(globals())


# UnboundLocalError:

num = 10
def display():
    num = num + 5
    print("inside:",num)
display()

print("outside:", num)

# UnboundLocalError by 'global' keyword and change value of global variables

num = 10
def display():
    global num
    num = num + 5
    print("inside:",num)
display()
print("outside:", num)

# Need of return statement: return value in place of caller function then store in a variable 
def simple_interest(p,n,r):
    si = (p*n*r)//100
    print("simple interest is :", si)
    return si

p = 10000
n = 9
r = 9.25
si = simple_interest(p,n,r)
print(si)
total = p + si
print(total)

# you can return any type of object

def display():
    return 'Saqib Jawad'
    # return [10,10,20]
    # return 10.2

var = display()
print(var)

# how you can return multiple values bcz after return keyword no statement executes, return tuple
def calci(a,b):
    add = a+b
    sub = a-b
    return add,sub
    # return add, 10.3
    # return sub

'''tuple unpacking'''

n1,n2 = (calci(10,5))
print("addition is: ",n1)
print("substration is: ",n2)


def calci(a,b):
    if a < 0:
        return
    add = a + b
    return add
    
print(calci(-10,5))



# function is an object

def display():
    print("function body")

print('10 is an object of',type(10))
print('display is an object of',type(display))
print(display) #memory location return in hexadecimel, oython allocate memory to objects

# creating aliases for function: Giving another name to the same object in memory

def display():
    print("function body")

var = display
var()




# Function sirf wahi cheez return karega jo return ke andar likhi ho
# sub calculate hua, but return nahi hua → lost
# 10.3 likha hai return mein → n2 = 10.3
# Multiple values return karna = tuple return
# nothing print after return 


# Nested Function
def outer():
    print("Hello World")
    def inner():
        print("Thankyou!")
        def inner1():
            print("Welcome")
            def inner2():
                print("I am a J.Developer")
            inner2()
        inner1()
    inner()
    
outer()


# Advantage and use of nested function
# 1-we can access inner function only inside outer function that provide Encapsulation
# 2-Nested function are commonly used in closures and decorators

'''parameters vs arguments
# parameters: varibales define in function() for holding actual values 
# arguments:value provided at function call'''
# Types of arguments

'''1-positional'''

def display(name, age):
    print(f"name is: {name} and age is {age}.")

'''while passing arguments order and numbers should be maintained'''
display('Saqib', 29)

# display(29,'Saqib')  
# display('saqib') # error 1 arguments is missing
# display("saqib", 29, 30) #error more than 2 arguments 

'''2-keyword
# used when we actually dont know the sequence of parameters mention in function statement of another modules
# we dont need to maintained order of arguments
# but we cannot pass more arguments than paramets assigned in function'''

def user(name,email):
    print(f"Name is {name}, Email is {email}")

user(name= 'Saqib', email = 'saqibjawad52@gmail.com')
user(email = 'saqibjawad52@gmail.com', name= 'Saqib')
# user(email = 'saqibjawad52@gmail.com', name= 'Saqib', password = '0001')  #TypeError: user() got an unexpected keyword argument 'password'
 
'''mixing keyword and positional arguments'''
def user(name,email):
    print(f"Name is {name}, Email is {email}.")

user('Saqib', email = 'saqibjawad52@gmail.com')
# user(email = 'saqibjawad52@gmail.com', 'Saqib') #SyntaxError: positional argument follows keyword argument
'''Positional arguments must come BEFORE keyword arguments'''


'''3-default 
A default argument is a function parameter that has a predefined value.
If the caller does not provide a value, Python automatically uses the default one.'''


def greet(name = 'Guest'):
    print(f"Hello {name}!")

greet('Saqib') #arguments given
greet() # no arguments guest is used




def power(base, exp=2):
    return base ** exp

print(power(5))     # 25 → default square
print(power(5, 3))  # 125 → cube

def total_cost(items, currency = 'USD'):
    total = sum(items.values())
    print(f"Total cost is: {total} {currency}")
    
cart = {'oranges': 5, 'Mangoes': 6, 'Bananna':7}
total_cost(cart) # BY DEFAULT CURRENCY IS USD
total_cost(cart, "PKR") # CALLING ARGUMRNT WILL PREFER OVER DEFAULT ONE

# how to check default parameters of any function
print(total_cost.__defaults__)


'''Rule 1: Default arguments must come AFTER non-default ones'''
# def user(age=18, name): #wrong
def user (name, age =29):
    print(f"name is {name}, age is {age}")

user('saqib')

'''Rule 2: Default values are evaluated ONLY ONCE in mutable datatypes
Never use mutable objects as default arguments. Use None and create them inside the function.'''


def add_item(item, lst = []):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item.__defaults__)
print(add_item(2))
print(add_item.__defaults__)
print(add_item(3))
print(add_item.__defaults__)
# Because the same list is reused every time.

def test(x=[]):
    print(id(x))
    x.append(1)

test()
test()
test()

# Real-world Example
def register(name, role="user", active=True):
    print(name, role, active)

register("Saqib")
register("Ali", role="admin")
register("Sara", active=False)

'''4-vaiable length positional arguments
1-you can pass multiple positional arguments as much as you want
2-values passed as arguments during function calling pass as single tuple'''

 
def addition(*nums): 
    print(nums) #will return a tuple
    # pass

print(addition(10,20,30))
print(addition(10,20,10))
print(addition(40,50,60,"hello"))


def addition (*nums):
    sum1 = 0
    for n in nums:
        sum1 = sum1 + n
    return sum1

addition(10,20,30)
addition(10,20,10)
addition(40,50,60)


'''variable length keyword arguments'''

def display (**nums):
    print(nums) # will return a dictionary

display(n1 = 10, n2 = 20, n3 = 30)
display(n1 = 10, n2 = 20)
display(n1 = 10, n2 = 40, n3 = 50, n4 = 100)

# how calculate addition in **kwarg
def addition (**nums):
    return sum(nums.values()) # will return sum of all values of keyword arguments 

addition(n1 = 10, n2 = 20, n3 = 30)
addition(n1 = 10, n2 = 20)
addition(n1 = 10, n2 = 40, n3 = 50, n4 = 100)

'''mixing variable length **kwrgs and *prgs
*args MUST come before **kwargs
Note:  Use *args for variable positional inputs, **kwargs for named inputs, and return a single meaningful result.'''


def display(*num, **nums, ): # *prgs come first
    print(num) 
    print(nums)

display(30,40,50, n1 = 10, n2 = 20, n3 = 30)


def addition(*args, **kwargs):
    total = sum(args) + sum(kwargs.values())
    return total

print(addition(30, 40, 50, n1=10, n2=20, n3=30))


def addition(*arg, **Kwarg): # *prgs come first
    sum1 = 0
    for n in arg:
        sum1 = sum1 + n
    sum_arg = sum1
    sum_kwarg = sum(Kwarg.values())
    return sum_arg, sum_kwarg

print(addition(30,40,50, n1 = 10, n2 = 20, n3 = 30))

# Realworld
def calculate_bill(*prices, tax=0, **extras):
    total = sum(prices) + sum(extras.values())
    total_cost= total + total * tax
    return total
    

'''Note: default arguments never come first while keyword arguments will never come first'''

'''# order: positional arguments --> *pargs --> keyword arguments -->**kwargs --> default arguments'''








def f(x):
    return lambda y: x + y

g = f(10)
print(g(5))
