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