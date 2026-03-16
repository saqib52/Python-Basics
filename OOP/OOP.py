'''What is OOP: a way of structuring our code around objects/ OOP is not a language It is a way of designing programs.
Each object manages its own data and behavior: Code becomes: modular, readable, easier to debug and extend.

classes vs object: 
First we design(Classess) something and then we create real things(Objects) from that design, class define attributes and methods of object
we can create multiple objects from a class just like: Blueprint → many houses, Same design, multiple houses

Object are real world entities that have attributes(data/info about objects) and methods(behavior/what object can do)
OOP structures code by grouping related data and functions together, instead of spreading them across the program.'''
"""In programming:We create things(Objects) and write code about those things"""


"""__init__is a special function that runs automatically when an object is created.
when we create s1 = Student("Ali", 3.5), Python automatically runs this :__init__("Ali", 3.5) 
"""

"""why self: one class has many objects and each objects has its own data Without self, Python would not know:
“Is this Ali’s GPA or Sara’s GPA?”"""



name = "Saqib"
print(name)
age= 29
print((name.upper()))
print(type(age))


class Student:                              #It defines what every student object will have and can do
    def __init__(self, name, gpa):          #constructor method: It runs automatically when an object is created self mean current object.
        self.name = name                    #Creates a variable name inside the object
        self.gpa = gpa                      #Creates another variable gpa inside the object
    def study(self):                        #Represents an action an object of class student can do
        print("Students are studying")

s1= Student("saqib", 3.8)                   #Creating first student object
print(s1.name)                              #Accessing and printing name of first student
print(s1.gpa)                               #Accessing and printing gpa of first student
s2= Student("Aqib", 3.9)                    #Creating Second student object
print(s2.name)                              #Accessing and printing name of Second student
print(s2.gpa)                               #Accessing and printing gpa of second student
s1.study()                                  #Calling study method using first student object



# Example no.1
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name      #attributes
        self.breed = breed    #attributes
        self.owner = owner   #attributes

    def bark(self):         #Method
        print("Whoof Whoof")
class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

owner1= Owner("Saqib", "fsd", "03069885341")
dog1= Dog("tommy", "german", owner1)
print(dog1.owner.name)
print(dog1.owner.address)
print(dog1.owner.phone_number)
print(dog1.name)
print(dog1.breed)
dog1.bark()

owner2= Owner("Talha", "lhr", "03061234567")
dog2= Dog("jack", "italian", owner2)
print(dog2.owner.name)
print(dog2.name)
print(dog2.breed)
dog2.bark() 

'''Example no:2'''

class Person:
    def __init__(self, name, age):
         self.name = name
         self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old.")

p1= Person("Saqib", 29)
print(p1.name)
p1.greet()

p2= Person("Aqib", 27)
print(p2.name)
p2.greet()
'''Different instances or objects of the same class can hold different data and can perform same behavior with data.
class is a blueprint of creating objects and this case person is the class and 
object or instances is the those specific example created from class p1 and p2 we have attributes callled variables
e.g name, age and methods (functions inside class) and self keyword which refer to specific instance and object of class'''


"""Different way of accessing and modifying data in objects.
1. Traditional way: Make the data private and use getters and setters:"""
        # later we make this email atribute private/protected by prefixing it with underscore
        # protected mean we should'nt read this attribute outside of this class or subclass
        # _protectd vs __private variables can be access inside class but not ouside of class    
        # protected mean with single underscore ethically you are suposed to not use this attribute outside of class 
        # rather you can control it inside class
        # private means impossible to access outside of class
from datetime import datetime
class User:
    def __init__(self, username, email, password):
        self.username = username
        # self.__email = email  # private 
        self._email = email # protected 
        self.password = password
    
    # def clean_email(self):
    #     return self._email.lower().strip()
     

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email 
    
    def set_email(self, new_email): #control way of updating emails. 
        if "@" in new_email:
            self._email = new_email

    
    def get_password(self):
        print(f"Password accessed at {datetime.now()}")
        return self.password

    def set_password(self, new_password):
        if len(new_password) < 8:
            print ("Password must be at least 8 characters long")
            return

      
    
    # def say_hi_to_user(self, user):
    #     print(f"Sending message to {user.username}: Hi {user.username}, its a {self.username}!")

user1 = User("Saqib","saqibjawad.ai@gmail.com",123)
# user2 = User("Aqib","aqibbehzad.ai@gmail.com",456)
# user1.say_hi_to_user(user2)

# print(user1.__email)

# print(user1._email)
# print(user1.get_email())
# print(user1.clean_email())

# user1.set_email("update@gmail.com")
# print(user1.get_email())


# user1._email = "rdp@gmail.com"
# print(user1._email)

user1.set_email("123@wdrr")
print(user1.get_email())

'''modifying data of object'''
# print(user1.email)
# user1.email = "saqibjawad52@gmail.com"
# print(user1.email)


'''Accessing and modifying data
2.properties'''

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    
    @property  #Converts a method into a read-only attribute instead of user.email() use user.email
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email
        return 


user1 = User("Aqib","aqibbehzad.ai@gmail.com",456)
# user1.email = "this is not an email"
print(user1.email)                  #Getter      
user1.email = "123@gmail.com"       #Setter
print(user1.email)                  #Note: No parentheses used here!


'''instance attribute and  static attributes static/class attribute'''
'''static/class attribute: An attribute that belongs to class not to any specific instance of class
Shared by ALL objects.

Instance attribute: belongs to objects every objects has different data in that attribute e.g name, email, password
balance, 
Instance attributes are per-object data; class attributes are shared by all objects.
'''
class User:
    total_user = 0              #static variable
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.total_user +=1
    
    @property
    def display_user(self):
        return f"username: {self.username} Email: {self.email}"
        
    
user1 = User("saqibjawad", "saqibjawad52@gmail.com")
user2 = User("Talharehman", "talaha2567@gmail.com")
user3 = User("Ali", "ALi43@gmail.com")
# Count the number of user created inside the class
print(User.total_user)
print(user1.email)
print(user1.display_user)



class User:
    
    platform = "Web"            

    def __init__(self, username):
        self.username = username

u1 = User("ali")
u2 = User("saad")

print(User.platform)
print(u1.platform)  #not recommended

User.paltform = "Mobile"

# u1.platform = "Mobile" # create instance attribute
print(u1.platform)
print(u2.platform)


class Student:
    school_name = "GGCSF"

s1 = Student()
s2 = Student()

print(s1.school_name)

s1.school_name = "LGS" #create instance variable for s1
print(s1.school_name)

print(s2.school_name)


'''Static vs Instance vs class method:  
static method belongs to class and and all objects of the class while instance method apply to instance/objects individually
to define static method we use decorator @staticmethod'''



class BankAccounts:
    MIN_BALANCE = 100 #In python, ALL CAPS variabels are treated as Constants, as no keywords;
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount): #instance method
        if amount > 0:
            self._balance = self._balance + amount
            print(f"{self.owner}'s new balance: ${self._balance}") 
        else: 
            print("Deposit amount must be positive")
    
    
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <=5
acc1 = BankAccounts("saqib", 2000)
acc1.deposit(1000)
print(BankAccounts.is_valid_interest_rate(3))
print(BankAccounts.is_valid_interest_rate(10)) 

# Private vs protected methods

'''Principles of OOP'''

# Encapsulation
# Abstraction
# Polymorphisms
# Encapuslation

'''Encapsulation:
Data ko protect karna aur us data ko sirf controlled methods ke zariye access ya modify karna.
it answers: “How can I protect my data from being misused?”

Encapsulation protects data by restricting direct access, 
while abstraction hides complex implementation details and exposes only essential functionality.
'''

# balance public hai, Koi protection nahi, Koi rules nahi, Koi validation nahi

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)

# _balance is hidden
# User cannot directly change balance
# Access is controlled via methods
# Rules are enforced

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property #lets you use a method like an attribute
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance = self._balance + amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance = self._balance - amount

account = BankAccount()
print(account._balance)
# account.balance = -1 # bad practice not work here due to encapsulation 
account.deposit = 1.99
print(account.deposit)
account.withdraw =0.99
print(account.withdraw)


'''Abstraction: Reduce complexity by hiding unnecessary details.
User should know WHAT a method does, not HOW it does it
Abstraction is the process of hiding internal implementation details and exposing only essential functionalities
to the user.
Abstraction hides complex implementation details and exposes only essential operations to the user.

It answers:
    “How can I make usage simple?”




The send_email() method serves as the public interface, orchestrating the full process without revealing
how _connect() and _authenticate() work internally. Users interact solely with send_email(), 
which reduces complexity by abstracting away server connection and authentication details. 
Private methods prefixed with _ (like _connect() and _authenticate()) signal they are internal helpers not meant for 
direct external use, enforcing this hiding principle



'''

class EmailService:
    def _connect(self):
        print("conecting to server")
    
    def _authenticate(self):
        print("authenticating...")
    
    def send_email(self):
        self._connect()  #inside a button send_email this fun connect user with server
        self._authenticate() ##inside a button send_email this fun start user authentication
        print("Sending email.....") 

    def disconnect(self):
        print("Disconnect")

email = EmailService()
# email.send_email() #By calling this for object call _connect and _authenticate automaticaly 
email._authenticate()
email.disconnect()

'''User only cares about paying one simple method does everything'''

class PaymentService:

    def _connect_to_bank(self):
        print("connecting to bank server.")
    
    def _verify_account(self):
        print("verifying bank account")
    
    def _deduct_amount(self):
        print("Deducting amount from account...")

    def pay(self):
 # Inside this "Pay" button, system connects to bank server
        self._connect_to_bank()
 # Inside this "Pay" button, system connects to bank server
        self._verify_account()
# Inside this "Pay" button, system deducts payment amount
        self._deduct_amount()

        print("payment Succesful ")

    def Disconnect(self):
         print("Disconnected from bank server")

payment = PaymentService() 
payment.pay() # Automatically calls all internal steps



class ATM:
    def _read_card(self):
        print("Reading ATM card...")

    def _verify_pin(self):
        print("Verifying PIN...")

    def _check_balance(self):
        print("Checking account balance...")

    def withdraw_cash(self):
        # Inside this "Withdraw" button, ATM reads the card
        self._read_card()

        # Inside this "Withdraw" button, ATM verifies the PIN
        self._verify_pin()

        # Inside this "Withdraw" button, ATM checks balance
        self._check_balance()

        # Final visible action to the user
        print("Dispensing cash 💵")

    def eject_card(self):
        print("Card ejected")


# User interaction (simple and clean)
atm = ATM()
atm.withdraw_cash()   # Automatically performs all internal steps
atm.eject_card()


'''Inheritance:Inheritance allows a class to acquire properties and methods of another class, 
promoting code reuse and hierarchical relationships.'''

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print( "vehicle is starting")
    
    def stop(self):
        print("vehicle is stopping")

class Car(Vehicle):
    def __init__(self, brand, model, year, carwheel, cardoors):
        # call parent constructor
        # super() is used to call methods of the parent class in a child class, enabling code reuse and supporting multiple inheritance.
        super().__init__(brand, model, year)
        self.carwheel = carwheel
        self.cardoors = cardoors

class Bike(Vehicle):
    def __init__(self, brand, model, year, bikewheel, bikemirror):
        super().__init__(brand, model, year)
        self.bikewheel = bikewheel
        self.bikemirror = bikemirror

car1= Car("Honda", "Civic", 2022, 4, 5)
bike1 = Bike("Yamaha", "YBZDx", 2023, 2, 2)

print(car1.brand)
print(car1.carwheel)

print(car1.__dict__)
print(bike1.__dict__)
car1.start()
car1.stop()




'''Composition means: one class HAS A object of another class'''
'''Inheritance models an IS-A relationship, while composition models a HAS-A relationship. 
Composition is generally preferred because it provides greater flexibility and lower coupling.'''

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def drive(self):
        self.engine.start()
        print("Car is driving")
car = Car()
car.drive()

# inheritance
class Engine:
    def start(self):
        print("Engine started")


class Car(Engine):  # Car IS-A Engine (not really correct)
    def drive(self):
        print("Car is driving")
car = Car()
car.start()   # inherited
car.drive()


'''What is Diamond Problem?
Ambiguity caused by multiple inheritance when the same method exists in multiple parent classes.
🔹 How Python solves it?
Using Method Resolution Order (MRO) with C3 linearization.
🔹 How to avoid issues?
Use super() consistently.'''


'''polymorphism:
    Here you can see we applying same method to different datatypes'''
print(len("polymorphism"))
print(len([1,2,3]))
print(len({1,2,3,4}))
# polymorphism through operators
print(1+1)
print("Hi " + "Saqib!")
print([1,2] + [3,4])

'''Without polymorphism'''

class Car:
    def __init__(self, model, brand, year, wheels):
        self.model = model
        self.brand = brand
        self.year = year
        self.wheels = wheels 
    
    def start_car(self):
        print("car is starting")
    def stop_car(self):
        print("car is stopping")

class Motorbike:
    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand
        self.year = year
    
    def start_bike(self):
        print("bike is starting")
     
    def stop_bike(self):
        print("bike is stopping")

# create list of vehicle to inspect
vehicles = [

    Car("Honda", "Civic", 2022, 4),
    Motorbike("Yamaha", "YBZDx", 2023),
    # "bus"
]

# loop through list of vehicle and inspect them
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"inspecting {vehicle.model} {vehicle.brand} type({type(vehicle).__name__})")
        vehicle.start_car()
        vehicle.stop_car()
    
    elif isinstance(vehicle, Motorbike):
        print(f"inspecting {vehicle.model} {vehicle.brand} type({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("object is not valid vehicle")


'''With polymorphism'''

class Vehicle:
    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand
        self.year = year
    
    def start(self):
        print("Vehicle is starting")
    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def __init__(self, model, brand, year, wheels):
        super().__init__(model, brand, year)
        self.wheels = wheels 
    
    def start(self):
        print("car is starting")
    def stop(self):
        print("car is stopping")

class Motorbike(Vehicle):
    def __init__(self, model, brand, year):
        super().__init__(model, brand, year)
    
    def start(self):
        print("bike is starting")
     
    def stop(self):
        print("bike is stopping")

class Bus(Vehicle):
    def __init__(self, model, brand, year, doors):
        super().__init__(model, brand, year)
        self.doors = doors

    
    def start(self):
        print("Bus is starting")
     
    def stop(self):
        print("Bus is stopping")


# create list of vehicle to inspect
vehicles: list[Vehicle] = [

    Car("Honda", "Civic", 2022, 4),
    Motorbike("Yamaha", "YBZDx", 2023),
    Bus("Daewoo", "z-10", 2020, 3)
    # "bus"
]

# loop through list of vehicle and inspect them
for vehicle in vehicles:
    print(f"inspecting {vehicle.model} {vehicle.brand} type({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()     



class EmailService:
    def connect(self):
        print("Connecting to server")

    def send(self):
        print("Sending email")


class GmailService():
    def send(self):
        print("Sending email via Gmail server")

email1 = EmailService()
email1.send()
email2 = GmailService()
email2.send()



# Python support private attributes
class A:
    def __init__(self):
        self.__x = 10  # private attribute

a = A()
# print(a.__x)  # AttributeError
print(a._A__x)  # 10, works via name mangling


'''@classmethod
Ye class ke level ka method hota hai, instance ke liye nahi.
Is method ka pehla argument hamesha cls hota hai, jo class ko refer karta hai.
Matlab: class ke attributes ya methods ko access kar sakta hai, bina instance banaye.'''

class Car:
    wheels = 4  # class attribute

    @classmethod
    def show_wheels(cls):
        print(f"Car has {cls.wheels} wheels")

Car.show_wheels() 


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def area(radius):
        return Circle.pi * radius ** 2

c = Circle.from_diameter(10)  # uses classmethod
print(c.radius)                # 5.0
print(Circle.area(5))          # 78.5, uses staticmethod


# In Python, child classes can override parent attributes and methods. 
# super() allows you to call the parent’s implementation before modifying or extending it.



'''Advanced topics:
1. How to use dir() function: show all attributes/method of an object
2. What is Coupling?
3. What is Dependency Injection?
4. '''






'''Backend OOP Principles (Most → Least Used)'''

'''In real backend development, the most used OOP principle is:
    Composition
Then Encapsulation
Then Abstraction
Then Polymorphism
    Inheritance is used the least'''


