
'''A one-line anonymous (nameless) function that can take any number of arguments but has only one expression.'''

'''Basic Syntax is:
# lambda arguments: expression'''

double = lambda x: x*2
print(double(5))

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


check_number = lambda x: "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
print(check_number(9))



