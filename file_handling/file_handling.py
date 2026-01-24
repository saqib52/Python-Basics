


'''File reading in Python is an OBJECT
When you do:

file = open("data.txt", "r")

Python creates a file object.
That object comes with fixed methods.
These methods are the core reading APIs.'''

"Synatx to open file"
file = open("filename", "mode")
# read mode
# File must exist.
file = open("data.txt", "r")
print(file.read())
file.close()

# Old data will be deleted.
file = open("data.txt", "w")
print(file.write("index0"))
file.close

# ✔ Old data is safe.
file = open("data.txt", "a")
print(file.write("\nindex2"))
file.close()

file1 = open("new.txt", "x")
print(file1.write("New file created"))
file.close()
# Error if file already exists.

# read() – Read entire file
file = open("data.txt", "r")
print(file.read())
file.close()

# read(n mean indices) – Read limited characters
file = open("data.txt", "r")
print(file.read(5))
file.close()

# Every read method moves a file pointer forward
file = open("data.txt", "r")
print(file.read(5))
print(file.read(5))
file.close()


# readline() – Read one line
file = open("data.txt", "r")
print(file.readline())
file.close()

#usind readline() multiple times –Reads next lines sequentially

file = open("data.txt", "r")
print(file.readline())
print(file.readline())
file.close()

# readlines() – Read all lines into a list
file = open("data.txt", "r")
print(file.readlines())
file.close()

# best practice is for loop
file = open("data.txt", "r")
for line in file:
    print(line)
file.close

# this automatically closes the file — no need to call close().
with open("data.txt", "r") as file:
    print(file.read())

# tell() – Current position of cursor output index
file = open("data.txt", "r")
print(file.tell())
file.read(5)
print(file.tell())
file.read(6)
print(file.tell())
file.read(6)
print(file.tell())
file.close()

# seek() – Move pointer

with open("data.txt", "r") as file:
    file.seek(3)
    print(file.read())

# These are the core reading APIs.
# Core reading APIs are the fundamental built-in file methods that directly read data from disk.

# Disk file
#    ↓
# open()
#    ↓
# File Object
#    ↓
# CORE APIs (read, readline, readlines)
#    ↓
# Higher-level tools (loops, CSV, JSON, Pandas)

# WRITING FILE DATA usually overwrite file data
file = open("new.txt", "w")
file.write("Welcome")
file.close()

file = open("new.txt","w")
file.writelines(["index0\n","index1\n","index2\n","index3\n","index5\n"])
file.close()

file = open("data.txt", "r")
file.seek(3)
print(file.read())
file.close()


with open("marks.txt", "w") as file:
    file.write("Danish: 85\nAli: 90\nSara: 88")

with open("marks.txt", "r") as file:
    print(file.read())

# Common Mistakes
'''❌ Forgetting close() 
❌ Using w instead of a 
❌ Reading non-existing file 
❌ Not adding \n for new line'''