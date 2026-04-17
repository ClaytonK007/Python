#
# Input and Output exercise
#

# 1. Multiplication of numbers input by user
print("Lets multiply two numbers")
print("-"*25)
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

result = num1 * num2

print(f"Mutiplication of {num1} and {num2}: {result}")

# 2. Display variables with * seperator
print("My", "name", "is", "Jeff", sep="***" )

# 3. Convert an input to octal(base of 8)
print("Find the octal value of a number")
print("-"*25)
num = int(input("Enter a number you want to find octal of: "))

result = "%o" % num

print(f"The octal number of {num} is {result}") 

# 4. Convert a numeric value input to binary
print("Lets turn a number into binary format")
print("-"*25)
num = int(input("Enter a number: "))

binary = f"{num:b}"

print(f"{num} in bianry is {binary}")

# 5. Accept 3 names in one input and seperate into 3 seperate variables.
print("Please give three names seperated by a space.\nIt will return as seprate variables.")
print("-"*25)
name1, name2, name3 = input("Enter 3 seperate names: ").split()

print("Name 1:", name1)
print("Name 2:", name2)
print("Name 3:", name3)

# 6. Convert a numeric input to hexadecimal
print("Lets turn a number into hexadecimal format")
print("-"*25)
num = int(input("Enter a number: "))

hex = f"{num:x}"

print(f"{num} in hexadecimal is {hex}")

# 7. Take a float with more than 2 decimal places and return a float with only 2 decimal places.
print("Display float number with 2 decimal places.\nPlease enter a float with more than two decimal places.")
print("-"*25)
num = float(input("Enter a float with more than 2 decimals: "))

dec = f"{num:.2f}"

print(f"{num} with two decimal places: {dec}")

# 8. Display a percentage.
print("Display a percentage.")
print("-"*25)
num1 = float(input("Enter a numerator: "))
num2 = float(input("Enter a denominator: "))

percentage = (num1 / num2) * 100

print(f"The percetnage of {num1} and {num2}: {percentage:.2f} ")

# 9. Print something and display it right aligned with a width of 25 characters.
print("Display with right alignment of 25 characters.")
print("-"*25)
name = input("Enter a name: ")
version = float(input("Enter a version number: "))

print(f"{name:>25} {version}")

# 10. Print text and center it within a 50 character field and hyphens as padding.
print("Display text and center it within a 50 character field and hyphens as padding.")
print("-"*25)
text = input("Enter a word or title: ")

formatted_text = f"{" " + text + " ":-^50}"
print(f"{formatted_text}")

# 11. Print a value with 5 leading zeros.
print("Print a number with 5 leading zeros.")
print("-"*25)
value = input("Enter a number: ")

print(value.zfill(5))

# 12. Take 3 variables and display it in an order you want using the .format() method.
print("Print values in an order that you want.")
print("-"*25)
quanity = 4
money = 600
price = 150

text = "I have ${1:.2f}, so I can buy {0} footballs for ${2:.2f} each."

print(text.format(quanity, money, price))

# 13. Format a given value into a currency with commas and 2 decimal places.
print("Display a large number as a currency which has commas and 2 decimal places.")
print("-"*25)
value =  float(input("Enter a large number: "))

formatted_value = f"${value:,.2f}"

print(f"Formatted value into currency: {formatted_value}")

# 14. Take inputs from a user and display it in a single list. 
print("Lets take multiple inputs from a user and store it into a list.")
print("-"*25)
numbers = []

for i in range(0, 5):
    print("Enter a float: ", i, ":")
    num =  float(input())
    numbers.append(num)

print("Users input as a list: ", numbers)

# 15. Display two lists in tabular format.
print("Lets print two lists as one table.")
print("-"*25)
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score'}")
print("-"*15)

for name, score in zip(names, scores):
    print(f"{name:<10} {score}")