import mysql.connector
from colorama import Fore, Style

mydb = mysql.connector.connect(
     host = "localhost",
    user = "(your username)",
    password = "(your password)",
     database = "hospital"
)

mycursor = mydb.cursor()

# Hospital functions
def add_hospital(Hospital_Name, Bed_Count):
    mycursor.execute('''INSERT INTO hospital.Hospital (Hospital_Name, Bed_count) VALUES (%s, %s)''', (Hospital_Name, Bed_Count))
    mydb.commit()
    print("*"*10)
    print(Fore.GREEN + f"Hospital {Hospital_Name}, added successfully." + Style.RESET_ALL)
    print("*"*10)

def search_hospital(Hospital_Name):
        mycursor.execute('''SELECT * FROM hospital.Hospital WHERE Hospital_Name = %s''', (Hospital_Name,))
        hospitals = mycursor.fetchone()
        print(Fore.GREEN + f"Hospital Info: " + Style.RESET_ALL)
        print("*"*10)
        if hospitals:
            print(Fore.GREEN + f"Hospital ID: {hospitals[0]}, Hospital Name: {hospitals[1]}, Bed Count: {hospitals[2]}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Hospital name not found or does not exist. Please try again." + Style.RESET_ALL)
        print("*"*10)

def update_hospital():
    pass
          

def delete_hospital(Hospital_Name):
            mycursor.execute('''DELETE FROM hospital.Hospital WHERE Hospital_Name = %s''', (Hospital_Name,))
            mydb.commit()
            print(Fore.GREEN + f"{Hospital_Name} has been deleted." + Style.RESET_ALL)
            print("-"*10)

def view_hospital():
    mycursor.execute('''SELECT * FROM hospital.Hospital''')
    hospitals = mycursor.fetchall()
    print("List of Hospitals: ")
    print("-"*10)
    for hospital in hospitals:
        print(Fore.GREEN + f"Id: {hospital[0]}, Name: {hospital[1]}, Bed Count: {hospital[2]}" + Style.RESET_ALL)
    print("-"*10)


# Doctors functions
def add_doctor(Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary):
    mycursor.execute('''INSERT INTO hospital.Doctor (Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s, %s, %s, %s, %s)''', (Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary))
    mydb.commit()
    print("*"*10)
    print(Fore.GREEN + f"Doctor: {Doctor_Name}, Hospital ID: {Hospital_Id}, Joining Date: {Joining_Date}, Speciality: {Speciality}, Salary: {Salary} added successfully." + Style.RESET_ALL)
    print("*"*10)

def search_doctor(Doctor_Name):
    mycursor.execute('''SELECT * FROM hospital.Doctor WHERE Doctor_Name = %s''', (Doctor_Name,))
    doctors = mycursor.fetchone()
    print(Fore.GREEN + f"Doctors Info: " + Style.RESET_ALL)
    print("*"*10)
    if doctors:
        print(Fore.GREEN + f"Doctor ID: {doctors[0]}, Doctors Name: {doctors[1]}, Hospital ID: {doctors[2]}, Joining Date: {doctors[3]}, Speciality: {doctors[4]}, Salary: {doctors[5]}, Experience: {doctors[6]}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Doctors name not found or does not exist. Please try again." + Style.RESET_ALL)
    print("*"*10)

def list_doctor_bySpec(Speciality, Salary):
    mycursor.execute('''SELECT * FROM hospital.Doctor WHERE Speciality = %s AND Salary <= %s''', (Speciality, Salary))
    doctors = mycursor.fetchall()
    print(Fore.GREEN + f"Doctors Info by specificaitons: " + Style.RESET_ALL)
    print("*"*10)
    if doctors:
        print(Fore.GREEN + f"Doctor ID: {doctors[0]}, Doctors Name: {doctors[1]}, Hospital ID: {doctors[2]}, Joining Date: {doctors[3]}, Speciality: {doctors[4]}, Salary from: {doctors[5]}, Experience: {doctors[6]} years" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Error. Please try again." + Style.RESET_ALL)
    print("*"*10)    

def update_doc_exp(Doctor_Id, new_experience):
    try:
        mycursor.execute('''UPDATE hospital.Doctor SET Experience = %s WHERE Doctor_Id = %s''', (new_experience, Doctor_Id,))
        mydb.commit()
        print(Fore.GREEN + f"Doctor ID experience has been updated to {new_experience}." + Style.RESET_ALL)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    print("*"*10)

def delete_doctor():
    pass

def show_all_doctors():
    pass

def list_doc_by_hospital():
    pass

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
            Hospital_Name = input("Enter Hospital Name to be added: ")
            Bed_Count = input("Enter bed count of new hospital added: ")
            add_hospital(Hospital_Name, Bed_Count)
        elif opt_1 == 2:
            Hospital_Name = input("Enter Hospital Name: ")
            search_hospital(Hospital_Name)
        elif opt_1 == 3:
            update_hospital()
        elif opt_1 == 4:
            Hospital_Name = input("Enter Hospital Name to delete: ")
            delete_hospital(Hospital_Name)
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
            Doctor_Name = input("Enter Name of doctor to add: ")
            Hospital_Id = int(input("Enter Hospital ID doctor is joining: "))
            Joining_Date = input("Enter joining date of doctor: ")
            Speciality = input("Enter doctors speciality: ")
            Salary = int(input("Enter doctors salary: "))
            add_doctor(Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary)
        elif opt_2 == 2:
            Doctor_Name = input("Enter Doctors name to search for: ")
            search_doctor(Doctor_Name)
        elif opt_2 == 3:
            Speciality = input("Enter desired doctor speciality: ")
            Salary_limit = input("Enter salary requirement greater than or equal to: ")
            list_doctor_bySpec(Speciality, Salary_limit)
        elif opt_2 == 4:
            Doctor_Id = int(input("Enter Doctor Id where experience must be updated: "))
            new_experience = int(input("Enter years of experience: "))
            update_doc_exp(Doctor_Id, new_experience)
        elif opt_2 == 5:
            delete_doctor()
        elif opt_2 == 6:
            show_all_doctors()
        elif opt_2 == 7:
            list_doc_by_hospital()
        elif opt_2 == 8:
            continue
        else:
            print("Incorrect option. Please choose valid option.")
    elif choice == 3:
        break
    else:
        print("Incorrect option. Please choose valid option.")
        




