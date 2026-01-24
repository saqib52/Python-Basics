'''You have a list You want only some values based on a condition Function must return True or False'''

# without map
num = [1,2,3,4,5,6]
result = [ ]
for n in num:
    if n % 2 == 0:
        result.append(n)
print(result)

nums = [1,2,3,4,5,6]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))

'''real world example'''

# filtering pass students

marks = [45, 80, 30, 90, 60 ]
passed = filter(lambda m: m >= 50, marks)
print(list(passed))

# filtering even and odd

num2 = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, num2)
print(list(evens))

