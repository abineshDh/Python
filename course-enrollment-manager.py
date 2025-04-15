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
students = set()
webdev_course = set()
python_course = set()

if __name__ == "__main__":
 while True:
  option = int(input(''' ===== COURSE ENROLLMENT MANAGER =====
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
           ======================================== ''')).strip()

  # Add student to the course
  if option == "1":
    new_student = input("Enter Student Name for enrollment: ")
    selected_course = input('''
          Select the desired Course from the list:
          (P) Python
          (W) Web Development
          Enter P or W for desired course -''').lower().strip()
    if selected_course == "p":
      students.add(new_student)
      # add the student to python courde
      python_course.add(new_student)
      print(f"{new_student}, You are now enrolled in Python Development Course!")
    elif selected_course == "w":
      students.add(new_student)
      # add the student to webdev course
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
      
  # View All Students
  elif option == "2":
    print("All Students List: ")
    for student in students:
      print(student)


  # Exit program
  else:
    print("Thank you Visit Again!")
    break



