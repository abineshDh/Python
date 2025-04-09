# Print first N natural numbers
n = 11
for x in range(1, 11):
  print(x)

# Print sum of N natural numbers
n = 5
sum = 0
for i in range(1, 6):
  sum += i
print("Sum of N natural num:" , sum)

# Print multiplication table of number 4
n = 4
for j in range(1, 11):
  print(f"{j} * {n} = {j * n}")

# Count digits in the number
# print(f"Count of digits in m: {count}" )
# # TypeError: 'int' object is not iterable

# #reverse the digit
# # Use num % 10 to extract digits, multiply reversed number by 10 and add digit. Remove the last digit from the original number
m = "1234567890000"
count = 0
for z in m:
  count += 1
print(f"Count of digits in m: {count}")

# Reverse the digits of a number
# # Modulo (%): Extracts the last digit of a number.
# # Integer Division (): Removes the last digit of a number.
# # Reversal Logic: Builds the reversed number by shifting digits left (rev * 10) 
# # and appending the extracted digit.
num = 123456789
rev = 0
while num > 0:
  digit = num % 10 
  rev = rev * 10 + digit
  num = num // 10
print("Reveresed digit is: ", rev)

# Check if the number is a palindrome
# Reverse the number and check if the its equal to the original
num = 121
original_num = num
rev = 0
while num > 0:
  digit = num % 10 
  rev = rev * 10 + digit
  num = num // 10
print(rev)
if rev == original_num:
  print("Palindrome")
else:
  print("Not a Palindrome")

# Calculate factorial of a number
num = 10
fact = 1
for x in range(1, num+1):
  fact = fact * x
print("Factorial :", fact)

# Print N even numbers
n = 10
print("Even Numbers: ")
for x in range(1, n + 1):
  if x % 2 == 0:
    print(x)

# Find the largest digit in a number
num = 64972
max_digit = 0
for x in str(num):
  digit = num % 10
  if digit > max_digit:
    max_digit = digit
  num = num // 10
print("Max Digit:", max_digit)

# Alternative method to find the largest digit in a number
num = 235372
max_digit = 0
for x in str(num):
  if int(x) > max_digit:
    max_digit = int(x)
print("Max digit:", max_digit)

# Fibonacci series up to N terms
n = 10
a = 0
b = 1
print(a)
print(b)
for i in range(n):
  c = a + b
  print(c)
  a = b
  b = c

# Fibonacci series with space-separated output
n = 10
a = 0
b = 1
print(a, end=" ")  
print(b, end=" ")  
for i in range(n - 2):  
    c = a + b
    print(c, end=" ")  
    a = b
    b = c
print("\n")

# Check if a number is positive, negative, or zero
num = 10
if num > 0:
  print("Positive")
elif num < 0:
  print("Negative")
else:
  print("Zero")

# Check if a year is a leap year
year = 2045
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("Leap year")
else:
  print("Not a Leap year")

# Check if a character is a vowel or consonant
char = "A"
if char in "AEIOUaeiou":
  print("Vowel")
else:
  print("Consonant")

# Print digits of a number one by one
num = "123456789"
for i in num:
  print(i)

# Count the number of vowels and consonants in a string
value = "AbineshKumar"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
value = value.lower()
for char in value:
  if char.isalpha():
    if char in vowels:
      vowel_count += 1
    else:
      consonant_count += 1
print(f"Number of Vowels: {vowel_count}")
print(f"Number of consonant: {consonant_count}")

# Simple calculator using match-case
a = 100
b = 50
operator = '+'  
match operator:
  case '+':
    result = a + b
  case '-':
    result = a - b
  case '*':
    result = a * b 
  case '/':
    result = a / b 
  case '%':
    result = a % b
  case _ :
    print("Invalid Operator")
print("Result", result)

# Print the day of the week using match-case
day = 3
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Looking for Weekend")

# Traffic signal interpretation using match-case
sign = "Red"
match sign:
  case "Red": print("Stop!")
  case "Yellow": print("Ready")
  case "Green": print("Go!")

# Compound interest calculation
principal_amt = 0
rate_of_interest = 0
time_years = 0
while True:
  principal_amt = float(input("Enter Principal Amount: "))
  if principal_amt < 0:
    print("Principal amount cannot be negative")
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
Total = principal_amt * pow(( 1 + rate_of_interest / 100), time_years)
print(f"Balance after {time_years} is {Total: .2f}")

# Countdown timer program
# divmod(x, y) --> (x //y), (x % y)
import time
countdown = int(input("Enter the time in seconds: "))
print("Countdown begins...")
for i in reversed(range(0, countdown + 1)):
  seconds = int(i % 60) # gives remaining seconds
  minutes = int((i // 60) % 60) # gives remaining minutes
  hours = int(i // 3600) # gives hours
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)
while countdown:
  mins, secs = divmod(countdown, 60)
  hours, mins = divmod(mins, 60)
  print(f"{hours:02}:{mins:02}:{secs:}")
  time.sleep(1)
  countdown -= 1
print("⏰ Times up!")

# Evaluate arithmetic expressions using eval
print(eval("10+20+30")) 
result = eval(input("Enter any arithmetic expression")) 
print(result)

# Print variable values using formatted strings
a , b , c = 100, 200, 300
print("a value %i" %a)
print("b value %d and c value is %d"%(b,c))
name = "Abinesh"
print("Hi Mr. %s"%name)

# Pattern printing: Right-angled triangle
row = 5
for row in range(1,6):
  for col in range(1, row+1):
    print(col, end=" ")
  print()

# Pattern printing: Pyramid with double spaces
rows = 5
for i in range(1, 6):
  for space in range(rows - i):
    print("  ", end="")
  for col in range(1, i + 1):
    print(col, end=" ")
  print() 

# Pattern printing: Pyramid with single spaces
rows = 5
for i in range(1, rows + 1):
  for space in range(rows - i):
    print(" ", end="")
  for col in range(1, i + 1):
    print(col, end=" ")
  print()





