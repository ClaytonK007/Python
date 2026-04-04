import mysql.connector
from datetime import datetime
from colorama import Fore, Style

# create databse connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "Admin",
    password = "SQLpassword!",
    )

mycursor = mydb.cursor()

# create database
mycursor.execute("CREATE DATABASE IF NOT EXISTS tasks")

print(mycursor.rowcount, "database created.")

mydb.close()