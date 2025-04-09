# ======================== PRINT STATEMENT ========================
# The print() function is used to display output in Python.
print("Hello World")

# ======================== VARIABLES & DATA TYPES ========================
# Variables store data values. Python has several built-in data types.

# String (text): Used to store a sequence of characters.
name = "Abinesh"
# Integer (whole number): Used to store numeric values without decimals.
age = 24
# Float (decimal number): Used to store numbers with decimals.
height = 5.9
# Boolean (True or False value): Used to store logical values.
is_employed = True

# Checking the data type of each variable using the type() function
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_employed))  # <class 'bool'>

# Printing the class name explicitly using the __class__.__name__ attribute
print(name.__class__.__name__)
print(age.__class__.__name__)
print(height.__class__.__name__)
print(is_employed.__class__.__name__)

# ======================== VARIABLE ASSIGNMENT ========================
# Assigning multiple values to multiple variables in one line
x, y, z = 10, 20, 30
print(x, y, z)

# Assigning the same value to multiple variables
a = b = c = 1000
print(a, b, c)

# Unpacking values from a collection (list) and assigning them to variables
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a, b, c)

# ======================== SCOPE OF VARIABLES ========================
# Global variable: A variable declared outside of a function. Can be accessed anywhere.
_global = "Global Variable"
def func():
    print("Inside function:", _global)
func()
print("Outside function:", _global)

# Local variable: A variable declared inside a function. It is accessible only within that function.
def myFunc():
    _local = "Local Variable"
    print(_local)
myFunc()
# print(_local)  # This would cause an error since _local is not accessible outside the function

# Using 'global' keyword inside a function to modify a global variable
def samplefunc():
    global x
    x = "I'm Awesome"
samplefunc()
print("Global Scope variable:", x)

# ======================== TYPE CONVERSION ========================
# Explicitly converting data types using built-in functions
m = 10
n = float(m)  # Convert integer to float
print(n, type(n))

# ======================== RANDOM NUMBER GENERATION ========================
# Generating a random number using the random module
import random
print(random.randrange(1, 10))  # Generate a random number between 1 and 9

# ======================== STRING MANIPULATION ========================
# Strings are sequences of characters enclosed in quotes.
Ex = "Hello, World!"

# Accessing individual characters and substrings using indexing and slicing
print(Ex[1])       # Get character at index 1 ('e')
print(Ex[2:5])     # Get substring from index 2 to 4 ('llo')
print(Ex[-5:-2])   # Get substring from the end ('orl')

# Looping through each character in a string using a for loop
for c in Ex:
    print(c)

# Checking if a substring exists within a string using 'in' keyword
print("World" in Ex)  # True

# String slicing to extract portions of a string
myName = "Abineshkumar"
print(myName[:7])    # 'Abinesh'
print(myName[-5:])   # 'kumar'

# ======================== STRING METHODS ========================
# Built-in string methods for modifying text
name = "   Hello World!   "
print(name.strip())     # Removes leading and trailing spaces
print(name.upper())     # Converts all letters to uppercase
print(name.lower())     # Converts all letters to lowercase
print(name.replace("World", "Python"))  # Replaces a substring with another
print(name.split())     # Splits the string into a list of words

# String concatenation: Joining strings using the '+' operator
string1 = "Hello"
string2 = "World"
print(string1 + " " + string2)  # 'Hello World'

# Using F-strings for formatted string output
print(f"I'm {name.strip()} and I'm {age} years old")

# ======================== ESCAPE CHARACTERS ========================
# Escape characters allow inserting special characters in a string
print("Hello \"World\" Python")  # Insert double quotes within a string
print("It's Alright")  # Using single quotes inside a double-quoted string

# ======================== ADDITIONAL STRING METHODS ========================
comName = "   My name, is Abinesh  24 "
print(comName.lstrip())  # Removes spaces from the left side
print(comName.rstrip())  # Removes spaces from the right side
print(comName.title())   # Converts the first letter of each word to uppercase
print(comName.capitalize())  # Capitalizes only the first letter of the string
print(comName.casefold())  # Converts all letters to lowercase
print(comName.center(50))  # Centers the string within a specified width (50 characters)
print(comName.replace("Abinesh", "Kumar"))  # Replaces 'Abinesh' with 'Kumar'
print(comName.split(" "))  # Splits the string into a list of words using space
print(comName.split(","))  # Splits the string into a list of words using comma
print(comName.join("Abinesh"))  # Joins the string with 'Abinesh' using the original string as a separator
print(comName.find("name"))  # Finds the index of the substring 'name'
print(comName.index("is"))  # Finds the index of the substring 'name' (raises an error if not found)
print(comName.count("i"))  # Counts the occurrences of 'is' in the string
print(comName.startswith("My"))  # Checks if the string starts with 'My'
print(comName.endswith("Abinesh"))  # Checks if the string ends with 'Abinesh'
print(comName.startswith(" "))
print(comName.endswith(" "))
text1 = "Hello123"
print(text1.isalnum())  # Checks if the string contains only alphanumeric characters (letters and numbers)
text2 = "Hello"
print(text2.isalpha())  # Checks if the string contains only alphabetic characters (letters)
text3 = "12345"
print(text3.isdigit())  # Checks if the string contains only digits (numbers)
text4 = "   "
print(text4.isspace())  # Checks if the string contains only whitespace characters (spaces, tabs, etc.)
txt = "45"
print(txt.zfill(5)) # Pads the string with zeros on the left to make it 5 characters long
print(txt.rjust(5)) # Pads the string with spaces on the left to make it 5 characters long
print(txt.ljust(5)) # Pads the string with spaces on the right to make it 5 characters long 

# ======================== TYPECASTING ========================
#Typecasting - converting one datatype into another
#Implicit Typecasting - done automatically by Python, converts smaller datatype into a bigger datatype
a1 = 10
a2 = 20.5
a3 = 5 + 3.40
print(type(a1)) #int
print(type(a2)) #float
print(type(a3)) #float

#explicit conversion - done manually by the user, converts bigger datatype into a smaller datatype
x = 10
print(float(x)) #converts int to float
print(int(x)) #converts float to int
print(str(x)) #converts int to string

# ======================== BOOLEAN ========================
# Boolean values represent True or False.
# They are often used in conditional statements and comparisons.
# Comparison operators return boolean values.
print(10 > 9)
print(10 == 9)
print(10 < 9)

x = 200
y = 100
if(y > x):
    print("y is greater than x")
else:
    print("x is greater than y")


# ======================== OPERATORS ========================
# Operators are special symbols that perform operations on variables and values.
# Python has various types of operators, including arithmetic, assignment, comparison, logical, and more.

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic Operators: Used to perform mathematical operations.
# Operator	Name	Example	
x = 5
y = 3
# +	Addition	x + y	
z = x + y
print(z) # 8

# -	Subtraction	x - y	
z = x - y
print(z) # 2

# *	Multiplication	x * y	
z = x * y
print(z) # 15

# /	Division	x / y
z = x /y
print(z) # 1.6666666666666667

# %	Modulus	x % y	
z = x % y
print(z) # 2

# **	Exponentiation	x ** y	
z = x ** y
print(z) # 125

# //	Floor division	x // y	
z = x // y
print(z) # 1

#Assignment Operators: Used to assign values to variables.
# Python Assignment Operators
# Assignment operators are used to assign values to variables:

# Operator	Example	Same As	Try it
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# :=	print(x := 3)	x = 3
# print(x)

# Comparison Operators: Used to compare two values.
# Operator	Name	Example	Try it
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y

# Logical Operators: Used to combine conditional statements.
# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
x = 4
y = x < 5 and x < 10
print(y) # True
# or	Returns True if one of the statements is true	x < 5 or x < 4	
y = x < 5 or x < 4
print(y) # True
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
y = not(x < 5 and x < 10)
print(y) # False

# Identity Operators: Used to compare the memory locations of two objects.
#Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location:

# is → Returns True if both variables refer to the same object in memory.
a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(a is b) # False, because a and b are different objects in memory ::Even though a and b have the same values, 
              # the important point is that they must refer to the same object in memory.
b = a # Assigning b to a makes them refer to the same object in memory
print(a is b) # True, because a and b now refer to the same object

# is not → Returns True if both variables refer to different objects in memory.
x = [1,2,3,4,5]
y = [1,2,3,4,5]
print(x is not y) # True, because x and y are different objects in memory
print(x is y)  # False, because x and y are different objects in memory
y = x # Assigning y to x makes them refer to the same object in memory
print(x is y) # True, because x and y now refer to the same object

# Membership Operators: Used to test if a value or variable is found in a sequence (string, list, tuple, set, dictionary).
# Membership operators are used to test if a sequence is presented in an object:

# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y	

# (with string)
txt = "Hello, welcome to my world."
print("Hello" in txt)   # True, because 'Hello' is present in the string
print("World" in txt)   # False, because 'World' is not present in the string bcoz, case sensitive

# (with List)
my_list = ["apple", "banana", "cherry", "mango"]
print("apple" in my_list)  # True, because 'apple' is present in the list
print("orange" in my_list)  # False, because 'orange' is not present in the list
print("Cherry" in my_list)  # False, because 'Cherry' is not present in the list bcoz, case sensitive

# (with Tuple)
my_tuple = ("apple", "banana", "cherry", "mango")
print("apple" in my_tuple)  # True, because 'apple' is present in the tuple
print("Banana" in my_tuple)  # False, because 'Banana' is not present in the tuple bcoz, case sensitive

# (with Set)
my_set = {"apple","banana", "cherry"}
print("apple" in my_set)  # True, because 'apple' is present in the set
print("Banana" in my_set)  # False, because 'Banana' is not present in the set bcoz, case sensitive

#(with Dictionary) - by default, it checks for keys
# In a dictionary, the 'in' operator checks for the presence of keys, not values.
my_dict = {"name": "Abinesh", "age": 24, "city": "Chennai"}
print("name" in my_dict)  # True, because 'name' is a key in the dictionary
print("Abinesh" in my_dict)  # False, because 'Abinesh' is not a key in the dictionary
print("City" in my_dict)  # False, because 'City' is not a key in the dictionary bcoz, case sensitive

# To check values in a dictionary, you can use the values() method:
print("Abinesh" in my_dict.values())  # True, because 'Abinesh' is a value in the dictionary

# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

#(with String)
print("Hii" not in txt)  # True, because 'Hii' is not present in the string

#(with List)
my_list = ["apple", "banana", "cherry", "mango"]
print("berry" not in my_list)  # True, because 'berry' is not present in the list

#(with Tuple)
my_tuple = ("apple", "banana", "cherry", "mango")
print("Guava" not in my_tuple)  # True, because 'Guava' is not present in the tuple

# (with Set)
my_set = {"apple","banana", "cherry"}
print("mango" not in my_set)  # True, because 'mango' is not present in the set

#(with Dictionary) - by default, it checks for keys
my_dict = {"name": "Abinesh", "age": 24, "city": "Chennai"}
print("job" not in my_dict)  # True, because 'job' is not a key in the dictionary

#Bitwise Operators: Used to perform bit-level operations on integers.
# Bitwise operators are used to compare binary numbers:
#They operate at the bit level, meaning they compare or manipulate individual bits (0s and 1s) of integer values.

# & 	AND	                   Sets each bit to 1 if both bits are 1	x & y	
# |	    OR	                   Sets each bit to 1 if one of two bits is 1	x | y	
# ^	    XOR	                   each bit to 1 if only one of two bits is 1	x ^ y	
# ~	    NOT	                   Inverts all the bits	~x	
# <<	Zero fill left shift   Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift     Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

# Operator	Description
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	ORBitwise OR	
# ==  !

#================================================= Input and Output =================================================
# Taking user input using the input() function
# Displaying output using the print() function

user_name = str(input("Enter name:"))
print(f"Hello! Nice to meet you Mr. {user_name}")

user_age = int(input("What is your age?"))
print(f"Your age is : {user_age}")

user_rating = float(input("Rate your exp from 1 to 10 : "))
print(f"Your rating is : {user_rating}")

# Immutability in Python - cannot be changed
# All Primary Datatypescannot be changed (int, float, boolean, string, complex)

f_name = "Abinesh"
s_name = "Abinesh"

print(id(f_name))
print(id(s_name))

