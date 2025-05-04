# ===========================
# PYTHON FUNCTIONS - 
# ===========================

# ===========================
# What is a Function?
# ===========================
# A function is a logical unit of code containing a sequence of statements.
# It is defined using the 'def' keyword.
# Functions are used to perform specific tasks, making code modular and reusable.
# You can pass data (parameters) into a function and receive data back (return values).

# Syntax:
# def function_name(parameters):
#     return "something"
# Function execution happens by calling its name, e.g., function_name()

def greet(name):
    return f"Hello, {name}!"
print(greet("Abineshkumar"))  # Example

# ===========================
# Function with Default Parameter
# ===========================

def greet(name='World'):
    return f"Hello {name}!"
print(greet())           # Uses default parameter
print(greet("Abinesh"))   # Passes argument manually

# ===========================
# Function with Multiple Parameters
# ===========================

def add(a, b):
    return a + b
print(add(2, 5))

# ===========================
# Passing Functions as Arguments
# ===========================
# Functions in Python are first-class citizens — you can pass them around like variables.

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("Hello, World")
    return greeting

print(greet(shout))   # Passing shout function
print(greet(whisper)) # Passing whisper function

# ===========================
# *args and **kwargs (Variable-Length Arguments)
# ===========================
# *args: Variable positional arguments
# **kwargs: Variable keyword arguments

# Example with *args

def add(*args):
    return sum(args)
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))

# Example with **kwargs

def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
info(name="Abinesh", age=22, City="Pondicherry")

# ===========================
# Functions inside a Class
# ===========================
# A Class groups functions (methods) and variables (attributes).
# Methods access data and behaviors specific to the instance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person = Person("Abinesh", 22)
print(person.greet())

# ===========================
# Return Statement
# ===========================
# Used to send a value back to the caller. If no return, the function returns None.

# ===========================
# Local and Global Variables
# ===========================
# Local Variables: Declared inside a function, accessible only inside it.
# Global Variables: Declared outside a function, accessible throughout the code.

def funct():
    x = 10
    b = 20
    return x + b
print(funct())

x = 40
y = 20

def fun():
    return x - y
print(fun())

x = 10

def test():
    x = 5
    print("local variable x:", x)
test()
print("global variable x:", x)

# ===========================
# Class-Based Functions
# ===========================

# Person Class
class Person:
    def __init__(self, name):
         self.name = name
    def greet(self):
        return f"Hi {self.name}, Good Morning!"
person = Person("Abinesh")
print(person.greet())

# Simple Calculator Class
class Calculator:
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mult(self, x, y):
        return x * y

calc = Calculator()
print(calc.add(10, 20))
print(calc.sub(20, 2))
print(calc.mult(22, 11))

# Percentage Calculation Class
class Percentage:
    def __init__(self, name, tamil, english, hindi):
        self.name = name
        self.tamil = tamil
        self.english = english
        self.hindi = hindi
    def average(self):
        total = self.tamil + self.english + self.hindi
        average = total / 3
        if average > 40:
            return f"{self.name}'s average mark is {average:.2f}, Passed!"
        else:
            return f"{self.name}'s average mark is {average:.2f}, Failed!"

marks = Percentage(name="Abinesh", tamil=80, english=78, hindi=45)
print(marks.average())

# Bank Account Class
class Account:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
    def deposit(self, deposit):
        self.balance += deposit
        return f"Hi {self.account_name}, Rs.{deposit} is deposited successfully!"
    def withdraw(self, withdraw):
        self.balance -= withdraw
        return f"Hi {self.account_name}, Rs.{withdraw} is withdrawn successfully!"
    def display(self):
        return f"{self.account_name}, Your Balance is Rs.{self.balance}"

account = Account(account_name="Abinesh", balance=0)
print(account.deposit(200))
print(account.withdraw(100))
print(account.display())

# Rectangle Class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        area = self.length * self.breadth
        return f"Area of a Rectangle is : {area} sq.m"
    def perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        return f"Perimeter of the Rectangle is: {perimeter} units"

rec = Rectangle(12, 21)
print(rec.area())
print(rec.perimeter())

# ===========================
# More Practical Examples
# ===========================

def add(a, b):
    return a + b
print(add(10, 20))

# Overriding previous add to accept *args

def add(*args):
    return sum(args)
print(add(10, 20, 30))

# Student Marks Example using **kwargs

def student_marks(**kwargs):
    for name, marks in kwargs.items():
        print(f"{name} : {marks}")

student_marks(
    Abinesh=100,
    Sathish=67,
    Rajesh=86,
    Suresh=78
)

# Square Calculation

def sqrt(n):
    n = n ** 2
    return n
print(sqrt(10))

# Global variable example

count = 0
print(count)

def fun():
    global count
    count += 1
fun()
print(count)

# Local variable example

def var():
    m = 'This is Local Var'
    return m
print(var())
# print(m) # Would throw an error since m is local

# Multiply and apply example

def multiply(n):
    n = n * 2
    return n

def apply(func, n):
    return func(n)

print(multiply(5))
print(apply(multiply, 10))

# Nested function example

def sum(n):
    def add(n):
        return n + 5
    return add(n)
print(sum(10))

# Greeting function with default argument

def greet(name='Guest'):
    return f"Good Morning! {name}"
print(greet())
print(greet("Abinesh"))

# userdefined functions - already defined in python

# 1 can = 7 sq.m

# height = int(input("Enter the height of the wall: "))
# width = int(input("Enter the width of the Wall: "))

def paint_area(coverage, height, width):
    area = height * width
    no_of_cans = area / coverage
    print(f"Yo will need: {no_of_cans} cans of paint")
paint_area(width=10, height=12, coverage = 7)

import math
# check prime number or not:
def prime_checker(n):
    # for a prime number it should be divided by itself and by 1
    # 5 % 2 == 0 (not a prime)
    is_prime = True
    if n == 1:
        is_prime = False
    for i in range(2, math.ceil(n/2)+1):  #2, 3, 4 , 5
        if n%i == 0:
            is_prime = False
    if is_prime == True:
        print("Its a prime number")
    else:
        print("Its not a prime number")
n = 7
prime_checker(n)

# =========================
# RECURSIVE FUNCTION
# =========================

# Recursion involves a function calling itself directly or indirectly to solve smaller part of the bigger problem.
# breaking a bigger problem into smaller ones, untill its so small so that you can be easily solve it
#It simplifies problems that are naturally repetitive.
# It replaces loops in a smart and clean way.
# It is used in file search, tree structures, games, AI, etc.

# def recursive_function(parameters):
#     if base_case_condition:
#         return base_result
#     else:
#         return recursive_function(modified_parameters)
    
    
import time
def countdown(n):
    if n == -1:
        print("Blast of! Boom!!!")
    else:
        print(n)
        # time.sleep(1)
        return countdown(n - 1)
countdown(10)

# factorial 
def factorial(n):
    # Base Case
    if n == 0:
        return 1
    # Recursive Case
    else:
        return n * factorial(n - 1)
print(factorial(5))

# 5 * 4
# 5 * 4 * 3
# 5 * 4 * 3 * 2
# 5 * 4 * 3 * 2 * 1
# if n = 0 returns 1

# Always have a base case (to stop recursion).
# Problem must get smaller each time.
# Otherwise, it will go forever (infinite recursion = crash).

# fibonacci - using Recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
# print 10 fibonacci
for i in range(10):
    print(fibonacci(i), end=" ")
    
    
# fibonacci using iteration 
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a = b
        b = a + b
fibonacci_iterative(10)

# ========================
# LAMBDA FUNCTIONS
# ========================

# lambda is a small anonymous functions for quick operations which is defined by the 'lambda' keyword
# lamba arguments : expression  operation or return value
# A lambda automatically returns the result of the expression.
# You don't use the *return keyword.
    # lambda: The keyword to define the function.
    # arguments: A comma-separated list of input parameters (like in expression that is evaluated and returned.    
# One expression only → no multiple lines.
# Cannot contain commands like print(), while, or for.
# Used mainly for small quick tasks.

# examples
# add
add = lambda a, b : a + b
print(add(10,20))
# sub
sub = lambda a, b : a - b
print(sub(20,10))
# square
square = lambda x : x * x
print(square(5))
#greet 
greet = lambda : "hello, world"
name = "Abinesh"
convert = lambda : name.upper()
print(convert())
print(greet())

# check if a number positive or negative
num_check = lambda x: "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
print(num_check(0))
print(num_check(10))
print(num_check(-10))

# lambda with list comprehension
list = [lambda arg=x : arg * 10 for x in range(1, 5)]
for i in list:
    print(i())

# check odd or even(if-else)
num = lambda x: "Even" if x%2 == 0 else "Odd"
print(num(10))

# perform multiple operations in one lambda function
calc = lambda x, y : (x + y, x * y)
result = calc(10, 2)
print(result)

# ===================
# map()
# filter()
# reduce()
# ===================

# Function | Purpose                             | Returns
# ---------|-------------------------------------|----------------
# filter() | Pick some items based on True/False | Filtered list
# map()    | Change/modify every item            | Transformed list
# reduce() | Collapse all items into one result  | Single value

# filter() -> it takes a function and a list of arguments and filters out certain elements based on certain condition
# function decides true/false for each items, keeps only the items whether the functions returns as true
# filter(function, iterable)

# check even number from list 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x : x % 2 == 0, numbers))
print(even)

# map() -> it takes a function and list as arguments, map() function tranforms all items in the list by applying the function and creates a new list of changed items
# map(function, iterable)

# square numbers in the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# reduce() -> it takes a function and a list of arguments , and combines all the elements into a single value
# reduce(function, iterable)
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, numbers)
print(product)
# The lambda multiplies two numbers at a time.
# reduce() applies this operation across the list.

from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# usage 
number_list = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, number_list))
print(evens)
squares = list(map(lambda x: x ** 2, evens))
print(squares)
sum = reduce(lambda x, y: x + y, squares)
print(sum)

# students marks processing
marks = [78, 34, 67, 98, 76, 45, 23, 17, 89, 90, 96, 84 ,89, 90, 91, 56 ,34, 39]
passed = list(filter( lambda x: x >= 40, marks))
print(f"Passed marks: {passed}")
bonus = list(map( lambda x: (x * 1.10), passed))
print(f"Bonus marks for passed students: {bonus}")
total_marks = reduce( lambda x, y: x + y, bonus)
print(f"Total marks of all passed students: {total_marks:.2f}")
count = len(passed)
print(f"Students Passed: {count}")








