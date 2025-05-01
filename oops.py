 # ======================================================
# OOPs - OBJECT-ORIENTED PROGRAMMING STRUCTURE
# ======================================================

# OOPS - Object Oriented Programming Principle is a way of organising code in a structure of Objects and Methods(functions) 
# enclosed by classes that represents real-world entities. It helps to structure the program in a clean, reusable and modular way

# Concept       | Meaning                        | Example
# Class         | Blueprint for creating objects | Car class
# Object        | Instance of a class            | A specific car like "BMW X5"
# Encapsulation | Hiding data inside the class   | Private variables
# Inheritance   | Child class inherits methods   | ElectricCar inherits from Car
#               | and properties of parent class | 
# Polymorphism  | Same method name behaves       | Different drive() methods for Car and Bike
#               | different for different classes|

# OOPs Concepts in Python
#----------------------------
# Class in Python
# Objects in Python
# Polymorphism in Python
# Encapsulation in Python
# Inheritance in Python
# Data Abstraction in Python

# ========================
# CLASSES AND OBJECTS
# ========================

# CLASS
#--------
# A class is a collection of objects. Classes are blueprints of creating objects. a class contains a set of attributes 
# and methods that the created objects can have.
# Classes are created by keyword "class". Attributes are the variables thar are belongs to a class. Attributes are always
# public can be accessed using the dot operator. (myclass.myattribute)

from copy import Error


class Dog:
    # class attribute - shared by all instances of the class
    species = "Cannine"
    # __init__ - (dunder methods) initializes name and age attribute wthen the new object is created
    def __init__(self, name, age):
        # instance attribute
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} is barking!")
# object creation
mydog = Dog("Rocky", 2)
print(mydog.name)
print(mydog.age)
mydog.bark() #calling out a method
        
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year 
    def display_info(self):
        return f"{self.brand} : {self.model} car is manufactured in the year {self.year}"
car_info = Car('Tesla', 'Model S', 2015)
print(car_info.display_info())

# OBJECT
# --------
# An object is the instance of the class. it represents the implementation of the class and hold down its data
# object state - represented by the attributes and refelected by the properties of an object
# behaviour state - represented by the methods of the object and reflects the response of the object to another object\
# # object identity - gives a unique name to an object and enables one object to interact with the other object

class Cat:
    # Class variable
    species = "Ginger"
    def __init__(self, name, age):
        # instance Variables
        self.name = name
        self.age = age
# object creation
mycat = Cat("Snowbell", 1.5)
print(mycat.species)
print(mycat.name)
print(mycat.age)

mycat.name = "Masha" # modify instance variable
print(mycat.name, mycat.age) # access instance variable
print(Cat.species) # access class variable

class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year 
    def __str__(self):
        return f"{self.title} : {self.year}"
mybook = Book("Great Gatsby", 1990)
print(mybook)

# self - reference to the current instance of the class, allows to access the attributes and methods of the object
# __init__ - it is a constructor method in python, automatically called when a new object is created. 
# it initializes the attributes of the class.
# __str__ - allows us to define custom string reperesentation of the object. 
# defines a string represent when you print an object.

# @Class Variables
# These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods. 
# All objects of the class share the same value for a class variable unless explicitly overridden in an object.

# @Instance Variables
# Variables that are unique to each instance (object) of a class. These are defined within the __init__ method or 
# other instance methods. Each object maintains its own copy of instance variables, independent of other objects.


# Constructor method
#--------------------
# constructor is a speacial method which is used to initialize the newly created object when its created
# it is used to assign values to the object, you must define it inside the class if you want to set the initial values


# | Type                          | Description                               |  Example  
# | **Default Constructor**       | No arguments except `self`.               | `def __init__(self): ...` 
# | **Parameterized Constructor** | Takes arguments to initialize attributes. | `def __init__(self, name, age): ...` 

# Default Constructor
class Bike:
    def __init__(self):
        self.brand = "Bajaj"
        self.model = "Pulsar N150"
        self.year = 2022
        print("Default Constructor Called")
bike = Bike()
print(bike.model)
print(bike.brand)
print(bike.year)

# Parameterized Constructor
class Product:
    def __init__ (self, name, price, unit):
        self.name = name
        self.price = price
        self.unit = unit
    def display_product(self):
        return f"{self.name} : {self.price} : {self.unit}"
soap = Product("Hamam", "Rs. 50", "50 grams")
shampoo = Product("Head&Shoulders", "Rs. 60", "40 grams")
print(soap.display_product())
print(shampoo.display_product())

# __new__ is a special method that actually creates the object.
# It is called before __init__.
# It allocates memory for the object and returns it.
# In simple words:
# __new__ creates the object : then __init__ initializes the object.

# __new__ is about creation.
# __init__ is about initialization.

# ========================
# ENCAPSULATION
# ========================

# Encapsulation is like bundling the data(attributes & variables) and methods(functions) which acting on data together 
# as a single unit(class) , while restricting access to some components
# why encapsulation?
# Protect Sensitive Data - Prevent Unwanted Changes - control via getters and setters

# Data(attributes) can be accessed and modified only through certain methods
# methods acts an external interface with the code and data stored in variable. private variables can be acccessed only through 
# getters and setters

# Private Data -> Bank Balance = restrict unauthorized access
# Public Methods -> Deposit and Withdraw = only way to access and modify the balance

# 1. PUBLIC MEMBERS (public)
#  it can be accessed from inside and outside of the class, anywhere

class Public:
    def __init__(self):
        self.name = "Johnny"
    def display(self):
        print(self.name)
person = Public()
person.display() # accessed
print(person.name) # accessed

# 2. PROTECTED MEMEBERS (_protected)
# accessible by child classes used for inheritence, technically can be accessed from directly, but shoulnot do so
# indicated by underscore (_protected)

class Person:
    def __init__(self):
        self._age = 20
    def age(self):
        return self._age
class Employee(Person):
    def display_age(self):
        print(self._age)
emp = Employee()
emp.display_age() # can be accessed
print(emp._age)

# 3. PRIVATE MEMBERS
# cannot be accessible directly from outside, indicated by double_underscore (__private)
# uses name mangling _className_attribute.

class Employee:
    def __init__(self):
        self.__salary = 10000
    def get_salary(self):
        return self.__salary
employee = Employee()
print(employee.get_salary()) # can be accessed
# print(employee.__salary) # Raise Attribute Error
print(employee._Employee__salary) # accessed through name mangling

# GETTERS ANS SETTERS
# -------------------
# getters -> used to retrieve(get) the value of private/protected attribute
# setters -> used to set or change the value of private/protected attribute safely
# Why?
# Protect the internal state of an object.
# Add validation logic when setting a value.
# Control how data is exposed or modified.

class Student:
    def __init__(self, name, age):
        self.__name = name     # private
        self.__age = age       # private
    # Getter
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name 
    # Setter
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")
    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            print("Enter a vallid name")
    
student = Student("Akash", 19)
# Access private variables via getters
print(student.get_age())
print(student.get_name())
# set new values for private variables using setters
student.set_age(17)
print(student.get_age())
student.set_name("Abinesh")
print(student.get_name())
# Raises error
student.set_age(-10)
student.set_name(" ")

# using @property
class Product:
    def __init__(self):
        self.__price = 0
        self.__name = ''
    # getters
    @property.getter
    def price(self):
        return self.__price
    @property.getter
    def name(self):
        return self.__name
    # setters
    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("price cannot be negative")
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self.__name = value
        else:
            print("Name cannot be empty!")
prod = Product()
# calls setters
prod.name = 'Soap'
prod.price = 25
# calls getters
print("Product Name: ", prod.name)
print("Product Price: ", prod.price)

# Excercise
# Employee system
class Employee:
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    @property
    def employee_name(self):
        return self.__name
    @property
    def employee_id(self):
        return self.__id
    @property
    def employee_salary(self):
        return self.__salary
    
    @employee_name.setter
    def employee_name(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name.upper()
        else:
            return "Enter a Valid Name"  
    @employee_id.setter
    def employee_id(self, id):
        if isinstance(id, int) and len(str(id)) == 5:
            self.__id = id
        else:
            return "Enter valid format of id"
    @employee_salary.setter
    def employee_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            return "Salary cannot be negative"
    
employee = Employee("name", 12345, 100000)

employee.set_emp_name = "Abineshkumar"
employee.set_emp_id = 67985
employee.set_emp_salary = 15000

print("Name:", employee.employee_name)
print("ID:", employee.employee_id)
print("Salary:", employee.employee_salary)

# Excercise
# banking System

class Savings_Account:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
    
    # getters
    @property
    def account_number(self):
        return self.__account_number  
    
    @property
    def account_holder(self):
        return self.__account_holder 
      
    @property
    def account_balance(self):
        return self.__balance 
    
    # setters
    @account_number.setter
    def account_number(self, number: str):
        if isinstance(number, str) and number.isalnum() and len(str(number)) == 10:
            self.__account_number = number
        else:
            raise ValueError("account number must be 10 digits and contains only alphabets and digits!")        
    
    @account_holder.setter
    def account_holder(self, name: str):
        if isinstance(name, str) and name.strip():
            self.__account_holder = name
        else:
            raise Error("Account name must not be empty")     
        
    @account_balance.setter
    def account_balance(self, bal:float):
        if isinstance(bal, (int, float)) and bal >= 0:
            self.__balance = float(bal)
        else:
            raise Error("Account balance shouldnot be Negative")
        
    # deposit method
    def deposit(self, amount):
       if isinstance(amount, (int, float)) and amount > 0:
           self.__balance += amount
           return f"Rs{amount:.2f} deposited successfully!"
       else:
           return f"Enter a valid non-negative number"
        
    # withdraw method
    def withdraw(self, amount: float):
       if isinstance(amount, (int, float)) and amount > 0:
           if amount <= self.__balance:
               self.__balance -= amount
               return f"Rs.{amount:.2f} withdrawn successfully!"
           else:
               return f"Insufficient Balance: {self.__balance}"
       else:
           return f"Enter a valid amount to withdraw"
    
    # checkbalance method
    def check_balance(self):
        return f"Your Current Account Balance is {self.__balance:.2f}"

# create object
account = Savings_Account("SBIN009867", "Abinesh", 10.0)
     
# change account details using setters
account.account_number = 'SBIN000981'
account.account_holder = 'Abineshkumar'
account.account_balance = 1000.90
# get account details using getters
print("Account number :", account.account_number)
print("Account name :", account.account_holder)
print(f"Account balance : Rs.{account.account_balance}/-")
# access deposit method
account.deposit(1000)
print(account.account_balance)
# access withdraw method
account.withdraw(450.50)
print(account.account_balance)
# access balance method
print(account.check_balance())
account.withdraw(550)
print(account.check_balance())
print(account.deposit(200.90))
print(account.withdraw(500))
print(account.check_balance())
print(account.withdraw(700))
print(account.check_balance())


# ==============
# INHERITANCE
# ==============

# Inheritance allows the class (child class or derived class) to inherit the properties and methods from another class (partent class or base class)
# promotes code reusability and extensibility and modular structure and a hierarchical structure.
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Types of Python Inheritance
# Single Inheritance: A child class inherits from one parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A class is derived from a class which is also derived from another class.
# Hierarchical Inheritance: Multiple classes inherit from a single parent class.
# Hybrid Inheritance: A combination of more than one type of inheritance.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Dog class inheriting the Animal class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"    # Overrides the speak method

dog = Dog("Arun")
print(dog.speak())

# **Single Inheritence** - One child class can inherit the properties of One Parent Class

# Dog class inherits the properties of the Animal class
# If the child class does not define its own __init__() method, 
# it will automatically inherit the one from the parent class.

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def personInfo(self):
        return f"Employee name: {self.name} || Employee id: {self.id}"

class Employee(Person):
    def info(self):
        return f"Employee name: {self.name} || Employee id: {self.id}"
        
# create object for the child class and access the properties of parent class
employee = Employee("Abinesh", 124576)
print(employee.info())
print(employee.name, employee.id)
# can access the attributes of parent class by object creation

# __init__() function is a constructor method in Python. 
# It initializes the object’s state when the object is created. If the child class does not define its own __init__() method, it will automatically inherit the one from the parent class.

# super() constructor used to call the parent class methods, used with child class __init__ method to initialize inherited attributes
# To reuse code from the parent class.
# Helps with maintainability and avoids repeating initialization code.
# Works well in multiple inheritance scenarios too.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print("Vehicle Constructor Called")
        
    def show_info(self):
        return f"Vehicle Brand: {self.brand}, Vehicle Model: {self.model}"
    
class Car(Vehicle):
    def __init__(self, brand, model, wheels: int, price: int, year: int):
        super().__init__(brand, model) # calls parent class constructor
        self.price = price
        self.wheels = wheels
        self.year = year
        print("Car constructor called")
        
    def car_info(self):
        return f'''
        Car Brand : {self.brand}
        Car Model : {self.model}
        Car wheels: {self.wheels}
        Car price : {self.price}
                '''
toyota = Car("Toyota", "Supra", 4, 2000000, 1994)
print(toyota.show_info())
print(toyota.car_info())

# | Concept              | Role                                                        |
# | `super().__init__()` | Calls the parent class constructor explicitly               |
# | Parent constructor   | Initializes common attributes (`brand`, `model`)            |
# | Child constructor    | Initializes specific attributes (`wheels`, `price`, `year`) |

import random

class Vehicle:
    def __init__(self, brand, wheels: int, engine_number: int):
        self.brand = brand 
        self.wheels = wheels
        self.engine_number = engine_number
        
    def display_vehicle_info(self):
        return {
            "Vehicle Brand"         : self.brand,
            "Vehicle Wheels"        : self.wheels,
            "Vehicle Engine Number" : self.engine_number
        }
        
class Car(Vehicle):
    def __init__(self, brand, wheels: int, engine_number: int, model, price: int, fuel_type):
        super().__init__(brand, wheels, engine_number)
        self.model = model
        self.price = price
        self.fuel_type = fuel_type
    
    def display_car_info(self):
        return {
            "Car Brand"         : self.brand,
            "Car Model"         : self.model,
            "Car Wheels"        : self.wheels,
            "Car Engine Number" : self.engine_number,
            "Car Price"         : self.price,
            "Car Fuel Type"     : self.fuel_type
        }
        
    def car_register(self):
        reg_num = f"{random.randint(100000, 999999):06d}"
        return f"{reg_num}: Your {self.brand} {self.model} Car Registration Successful!"
    
class Bike(Vehicle):
    def __init__(self, brand, model, wheels: int, engine_number: int, type, cc):
        super().__init__(brand, wheels, engine_number)
        self.model = model
        self.cc = cc
        self.type = type
        
    def bike_specs(self):
        return {
            "Bike Brand" : self.brand,
            "Bike Model" : self.model,
            "Bike Wheels": self.wheels,
            "Bike CC"    : self.cc,
            "Bike Type"  : self.type
        }
    
    def bike_register(self):
        reg_num = f"{random.randint(100000, 999999):06d}"
        return f"{reg_num}: Your {self.model} Registration Successful!"
    
# car object creation
car = Car(
    brand="Toyota",
    wheels=4,
    engine_number=14628,
    model="Supra",
    price=1200000,
    fuel_type="Combustion Engine"
)

# access car info and fetch details
car_info = car.display_car_info()

print("Car Details:\n-------------")
for key, value in car_info.items():
    print(f"{key} : {value}")

print(car.car_register())

# bike object creation
bike = Bike(
    brand="Bajaj",
    model="Pulsar N150",
    wheels=2, 
    engine_number=568261,
    type="Sports Cruiser",
    cc=250
)

# access bike info and fetch details
bike_info = bike.bike_specs()

print("\nBike Details:\n-------------")
for key, value in bike_info.items():
    print(f"{key} : {value}")

print(bike.bike_register())

# vehicle object
vehicle = Vehicle(
    brand='Volvo',
    wheels=6,
    engine_number=786462
)

vehicle_info = vehicle.display_vehicle_info()

for key, value in vehicle_info.items():
    print(f"{key} : {value}")


# **Multiple Inheritence** a child class can inherits the properties of more than one parent class, the derived class can inherits al the properties of base class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Work:
    def __init__(self, job_title):
        self.job_title = job_title
    
    def show_job(self):
        print(f"Job : {self.job_title}")

# inherits from both the parents class
class Employee(Person, Work):
    def __init__(self, name, age, job_title, salary):
        # initializes parent class constructor
        Person.__init__(self, name, age)
        Work.__init__(self, job_title)
        self.salary = salary 
        
    def show_details(self):
        print(f'''
        Employee Name   : {self.name}
        Employee Age    : {self.age}
        Employee Job    : {self.job_title}
        Employee Salary : {self.salary}
        ''')
employee = Employee("Abinesh", 23, "Developer", 25000)
employee.show_details()
employee.show_job()
employee.show_name()

print(Employee.__mro__) 

#MRO is the order in which Python searches classes when you call a method or initialize with super() in multiple inheritance.
# Cooperative Initialization is when all classes in a multiple inheritance chain use super(), so each class has a chance to initialize its own data safely.
#Each __init__() calls super().__init__(), and Python moves through the MRO in order.

# | Term                    | Meaning                                                                   |
# |-------------------------|-------------------------------------------------------------------------  |
# | **MRO**                 | Order Python uses to search for methods in multiple inheritance.          |  
# | **super()**             | Calls the next class in the MRO.                                          |
# | **Cooperative Init**    | Every class uses `super()` to allow smooth, conflict-free initialization. |

# | Benefit                              | Why it matters                                                |
# |------------------------------------------------------------------------------------------------------|
# | Allows all classes to be initialized | Even if they don’t know all the arguments upfront             |
# | Enables MRO-safe `super()` chains    | Prevents double initialization and missing arguments          |
# | Makes code cleaner and extensible    | Easy to add new parent classes later without breaking others  |

# Constructor chaining means calling one constructor from another in a multi-class inheritance hierarchy, ensuring that all parent class 
# constructors get called automatically and in the right order.

class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age
        print("Person Constructor Called")
    
class Work:
    def __init__(self, job, **kwargs):
        super().__init__(**kwargs)
        self.job = job
        print("Work class Contructor called")

class Employee(Work, Person):
    def __init__(self, name, age, job, salary ):
        super().__init__(name=name, age=age, job=job)
        self.salary = salary
        print("Employee class constructor called")

emp = Employee("Abinesh", 24, "Developer", 22000)

# Excercise
# Smart Device System

# Base: 1
class Device:
    def __init__(self, brand, model, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        self.model = model
    
    def device_info(self):
        print("Device Info: \n" + "-" * 20)
        print(f"Brand    : {self.brand}")
        print(f"Model    : {self.model}")
        
# Base: 2
class Connectivity:
    def __init__(self, bluetooth, wifi_enabled, **kwargs):
        super().__init__(**kwargs)
        self.bluetooth = bluetooth
        self.wifi_enabled = wifi_enabled
        
    def connectivity_info(self):
        print("Connectivity Info: \n" + "-" * 20)
        print(f"Bluetooth:   {self.bluetooth}")
        print(f"WiFi     :   {self.wifi_enabled}")
    
# Child: 1
class SmartPhone(Device, Connectivity):
    def __init__(self, brand, model, bluetooth, wifi_enabled, os, **kwargs):
        super().__init__(brand=brand, 
                         model=model, 
                         bluetooth=bluetooth, 
                         wifi_enabled=wifi_enabled, 
                         **kwargs)
        self.os = os
        
    def phone_info(self):
        print("Smartphone Info: \n" + "-" * 20)
        smartphone = {
            "Brand"      : self.brand,      
            "Model"      : self.model,
            "OS"         : self.os,
            "Bluetooth"  : self.bluetooth,
            "WiFi"       : self.wifi_enabled
        }
        for key, value in smartphone.items():
            print(f"{key:<15} : {value}")  # Left-align keys with a width of 15


# Child: 2
class SmartWatch(Device, Connectivity):
    def __init__(self, brand, model, bluetooth, wifi_enabled, heart_rate_monitor, **kwargs):
        super().__init__(brand=brand, 
                         model=model, 
                         bluetooth=bluetooth, 
                         wifi_enabled=wifi_enabled, 
                         **kwargs)
        self.heart_rate_monitor = heart_rate_monitor
    
    def watch_info(self):
        print("Smartwatch Info: \n" + "-" * 20)
        smartwatch = {
            "Brand"              : self.brand,      
            "Model"              : self.model,
            "Heart Rate Monitor" : self.heart_rate_monitor,
            "Bluetooth"          : self.bluetooth,
            "WiFi"               : self.wifi_enabled
        }
        for key, value in smartwatch.items():
            print(f"{key:<20} : {value}")  # Left-align keys with a width of 20

# Smart Phone Object
smartphone = SmartPhone(
    brand="Samsung",
    model="Galaxy S22",
    os="Android Pi",
    bluetooth="Yes",
    wifi_enabled="Enabled"
)

smartphone.phone_info()
smartphone.device_info()

# Smart Watch Object
smartwatch = SmartWatch(
    brand="Apple",
    model="Watch Series 9",
    heart_rate_monitor="Yes",
    bluetooth="Yes",
    wifi_enabled="Disabled"
)

smartwatch.watch_info()
smartwatch.device_info()

