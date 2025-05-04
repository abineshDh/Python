
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

from copy import Error

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

