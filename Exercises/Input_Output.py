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

# 4. Convert a numeric input to binary
print("Lets turn a number into binary format")
print("-"*25)
num = int(input("Enter a number: "))

binary = f"{num:b}"

print(f"{num} in bianry is {binary}")
