# Python Collections: List, Set, and Tuple

# COLLECTIONS = A single variable used to store multiple values

# List []   = Ordered and Mutable (changeable), Duplicates allowed
# Set  {}   = Unordered and Immutable (elements can't be changed but can be added/removed), No Duplicates
# Tuple ()  = Ordered and Unchangeable, Duplicates allowed

# LIST - Ordered & Mutable
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

# Built-in Functions
print(len(cars))         # Length of list
print('Audi' in cars)    # Check if an item exists

# Modify Elements
cars[0] = "BMW"           # Change element at index 0
print(cars)

# Add / Remove / Insert
cars.append("Porsche")    # Add to the end
print(cars)

cars.remove("Benz")       # Remove specific element
print(cars)

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

# Shopping cart Program
foods = []
prices = []
total = 0

while True:
  food = input("Enter food to buy (or q to quit): ")
  if food.lower() == "q":
    break
  else:
    price = float(input(f"Enter the pice of {food}: $"))
    foods.append(food)
    prices.append(price)

print("========== YOUR CART ==========")

for food in foods:
  print(food, end=" | ")
print("\n")

for price in prices:
  total += price

print(f"Your Total is: ${total: .2f}")
