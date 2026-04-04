import mysql.connector

# create databse connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "(your username)",
    password = "(your password)",
    )

mycursor = mydb.cursor()

# create database
mycursor.execute("CREATE DATABASE IF NOT EXISTS tasks")

print(mycursor.rowcount, "database created.")

mydb.close()
