class User:
    def __init__(self, username, email, password):
        self.username = username 
        self._email = email
        self.password = password

    def set_password(self, new_password):

        if len(new_password) < 8:
            print("Password must be at least 8 characters long")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "@#$%^&"

    for ch in new_password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        self.password = new_password
        print("Password updated successfully")
    else:
        print("Password must contain uppercase, lowercase, number, and special character (@#$%^&)")


'''Allow any special characters'''

def set_password(self, new_password):

    if len(new_password) < 8:
        print("Password must be at least 8 characters long")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in new_password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():  #this will work for special charaters
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        self.password = new_password
        print("Password updated successfully")
    else:
        print(
            "Password must contain uppercase, lowercase, number, and at least one special character"
        )



'''Regex-based password validation uses pattern matching to enforce 
multiple security rules efficiently in a single expression.'''

'''Regex validation'''

import re

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email        # protected attribute
        self._password = password # protected attribute

    def set_password(self, new_password):
        # Regex pattern for strong password
        # ^                 → start of string
        # (?=.*[A-Z])       → at least one uppercase letter
        # (?=.*[a-z])       → at least one lowercase letter
        # (?=.*\d)          → at least one digit
        # (?=.*[^A-Za-z0-9])→ at least one special character
        # .{8,}             → minimum 8 characters
        # $                 → end of string
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'

        # Check if new password matches the pattern
        if re.match(pattern, new_password):
            self._password = new_password
            print("Password updated successfully")
        else:
            # Show error message if password is weak
            print(
                "Password must be at least 8 characters long and include "
                "uppercase, lowercase, digit, and special character"
            )


