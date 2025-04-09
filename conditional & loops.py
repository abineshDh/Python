"""
====================================
Conditional Statements & Loops
====================================

🔹 Conditional Statements (`if`, `elif`, `else`)
🔹 Looping in Python (`for`, `while`)
🔹 Special Loop Control Statements (`break`, `continue`, `pass`)
🔹 The `match` Statement
"""

# =============================================
# CONDITIONAL STATEMENTS
# =============================================

# Conditional statements control the program flow based on conditions.
# The main keywords used are: if, elif, and else.

# Example 1: Checking Odd or Even Number
num = 10
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Example 2: Grade System
marks = 95
if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
elif marks >= 50:
    print("D Grade")
elif marks >= 40:
    print("E Grade")
else:
    print("F Grade")

# Example 3: Nested If-Else
x = 45
if x > 10:
    print("Above 10")
    if x > 20:
        print("Above 20")
    else:
        print("Not above 20")
else:
    print("Not above 10")

# Example 4: Age Classifier
age = int(input("Enter your age: "))
if age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")

# =============================================
# LOOPS (for, while)
# =============================================

# Example 5: Using range() in a for loop
for i in range(1, 6):
    print("Iteration:", i)

# Example 6: Iterating through a List
names = ["John", "Karlsen", "Adam", "Mark"]
for name in names:
    print(name)

# Example 7: Printing a Multiplication Table
num = 5
for i in range(1, 11):
    print(f"{i} * {num} = {num * i}")

# =============================================
# BREAK and CONTINUE
# =============================================

# Example 8: Break Statement
fruits = ["Apple", "Banana", "Cherry", "Mango"]
for fruit in fruits:
    if fruit == "Banana":
        break
    print(fruit)

# Example 9: Continue Statement
for fruit in fruits:
    if fruit == "Banana":
        continue
    print(fruit)

# =============================================
# WHILE LOOP
# =============================================

# Example 10: While Loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Example 11: Password Authentication
password = "Admin@2025"
attempts = 3
while attempts > 0:
    user_pass = input("Enter Password: ")
    if user_pass == password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"You have {attempts} attempts remaining!")
if attempts == 0:
    print("Account Locked!")

# =============================================
# MATCH STATEMENT
# =============================================

holiday = 3
match holiday:
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

# Using OR operator in match statement

day = 6
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a Weekday")
    case 6 | 7:
        print("I Love Weekend")

# =============================================
# MENU-DRIVEN PROGRAM CHALLENGE
# =============================================
import math

while True:
    try:
        print("\n📌 MENU OPTIONS:")
        print("1️⃣ Check Even or Odd")
        print("2️⃣ Print Multiplication Table")
        print("3️⃣ Find Factorial")
        print("4️⃣ Exit")
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 4:
            print("Exiting the Program")
            break
        
        num = int(input("Enter a number between 1 to 10: "))
        
        if choice == 1:
            print("Even Number" if num % 2 == 0 else "Odd Number")
        elif choice == 2:
            for i in range(1, 11):
                print(f"{i} * {num} = {i * num}")
        elif choice == 3:
            print(f"Factorial of {num} is {math.factorial(num)}")
        else:
            print("Invalid Choice")
    except ValueError:
        print("Invalid Input! Enter a valid number.")



