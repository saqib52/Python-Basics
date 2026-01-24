'''Hashing: a bcrypt password hash: b'$2b$12$luWpa3.mEBEYBJn7lAfEduvoZDLLSew/5bAWXtPDHqZi49tF8SgKC'
$2b$12$<salt><hash> Algorithm = 2b bcrypt, Cost = 12, Salt = embedded, Hash = result    

cost makes hacking slow.

Salt = random extra text added to a password before hashing 22 characters long.
Make every password hash unique, even if passwords are the same.
Salt prevents same-password same-hash, bcz same password has different salt so hasged different. 
hash = password + salt + cost
'''

"""Without Regex"""

import bcrypt

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self._password = None      # store HASH, not plain password
        self.set_password(password)

    def set_password(self, new_password):

        # 1️⃣ Length check
        if len(new_password) < 8:
            print("Password must be at least 8 characters long")
            return

        # 2️⃣ Flags
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        special_chars = "@#$%^&"

        # 3️⃣ Character checking
        for ch in new_password:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True
            elif ch in special_chars:
                has_special = True

        # 4️⃣ Final validation
        if has_upper and has_lower and has_digit and has_special:
            # 🔐 HASHING HERE
            password_bytes = new_password.encode("utf-8")
            self._password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            print("Password updated and hashed successfully")
        else:
            print(
                "Password must contain uppercase, lowercase, number, "
                "and special character (@#$%^&)"
            )

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self._password)


user1= User("saqibjawad", "saqibjawad@gmail.com", "123@Abcde" )
print("Hash of first password = ", user1._password)
print("checking password = ", user1.check_password("123@Abcde"))
user1.set_password("456@Abcde")
print("Hash of changed password = ",user1._password)
print("checking changed password = ",user1.check_password("456@Abcde"))




'''Regex and hashing password'''


import re
import bcrypt


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email          # protected attribute
        self._password = None        # will store HASH, not plain password
        self.set_password(password) # validate + hash during creation

    def set_password(self, new_password):
        # Regex pattern for strong password
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'

        # Step 1: validate password strength
        if not re.match(pattern, new_password):
            print(
                "Password must be at least 8 characters long and include "
                "uppercase, lowercase, digit, and special character"
            )
            return

        # Step 2: hash the password
        password_bytes = new_password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        # Step 3: store hashed password
        self._password = hashed_password
        print("Password updated and hashed successfully")

    def check_password(self, password):
        # Convert entered password to bytes
        password_bytes = password.encode("utf-8")

        # Compare entered password with stored hash
        return bcrypt.checkpw(password_bytes, self._password)

user1= User("saqibjawad", "saqibjawad@gmail.com", "123@Abcde" )


# Next logical steps (recommended)
# @property for password setter
# Replace prints with exceptions
# Add email validation
# Build signup/login flow
# Learn JWT authentication
# FastAPI auth
# Rate limiting & brute-force protection
# Session vs token auth
# OAuth basics
# .py vs .env
# Secrets management
# Django / FastAPI settings
# Dependency injection (advanced)
# Clean Architecture basics
# Build a full FastAPI project step-by-step
# Explain dependency injection
# Show real login/signup flow
# Connect this to AI model APIs
# If you want, we can refactor this into @property-based design next.


# 1️⃣ Environment & config (DONE)
# 2️⃣ Project structure (routers, services) ← NEXT
# 3️⃣ Request & response flow
# 4️⃣ User model (without DB)
# 5️⃣ Password hashing
# 6️⃣ Authentication basics
# 7️⃣ Database connection
# 8️⃣ JWT tokens
# 9️⃣ Role-based access