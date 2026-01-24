# # Questions
# # Q1. What will be the output of the following code?

# # Python
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# # Q2. Which of the following is not a valid Python keyword?

# # A. pass
# # B. eval
# # C. assert
# # D. lambda

# # Q3. What will the following loop output?

# for i in range(1, 5):
#     if i % 2 == 0:
#         continue
#     print(i, end=", ")

# # Q4. Which Python code correctly checks if a number is prime?

# # A. ```python def is_prime(n): for i in range(2, n): if n % i == 0: return False return True
# # B.
# # def is_prime(n):
# #     return all(n % i != 0 for i in range(2, n))
# # C. (Logic: returns n in [2, 3, 5, 7])
# # D. Both A and B

# # Q5. What does this return? "".join(sorted("banana"))

# # Q6. What is the output?


# a = [1, 2, 3]
# print(a * 2)

# # Q7. What is the output of the following?


# def func(x=[]):
#     x.append(1)
#     return x

# print(func())
# print(func())

# # Q8. What will be printed?

# def f(x):
#     return lambda y: x + y

# g = f(10)
# print(g(5))

# # Q9. Which is true about Python classes?
# # A. Python doesn't support private attributes.
# # B. __init__ is optional.
# # C. Python does not support inheritance.
# # D. @classmethod and @staticmethod are identical.

# # Q10. What is printed?

# class A:
#     def __init__(self):
#         self.var = 10
#     def display(self):
#         print(self.var)

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.var = 20

# b = B()
# b.display()

# # Q11. Which function is a generator?

# # A. def f(): yield 1
# # B. def f(): return [1]
# # C. def f(): return 1
# # D. def f(): pass

# # Q12. What is the result of the following?

# def add(x, y): return x + y
# print((lambda f: f(2, 3))(add))

# # A. 5
# # B. add
# # C. <function>
# # D. Error

# # # Q13. What is the time complexity of set.add() in average case?

# # A. O(1)
# # B. O(n)
# # C. O(logn)
# # D. O(nlogn)

# # Q14. Which data structure maintains insertion order?
# # A. dict (Python 3.7+)
# # B. set
# # C. frozenset
# # # D. Counter

# # Q15. Which file mode lets you write without truncating and create if not exists?

# # A. 'w'
# # B. 'r+'
# # C. 'a'
# # D. 'x'

# # Q16. What is the output?

# import os
# print(os.path.basename("/home/user/file.txt"))
# # A. file.txt
# # B. user
# # C. /home/user
# # D. txt

# # Q17. What will be the output?
# # def f(a, b=5, c=10):
# #     print(a, b, c)

# # f(3, c=20)
# # A. 3 5 20
# # B. 3 20 5
# # C. 3 10 20
# # D. Error

# # Q18. What is printed here?

# def foo(x, y=[]):
#     y.append(x)
#     return y

# print(foo(1))
# print(foo(2))
# # A. [1], [2]
# # B. [1], [1, 2]
# # C. [1, 2], [1, 2]
# # D. Error

# # Q19. What will the following code print?
# nums = [1, 2, 3, 4]
# squared = [x*x for x in nums if x % 2 == 0]
# print(squared)
# # A. [1, 4, 9, 16]
# # B. [4, 16]
# # C. [2, 4]
# # D. [1, 9]

# # Q20. What is the output of this nested loop?

# for i in range(2):
#     for j in range(2):
#         print(i + j, end=" ")
# # A. 0 1 1 2
# # B. 0 1 2 3
# # C. 0 1 0 1
# # D. 1 2 3 4

# # Q21. Which operation modifies the list in-place?

# # A. sorted(lst)
# # B. lst.sort()
# # C. lst = lst.sort()
# # D. lst[::-1]

# # Q22. Which of these statements is true about tuples?
# # A. Tuples are mutable
# # B. Tuples use more memory than lists
# # C. Tuples can contain lists
# # D. You cannot access tuple elements by index

# # Q23. What will be printed here?

# t = (1, 2, [3, 4])
# t[2].append(5)
# print(t)

# # A. (1, 2, [3, 4])
# # B. (1, 2, [3, 4, 5])
# # C. Error (tuples can't be modified)
# # D. (1, 2, 3, 4, 5)


# # Q24. What will this code print?
# class Parent:
#     def hello(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def hello(self):
#         super().hello()
#         print("Hello from Child")

# c = Child()
# c.hello()
# # A. Hello from Child
# # B. Hello from Parent
# # C. Hello from Parent\nHello from Child
# # D. Error

# # # Q25. Which of these defines a class variable, not an instance variable?
# # A. class A: count = 0
# # B.
# # class A:
# #     def __init__(self):
# #         self.count = 0
# # C. class A: def init(self): count = 0
# # D. All are class variables  


# # ### **Q26. What will this output?**

# # class A:
# #     def __init__(self):
# #         self.val = 1
# #     def update(self):
# #         self.val += 1

# # a1 = A()
# # a2 = A()
# # a1.update()
# # print(a1.val, a2.val)
# # A. 2 1

# # B. 1 2

# # C. 2 2

# # D. 1 1

# # Q27. Which will catch both IndexError and ZeroDivisionError?
# # A. try: ... except IndexError or ZeroDivisionError: ...
# # B.
# # try:
# #     ...
# # except (IndexError, ZeroDivisionError):
# #     ...
# # C.try: ... except IndexError and ZeroDivisionError: ...

# # D.None



# # ### Q28. What will happen here?**```python
# # try:
# #     x = 1 / 0
# # except:
# #     print("Error")
# # else:
# #     print("No Error")
# # finally:
# #     print("Done")
# # A. Error
# # B. Error\nDone
# # C. No Error\nDone
# # D. Done

# # Q29. What will this code output?

# # def outer():
# #     x = 5
# #     def inner():
# #         print(x)
# #     return inner

# # f = outer()
# # f()
# # A. 5
# # B. None
# # C. Error
# # D. inner

# # # Q30. What will be printed here?


# # x = 10
# # def func():
# #     x = 20
# #     return (lambda y: x + y)(5)

# # print(func())
# # A. 15
# # B. 25
# # C. 30
# # D. 10

# # Q31. Which of these is a valid use of lambda?
# # A. add = lambda x, y: x + y
# # B. lambda x, y: return x + y
# # C. lambda x, y: x + y;
# # D. def lambda x: x

# # Q32. What will be printed?

# # a = [1, 2, 3]
# # b = [4, 5, 6]
# # for x, y in zip(a, b):
# #     print(x + y, end=" ")
# # A. 5 7 9
# # B. 1 2 3 4 5 6
# # C. 4 5 6
# # D. Error

# Q33. What does enumerate do in this code?

# Python
# for i, val in enumerate(['a', 'b', 'c'], start=1):
#     print(i, val)
# A. Prints index and value starting from 0

# B. Prints index and value starting from 1

# C. Prints only values

# D. Throws error

# Q34. What will be the output?

# Python
# a = [[1, 2]] * 3
# a[0][0] = 99
# print(a)
# A. [[99, 2], [99, 2], [99, 2]]

# B. [[99, 2], [1, 2], [1, 2]]

# C. [[1, 2], [1, 2], [1, 2]]

# D. Error

# Q35. Which method performs a shallow copy of a list?

# A. list.copy()

# B. copy.deepcopy()

# C. a[:]

# D. Both A and C

# Q36. What is the output?

# Python
# result = [i*j for i in range(1, 3) for j in range(2, 4)]
# print(result)
# A. [2, 3, 4, 6]

# B. [2, 3, 4, 6, 8]

# C. [2, 3, 4, 6]

# D. [2, 3, 4]

# Q37. Which of the following creates a flattened list from nested lists?

# a = [[1, 2], [3, 4], [5]]

# A. [x for sub in a for x in sub]

# B. [x for x in a]

# C. sum(a)

# D. list(a)

# Q38. What does this print?

# Python
# def f(*args):
#     print(args)

# f(1, 2, 3)
# A. [1, 2, 3]

# B. {1, 2, 3}

# C. (1, 2, 3)

# D. Error

# Q39. What will this print?

# Python
# def f(a, b, c):
#     print(a, b, c)

# args = [1, 2, 3]
# f(*args)
# A. (1, 2, 3)

# B. 1 2 3

# C. [1, 2, 3]

# D. Error

# Q40. What will be the output?

# Python
# def f(**kwargs):
#     print(kwargs)

# f(a=1, b=2)
# A. {'a': 1, 'b': 2}

# B. ['a', 'b']

# C. Error

# D. a=1, b=2

# Q41. What will be printed?

# Python
# x = 3
# x = x + 2 * x
# print(x)
# A. 9

# B. 15

# C. 12

# D. None

# Q42. What will this output?

# Python
# x = 10
# y = x
# x += 1
# print(x, y)
# A. 10 10

# B. 11 11

# C. 11 10

# D. 10 11

# Q43. What will be printed here?

# Python
# x = 5
# y = 2
# z = x ** y // y
# print(z)
# A. 12

# B. 10

# C. 25

# D. 6