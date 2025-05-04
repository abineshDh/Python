# ===============
# ABSTRACTION
# ===============

# Abstraction hides the complex implementation details while showing only the important datas and functions of the objects. It makes the code reusable, modular  and well-organized
# In Python, we can achieve data abstraction by using abstract classes and abstract classes can be created using abc (abstract base class) module and abstractmethod of abc module.
# @abstractmethod decorator from the abc module

# ABSTRACT CLASS AND METHODS:

# Abstract Class - An abstract class acts as a blueprint for other classes. It contains one or more abstract methods and cannot be instantiated.
# Abstract method - when a method is declared in a class without implementation details its called an abstract method
# Abstract method of base class force its child class to write the implementation of the all abstract methods defined in base class

from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass
     
# Concrete method - when a method in an abstract class with its complete implementation details given. reduces redundant of code only declared in parent class to be reused in subclass

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = True

    def startEngine(self):
        if not self.engine_started:
            print(f"Starting the {self.model}'s engine.")
            self.engine_started = True
        else:
            print("Engine is already running.")
            
# | Term              | Description                                   | 
# |-------------------|-----------------------------------------------|
# | Abstract Class     | Blueprint with abstract methods              | 
# | ABC module         | Used to define abstract base classes         | 
# | Abstract Method    | Must be overridden by subclasses             | 
# | Concrete Method    | Already implemented, can be used as-is       | 


# Python - **Interface module**
# pure abstract methods in an abstract class - with no implementation logics in the abstract methods
# interface contains a set of abstract methods that can be only instanciated by subclass 


# Excercise
# Abstract Payment System

from abc import abstractmethod, ABC

class Payments(ABC):
    
    @abstractmethod
    def make_payment(self, amount):
        pass
    
class CreditCardPayment(Payments):
    def __init__(self, card_number):
       self.card_number = card_number
       
    def make_payment(self, amount):
        print(f"Processing credit card payment of ₹{amount} using card {self.card_number}")
        
class UPIPayment(Payments):
    def __init__(self, upi_id):
        self.upi_id = upi_id
        
    def make_payment(self, amount):
         print(f"Processing UPI payment of ₹{amount} via {self.upi_id}")
         
class PayPalPayment(Payments):
    def __init__(self, email):
        self.email = email
    
    def make_payment(self, amount):
        print(f"Processing PayPal payment of ₹{amount} using account {self.email}")

payments = [
    CreditCardPayment("1234-5678-9876"),
    UPIPayment("abinesh@upi"),
    PayPalPayment("abinesh@example.com")
]

for payment in payments:
    payment.make_payment(1000)
    
# Fully Abstraction using Interface
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self, amount:float) -> None:
        pass
    
    @abstractmethod
    def payment_status(self) -> None:
        pass
    
class CreditCardPayment(PaymentMethod):
    
    def __init__(self, card_number, card_holder, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        
    def pay(self, amount:float) -> None:
        print(f"{self.card_holder} paid Rs.{amount}")
        
    def payment_status(self) -> None:
        print(
            f'''
            Card Number: {self.card_holder}
            Card Number: {self.card_number}
            Payment Transaction done successfully!
            '''
        )
        
class UPIPayment(PaymentMethod):
    
    def __init__(self, mobile_number, upi_id):
        self.mobile_number = mobile_number
        self.upi_id = upi_id                                                                                                                                                                                                                                                                                                                                                                                    
        
    def pay(self, amount:float) -> None:
        print(f"{self.upi_id} paid Rs.{amount}")
        
    def payment_status(self) -> None:
        print(
            f'''
            UPI ID       : {self.upi_id}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            Mobile Number: {self.mobile_number}
            Payment Transaction done successfully!
            '''
        )

cc_payment = CreditCardPayment("1234-5678-9876-5432", "Abinesh", 123)
cc_payment.pay(2500)
cc_payment.payment_status()

upi_payment = UPIPayment("abinesh@upi", "9876543210")
upi_payment.pay(800)
upi_payment.payment_status()

# Interface = Job Description
# Class = Employee
# Object = Actual person doing the job
# The job description tells what must be done. The employee (class) agrees to do all tasks. 
# The person (object) performs them.

