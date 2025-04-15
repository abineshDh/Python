# # List Excercises ========================================================================================================

# # Sum of all Elements in the list
# num = [124, 1234, 1323, 1324, 324, 209,243,335 ,53]
# sum = 0
# for x in num:
#   sum += x
# print("Sum of elements: ", sum)

# # Add elements to a list
# items = []
# # item = input("Enter an item: ")
# # items.append(item)
# print(items)

# # Remove specific item
# list = ["apple", "banana", "cherry"]
# list.remove("apple")
# print(list)

# # Reverse a list
# rev_list = [1, 2, 3, 4 ,5, 6 ,7 ,8 ,9 ]
# print(rev_list[::-1])

# # check item exists in list
# list = ["apple", "banana", "cherry", "mango"]
# print("mango" in list)

# # check occurance of "a" in list
# list2 = ["a", "b", "a", "c", "a"]
# print(list2.count("a"))

# # Find max and min
# list3 = [3, 6, 1, 9, 2]
# print(max(list3))
# print(min(list3))

# # Remove duplicate elements in the list
# prim_list = ["Apple", "Samsung", "Oppo", "Vivo", "Nokia", "Apple", "Oppo", "Vivo"]
# new_list = set(prim_list)
# print(new_list)

# # check if two list have common elements
# list_1 = ["Ajith", "Vijay", "Surya", "Simbu", "Dhanush"]
# list_2 = ["Karthi", "SK", "VJS", "Simbu", "Dhanush"]

# # set intersection
# common_list = set(list_1) and set(list_2)
# if common_list:
#   print("common elements found")
# else:
#   print("no common elements found")

# # using loop
# for name in list_1:
#   if name in list_2:
#     print("common elements found", name)

# # list comprehension
# common = [name for name in list_1 if name in list_2]
# print(common)

# ======================================================================================================================

# SET excercises

# Remove dupliactes from the SET
names = ["Ajith", "Vijay", "Ajith", "Surya", "Vijay", "Simbu"]
# Change the List into a Set to remove the duplicate elements
names = set(names)
print(names)

# Find the common elements in the SetA and SetB
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "kiwi", "cherry"}
# use intersection to return common elements
set_c = set_a.intersection(set_b)
print(set_c)

# Display only the elements that are in set1 but not in set2.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
# use difference to seperate set1 elements from set2
set3 = set1.difference(set2)
print(set3)

# Combine both sets and show the result without any duplicate values.
colors_1 = {"red", "green", "blue"}
colors_2 = {"blue", "yellow", "pink"}
# use symmetric difference to combine both the set without any duplicate
print(colors_1.symmetric_difference(colors_2))

# Check if small is a subset of large.
small = {1, 2, 3}
large = {1, 2, 3, 4, 5, 6}
# use issubset() to find the subset
print(small.issubset(large))

# Create a set containing even numbers from 1 to 20. 
# Then remove all numbers less than 10 and print the updated set.
eve_set = {2,4,6,8,10,12,14,16,18,20}
eve_set = {2,4,6,8,10,12,14,16,18,20}
eve_set = {num for num in eve_set if num >= 10}
print(eve_set)

# Remove all animals in set_2 from set_1.
set_1 = {"dog", "cat", "rabbit", "parrot"}
set_2 = {"cat", "parrot"}
print(set_1.difference(set_2))  


# Find and print elements that are in set_x or set_y, but not in both.
set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}
# symmetric_difference() - print uncommon elements from both the sets
uncommon_elements = set_x.symmetric_difference(set_y)
print(uncommon_elements)

# 
fruits = {"apple", "banana", "mango"}
fruits.clear()
print(fruits)
if not fruits:
   print("Set is Empty")
else:
   print("Set is not Empty  ")

# Use a set to find all unique letters used across all words.
words = ["hello", "world", "python"]
# initialized the empty set
unique_chars = set()  
# loop through each word and each char to seperate char, and add each char to a set to remove duplicates
for word in words:
    for char in word:
        unique_chars.add(char)  #
print(unique_chars)












