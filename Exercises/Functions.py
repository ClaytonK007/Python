#
#   1. Create a Function with Parameters
#
def sentence(name, job):

    print(f"My name is {name} and I am a {job}.")

sentence("Ted", "Python programmer")

#
#   2. Variable Length of Arguments (*args)
#
def func1(*args):
    print("Printing values:")
    for i in args:
        print(i)
#   Call 1
func1(20, 40, 60)
#   Call 2
func1(80, 100)

#
#   3. Return Multiple Values from a Function
#
def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub

add, sub = calculation(40, 10)
print(add)
print(sub)

#
#   4. Function with Default Argument
#
def show_employee(name, salary=9000):
    print("Name :", name, "| Salary :", salary)

#   Call 1
show_employee("Ben", 12000)
#   Call 2
show_employee("Jess")

#
#   5. Create an Inner Function
#
def outter(a, b):

    def inner(a, b):
        return a + b
    
    add = inner(a, b)
    return add + 5

result = outter(5, 10)
print(result)

#
#   6. Create a Recursive Function
#
def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0

result = addition(10)
print(result)

#
#   7. Assign a Different Name to Function and Call It
#
def display_student(name, age):
    print(name, age)

show_student = display_student

show_student("Emma", 26)

#
#   8. Generate a List of Even Numbers (Range Function)
#
def even_num():
    return list(range(4, 30, 2))

print(even_num())

#
#   9. Find the Largest Item in a List
#
def max(x_list):
    largest = x[0]
    for num in x_list:
        if num > largest:
            largest = num
    return largest

x = [4, 6, 8, 24, 12, 2]
print(max(x))

#
#   10. Call Function using Positional and Keyword Arguments
#
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

#   Call 1
describe_pet("hamster", "Harry")
#   Call 2
describe_pet(animal_type="dog", pet_name="Willie")

#
#   11. Create a Function with Keyword Arguments
#
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name="Alice", age=30, city="New York")

#
#   12. Modifying Global Variables
#
global_var = 10

def modify():
    global global_var
    global_var = 20

print("Initial:", global_var)
modify()
print("Modified:", global_var)

#
#   13. Recursive Factorial (Non-Negative Integers)
#
def factorial(n):
    if n <= 1:
        return  1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")

#
#   14. Create a Lambda Function to Square a Number
#
square = lambda x: x**2

print(square(5))

#
#   15. Filter a List Using Lambda and filter()
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = list(filter(lambda x: x % 2 == 0, numbers))

print(filtered)

#
#   16. Transform a List Using Lambda and map()
#
numbers = [1, 2, 3, 4, 5]
double = list(map(lambda x: x * 2, numbers))

print(double)

#
#   17. Sort Complex Data with sorted() and Lambda
#
students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)

#
#   18. Create a Higher-Order Function
#
def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(add, 5, 3)
result2 = apply_operation(multiply, 5, 3)

print("Addition result:", result1)
print("Multiplication result:", result2)