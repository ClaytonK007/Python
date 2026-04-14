#      Arithmetic Product and Conditional Logic
#   1. Write a function that takes two integer values. if the product of the two numbers 
#      are less than or equal to 1000 return the result, else return the sum. Case 1 num1 = 20 
#      & num2 = 30, Case 1 num1 = 40 & num2 = 30 
#
def prod_or_sum(num1, num2):
    answer = num1 * num2

    if answer <= 1000:
        return answer
    else:
        return num1 + num2
    
case1 = prod_or_sum(20, 30)
print("result is:", case1)

case2 = prod_or_sum(40, 30)
print("result is:", case2)

#      Cumulative Sum of a Range
#   2. Iterate through first ten numbers. Print current number, previous number and their sum. 
#      Initialize the count. Use a for loop to increment range 0 - 9. Update the counter inside 
#      the loop.
#
print("Printing current number, previous number and their sum.")

prev_num = 0

for i in range(10):
    sum = prev_num + i
    print(f"Current num : {i}, Previous num : {prev_num} and their Sum : {sum}")
    
    prev_num = i

#      String Indexing and Even Slicing
#   3. From the string pynative, only print the letters which an in an even index number.
#      Use list slicing method (start, stop, step). Use a for loop to iterate through each
#      letter.
#
string = "pynative"
print("Original string is", string)

even = string[0::2]

print("Now printing only letters in even index")
for letters in even:
    print(letters)

#      String Slicing and Substring Removal
#   4. Write a function that removes characters from a string and return a new string.
#      Extract from given index start to the end.Return "tive" and "native".
#
def remove(string, n):
    print("Original string:", string)
    result = string[n:]
    return result

print("Removing from string:")
print(remove("pynative", 4))
print(remove("pynative", 2))

#      List Comparison and Boolean Logic
#   5. Write a function that returns true if the first and last index values are 
#      the same and false if they are differet.
#
def the_same(num_list):
    print("The given list: ", num_list)

    first = num_list[0]
    last = num_list[-1]

    if first == last:
        return True
    else:
        return False
    
list1 = [20, 10, 40, 30, 20]
print("result is", the_same(list1))

list2 = [75, 30, 25, 75, 70]
print("result is", the_same(list2))

#      Filtering Lists with Conditional Logic
#   6. Iterate through a list of numbers and print only numbers divisible by 5.
#
num_list = [10, 20, 33, 46, 55]
print("List is:", num_list)
print("Values divisible by 5:")

for num in num_list:
    if num % 5 == 0:
        print(num)

#      Merging Lists with Parity Filtering
#   7. Merge 2 lists only keeping the odd values from the first and even from the second.
#
def merge_list(list1, list2):
    result_list = []

    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)

    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("reult list:", merge_list(list1, list2))        

#      Integer Digit Extraction and Reversal
#   8. Extract the digits in a number and return it in reverse order.
#
num = 98765
print("List of numbers:", num)

print("Number in reverse: ")
while num > 0:
    digit = num % 10
    num = num // 10

    print(digit, end="") 

#      Nested Loops for Multiplication Tables
#   9. Create a formatted grid with a multiplication table. 
#
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")

    print("\n")

#       Multi-Tiered Income Tax Calculation
#   10. Calculate income tax based on three rules: first 10000 0%, next 10000 10%, remaning at 20%.
#
income = 45000
tax = 0
print("Income: ", income)

if income <= 10000:
    tax = 0
elif income <= 20000:
    tax = (income - 10000) * 0.1
else:
    tax = 0 + (10000 * 0.1)
    tax += (income - 20000) * 0.2

print(f"Total incometax: {tax:.2f}")

#       Generate Fibonacci Series
#   11. Print first 15 number of Fibonacci series with start being 0 and 1
#
num1, num2 = 0, 1
print("Fibonacci Series:")

for i in range(15):
    print(num1, end=" ")

    res = num1 + num2

    num1 = num2
    num2 = res

#       Capitalize First Letter
#   12. Capitilize the first letters of a strong wihtout the title method.
#
string= "i love learning python, it's really fun!"

text = string.split()
caps = []

for word in text:
    caps.append(word.capitalize())

result = " ".join(caps)
print(result)

#       Digit Detection in Strings
#   13. Check if a string contains any numeric digits.
#
input = "3Python3"
contain_digits = False

for char in input:
    if char.isdigit():
        contain_digits = True
        break

print(f"Input : {input}, contains digits:  {contain_digits}")
