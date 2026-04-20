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