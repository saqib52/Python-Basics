fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])


'''The enumerate() function in Python is used when you want to loop over a sequence 
and also keep track of the index (position) at the same time.'''

fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):
    print(index, value) # actually do [(0, "apple"), (1, "banana"), (2, "cherry")]

# by default enumerate start from 0 index
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)



"""For_Loop

Teach me the Python for loop from absolute beginner level to advanced level.
Assume I am a beginner who wants to build strong logic and write programs independently.

Follow these strict rules:
1. Explain everything step by step.
2. Use simple English + easy logic explanations.
3. Use real-life analogies where possible.
4. Show dry runs for every important example.
5. Explain WHY each line of code is written.
6. Gradually increase difficulty (very basic → intermediate → advanced).
7. Include common mistakes and how to fix them.
8. Include practice questions after each section.
9. Do NOT skip any concept.
10. Keep examples short but meaningful.
Section 1: Introduction to for loop

What is a for loop?

Real-life analogies

Basic for loop with range()

Common mistakes

Section 2: Looping through numbers

range(start, stop)

range(start, stop, step)

Positive and negative steps

Dry runs and common mistakes

Section 3: Looping through sequences

Looping through lists

Looping through strings

Looping through tuples

Looping through dictionaries (keys, values, items)

Section 4: Using for loop with conditions

if inside a loop

Filtering items during iteration

Sum, max, min, count with loops

Real-life examples

Section 5: Nested for loops

Concept of nested loops

Dry run with tables, patterns, matrices

Common mistakes and tips

Section 6: Loop control statements

break → stop loop early

continue → skip current iteration

else with for loop

Examples and dry runs

Section 7: Advanced for loop techniques

Using enumerate() → get index + value

Using zip() → loop over multiple lists

List comprehensions → short and powerful loops

Dictionary comprehensions

Section 8: Real-life applications & projects

Pattern printing (triangles, pyramids, etc.)

Simple number games

Summing digits, factorial, and other problems

Mini project: attendance tracker, transaction statements

Section 9: Common mistakes and debugging tips

Indentation errors

Wrong range() usage

Overwriting loop variables

Off-by-one errors

Section 10: Practice questions & challenges

From beginner to advanced

Mix of numbers, sequences, nested loops, conditions

Mini projects to reinforce learning

If you want, I can start Section 1 immediately and teach it step by step with examples, dry runs, mistakes, and practice questions.

Do you want me to start Section 1 now?
"""

# Basic Syntax
# for variable in sequence:
#     # code to repeat

for i in range(5):
  print(i)

# for → tells Python we are starting a loop
# for loop = repetition
# Loop variable changes automatically
# Indentation is mandatory
# Colon : is required

# What is range()?

# range() generates a sequence of numbers that a for loop can use one by one.

# Think of range() as a number machine.
# It creates numbers and gives them to the loop step by step.

# range(start, stop) start by default=0 , stop value is excluisve
# range(n) → starts from 0, ends at (n-1)

for i in range(1, 6):
  print(i)

for i in range(5):
  print("Hello Saqib")

# range(start, stop, step)
# step → how much to jump each time
for i in range(2,11,2):
  print(i)

# Positive vs Negative Step
# by default step is +1

# for i in range(0,6,1) is same for i in range (0,6)

# Neagtive step
# When step is negative:

# Start must be greater than stop
# () never includes stop
# ✔ Step decides direction
# ✔ Negative step → start > stop
# ✔ Loop ends automatically

# Print numbers from 10 to 15
# Print numbers from 1 to 10

for i in range(10,16):
  print(i)

for j in range(1,11):
  print(j)

# printing python five times
for i in range(5):
#  for i in range(1,6):
  print(i,"Python")

# priting even number from 2-20

for i in range(2,21,2):
  print("Even",i)

for i in range(1,10,2):
  print("Odd",i)

# priting number in reverse from 10-1
for i in range(10,0,-1):
  print(i)

# printing number in reverse from 20 t0 2 with step of 2
for i in range(20,1,-2):
  print(i)



for i in range(5, 0, -1):
    print(i)

# printing number from 0 t0 4
for i in range(5):
  print(i)

# Section 3: Looping Through Sequences
# Think of a sequence as a box of items
# A for loop takes one item at a time from that box.

# Looping through a List
fruits=["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

# Loop through a string
Greet = "Hello"
for ch in Greet:
  print(ch)

# looping through dictionaries
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}

# for key in student:
#   print(key)

# By default, a dictionary loop gives keys only.

for value in student.values():
  print(value)

for key, value in student.items():
  print(key, value)

# Loop through a list of 5 colors and print each
colors=["Red", "Green", "Blue", "Orange", "Yellow"]
for color in colors:
  print(color)
# Loop through your name and print each letter
name= "saqib"
for ch in name:
  print(ch)

for x in "Saqib":
  print(x)

# Section 4: Using for Loop with Conditions
# checking condition after each iteration and then move
# printing even numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
# printing greater number than 5
for i in range(1, 11):
    if i > 5:
        print(i)

# Counting with a loop
# Count even numbers
count=0

for i in range(2,11):
  if i % 2 == 0:
    count=count+1

print(count)

# Summing values with a loop
total=0
for i in range(1,6):
  total= total + i
print(total)