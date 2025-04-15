# To-do list Manager
print("============= To-do List =============")

task_list = []

while True:
    menu = input('''
  ================================================
    1. Add task
    2. Remove task
    3. View Task
    4. Sort Tasks
    5. Search Task
    6. Clear All Tasks
    **Press q key to exit
    (Enter appropriate number to navigate: )
  =================================================
''')
    if menu == "1":
        # Add task
        task_name = input("Task To-do: ").lower().strip()
        if task_name:
          task_list.append(task_name)
          print("Task added successfully!")
          print("Current Task List:")
          index = 0
          for task in task_list:
            index += 1
            print(f"{index} : {task}")
        else:
          print("Task List cannot be Empty")
    elif menu == "2":
       if not task_list:
          print("Task list is empty. Nothing to remove")
       else:
          remove_task = input("Enter Task name to remove. ").lower()
          if remove_task in task_list:
             task_list.remove(remove_task)
             print("Task removed successfully!")
          else:
             print("Task not found!")
    elif menu == "3":
        # View tasks
        if not task_list:
           print("No tasks in the list.")
        else:
           print("Your Task: ")
           index = 0
           for task in task_list:
              index +=1
              print(f"{index} : {task}")
    elif menu == "4":
       #sort the list alphabet order
       task_list.sort() 
       index = 0
       for task in task_list:
          index +=1
          print(f"{index} : {task}")
    elif menu == "5":
       #enter task to search
       search = input("Enter Task Name to search: ").lower()
       # search task
       if search in task_list:
          print("Found Task: ", search) 
       else:
          print("Task not found. Try Again!") 
    elif menu == "6":
       clear = input("Do you want to clear all tasks? (Y / N): ").lower()
       if clear == "y":
          task_list.clear()
          print("All Tasks deleted sucessfully!")
       else:
         print("Noting to clear!")
         break
    elif menu == "q":
        # Exit the program
        print()
        print("Thank you! Have a Nice Day! :)")
        break
    else:
        print("Invalid option. Please try again.")


