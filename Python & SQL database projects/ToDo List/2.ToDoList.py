import mysql.connector
from datetime import datetime
from colorama import Fore, Style

# create databse connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "Admin",
    password = "SQLpassword!",
    database = "tasks"
    )

mycursor = mydb.cursor()

# create table
mycursor.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
                 id INTEGER AUTO_INCREMENT PRIMARY KEY, 
                 task_name VARCHAR (255) NOT NULL, 
                 description VARCHAR (255), 
                 status VARCHAR (255) DEFAULT 'pending', 
                 date_added DATETIME DEFAULT CURRENT_TIMESTAMP) ''')
mydb.commit()
print(mycursor, "tables created.")

# define functions
def add(task_name, description):
        date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mycursor.execute('''INSERT INTO tasks (task_name, description, status, date_added) 
                         VALUES (%s, %s, 'pending', %s)''', (task_name, description, date_added))
        mydb.commit()
        print(Fore.GREEN + f"Task, '{task_name}', added successfully." + Style.RESET_ALL)
        print("-"*10)

def delete(task_id):
    mycursor.execute('''DELETE FROM tasks WHERE id = %s''', (task_id,))
    mydb.commit
    print(Fore.RED + f"Task ID {task_id} deleted." + Style.RESET_ALL)
    print("-"*10)

def view():
    mycursor.execute("SELECT * FROM tasks")
    tasks = mycursor.fetchall()
    print("\nCURRENT TASKS:")
    print("-"*10)
    for task in tasks:
        print(Fore.CYAN + f"ID: {task[0]}, Name: {task[1]}, Status: {task[3]}, Added: {task[4]}" + Style.RESET_ALL)
    print("-"*10)

def update(task_id, new_status):
    mycursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (new_status, task_id))
    mydb.commit()
    print(Fore.YELLOW + f"Task ID {task_id} has been updated to '{new_status}'." + Style.RESET_ALL)
    print("-"*10)


while True:
    try:
        print("TO-D0 List Menu\n1. Add task.\n2. Delete task.\n3. View all tasks.\n4. Update task status.\n5. Exit")
        opt = int(input("Choose option: "))
    except ValueError:
        print("Incorrect option. Please try again.")
        continue

    if opt == 1:
        task_name = input("Enter task name: ")
        description = input("Enter task description: ")
        add(task_name, description)
    elif opt == 2:
        task_id = int(input("Enter task ID to be removed: "))
        delete(task_id)
    elif opt == 3:
        view()
    elif opt == 4:
        task_id = input("Enter ID of task you want to update: ")
        new_status = input("Enter new status (pending, in-progress, complete): ")
        update(task_id, new_status)
    elif opt == 5:
        break
    else:
        print("Invalid option. Please choose correct option.")

mydb.close()