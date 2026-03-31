#
# 1. Define and call a function.
#    Name the function greet() and call it. 
#
def greet():
    print("Hi there. It is fun to learn.")

greet()

#
# 2. Create a function with parameters.
#    Name the function message() with a 'name' and 'language' parameter.
#
def message(name, language):
    print(f"Hi there. My name is {name} and I love learning {language}")

message("Barney", "Python")

#
# 3. Create a function that returns a value.
#    Name the function square() which returns a square of a number.
#    Use input() to ask user for a number. 
#
def square(num):
    return num * num 

num = int(input("Enter a number to square: "))

result = square(num)
print(f"The square of {num} is: {result}")

#
# 4. Create a function using a default parameter.
#    Name the function greet().
#    Call the fundtion with and without a parameter. 
#
def greet(name = "Ted"):
    print(f"Hi there. My name is {name}.")

greet()
greet("Marshall")

#
# 5. Create a function using a global variable.
#    Create a global variable outside a function and access it. 
#
language = "Python"

def message():
    print(f"I love learning {language}.")

message()

#
# 6. Create a function with a local variable.
#    Create a local variable inside a function and access it. 
#    Try accessing the variable outside the function also. 
#
def message():
    language= "Python"
    print(f"I love learning {language}.")

message()
print(f"Trying to access local variable: {language}") # Will cause an NameError

#
# 7. Create a recursive function to complete a factorial.
#    A recursive function requires a base case and a recursive step.
#
def recursive(num):
    if num == 0 or num == 1: # base case
        return 1
    return num * recursive(num - 1) # recursive step

num = int(input("Enter a number you want to find a factorial of: "))

print(f"The factorial of {num} is: {recursive(num)}")

#
# 8. Create a function that returns multiple values. 
#
def calculate(x, y):
    return x + y, x * y

num_x = int(input("Enter a value for x: "))
num_y = int(input("Enter a value for y: "))

sum, product = calculate(num_x, num_y)

print(f"The sum of x & y is: {sum}.")
print(f"The product of x & y is: {product}.")