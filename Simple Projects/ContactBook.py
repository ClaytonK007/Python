#
#   Create a contact book. Allow users to add a new contact, search for a contact, display
#   all contacts and save all contacts to a file.
#
contact = {}

def add():
    name = input("Enter contact name: ")
    num = input("Enter contact number: ")
    contact[name] = num
    print("Contact has been added.")
    print(f"-"*23)

def search():
    name = input("Enter contact name: ")
    print(f"{name} : {contact.get(name, 'Not Found.')}")

def display():
    if not contact:
        print("No contacts in list.")
        return
    
    print("List of contacts")
    print(f"-"*16)
    for name, num in contact.items():
        print(f"{name} : {num}")
    print(f"-"*16)

def save():
    with open("contacts.txt", 'a') as file:
        for name, num in contact.items():
            file.write(f"{name} : {num}\n")
        print("Contacts saved.")

while True:
    print("1. Add contact.\n2. Search contact.\n3. Display all contacts.\n4. Save and Exit.")
    choice = input("Enter an option: ")

    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "3":
        display()
    elif choice == "4":
        save()
        break
    else:
        print("Invalid option. Please try again.")