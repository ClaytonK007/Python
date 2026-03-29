#
# 1. Read a text file and count number of lines.
#    Add error handling if file not found or if error occured.
#
file_name = input("Enter file name: ")

try:
    with open(file_name, "r") as file: # open file with read argument
        lines = file.readlines() # function to read number of lines
        print(f"Number of lines in file: {len(lines)}")
except FileNotFoundError:
    print(f"{file_name} not found.")
except Exception as e:
    print(F"An error occured: {e}")

#
# 2. Write a record to a file and add error handling
#
car = input("Enter car make: ")
model = input("Enter car model: ")
year = int(input("Enter car year: "))

record = f"Car make: {car}, Car model: {model}, Car year: {year}" # format of record

try:
    with open(car.txt, "a") as file: # creates the text file name with the append attritube
        file.write(record + "\n") # write record to file and create a new line
except Exception as e:
    print(f"An error occured: {e}")

print(f"Record written to file : car.txt")

#
# 3. Create a division calculator and add error handling
#
try:
    num_1 = float(input("Enter numerator: "))
    num_2 = float(input("Enter denominator: "))
    result = num_1 // num_2
    print(f"Result is: {result}")
except ZeroDivisionError:
    print("Error. Divison by 0 is not allowed.")

#
# 4. Prompt a user for a number and add error handling
#
while True:
    try:
        num = int(input("Enter a number: "))
        print(f"The number you entered is: {num}")
        break
    except ValueError:
        print("Incorrect input. Please enter a number only.")