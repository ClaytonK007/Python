#
#   Create a To-Do list. Allow user to add, remove, view all tasks and save to a file.
#
tasks = []

def add():
    task = input("Please enter task: ")
    tasks.append(task)
    print("Task added.")
    print("-"*10)

def remove():
    task = input("Enter task to be removed: ")
    if task in tasks:
        tasks.remove(task)
        print("Task has been removed.")
    else:
        ("Task not found.")
    print("-"*10)

def view():
    print("\nTo-Do List:")
    print("-"*10)
    for index, task in enumerate(tasks, start=1):
        print(f"{index} : {task}")
    print("-"*10)

def save():
    with open("tasklist.txt", 'w') as file:
        for index, task in enumerate(tasks, start=1):
            file.write(f"{index} : {task}\n")
        print("To-Do list saved to file.")
    print("-"*10)

while True:
    try:
        print("To-D0 List Menu\n1. Add task.\n2. Remove task.\n3. View all tasks.\n4. Save tasks.\n5. Exit")
        opt = int(input("Choose option: "))
    except ValueError:
        print("Incorrect option. Please try again.")
        continue

    if opt == 1:
        add()
    elif opt == 2:
        remove()
    elif opt == 3:
        view()
    elif opt == 4:
        save()
    elif opt == 5:
        break
    else:
        print("Invalid option. Please choose correct option.")