#   Create a student grade system that allows users to add a new student, update
#   an existing grade, get a specific students grade and display all grades.
#
students = {}

def add():
    name = input("Enter students name: ")
    grade= input("Enter students grade: ")
    students[name] = grade
    print("Student has been added successfully.")

def update():
    name = input("Enter a students name: ")
    if name in students:
        grade = input("Enter new grade: ")
        students[name] = grade
        print("Grade updated.")
    else:
        print("Students name not found.")

def get():
    name = input("Enter students name: ")
    print(f"{name}'s grade: {students.get(name, 'Not Found')}")

def display():
    print("List of students grades")
    print(f"-"*23)
    for name, grade in students.items():
        print(f"{name} : {grade}")

while True:
    print("1. Add a Student\n2. Update Student grade\n3. Get a students grade \n4. Display all grades\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        update()
    elif choice == "3":
        get()
    elif choice == "4":
        display()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
