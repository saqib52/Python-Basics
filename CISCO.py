# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])

# print(my_list)


# def function_1(a):
#     return None


# def function_2(a):
#     return function_1(a) * function_1(a)


# print(function_2(2))



# print(1 // 2)


# def func(a, b):
#     return b ** a


# print(func(b=2, 2))


# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y
# print(x)

# my_list =  [x * x for x in range(5)]


# def fun(lst):
#     del lst[lst[2]]
#     return lst


# print(fun(my_list))

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2


# print(fun(fun(2)))

# nums = [1, 2, 3]
# vals = nums
# del vals[:]
# print(len(nums))
# print(len(vals))


x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)

y = input()
x = input()
print(x + y)

print("a", "b", "c", sep="sep")

my_tuple[1] = my_tuple[1] + my_tuple[0]

x = float(input())
y = float(input())
print(y ** (1 / x))

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)

# how many elements does the lst containi?
lst = [i for i in range(-1, -2)]
print(lst)

# Recursive fun
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))


# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

# tup[-2:-1] → slicing → always returns a tuple, even if length 1.
# tup[-1] → indexing → returns the element itself, not a tuple.

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

# dct[x][1] → access second element of tuple stored in dictionary.
# end="" → prevents a newline, so outputs are concatenated.
# Python dictionaries maintain insertion order (3.7+), so '1' comes first, '2' second.

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
# if user enter 0:
try:
    value = input("Enter a value: ")
    print(int(value)/len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

# expected behaviorof thi snippet?

try:
    print(5/0)
    break
except:
    print("Sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print("Too bad...")

# Problem:
# In Python, a bare except: must come last.
# You cannot have a more specific except after a bare except, because the bare except catches all exceptions first.
# Python will raise a SyntaxError for this code.

foo = (1, 2, 3)
foo.index(0)

# 0 is not in the tuple.
# Python raises a ValueError:


# A:
except (TypeError, ValueError, ZeroDivisionError):
    # Some code.

# B:
except TypeError, ValueError, ZeroDivisionError:
    # Some code.

# correct way of hanling multiple exceptions in single except clause?
# # C:
# except: (TypeError, ValueError, ZeroDivisionError)
#     # Some code.

# # D:
# except: TypeError, ValueError, ZeroDivisionError
#     # Some code.

# # E:
# except (TypeError, ValueError, ZeroDivisionError)
#     # Some code.

# # F:
# except TypeError, ValueError, ZeroDivisionError
#     # Some code.

