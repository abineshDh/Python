# #Print first N natural numbers
# import operator


# n = 11
# for x in range(1, 11):
#   print(x)

# #Print sum of N natural numbers
# n = 5
# sum = 0
# for i in range(1, 6):
#   sum += i

# print("Sum of N natural num:" , sum)

# #Print multiplication table of number 4
# n = 4
# for j in range(1, 11):
#   print(f"{j} * {n} = {j * n}")

# #count digits in the number
# m = "1234567890000"
# count = 0
# for z in m:
#   count += 1

# print(f"Count of digits in m: {count}" )
# # TypeError: 'int' object is not iterable

# #reverse the digit
# # Use num % 10 to extract digits, multiply reversed number by 10 and add digit. Remove the last digit from the original number
# num = 123456789
# rev = 0

# while num > 0:
#   digit = num % 10 
#   rev = rev * 10 + digit
#   num = num // 10

# print("Reveresed digit is: ", rev)

# # Modulo (%): Extracts the last digit of a number.
# # Integer Division (): Removes the last digit of a number.
# # Reversal Logic: Builds the reversed number by shifting digits left (rev * 10) 
# # and appending the extracted digit.

# #Check if the number is Palindrome
# # Reverse the number and check if it's equal to the original.
# num = 121
# original_num = num
# rev = 0

# while num > 0:
#   digit = num % 10 
#   rev = rev * 10 + digit
#   num = num // 10

# print(rev)

# if rev == original_num:
#   print("Palindrome")
# else:
#   print("Not a Palindrome")

# # factorial of a Number
# num = 10
# fact = 1

# for x in range(1, num+1):
#   fact = fact * x

# print("Factorial :", fact)

# # Print N Even numbers
# n = 10
# print("Even Numbers: ")

# for x in range(1, n + 1):
#   if x % 2 == 0:
#     print(x)

# #Find the Largest digit in the number
# num = 64972
# max_digit = 0

# for x in str(num):
#   digit = num % 10
#   if digit > max_digit:
#     max_digit = digit
#   num = num // 10

# print("Max Digit:", max_digit)

# num = 235372
# max_digit = 0

# for x in str(num):
#   if int(x) > max_digit:
#     max_digit = int(x)

# print("Max digit:", max_digit)

# #Fibonacci Series upto N
# n = 10

# a = 0
# b = 1

# print(a)
# print(b)

# for i in range(n):
#   c = a + b
#   print(c)
#   a = b
#   b = c

# n = 10

# a = 0
# b = 1

# print(a, end=" ")  # Print the first term with a space
# print(b, end=" ")  # Print the second term with a space

# for i in range(n - 2):  # Loop for the remaining terms (n - 2 because 2 terms are already printed)
#     c = a + b
#     print(c, end=" ")  # Print the next term with a space
#     a = b
#     b = c
# print("\n")

# #Check if the number pos, neg, zero
# num = 10

# if num > 0:
#   print("Positive")
# elif num < 0:
#   print("Negative")
# else:
#   print("Zero")

# #check if the number is leap year
# year = 2045

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#   print("Leap year")
# else:
#   print("Not a Leap year")


# #Check Vowel or Consonant
# char = "A"

# if char in "AEIOUaeiou":
#   print("Vowel")
# else:
#   print("Consonant")

# #print digits of the number one-by-one
# num = "123456789"
# for i in num:
#   print(i)

# #count number of Vowels and Consonants 
# value = "AbineshKumar"

# vowels = "aeiou"
# vowel_count = 0
# consonant_count = 0

# value = value.lower()

# for char in value:
#   if char.isalpha():
#     if char in vowels:
#       vowel_count += 1
#     else:
#       consonant_count += 1

# print(f"Number of Vowels: {vowel_count}")
# print(f"Number of consonant: {consonant_count}")

# # match-case: simple calculator
# a = 100
# b = 50

# operator = '+'  # Assign a value to the operator variable
# match operator:
#   case '+':
#     result = a + b
#   case '-':
#     result = a - b
#   case '*':
#     result = a * b 
#   case '/':
#     result = a / b 
#   case '%':
#     result = a % b
#   case _ :
#     print("Invalid Operator")

# print("Result", result)

# #day of the week
# day = 3

# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:
#     print("Looking for Weekend")

# #Traffic Sign
# sign = "Red"
# match sign:
#   case "Red": print("Stop!")
#   case "Yellow": print("Ready")
#   case "Green": print("Go!")


# # Python Compound interest calculation
# # Total = Principle * pow(( 1 + r / n), t)

# principal_amt = 0
# rate_of_interest = 0
# time_years = 0

# while True:
#   principal_amt = float(input("Enter Principal Amount: "))
#   if principal_amt < 0:
#     print("Principal amount cannot be negative")
#   else:
#     break

# while True:
#   rate_of_interest = int(input("Enter Interest rate: "))
#   if rate_of_interest < 0:
#     print("Rate of Interest cannot be negative")
#   else:
#     break

# while True:
#   time_years = int(input("Enter number of years: "))
#   if time_years < 0:
#     print("Time of years cannot be negative")
#   else:
#     break

# Total = principal_amt * pow(( 1 + rate_of_interest / 100), time_years)
# print(f"Balance after {time_years} is {Total: .2f}")

# Countdown Timer Program
# Hours : Minutes : Seconds ( HH:MM:SS )
# import time

# countdown = int(input("Enter the time in seconds: "))

# print("Countdown begins...")

# for i in reversed(range(0, countdown + 1)):
#   seconds = int(i % 60) # gives remaining seconds
#   minutes = int((i // 60) % 60) # gives remaining minutes
#   hours = int(i // 3600) # gives hours
#   print(f"{hours:02}:{minutes:02}:{seconds:02}")
#   time.sleep(1)

# divmod(x, y) --> (x //y), (x % y)

# while countdown:
#   mins, secs = divmod(countdown, 60)
#   hours, mins = divmod(mins, 60)
#   print(f"{hours:02}:{mins:02}:{secs:}")
#   time.sleep(1)
#   countdown -= 1

# print("⏰ Times up!")

# ===================================================================================================

# print(eval("10+20+30"))
# result = eval(input("Enter any arithmetic expression")) # simple calculator
# print(result)

# a , b , c = 100, 200, 300
# print("a value %i" %a)
# print("b value %d and c value is %d"%(b,c))

# name = "Abinesh"
# print("Hi Mr. %s"%name)

# ==========================================================================================================

# Pattern Print

# 1                     
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5

row = 5
for row in range(1,6):
  for col in range(1, row+1):
    print(col, end=" ")
  print()


#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

rows = 5

for i in range(1, 6):
  for space in range(rows - i):
    print("  ", end="")
  for col in range(1, i + 1):
    print(col, end=" ")
  print() 

#      1
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5

rows = 5

for i in range(1, rows + 1):
  for space in range(rows - i):
    print(" ", end="")
  for col in range(1, i + 1):
    print(col, end=" ")
  print()





