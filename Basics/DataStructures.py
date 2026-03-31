#
# 1. Create a list and add an item. 
#    Add an item using the apend() function
#
list = ["Dog", "Cat", "Bird"]
list.append("Fish")

print(list)

#
# 2. Sort a list in ascending order. 
#    Add an item using the sort() function
#
list_1 = ["Dog", "Fish", "Cat", "Bird"]
list_2 = [45, 62, 32, 81, 77, 100]

list_1.sort()
list_2.sort()

print(list_1)
print(list_2)

#
# 3. Find highest value in a list using the max() function.
#
numbers = [123, 546, 321, 432, 101]
max_num = max(numbers)

print(f"The highest value is: {max_num}")

#
# 4. Count frequency a word is used in a sentence.
#    Use the split() and get() function to count.
#
sentence = "Learning Python is great. Learning Python is fun too."
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

#
# 5. Find common elements is two sets using the & comparison operator. 
#
set_one = {"Ted", "Marshall", "Robin", "Barney"}
set_two = {"Bob", "Robin", "Lilly", "Ted"}

common = set_one & set_two
print(common)

#
# 6. Find most requent value in a dictionary using the max() and get() function. 
#
numbers = [12, 32, 12, 45, 65, 12, 78, 12, 101, 12]
num_count = {}

for num in numbers:
    num_count[num] = num_count.get(num, 0) + 1

most_frequent = max(num_count, key=num_count.get)

print(f"Most frequent value: {most_frequent}")

#
# 7. Merge two dictionaries using **kwargs
#
dict_1 = {"Keyboards": 8, "Mice": 12}
dict_2 = {"Laptops": 10, "Monitors": 5}

merg = {**dict_1, **dict_2}

print(merg)

#
# 8. Remove duplicates from a list.
#
product_ids = [101, 102, 103, 101, 104, 102]
names = ["Ted", "Alan", "Jim", "Ted", "Barney", "Fred", "Marshall", "Barney"]

unique_products = list(set(product_ids))
unique_names = list(set(names))

print(f"Unique product IDs: {unique_products}")
print(f"Unique names: {unique_names}")

#
# 9. Remove item from a dictionary.
#
items = {20, 34, 84, 101, 99, 69}
remove = {34, 99}
new = items - remove

print(new)