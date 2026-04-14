#      List Comprehension
#   1. Create a list of strings, filter out words than have less than 4 characters and return
#      remaining string to uppercase.
#
words = ["apple", "bat", "cherry", "dog", "elderberry"]
filtered_words = [w.upper() for w in words if len(w) >= 4 ]

print(f"Orginal list: {words}")
print(f"Filtered list: {filtered_words}")