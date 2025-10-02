'''

PAUSED: RESUME AT HOME

Beginner: Python To-Do List

Create an empty list to store tasks

Use a while loop to display a menu with add task, view tasks, 
remove tasks and exit options.

'''

toDoList = []

loop = "on"
while loop == "on":
    userinp = int(input("""
Welcome to the Python to do list. Please enter:
          1 - Add task
          2 - View task
          3 - Remove task
          4 - Exit
          """))
    if userinp == 1:
        break
    if userinp == 2:
        break
    if userinp == 3:
        break
    if userinp == 4:
        break
    else:
        print("Error.")
