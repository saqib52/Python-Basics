

# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

# How If Statements Work
# The if statement evaluates a condition (an expression that results in True or False).
# If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
# Note: You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block.


# Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.

# Using Variables in Conditions
# Boolean variables can be used directly in if statements without comparison operators.

# Python can evaluate many types of values as True or False in an if statement.
# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.
# This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).

# The Elif Keyword
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

# Multiple Elif Statements
# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

# When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
# Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

# When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.

# Important: Only the first true condition will be executed.
# Even if multiple conditions are true, Python stops after executing the first matching block.

# When to Use Elif
# Use elif when you have multiple mutually exclusive conditions to check.
# This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

# The Else Keyword
# The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

# How Else Works
# The else statement provides a default action when none of the previous conditions are true.
# Think of it as a "catch-all" for any scenario not covered by your if and elif statements.
# Note: The else statement must come last. You cannot have an elif after an else.

# Else as Fallback
# The else statement acts as a fallback that executes when none of the preceding conditions are true.
# This makes it useful for error handling, validation, and providing default values.

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
# Note: You still need the colon : after the condition.

# Note: You still need the colon : after the condition.

# Nested If Statements
# You can have if statements inside if statements. This is called nested if statements.

# How Nested If Works
# Each level of nesting creates a deeper level of decision-making.
# The code evaluates from the outermost condition inward.


# How Nested If Works
# Each level of nesting creates a deeper level of decision-making.
# The code evaluates from the outermost condition inward.

# Both approaches produce the same result.
# Use nested if statements when the inner logic is complex or depends on the outer condition.
# Use and when both conditions are simple and equally important.

# Example
# Login validation with nested checks:
username = True
password = True
is_active = False

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

# Grade calculation with nested logic:

score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

# The pass Statement
# if statements cannot be empty,
# but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

a = 33
b = 200
if b > a:
  pass

# Why Use pass?
# The pass statement is useful in several situations:

# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later

# pass in Development
# During development, you might want to sketch out your program structure before implementing the details.
# The pass statement allows you to do this without syntax errors.


# pass vs Comments
# A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing).
# You need pass where Python expects a statement, not just a comment.

age = 150

if age >= 0 and age <= 120:
    print("Valid age")
else:
    print("Error: Age value is not valid")

# Short Hand If:
# If you have only one statement to execute, you can put it on the same line as the if statement.
a = 5
b = 2
if a > b: print("a is greater than b")

# One-line if/else that prints a value:

a1 = 2
b2 = 330
print("A") if a1 > b2 else print("B")

# This is called a conditional expression (sometimes known as a "ternary operator").

# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

number = -5
result = "Positive" if number > 0 else "Negative or Zero"
print(result)

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

"""Shorthand if statements and ternary operators should be used when:
The condition and actions are simple:
It improves code readability
You want to make a quick assignment based on a condition
Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions.
For readability, use regular if-else statements when dealing with multiple lines of code or complex logic."""

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

age1 = 25
is_student = False
has_discount_code = True
# (precedence) not,and,or

if (age1 < 18 or age1 > 65) and not is_student or has_discount_code:
  print("Discount applies!")
else:
  print("No Discount")

age1 = 25
if age1 < 18 or age1 > 65:
  print("YES")
else:
  print("NO")

score = 85
attendance = 90
submitted = False

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
# Example
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")