# Hospital functions
def add_hospital():

def search_hospital():

def update_hospital():

def delete_hospital():

def view_hospital():

# Doctors functions
def add_doctor():

def search_doctor():

def list_doctor_bySpec():

def update_doc_exp():

def delete_doctor():

def show_all_doctors():

def list_doc_by_hospital():

# Menu
while True:
    try:
        print("HOSPITAL MANAGEMENT SYSTEM")
        print("*"*26)
        print("Choose which topic you want to work in: ")
        print("1. Hospital.\n2. Doctors.\n3. Exit")
        choice = int(input("Enter option: "))
    except ValueError:
        print("Incorrect option. Please choose listed options.")

    if choice == 1:
        print("Hospital menu")
        print("*"*13)
        print("1. Add Hospital.\n2. Search Hospital\n3. Update Hospital\n4. Delete Hospital\n5. View Hospitals\n6. Go back.")
        opt_1 = int(input("Enter option: "))
        if opt_1 == 1:
            add_hospital()
        elif opt_1 == 2:
            search_hospital()
        elif opt_1 == 3:
            update_hospital()
        elif opt_1 == 4:
            delete_hospital()
        elif opt_1 == 5:
            view_hospital()
        elif opt_1 == 6:
            continue
        else:
            print("Incorrect option. Please choose valid option.")
    elif choice == 2:
        print("Doctors menu")
        print("*"*13)
        print("1. Add Doctor.\n2. Search Doctor.\n3. Get list of Doctors by speciality or salary.\n4. Update Doctors experience.\n5. Delete Doctor.\n6. Show list of Doctors.\n7. Show Doctors from specific Hospital.\n8. Go back.")
        opt_2 = int(input("Enter option: "))
        if opt_2 == 1:
            add_doctor()
        if opt_2 == 2:
            search_doctor()
        if opt_2 == 3:
            list_doctor_bySpec()
        if opt_2 == 4:
            update_doc_exp()
        if opt_2 == 5:
            delete_doctor()
        if opt_2 == 6:
            show_all_doctors()
        if opt_2 == 7:
            list_doc_by_hospital()
        if opt_2 == 8:
            continue
        else:
            print("Incorrect option. Please choose valid option.")
    elif choice == 3:
        break
    else:
        print("Incorrect option. Please choose valid option.")
        




