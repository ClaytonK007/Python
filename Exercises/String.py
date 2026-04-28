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

#
#   10. Prefix/Suffix Check
#
str1 = "https://google.com"

if str1.startswith("https") and str1.endswith(".com"):
    print("Is valid URL: True")
else:
    print("Is valid URL: False")

#
#   11. Swap Case
#
str1 = "PyThOn"
swap = str1.swapcase()

print(swap)

#
#   12. Remove Whitespace
#
str1 = " P y t h o n "
modified = str1.replace(" ", "")

print(modified)

#
#   13. N-th Character Removal
#
str1 = "Python"
i = 2

first = str1[:i]
second = str1[i + 1:]

result = first + second
print("After removing index", i, ":", result)

#
#   14. String Partitioning
#
str1 = "username@company.com"

modified = str1.partition("@")

print("Original string:", str1)
print("Partitioned result:", modified)
print("Username:", modified[0])

#
#   15. Extract File Extension
#
file_name = "report_final_v2.pdf"
modified = file_name.split(".")[-1]

print("File name:", file_name)
print("Extension:", modified)

#
#   16. Lowercase First
#
str1 = "PyNaTive"
lower = []
upper = []

for char in str1:
      if char.islower():
            lower.append(char)
      else:
            upper.append(char)

result = "".join(lower + upper)
print("Result:", result)

#
#   17. Count all letters, digits, and special symbols from a given string
#
def count(string):
      char_count = 0
      digit_count = 0
      symbol_count = 0

      for char in string:
            if char.isalpha():
                  char_count += 1
            elif char.isdigit():
                  digit_count += 1
            else:
                  symbol_count += 1

      print(f"Total count, Characters: {char_count}, Digits: {digit_count}, Symbols: {symbol_count}")

count("P@#yn26at^&i5ve")

#
#   18. Create a mixed string using alternating characters
#
s1 = "Abc" 
s2 = "Xyz"

s1_len = len(s1)
s2_len = len(s2)

length = s1_len if s1_len > s2_len else s2_len
result = ""

s2 = s2[::-1]

for i in range(length):
      if i < s1_len:
            result = result + s1[i]
      if i < s2_len:
            result = result + s2[i]

print(result)

#
#   19. Calculate the sum and average of the digits present in a string
#
str1 = "PYnative29@#8496"
total_sum = 0
count = 0

for char in str1:
    if char.isdigit():
        total_sum += int(char)
        count += 1

average = total_sum / count
print("Sum is:", {total_sum} ,"Average:", {average})