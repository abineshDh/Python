# Course Enrollment Manager
# --------------------------

# Web-development Course
# Python Course

# enrolled only Python - difference  A - B
# enrolled only Web-Dev - difference B - A
# enrolled both - union A + B
# enrolled in any one course but not both - not common in both - A or B - symmetric_difference
# one course list is subset of others. - subset() - A subset of B

# define Set for adding elements
students = set(("Ravi", "Pravin", "Ragavan", "Venkatesh"))
webdev_course = set()
python_course = set()

if __name__ == "__main__":
 while True:
  print("\n")
  option = input(''' 
    ===== COURSE ENROLLMENT MANAGER =======
      1. Add student to course
      2. View all students
      3. Remove student from course
      4. Common students (Both Courses)
      5. Students only in Python
      6. Students only in Web Dev
      7. Exclusive students (Not in both)
      8. Check subset
      9. Clear a course
      0. Exit
      Choose an option: _
    ======================================== ''')

  # 1. Add student to the course
  if option == "1":
    new_student = input("Enter Student Name for enrollment: ")
    selected_course = input('''
          Select the desired Course from the list:
          (P) Python
          (W) Web Development
          Enter P or W for desired course -''').lower().strip()
    if selected_course == "p":
      students.add(new_student)
      python_course.add(new_student)
      print(f"{new_student}, You are now enrolled in Python Development Course!")
    elif selected_course == "w":
      students.add(new_student)
      webdev_course.add(new_student)
      print(f"{new_student}, You are now enrolled in Web Development Course!")
    else:
      print("Please select a valid option: ")
      selected_course = input('''
          Select the desired Course from the list:
          (P) Python
          (W) Web Development
          Enter P or W for desired course - 
                          ''')

  # 2. View All Students
  elif option == "2":
    print("All Students List:\n--------------------")
    for index, student in enumerate(students, start=1):
      print(f"{index}: {student}")

  # 3. Remove Student from the course
  elif option == "3":
    remove_student = input("Enter the Name of the Student to remove: ")
    removed = False

    if remove_student in webdev_course:
      webdev_course.discard(remove_student)
      removed = True
    if remove_student in python_course:
      python_course.discard(remove_student)
      removed = True

    # Only remove from 'students' if not in either course anymore
    if removed:
      if remove_student not in webdev_course and remove_student not in python_course:
        students.discard(remove_student)
      print(f"{remove_student} is removed successfully!")
    else:
      print("Please enter a valid name")

  # 4. Common students in both courses
  elif option == "4":
    common_students = webdev_course.intersection(python_course)
    print("Common Students in Both Course:\n-------------------------------")
    for index, student in enumerate(common_students, start=1):
      print(f"{index}: {student}")

  # 5. Student only in Python 
  elif option == "5":
    only_python = python_course.difference(webdev_course)
    print("Students only in Python Course:\n----------------------------")
    for index, student in enumerate(only_python, start=1):
      print(f"{index}: {student}")

  # 6. Student only in Webdevelopment 
  elif option == "6":
    only_web = webdev_course.difference(python_course)
    print("Students only in Webdevelopment Course:\n----------------------------")
    for index, student in enumerate(only_web, start=1):
      print(f"{index}: {student}")

  # 7. Exclusive students not in both
  elif option == "7":
    print("Students who are not common in Both Course:\n-------------------------------")
    uncommon_students = webdev_course.symmetric_difference(python_course)
    for index, student in enumerate(uncommon_students, start=1):
      print(f"{index}: {student}")

  # 8. Check if a Subset
  elif option == "8":
    if python_course.issubset(webdev_course):
      print("Python course is a Subset of Webdevelopment course! ")
    elif webdev_course.issubset(python_course):
      print("Webdevelopment course is a subset of Python course! ")
    else:
      print("None")

  # 9. Clear a Course
  elif option == "9":
    clear_course = int(input('''
      Select the Course to clear:
      1. Python
      2. Web Development
      - Choose 1 or 2 to clear. '''))

    if clear_course == 1:
      python_course.clear()
      print("Python course contents are cleared! ")
    elif clear_course == 2:
      webdev_course.clear()
      print("Webdevelopment course contents are cleared! ")
    else:
      print("Invalid input. Please try again.")

  # 0. Exit program
  elif option == "0":
    print("Thank you Visit Again!")
    break
  else:
    print("Invalid option. Please choose from the menu.")
