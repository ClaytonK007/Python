#
#   1. Create a string made of the first, middle, and last character
#
str1 = "James"
print("Original string:", str1)

first_char = str1[0]

middle_index = int(len(str1) / 2)
middle_char = str1[middle_index]

last_char = str1[-1]

result = first_char + middle_char + last_char

print("New string:", result)

#
#   2. Create a string made of the middle three characters
#
str1 = "JohnJimJack"
print("Original string:", str1)

middle_index = int(len(str1) / 2)
result = str1[middle_index - 1:middle_index + 2]

print("New string:", result)

#
#   3. Append new string in the middle of a given string
#
str1 = "Jones"
str2 = "Kelly"
print("Original string 1:", str1)
print("Original string 2:", str2)

middle_index = int(len(str1) / 2)
result = str1[:middle_index] + str2 + str1[middle_index:]

print("New string:", result)


#
#   4. Create a new string made of the first, middle, and last characters of each input string
#
str1 = "South Africa"
str2 = "Ireland"
print("Original string 1:", str1)
print("Original string 2:", str2)

first_1 = str1[0]
middle_char_1 = str1[int(len(str1) / 2)]
last_1 = str1[-1]

first_2= str2[0]
middle_char_2 = str2[int(len(str2) / 2)]
last_2 = str2[-1]

result = first_1 + first_2 + middle_char_1 + middle_char_2 + last_1 + last_2

print("New string:", result)

#
#   5. Reverse a given string
#
str1 = "Python"
print("Original string 1:", str1)

reversed_str = str1[::-1]

print(reversed_str)

#
#   6. Find the last position of a given substring
#
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original string 1:", str1)

sub_str = str1.rfind("Emma")

print("The last occurance of 'Emma' starts at index:", sub_str)

#
#   7. Split a string on hyphens
#
str1 = "Emma-is-a-data-scientist"
print("Original string 1:", str1)

split_str = str1.split("-")

print("Each substring:")
for string in split_str:
    print(string)

#
#   8. Find all occurrences of a substring in a given string by ignoring the case
#
str1 = "Welcome to USA. usa awesome, isn't it?"
print("Original string 1:", str1)

change = str1.lower()

occurance = change.count("usa")

print("The USA count is:", occurance)

#
#   9. Vowel Counter
#
str1 = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for string in str1:
    if string in vowels:
        count += 1

print("Vowel Count:", count)