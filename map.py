"""use case: when we have a list and we have to apply
same operation to each item in list"""

# withou map: more lines, more code
num = [1,2,3,4,5]
double = [ ]
for i in num:
    double.append(i*2)
print(double)

# map() exists to do this in one step
'''Think of map() like a machine:
It takes a function, a list It: Takes one item from list sends it into the function
Stores result and repeats'''

# Note: map does not return a list

nums = [1,2,3,4,5]
result = map(lambda x: x*2, nums)
# print(result)
'''Because map() only knows how to generate values, it does not store them.
Think of it like a factory machine: It knows how to make products
But it doesn’t show products until you ask for them'''

# print(list(result))

# we can loop throut it
for value in result:
    print(value) 

# Its not compulsory to use map with lambda we can use simple fun as well
def double(x):
    return x*2

num1 = [1,2,3,4]
cal = map(double, num1)
print("cal = ",list(cal))


# Real world example

salaries = [1000, 2000, 3000]
new_salaries = map(lambda s: s + 500, salaries)
print(list(new_salaries))