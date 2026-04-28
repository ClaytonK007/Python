#
#   1. Print first 10 natural numbers using while loop
#
for i in range(1, 11):
    print(i)

#   OR
i = 1

while i <= 10:
    print(i)
    i += 1

#
#   2. Display numbers from -10 to -1 using for loop
#
for i in range(-10, 0):
    print(i)

#
#   3. Display a message “Done” after successful execution of for loop
#
for i in range(5):
    print(i)
else:
    print("Done!")

#
#   4. Calculate the sum of all numbers from 1 to N
#
n = 10
s = 0

for i in range(1, n + 1):
    s += i

print("Sum of all natural numbers:", s)

#
#   5. Print multiplication table of a given number
#
num = 2

for i in range(1, 11):
    product = num * i

    print(product)

#
#   6. Calculate the cube of all numbers from 1 to a given number
#
num = 6

for i in range(1, num + 1):

    print(f"Current number: {i} , the cube thereof: {i ** 3}")

#
#   7. Display numbers from a list using a loop with specific conditions
#
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break

    if i > 150:
        continue

    if i % 5 == 0:
        print(i)

#
#   8. Count occurrences of a specific element in a list
#
list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0

for num in list1:
    if num == target:
        count += 1

print(f"{target} appears {count} times.")

#
#   9. Print elements from a list present at odd index positions
#
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1, len(my_list), 2):
    print(my_list[i], end=" ")

#
#   10. Print list in reverse order using a loop
#
list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)

#   OR
list1 = [10, 20, 30, 40, 50]
rev_list = len(list1) - 1

for i in range(rev_list, -1, -1):
    print(list1[i])

#
#   11. Reverse a string using a for loop (no slicing)
#
string = "I love learing Python!"
rev_string = ""

for char in string:
    rev_string = char + rev_string

print(f"Original string: {string}")
print(f"Reversed string: {rev_string}")

#
#   12. Count vowels and consonants in a sentence
#
string = "Loops are Fun!"
vowels = "aeiou"
v = 0
c = 0

for char in string.lower():
      if char.isalpha():
            if char in vowels:
                  v += 1
            else:
                  c += 1
print("Vowels:", v)
print("Consonants:", c)

#
#   13. Count total number of digits in a number
#
num = 75869
count = 0

while num != 0:
    num //= 10
    count += 1

print("Total number of digits:", count)

#
#   14. Reverse an integer number
#
num = 75869
reversed_num = 0
print("Original number:", num)

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed number:", reversed_num)

#
#   15. Find largest and smallest digit in a number
#
num = 75869
print("Original number:", num)
largest = 0
smallest = 9


while num > 0:
    digit = num % 10
    largest = max(digit, largest)
    smallest = min(digit, smallest)
    num //= 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)

# OR

num = 75869
print("Original number:", num)
largest = 0
smallest = 9

while num > 0:
      digit = num % 10

      if digit > largest:
            largest = digit
      
      if digit < smallest:
           smallest = digit

      num //= 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)

#
#   16. Check if a number is a palindrome
#
num = 121
print("Original number:", num)
temp = num
check = 0


while num > 0:
    digit = num % 10
    check = (check * 10) + digit
    num //= 10

if temp == check:      
      print("Yes, number is palindrome.")
else:
      print("No, number is not palindrome.")

#
#   17. Find factorial of a number
#
num = 5
factorial = 1

if num < 0:
      print("Factorial does not exist for negative numbers.")
elif num == 0:
      ("Factorial of 0 is 1.")
else:
      for i in range(1, num + 1):
            factorial = factorial * i
      print(f"The factorial of {num} is {factorial}")  

#
#   18. Collatz Conjecture: Generate a sequence until it reaches 1
#
num = 6
print(num, end="")

while num != 1:
      if num % 2 == 0:
            num = num // 2
      else:
            num = (3 * num) + 1
      print(f", {num}", end="")

#
#   19. Armstrong Number Check
#
num = 153
num_to_str = str(num)
power = len(num_to_str)
total = 0

for digit in num_to_str:
    total += int(digit) ** power

if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#
#   20. Print right-angled triangle Number Pattern using a Loop
#
print("Number pattern:")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#
#   21. Print the decreasing pattern
#
n = 5

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

#
#   22. Print the alternate numbers pattern
#
for i in range(1, 21, 2):
    print(i, end=" ")

#
#   23. Print Alphabet pyramid (A, BB, CCC) pattern
#
for i in range(5):
    letter = chr(65 + i)
    for j in range(i + 1):
        print(letter, end=" ")
    print()

#
#   24. Hollow square pattern
#
for i in range(5):
      for j in range(5):
            if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1:
                  print("*", end=" ")
            else:
                  print(" ", end=" ")
        
      print()

#
#   25. Print pyramid pattern of stars
#
for i in range(1, 5 + 1):
    print("*" * i)
for i in range(5 - 1, 0, -1):
    print("*" * i)

#
#   26. Print full multiplication table (1 to 10)
#
for i in range(1, 11):
      for j in range(1, 11):
            print(i * j, end="\t")

      print()

#
#   27. List Cumulative Sum: Each element is the sum of all previous
#
nums = [1, 2, 3, 4]
sum = 0
result = []

for num in nums:
    sum += num
    result.append(sum)

print("Cumulative Sum:", result)

#
#   28. Dictionary Filter: Extract pairs where value exceeds a threshold.
#
scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
threshold = 75

filtered = {k: v for k, v in scores.items() if v > threshold}

print("Passing Students:", filtered)

#     OR
scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
threshold = 75
passing = {}

for name, score in scores.items():
    if score >= threshold:
        passing[name] = score
print(f"Passing Students:", passing)

#
#   29. Find common elements (Intersection) using loop
#
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
intersection = []

for i in list_a:
    for j in list_b:
        if i == j:
            if i not in intersection:
                intersection.append(i)

print(intersection)

#
#   30. Remove duplicates without set
#
nums = [1, 2, 2, 3, 4, 4, 4, 5]
unique = []

for num in nums:
    if num not in unique:
       unique.append(num)

print("Unique list:", unique)