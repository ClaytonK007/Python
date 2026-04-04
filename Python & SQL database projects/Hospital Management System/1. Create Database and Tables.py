import mysql.connector
from colorama import Fore, Style

mydb = mysql.connector.connect(
    host = "localhost",
    user = "(your username)",
    password = "(your password)"
)

mycursor = mydb.cursor()

# create database
mycursor.execute ("CREATE DATABASE IF NOT EXISTS hospital")

print(Fore.GREEN + str(mycursor.rowcount), "databse created." + Style.RESET_ALL)

# create doctors table
mycursor.execute(''' CREATE TABLE IF NOT EXISTS hospital.Doctor (
                 Doctor_Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                 Doctor_Name VARCHAR (255) NOT NULL,
                 Hospital_Id INT NOT NULL,
                 Joining_Date DATE NOT NULL,
                 Speciality VARCHAR (255),
                 Salary INT NULL,
                 Experience INT NULL
                )''')
mydb.commit()
print(Fore.GREEN + str(mycursor.rowcount), "doctors table created." + Style.RESET_ALL)

# insert data into doctors table 
sql_doctors = "INSERT INTO hospital.Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary ) VALUES (%s, %s, %s, %s, %s, %s)"
val_doctors = [
        ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000'), 
        ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000'), 
        ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000'), 
        ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000'), 
        ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000'), 
        ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000'), 
        ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000'), 
        ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000')
            ]
mycursor.executemany(sql_doctors, val_doctors)
mydb.commit()
print(Fore.GREEN + str(mycursor.rowcount), "doctors data inserted." + Style.RESET_ALL)

# create hostpital table
mycursor.execute(''' CREATE TABLE IF NOT EXISTS hospital.Hospital (
                 Hospital_Id INT PRIMARY KEY NOT NULL,
                 Hospital_Name VARCHAR (255) NOT NULL,
                 Bed_Count INT
                )''')
mydb.commit()
print(Fore.GREEN + str(mycursor.rowcount), "hospital table created." + Style.RESET_ALL)

# insert hospital data
sql_hospital = "INSERT INTO hospital.Hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES (%s, %s, %s)"
val_hospital = [
    (1, 'Mayo Clinic', 200),
    (2, 'Cleveland Clinic', 400),
    (3, 'Johns Hopkins', 1000),
    (4, 'UCLA Medical Center', 1500)
]
mycursor.executemany(sql_hospital, val_hospital)
mydb.commit()
print(Fore.GREEN + str(mycursor.rowcount), "data inserted into hospital table." + Style.RESET_ALL)

mydb.close()
