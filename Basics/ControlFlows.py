#
# 1. Basic 'if' statement. 
#
var_1 = 24
var_2 = 100

if var_1 < var_2:
    print("Variable 1 is less than variable 2.")

#
# 2. Basic 'if-else' statement. 
#
var_1 = 24
var_2 = 100

if var_1 > var_2:
    print("Variable 1 is less than variable 2.")
else:
    print("Variable 2 is greater than variable 1.")

#
# 3. Check if a number is Odd or Even using an 'if' and 'else' statement.
#    Use the input() function to ask user for a number. 
#
number = int(input("Enter a number: "))

if number % 2 == 0: # divisible by 2 and no remainder
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#
# 4. Find the largest number using an 'if', 'elif' and 'else' statements.
#    Use the input() function to ask user for 3 numbers. 
#    The map() function applies to each object. 
#    The split() function turns a string (input objects) into a list.
#
a, b, c = map(int, input("Enter three numbers (separate by spaces eg. 3 6 9 ): ").split())

if a >= b and a >= c:
    print(f"The largest number is {a}.")
elif b >= a and b >= c:
    print(f"The largest number is {b}.")
else:
    print(f"The largest number is {c}.")

#
# 5. Count numbers from 1 to N. 
#    Use the input() function to ask user for a number. 
#    Use a for loop and range(start, stop) function to count.
#    
num = int(input("Enter a number: "))

for count in range(1, num + 1):
    print(count, end = ", ")

#
# 5. Count all even numbers from 2 to N. 
#    Use the input() function to ask user for a number. 
#    Use a for loop and range(start, stop, step) function to count.
#    
num = int(input("Enter a number: "))

for count in range(2, num +1, 2):
    print(count, end = ", ")

#
# 6. Sum of the first natural numbers of N (arithmetic series of number).
#    Use the input() function to ask user for a number. 
#    Use a for loop and range(start, stop) function to count.
#  
num = int(input("Enter a number: "))
sum = 0 # initialize variable which is then used to accumulate total sum

for count in range(1, num + 1):
    sum += count

print(f"The sum of the first {num} numers: {sum}")

#
# 7. Facorial of a number.
#    Use the input() function to ask user for a number. 
#    Use a for loop and range(start, stop) function.
#  
num = int(input("Enter a number: "))
factorial = 0 # initialize variable to store the factorial

for count in range(1, num + 1):
    factorial *= count

print(f"The factorial of {num} is: {factorial}")

#
# 7. Reverse a number.
#    Use the input() function to ask user for a number. 
#    Use a while loop to execute aslong as condition is true.
#  
num = int(input("Enter a number: "))
reverse = 0 # initialize variable 

while num > 0:
    digit = num % 10 # to extract last digit of number
    reverse = reverse * 10 + digit # extract digits from right to left
    num //= 10

print(f"The reversed number is: {reverse}")

#
# 7. Multiplication table up to 10.
#    Use the input() function to ask user for a number. 
#    Use a for loop and range(start, stop) function.
#  
num = int(input("Enter a number: "))

for count in range(1, 11):
    print(f"{num} * {count} = {num * count}")

#
# 8. Count number of digits in a number.
#    Use the input() function to ask user for a number. 
#    Use a while loop.
#  
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num //= 10
    count += 1
print(f"The number '{num}' has {count} digits.")