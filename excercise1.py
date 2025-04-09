# # =========== Variables and Datatypes =============

# name = "Abinesh"
# age = int(24)
# height = float(175.34)
# is_student_or_not = True

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_student_or_not))

# # print(f"Hi I'm {name} and I'm {age} years old, My height is {height} , I'm a {is_student_or_not} Student")

#List
# fav_fruits = ["Apple", "Banana", "Cherry", "Mango"]

#Tuple
# fav_colors = ("Red", "Green", "Blue","Orange")

#Dictionary
# bio = {"name": "Abinesh", "age": 24, "city": "Pondicherry", "job":"Developer"}

# #Set
# fav_nos = { 112, 525, 90992}

# print(fav_fruits)
# print(fav_colors)
# print(fav_nos)
# print(bio)

# #================ Typecasting & UserInput ==============================

# user_name = input("Enter your Name: ")
# print(f"Your name is {user_name}")

# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))

# sum = first_num + second_num

# print(f"The sum of 2 numbers is: {sum}")

# birth_year = int(input("Enter your Birth Year: "))
# current_year = 2025

# user_age = current_year - birth_year

# print(f"Your age is : {user_age}")

# number = 1000
# print(number)
# print(type(number))

# number = float(number)
# print(type(number))

# print(number)

# print(int(number))

# # ======================= String Manipulation ===================================

# name = "Abinesh Kumar"

# print(name.upper())

# print(name.lower())

# print(name[0:7])

# print(name[8:13])

# print(name.replace("Abinesh", "Kokki"))

# print(name.split())

# para = input("Enter a Sentence")
# print(para)

# print(f"The number of a' occurence in para is :{para.count("a")}")

# check = "Python" in para

# print(f"Check the word Python in para: {check}")


# f_name = input("Enter First Name")
# l_name = input("Enter Last Name")
# birth_year = int(input("Enter your Birth Year"))

# current_year = 2025

# age = current_year - birth_year

# user = f_name + l_name

# print(f"Hi Mr. {user} , you are {age} years old, in {current_year}")


# ================= String Manipulation ===========================================================

# name = "Abinesh Kumar"

# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# print(name.casefold())
# print(name.swapcase())

# name = "  Hi Hello, Welcome to Python  "

# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())

# sentence = "Good deeds done do good; bad deeds done bad good"

# print(sentence.replace("bad", "good"))
# print(sentence.replace(" ", "-"))

# paragraph = "Hello Im learning Python, and my favourite programming language is Python, Python was introduced in 2005 Python"

# print(paragraph.find("Python"))
# print(paragraph.rfind("Python"))

# print(paragraph.count("a"))

# print(paragraph.count("Python"))

# print(paragraph.startswith("Hello"))

# print(paragraph.endswith("Python"))

# paragraph = "Hello Im learning Python, and my favourite programming language is Python, Python was introduced in 2005 Python"

# new_para = paragraph.split()

# print(new_para)

# new_list = ", ".join(new_para)

# print(new_list)

# new_name = "ABINESH kumar"

# print(new_name.swapcase())

# new_name = "ABINESH KUMAR"

# print(new_name.center(20,"-"))
# print(new_name.ljust(20, "-"))
# print(new_name.rjust(20, "-"))

# keyword = input("Enter Pass Code: ")

# if ("4042Fg" in keyword):
#   print("Found!")
# else:
#   print("Not found")


#User Password 

# user_input = input("Enter Password: ")

# if user_input.isalpha():
#     print("Password contains only alphabets, add numbers or special characters to make it stronger.")
# elif user_input.isdigit():
#     print("Password contains only digits, add letters or special characters to make it stronger.")
# elif user_input.islower():
#     print("Password contains only lowercase letters, consider mixing uppercase for better security.")
# elif user_input.isupper():
#     print("Password contains only uppercase letters, consider adding lowercase or numbers.")
# elif user_input.isalnum():
#     print("Your password is strong but could be better with special characters.")
# else:
#     print("Your password contains a mix of alphabets, numbers, and special characters—good job!")


#
# short_intro = """Hi Hello My Name is Abinesh
# Python and I love Python
# I like to play Video Games"""

# my_list = short_intro.split("\n")
# print(my_list)

# clean_list = [line.strip() for line in my_list]

# print(clean_list)

# print(f"Total Lines : {len(clean_list)}")

# name = "Abineshkumar"

# x = 10
# y = 5

# x = x - y
# print(x)

# y = y + x
# print(y)

# a = 20  
# b = 3.14  
# c = "Hello, Python!"  
# d = True  
# e = None  

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# b = int(b)
# print(b)
# print(type(b))

# print(c.upper())

# d = int(d)
# print(d)

# user_name = input("Whats your Name?")

# user_age = int(input("Whats your age?"))

# if (user_age > 18):
#   print("Eligible to vote")
# else:
#   print("Not-eligible to Vote")


# x = 12

# if (x > 10 & x%2==0):
#   print("Even number")
# else:
#   print("Odd Number")

# x = True
# y = False

# print(x and y)
# print(x or y)
# print(not x)

# ============================== Conditionals & Loops ==============================

# Odd or Even
# user_input = int(input("Enter a number between 1 to 10: "))

# if user_input % 2 == 0:
#   print(f"The number {user_input} is Even")
# else:
#   print(f"The number {user_input} is Odd")

# Grade Calculator

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

# marks = int(input("Enter marks: "))

# if marks >= 90 and marks <= 100:
#     print("A Grade")
# elif marks >= 80 and marks <= 89:
#     print("B Grade")
# elif marks >= 70 and marks <= 79:
#     print("C Grade")
# elif marks >= 60 and marks <= 69:
#     print("D Grade")
# elif marks < 60:
#     print("F Grade")
# else:
#     print("Enter Proper Marks")

# #Positive, Negative and Zero
# number = int(input("Enter a number: "))

# if number > 0:
#     print("The Number is Positive")
# elif number < 0:
#     print("The Number is Negative")
# else:
#     print("The number is Zero")

# # leap year checking 
# leap_year = 2001

# if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# # print N numbers
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(i)

#Sum of first N natural numbers
# n = 100
# sum = 0

# for i in range(1, n+1):
#   sum += i

# print(f"The Sum of first 100 N Natural Number is: {sum}")

# # multiplication table for an Input number 
# num = int(input("Enter a number from 1 to 10: "))

# for i in range(1, 11):
#   print(f"{i} * {num} = {i * num}")

# import math
# #factorial of a number
# n = 10
# factorial = 10
# for i in range(1, n+1):
#   factorial = factorial * i

# print(f"Factorial of {n} is: {factorial}")

#count digits in the number
# n = 123456789
# n = str(n)
# print(type(n))
# print(len(n))

# m = 9876543210
# count = 0
# while m > 0:
#   count += 1
#   m = m // 10

# print(count)

# Reverse a Number
# sequence[start : stop : step]
# num = 1234
# reversed_num = str(num)[::-1]
# print("Reversed Number:", int(reversed_num))

# To reduce the Last number use : n = n // 10
# To get the Last number use : d = n % 10

# num = 12345
# print(num)
# rev = 0
# while num > 0:
#   digit = num % 10 #get the remainder
#   rev = rev * 10 + digit #add the remainder to the rev num
#   num = num // 10 #to remove the last digit

# print(rev)
  
# Partner Signup
# user = int(input("Enter your Age. must be 18+"))

# if user >= 100:
#   print("Too Old to Sign up")
# elif user >= 18:
#   print("You are Signed up!")
# elif user < 18:
#   print("You need to be atleast 18+")
# else:
#   print("You are not born yet")

#food input
# user = input("Do you want food. (Y / N)")

# if user == "Y":
#   print("Have some food")
# else:
#   print("Are you not Hungry")

# for_sale = True
# if for_sale: 
#   print("This item is for Sales")
# else:
#   print("This item is not for Sales")
  
import math
# Math Operators
# friends = 0
# friends += 1 #augumneted assignment operator
# print(friends)
# friends -= 1
# print(friends)

#builtin functions
# x = 3.14
# y = 4
# z = 5
# result = round(x)
# print(result)

# y = -4
# result = abs(y)
# print(result)

# result = pow(y, 3)
# print(result)

# result = max(x, y, z) #max value of the variable value
# print(result)
# result = min(x, y, z)
# print(result)

# pi_value = math.pi
# print(pi_value)

# result = math.sqrt(x)
# print(result)

# result = math.ceil(y)
# print(result)

# result = math.floor(z)
# print(z)

#circumference of the circle
# c = 2piR
# radius = float(input("Enter the radius of the circle"))
# circumference = 2 * math.pi * radius
# print(f"The Circusference of the circle is: {round(circumference, 2)}")

#Area of the Cirrcle
# Area = pi * r*2
# radius = float(input("Enter the Radius of the Circle"))
# area = math.pi * pow(radius, 2)
# print(f"The Area of the Circle is : {round(area, 2)}")

#validate user input
#username is not more than 12 characters
#username must not contain any spaces
#username must not contain any digits

# username = input("Enter your username: ")

# if len(username) > 12:
#   print("username should not be more than 12 characters")
# elif " " in username:
#   print("username should not contain any space")
# elif any(char.isdigit() for char in username):
#   print("username should not contain any digits")
# else:
#   print("Succesful Login")


# credit_card = "1234-5678-9101-8976"

# last_digit = credit_card[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digit}")


# reversed_digits = credit_card[::-1]
# print(reversed_digits)

# python email slicer
# email = 'abineshspartan2001@gmail.com'
# # username = email.index("@") 
# # print(username)

# username = email[:email.index("@")]
# print(username)
# domain = email[email.index("@") + 1:]
# print(domain)

# Python Compound interest calculation
# Total = Principle * pow(( 1 + r / n), t)

principle_amt = 0
rate_of_interest = 0
time_years = 0

while True:
  principle_amt = float(input("Enter Principle Amount: "))
  if principle_amt < 0:
    print("Priniciple amount cannot be negative")
  else:
    break

while True:
  rate_of_interest = int(input("Enter Interest rate: "))
  if rate_of_interest < 0:
    print("Rate of Interest cannot be negative")
  else:
    break

while True:
  time_years = int(input("Enter number of years: "))
  if time_years < 0:
    print("Time of years cannot be negative")
  else:
    break

Total = principle_amt * pow(( 1 + rate_of_interest / 100), time_years)
print(f"Balance after {time_years} is {Total: .2f}")


# Nested Loop : a loop within the another loop
# ----Outer Loop ---
# ------Inner Loop ---

# rows = int(input("Enter rows: "))
# cols = int(input("Enter cols: "))
# symbol = input("Enter symbol: ")

# print("\n")
# for x in range(rows):
#   for y in range(cols):
#     print(symbol, end="")
#   print()

# =========================================================================

# find the occurences of y 
# sent = "Python is very easy"

# length = len(sent)
# position = -1
# count = 0

# while True:
#   position = sent.find("y", position+1, length)
#   count +=1
#   if position == -1:
#     break
#   print("y is present at", position)
# print("Y count", count)

# count = 0
# position = 0
# for x in sent:
#   if x == "y":
#     print("y is present at: ", position)
#     count += 1
#   position += 1
# print("Count of y", count)

# numbers --> Iteration
# iteration --> loops
# loops --> conditions
# length, position, 

#get only numbers from mail id
# mail_id = input("Enter your email id: ")
# i = 0
# while i < len(mail_id):
#   if mail_id[i] >= '0' and mail_id[i] <= '9':
#     print(mail_id[i], end="")
#   i +=1

# for char in mail_id:
#   if char.isdigit():
#     print(char, end="")




