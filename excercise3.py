# List Excercises ========================================================================================================

# Sum of all Elements in the list
num = [124, 1234, 1323, 1324, 324, 209,243,335 ,53]
sum = 0
for x in num:
  sum += x
print("Sum of elements: ", sum)

# Add elements to a list
items = []
# item = input("Enter an item: ")
# items.append(item)
print(items)

# Remove specific item
list = ["apple", "banana", "cherry"]
list.remove("apple")
print(list)

# Reverse a list
rev_list = [1, 2, 3, 4 ,5, 6 ,7 ,8 ,9 ]
print(rev_list[::-1])

# check item exists in list
list = ["apple", "banana", "cherry", "mango"]
print("mango" in list)

# check occurance of "a" in list
list2 = ["a", "b", "a", "c", "a"]
print(list2.count("a"))

# Find max and min
list3 = [3, 6, 1, 9, 2]
print(max(list3))
print(min(list3))

# Remove duplicate elements in the list
prim_list = ["Apple", "Samsung", "Oppo", "Vivo", "Nokia", "Apple", "Oppo", "Vivo"]
new_list = set(prim_list)
print(new_list)

# check if two list have common elements
list_1 = ["Ajith", "Vijay", "Surya", "Simbu", "Dhanush"]
list_2 = ["Karthi", "SK", "VJS", "Simbu", "Dhanush"]

# set intersection
common_list = set(list_1) and set(list_2)
if common_list:
  print("common elements found")
else:
  print("no common elements found")

# using loop
for name in list_1:
  if name in list_2:
    print("common elements found", name)

# list comprehension
common = [name for name in list_1 if name in list_2]
print(common)

# ======================================================================================================================







