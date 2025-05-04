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


# Excercise
class PersonAccount:
    def __init__(self, first_name, last_name, income, expenses):
        self.first_name = first_name
        self.last_name = last_name
        self.income = income
        self.expenses = expenses
        
    def add_income(self, amount):
        self.income += amount
        print(f"Revenue added by Rs.{amount}. Revenue = Rs.{self.income}")
        
    def add_expense(self, amount):
        self.expenses += amount 
        print(f"Expenses added by Rs.{amount}. Expenses = Rs.{self.expenses}")
        
    def total_income(self):
        print(f"Total Income is Rs.{self.income}")
        
    def total_expenses(self):
        print(f"Total Expenses Rs.{self.expenses}")
        
    def account_info(self):
        info = {
            'First Name'    : self.first_name,
            'Last Name'     : self.last_name,
            'Full Name'     : self.first_name + self.last_name,
            'Total Income'  : self.income,
            'Total Expenses': self.expenses
        }
        for key, value in info.items():
            print(f"{key:<15} : {value}")

            
account = PersonAccount(
    first_name="Abinesh",
    last_name="Kumar",
    income=1000,
    expenses=500
)
account.add_income(1000)
account.add_expense(500)
account.total_income()
account.total_expenses()
account.account_info()


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