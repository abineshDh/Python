# Python Collections: List, Set, and Tuple

# COLLECTIONS = A single variable used to store multiple values

# List []   = Ordered and Mutable (changeable), Duplicates allowed
# Set  {}   = Unordered and Immutable (elements can't be changed but can be added/removed), No Duplicates
# Tuple ()  = Ordered and Unchangeable, Duplicates allowed

# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# ===============================================================================================================================

# LIST - Ordered & changeable and Duplicates are allowed. Lists are indexed based starts from index[0] and index[n]
cars = ["Audi", "Benz", "Mustang", "Toyato", "Lamborghini"]

# Accessing Elements
print(cars[0:4])     # From index 0 to 3
print(cars[:4])      # From beginning to index 3
print(cars[2:4])     # From index 2 to 3
print(cars[::2])     # Every 2nd element
print(cars[::-1])    # Reverse the list

# Loop through list
for car in cars:
  print(car)

# loop through index of list 
for i in range(len(cars)):
  print(cars[i])

# using while loop
i = 0
while i < len(cars):
  print(cars[i])
  i += 1

# loop using list comprehension - short syntax
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry"]
[print(fruit) for fruit in fruits]

# create a new list with fruits that starts with "a" while leaving the old list unchanged
new_fruits = [x for x in fruits if "a" in x]
print(new_fruits)

# Built-in Functions
print(len(cars))         # Length of list
print('Audi' in cars)    # Check if an item exists

# Modify Elements
cars[0] = "BMW"           # Change element at index 0
print(cars)

# Add / Remove / Insert
cars.append("Porsche")    # Add to the end
print(cars)
# Lists are ordered if we add a new item, it adds at end of the list, order will not change


cars.remove("Benz")       # Remove specific element
print(cars)
# If there are more than one item with the specified value, 
# the remove() method removes the first occurrence

cars.insert(5, "Cheverlotte")  # Insert at specific position
print(cars)

# Sorting / Reversing
cars.sort()               # Sort alphabetically
print(cars)

cars.reverse()            # Reverse the list
print(cars)

# Get Index / Count Occurrences
print(cars.index("BMW"))  # Find index of an item

cars.append("Toyato")     # Add duplicate
print(cars.count("Toyato"))  # Count occurrences

# Clear the list (optional)
cars.clear()
print(cars)

# List items - Datatypes - a list can contain multiple datatypes
my_list = ["abc", 123, True, 12.67]
print(my_list)

new = list((1 , 2 , 3 , 4 , 5))
print(new)

# extend() - to add elements from another list to the current list - elements will be added in the end of the list
# to join lists
first_list = ["Kitkat", "Munch", "DairyMilk"]
second_list = ["Oreo", "JimJam", "Darkfantasy"]
first_list.extend(second_list)
print(first_list)

#to join 2 lists by appending elemts from list2 to list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# copy() = to make a copy of the list
mylist = first_list.copy()
print(mylist)

# use list() - to make a copy
mylist = list(cars)
print(mylist)

# List Methods:
# | Method      | Description                                                                 |
# |-------------|-----------------------------------------------------------------------------|
# | append()    | Adds an element at the end of the list                                      |
# | clear()     | Removes all the elements from the list                                      |
# | copy()      | Returns a copy of the list                                                  |
# | count()     | Returns the number of elements with the specified value                     |
# | extend()    | Add the elements of a list (or any iterable), to the end of the current list|
# | index()     | Returns the index of the first element with the specified value             |
# | insert()    | Adds an element at the specified position                                   |
# | pop()       | Removes the element at the specified position                               |
# | remove()    | Removes the item with the specified value                                   |
# | reverse()   | Reverses the order of the list                                              |
# | sort()      | Sorts the list                                                              |

# ======================================================================================================

# SET - Unordered & Immutable
bikes = {"Pulsar", "Apache", "Kawazaki", "Enfield", "Jawa"}

print(bikes)
print(len(bikes))            # Length of set
print("Pulsar" in bikes)     # Check membership

# Add / Remove
bikes.add("KTM")             # Add item
print(bikes)

bikes.remove("KTM")          # Remove item
print(bikes)

bikes.pop()                  # Remove random item (unordered)
print(bikes)

# The del keyword can also delete the list completely.
# del bikes

# Clear all items (optional)
bikes.clear()
print(bikes)

# TUPLE - Ordered & Unchangeable
vehicles = ("Cars", "Bikes", "Bus", "Train", "Cycle", "Airplane")

print(vehicles)
print(len(vehicles))          # Length of tuple
print("Bikes" in vehicles)    # Check if exists

# Tuple methods
print(vehicles.index("Bus"))     # Get index of item
print(vehicles.count("Cycle"))   # Count occurrence of item

# Loop through tuple
for vehicle in vehicles:
  print(vehicle)

# Simple Shopping cart Program
# foods = []
# prices = []
# total = 0

# while True:
#   food = input("Enter food to buy (or q to quit): ")
#   if food.lower() == "q":
#     break
#   else:
#     price = float(input(f"Enter the pice of {food}: $"))
#     foods.append(food)
#     prices.append(price)

# print("========== YOUR CART ==========")

# for food in foods:
#   print(food, end=" | ")
# print("\n")

# for price in prices:
#   total += price

# print(f"Your Total is: ${total: .2f}")

print(type(cars))
print(type(bikes))
print(type(vehicles))

