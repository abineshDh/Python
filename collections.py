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

# enumerate() is a built-in Python function used in loops to automatically add an index (or counter) 
# to each item in an iterable (like a list, tuple, etc.).


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

# SET - Unordered & Immutable (unchangeable), unindexed, and does not allow duplicate values
bikes = {"Pulsar", "Apache", "Kawazaki", "Enfield", "Jawa"}

print(bikes)
print(len(bikes))  # Length of set
print("Pulsar" in bikes)  # Check membership

# set() - Constructor used to make a set
list = {1, 2, 3, 4, 5}
set = set((list))

# Loop through a Set
for bike in bikes:
    print(bike)

# Add / Remove
bikes.add("KTM")  # Add item
print(bikes)
bikes.add("Bajaj")  # Add another item

# Add items from one set to another set
bikes = {"Pulsar", "Apache", "Kawazaki", "Enfield", "Jawa"}
Scooter = {"Dio", "RayZ", "Access125", "Ola", "Aether"}
bikes.update(Scooter)  # Add all items from Scooter to bikes
print(bikes)

# Remove an item
# bikes.remove("KTM")  # Uncomment to remove "KTM"
print(bikes)

# If remove() doesn't work, use discard() to remove an item
bikes.discard("Dio")

# Remove a random item (unordered)
bikes.pop()
print(bikes)

# Clear all items (optional)
bikes.clear()
print(bikes)

# Note: 1 and True are treated as the same value in a set, considered duplicates
values = {0, 1, True, False}
print(values)

# To join SETs
# ------------

# The union() method joins all items from both sets, excluding duplicates
setA = {"a", "b", "c", "d"}
setB = {1, 2, 3, 4, 5}
setC = setA.union(setB)
print(setC)

# The intersection() method keeps ONLY the duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)  # Print only the duplicates

# The difference() method keeps items from the first set that are not in the other set(s)
setX = {"apple", "banana", "cherry"}
setY = {"google", "microsoft", "apple"}
setZ = setX.difference(setY)
print(setZ)

# The symmetric_difference() method keeps all items EXCEPT the duplicates
setM = {"apple", "banana", "cherry"}
setN = {"google", "microsoft", "apple"}
setO = setM.symmetric_difference(setN)
print(setO)

# Set Methods:
# | Method               | Description                                                        |
# |----------------------|--------------------------------------------------------------------|
# | add(elem)            | Adds a single element to the set                                  |
# | update(iterable)     | Adds multiple elements (from list, tuple, etc.) to the set        |
# | remove(elem)         | Removes the specified element. Raises KeyError if not found      |
# | discard(elem)        | Removes the specified element. Does not raise an error if not found |
# | pop()                | Removes and returns a random element from the set                |
# | clear()              | Removes all elements from the set                                |

# Additional Set Methods:
# | Method                  | Description                                                   |
# |-------------------------|---------------------------------------------------------------|
# | union(set)              | Returns a new set with all elements from both sets            |
# | intersection(set)       | Returns a set of common elements                              |
# | difference(set)         | Returns a set of elements in this set but not in the other    |
# | symmetric_difference(set)| Returns elements not common to both sets                     |

# -------------------------------------------------------------------------------------
# | Method                        | Description                                      |
# |------------------------------|--------------------------------------------------|
# | set()                        | Creates a new empty set                          |
# | add(elem)                    | Adds a single element to the set                |
# | update(iterable)            | Adds multiple elements to the set               |
# | remove(elem)                | Removes element; raises error if not found      |
# | discard(elem)               | Removes element; does nothing if not found      |
# | pop()                       | Removes and returns a random element            |
# | clear()                     | Removes all elements from the set               |
# | union(set)                  | Returns all elements from both sets             |
# | intersection(set)           | Returns common elements between sets            |
# | difference(set)             | Returns elements only in the first set          |
# | symmetric_difference(set)   | Returns elements not common to both sets        |
# | intersection_update(set)    | Keeps only common elements in original set      |
# | difference_update(set)      | Removes elements found in another set           |
# | symmetric_difference_update(set) | Updates set with uncommon elements         |
# | issubset(set)               | Checks if current set is a subset               |
# | issuperset(set)             | Checks if current set is a superset             |
# | isdisjoint(set)             | Checks if sets have no common elements          |
# ---------------------------------------------------------------------------------

# ===================================================================================================================================================

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

