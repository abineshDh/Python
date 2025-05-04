# ===================
# FILE HANDLING
# ===================

# File Handling used to perform operations on a file such as creating, opening, reading, writing and clsoing it through programming interface


# **To OPEN a file use - open('file.ext', 'r') which requires file path and mode as arguments
# 'r' to open it in read mode. file.read() method to read it in binary

# -- best practice --
try:
    # open() and read() from a file
    open_data = open('File-Handling/data.json', 'r')
    read_data = open_data.read() 
    print(read_data)
except FileNotFoundError as e:
    # raise exception if file not found
    print(f"[ERROR] File Not Found : {e}")
finally:
    # close the file after reading it
    open_data.close()
    
# **To WRITE in a file - open it in 'w' write mode. use write() function to write in a file
try:
    # write the data in 'w' mode
    open_data = open('File-Handling/data.txt', 'w')
    write_data = open_data.write("Hello This a Sample Text for testing Python File Handling.\nHello World!\nLorem ipsum dolor sit amet, consectetur adipisicing elit. Earum esse, eius minus delectus est voluptate,\nporro voluptas possimus minima deserunt,\nincidunt ut quibusdam vel ex rerum cupiditate. Unde, exercitationem eveniet.\n")
except FileNotFoundError as e:
    print(f"[ERROR] {e}")
finally:
    open_data.close()
    
# **with open(...) as file: automatically handles closing the file (better than using finally).
try:
    # read the data in read mode and print in console
    with open('File-Handling/data.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"[ERROR] {e}")
    
# **to ADD a new line in an existing file - use 'a' append mode
try:
    with open('File-Handling/data.txt', 'a') as file:
        content = file.write("\n--Writing a new line in an Existing file...")
except FileNotFoundError as e:
    print(f"[ERROR] {e}")
finally:
    with open('File-Handling/data.txt', 'r') as file:
        content = file.read()
        print(content)
        
# **Read a file line-by-line
try:
    with open('File-Handling/data.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError as e:
    print(f"[ERROR] {e}")

# Use open() with appropriate mode (r, w, a, etc.)
# Use 'with' to handle automatic file closing
# Remember to use error handling (like FileNotFoundError)
# File methods like read(), write(), seek() help manipulate files
# Use os module for file system operations

# *** Writing into a JSON file ***

# Convert Python dictionary/list to JSON string using json.dump() or json.dumps()
# Save it to a file

import json

data = {
        "id" : 1,
        "name" : "Abinesh",
        "age" : 24,
        "email" : "abinesh21@gmail.com",
        "Github" : "abineshDh",
        "Language" : "Python",
        "Experience" : "Beginner",
        "Projects" : [ "Portfolio", "ToDo App", "Shopping Cart"]
}

try:
    with open('File-Handling/data2.json', 'w') as json_file:
        json.dump(data, json_file, indent=4) # converts python_dict into a json_string using dumps()
        
    with open('File-Handling/data2.json', 'r') as json_file:
        content = json_file.read()
        print(content)
except FileNotFoundError as e:
    print(f"[ERROR] {e}")
    
# *** Write into an EXCEL file ***

# openpyxl for .xlsx files (Install using: pip install openpyxl)
# Optionally, pandas for simplified data handling   

from openpyxl import Workbook

# Create an Excel workbook
workbook = Workbook()

# Create a worksheet
worksheet = workbook.active

# Set a title
worksheet.title = 'Grocery List'

# Add Headers
worksheet.append(['Items', 'Unit', 'Price'])

# Add Data
worksheet.append(['Tomato', '3Kgs', 'Rs.100'])
worksheet.append(['Onion', '4Kgs', 'Rs.30'])
worksheet.append(['Brinjal', '2Kgs', 'Rs.60'])

# Save the file
workbook.save('File-Handling/data.xlsx')

# by using Pandas
import pandas as pd
data = [
    {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "is_active": True
    },
    {
        "id": 2,
        "name": "Bob",
        "email": "bob@example.com",
        "is_active": False
    },
    {
        "id": 3,
        "name": "Charlie",
        "email": "charlie@example.com",
        "is_active": True
    }
]
dataframe = pd.DataFrame(data)
dataframe.to_excel('File-Handling/devs.xlsx', index=False)







        


    


