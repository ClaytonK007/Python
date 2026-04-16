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