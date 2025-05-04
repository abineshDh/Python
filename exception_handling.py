# ===================
# EXCEPTION HANDLING
# ===================

# Exception Handling is used to catch runtime errors without interupting the normal flow of the code.
# it handles the unexpected errors and gracefully shows error messages 

# try:
#     # Code that may raise an error
# except <ExceptionType>:
#     # Code that runs if an error occurs
# else:
#     # Code that runs if NO error occurs (optional)
# finally:
#     # Code that always runs (optional)

try:
    num = 10
    result = num / 0
    print(result)
except ZeroDivisionError:
    print(f'[ERROR] Any number cannot be divided by zero')
else:
    print("Division Successful")
finally:
    print('Execute this program no matter what!')
    num = 10
    result = int(10 / 2)
    print(result)
    
# try -> tries out the code which might have an exception,
# except -> if the try block has certain errors, except block will be executed to handle the error with the appropriate exception
# else -> else block will be executed only if there are no error occurs
# finally -> finally block will be executed no matter what

# raise -> we can raise an error in python using raise keyword with Exception instance class

try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be a negative integer")
    print(f"Age is set to {age}")
except ValueError as e:
    print([e])

# Catch multiple exception with the try/ except block

try:
    num = int(input('Enter a number: '))
    result = 10 / num
except ValueError as e:
    print([e], ": 'str' cannot be taken as an input")
except ZeroDivisionError as e:
    print([e], ": Any number cannot be divided by 0")
else:
    print('result', result)
    print("Division successful!")
    
    
# | **Exception Name**    | **Description**                                                           |
# | --------------------- | ------------------------------------------------------------------------- |
# | `BaseException`       | The base class for all built-in exceptions.                               |
# | `Exception`           | The base class for all exceptions that are not meant to exit the program. |
# | `ArithmeticError`     | Base class for errors related to arithmetic calculations.                 |
# | `ZeroDivisionError`   | Raised when dividing or taking modulo by zero.                            |
# | `OverflowError`       | Raised when a numeric operation exceeds the limits of the data type.      |
# | `FloatingPointError`  | Raised when a floating-point calculation fails.                           |
# | `AssertionError`      | Raised when an `assert` statement fails.                                  |
# | `AttributeError`      | Raised when an invalid attribute reference or assignment is made.         |
# | `IndexError`          | Raised when an index is out of range in sequences (like lists, tuples).   |
# | `KeyError`            | Raised when a key is not found in a dictionary.                           |
# | `MemoryError`         | Raised when memory is exhausted during operation.                         |
# | `NameError`           | Raised when a variable or function name is not defined.                   |
# | `OSError`             | Raised for operating system-related errors (e.g., file not found).        |
# | `TypeError`           | Raised when a function is applied to an object of inappropriate type.     |
# | `ValueError`          | Raised when the correct type is passed, but the value is invalid.         |
# | `ImportError`         | Raised when importing a module or object fails.                           |
# | `ModuleNotFoundError` | Raised when a module can’t be located (subclass of `ImportError`).        |


print("Safe Calculator")

def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "[Error] Division by Zero not possible"
        case _:  # Corrected wildcard case
            return "[ERROR] Invalid Operation"

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    result = calculate(num1, num2, operation)
    print(f"RESULT: {result}")
except ValueError as e:
    print("[ERROR] Invalid Input: Please enter numeric values.")
except KeyboardInterrupt:
    print("\n[INFO] Program interrupted by user.")
except Exception as e:
    print(f"[ERROR] {e}")

    
# User-defined exception - can be able to define our own exception by inheriting builtin exception class or its subclass


class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

try:
    set_age(150)  
except InvalidAgeError as e:
    print(f"[ERROR] {e}")
    

# ** NOTES

# All exceptions are derived from BaseException. Commonly used ones are under Exception.
# Understanding this helps when catching multiple exceptions.
# except Exception:  # catches most runtime errors
# except BaseException:  # catches all including SystemExit, KeyboardInterrupt

# Always runs finally() block— whether an exception occurred or not. Ideal for resource cleanup (e.g., closing files).
# try:
#     file = open("data.txt")
#     # operations
# except FileNotFoundError:
#     print("File not found")
# finally:
#     file.close()  # ensures the file is always closed

# Instead of just printing, use the logging module to record exceptions.
# import logging

# try:
#     1 / 0
# except ZeroDivisionError as e:
#     logging.exception("Division failed")  # includes traceback


        

        
    
    
