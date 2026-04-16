#      List Comprehension
#   1. Create a list of strings, filter out words than have less than 4 characters and return
#      remaining string to uppercase.
#
words = ["apple", "bat", "cherry", "dog", "elderberry"]
filtered_words = [w.upper() for w in words if len(w) >= 4 ]

print(f"Orginal list: {words}")
print(f"Filtered list: {filtered_words}")

#      Dictionary Merging with Logic
#   2. Merge two dictionaries without overwriting duplicate keys. 
#
def merge_dictionary(d1, d2):
    merge = d1.copy()

    for key, value in d2.items():
        merge[key] = merge.get(key, 0) + value
    return merge

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

result = merge_dictionary(dict_a, dict_b)
print(f"Merged dicitonary: {result}")

#      Frequency Map with Counter
#   3. Count the number of characters in a string. Import Counter from collections module.
#
from collections import Counter

def frequency(input):
    freq = input.lower().replace(" ", "")

    return Counter(freq)

string = "Python Programming"
count = frequency(string)

print(f"Original text: {string}")
print(f"Character frequency: {count}")

#      Anagram Checker
#   4. Check if two strings are anagrams.
#
def anagram(s1, s2):
    str1 = sorted(s1.lower().replace(" ", ""))
    str2 = sorted(s1.lower().replace(" ", ""))

    return str1 == str2

string1, string2 = "listen", "silent"
result = anagram(string1, string2)

print(f"Is '{string1}' an anagram of '{string2}': {result}")

#      Flatten a Nested List
#   5. Convert a multidimensional or nested list into a flat list.
#
def flatten(l_ist):
    flat_list = []

    for item in l_ist:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list

nested = [1, [2, 3], [4, [5, 6]], 7]
result = flatten(nested)

print(f"Orgiinal nested list: {nested}")
print(f"Flattened list: {result}")

#      Reverse Each Word of a String
#   6. Reverse words in a sentence and keep original word order.
#
def reverse(sentence):
    words = sentence.split()
    reverse_words = [word[::-1] for word in words]

    return " ".join(reverse_words)

text = "Learning Python is fun and awesome"
result = reverse(text)

print(f"Original sentence: '{text}'")
print(f"Reversed sentence: '{result}'")

#      Dictionary Sorting (Lambda)
#   7. Sort a dicitonary, finding the highest to lowest using lambda.
#
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 70000},
    {"name": "Charlie", "salary": 60000}
]

sort_emp = sorted(employees, key=lambda x: x['salary'], reverse=True)

for emp in sort_emp:
    print(emp)

#      Subset and Superset Validation
#   8. Take two lists, turn them into sets and determine if they are a superset
#      or subset or disjoint. 
#
def validation(list1, list2):
    a = set(list1)
    b = set(list2)

    if a.issubset(b):
        print("Set A is a subset of B.")
    elif a.issuperset(b):
        print("Set A is a superset of B.")

    if a.isdisjoint(b):
        print("Sets are disjoint because they share no common elements.")
    else:
        print(f"The sets share these elements: {a & b}")

validation([1, 2, 3], [1, 2, 3, 4, 5])

#      Set Symmetric Difference
#   9. Find exclusive ids in a list which are not in both lists.  
#
def exclusive_ids(ids1, ids2):
    set1 = set(ids1)
    set2 = set(ids2)

    return set1 ^set2

jan_visitors = [101, 102, 103, 104]
feb_visitors = [103, 104, 105, 106]

exclusive = exclusive_ids(jan_visitors, feb_visitors)
print(f"Visitors exclusive to one month: {exclusive}")

#       Power Set Generation
#   10. Generate a power set of a given set - all possible subsets of the given set
#
from itertools import combinations

def powerset(s):
    elements = list(s)
    power_set = []

    for r in range(len(elements) + 1):
        for combo in combinations(elements, r):
            power_set.append(combo)
            
    return power_set

set = {1, 2, 3}
print(f"Power Set: {powerset(set)}")

#       Age Calculator (Exact)
#   11. Calculate exact age in years, months and days.
#
from datetime import datetime
from dateutil.relativedelta import relativedelta

def exact_age(bday_string):
    try:
        birthdate = datetime.strptime(bday_string, "%Y-%m-%d").date()
        today = datetime.now().date()

        diff = relativedelta(today, birthdate)

        return f"{diff.years} years, {diff.months} months, {diff.days} days"
    except ValueError:
        return "Invalid date format. Please try YYYY-MM-DD"


age = exact_age("1994-9-15") 
print(f"Exact age: {age}")