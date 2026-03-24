#
# 1. Arithmetic operators.
#    Addition, subtraction, multiplication, division and modulus. 
#
num_1 = 10
num_2 = 5

print(f"Addition: {num_1 + num_2}")
print(f"Subtraction: {num_1 - num_2}")
print(f"Multiplication: {num_1 * num_2}")
print(f"Divison: {num_1 / num_2}")
print(f"Modulus: {num_1 % num_2}")

#
# 2. Comparison operators.
#    Compare two values which returns a boolean.
#
a = 10
b = 5

print(f"Greater than: {a > b}")
print(f"Less than: {a < b}")
print(f"Equals to: {a == b}")
print(f"Not equal: {a != b}")
print(f"Greater than and equal to: {a >= b}")
print(f"Less than and equal to: {a <= b}")

#
# 3. Logical operators.
#    Use 'and', 'or' and 'not' to evaluate two expressions. 
#    Returns a boolean value.
#
first = True
second = False

print(f"True 'and' False: {first and second}")
print(f"True 'or' False: {first or second}")
print(f"First not: {not first}")
print(f"Second not: {not second}")

#
# 4. Assignment operators.
#    Used to modify or assign values of a variable. 
#
x = 10
print(f"Initial value: {x}")

x += 5
# becomes result = x + 5
print(f"After += : {x}")

x -= 3
# becomes result = x - 3
print(f"After -= : {x}")

x *= 2
# becomes result = x * 2
print(f"After *= : {x}")

x /= 3
# becomes result = x / 3
print(f"After /= : {x}")

x %= 2
# becomes result = x % 5
print(f"After %= : {x}") 

#
# 5. Bitwise operators.
#    Use AND, OR, XOR, Left Shift and Right Shift to compare binary numbers. 
#
b_1 = 5
b_2=  3

print(f"{b_1} & {b_2} = {b_1 & b_2}") # AND
print(f"{b_1} | {b_2} = {b_1 | b_2}") # OR
print(f"{b_1} ^ {b_2} = {b_1 ^ b_2}") # XOR
print(f"{b_1} << 1 = {b_1 << 1}") # Left Shift
print(f"{b_1} >> 1 = {b_1 >> 1}") # Right Shift
print(f"{b_2} << 1 = {b_2 << 1}") # Left Shift
print(f"{b_2} >> 1 = {b_2 >> 1}") # Right Shift