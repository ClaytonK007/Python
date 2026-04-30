#
#   1. Basic Set Operations
#
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)


fruits.add("mango")
print("After adding:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits.discard("grape")
print("After discard of an element not present:", fruits)

#
#   2. Clear All Elements
#
colors = {"red", "green", "blue"}
print("Original set:", colors)

colors.clear()

print("After clear:", colors)

#
#   3. Find the Length of a Set
#
animals = {"cat", "dog", "bird", "fish"}
print("Original set:", animals)

count = 0

for set in animals:
    count += 1

print("Length of set", count)

#
#   4. Check if a Set is Empty
#
data = set()
print("Original set:", data)

if not data:
    print("Set is empty.")
else:
    print("Set is not empty.")

#
#   5. Union of Sets
#
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Original set A:", set_a)
print("Original set B:", set_b)

union = set_a | set_b

print("Union:", union)

#
#   6. Intersection of Sets
#
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Original set A:", set_a)
print("Original set B:", set_b)

intersection = set_a & set_b

print("Intersection:", intersection)

#
#   7. Difference of Sets
#
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Original set A:", set_a)
print("Original set B:", set_b)

difference = set_a - set_b

print("Difference of A and B:", difference)

#
#   8. Symmetric Difference
# 
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Original set A:", set_a)
print("Original set B:", set_b)

symmetric = set_a ^ set_b

print("Symmetric difference of A and B:", symmetric)

#
#   9. Find Max and Min
#
numbers = {42, 7, 19, 85, 3, 56}
print("Original set:", numbers)

print("Max:", max(numbers))
print("Min:", min(numbers))

#
#   10. Sum of Set Elements
#
numbers = {10, 20, 30, 40, 50}
print("Original set:", numbers)

total = 0

for num in numbers:
    total += num

print("Sum of numbers:", total)

#   OR
numbers = {10, 20, 30, 40, 50}
print("Original set:", numbers)

print("Sum of numbers:", sum(numbers))

#
#   11. Add a List of Elements
#
fruits = {"apple", "banana"} 
new_fruits = ["cherry", "mango", "apple"]

fruits.update(new_fruits)
print("List added to set:", fruits)

#
#   12. Update with Multiple Iterables
#
base = {1, 2}
from_list = [3, 4]
from_tuple = (5, 6)
from_set = {7, 8}

base.update(from_list, from_tuple, from_set)
print("List added to set:", base)

#
#   13. Check Subset and Superset
#
set_a = {1, 2, 3} 
set_b = {1, 2, 3, 4, 5}

sub = set_a.issubset(set_b)
super = set_b.issuperset(set_a)
print("Is set_a a subset of set_b?:", sub, "and is set_b a superset of set_a?:", super)

#
#   14. Intersection Check with isdisjoint()
#
set_a = {1, 2, 3} 
set_b = {4, 5, 6}

print("Are sets disjoint?:", set_a.isdisjoint(set_b))

#
#   15. Set Difference Update
#
a = {1, 2, 3, 4, 5} 
b = {3, 4, 5, 6, 7}

a.difference_update(b)
print("Set difference update:", a)

#
#   16. Set Intersection Update
#
a = {1, 2, 3, 4, 5} 
b = {3, 4, 5, 6, 7}

a.intersection_update(b)
print("Set intersection:", a)

#
#   17. Set Symmetric Difference Update
#
a = {1, 2, 3, 4, 5} 
b = {3, 4, 5, 6, 7}

a.symmetric_difference_update(b)
print("Set symmetric difference:", a)

#
#   18. Remove Items Simultaneously
#
items = {10, 20, 30, 40, 50, 60} 
to_remove = {20, 40, 60}

items.difference_update(to_remove)
print("Items removed simultaneously:", items)

#
#   19. The Pop Operation
#
s = {100, 200, 300}
popped = s.pop()
print("Popped:", popped)

s = set()
try:
    s.pop()
except KeyError as e:
    print("Error:", e)

#
#   20. Filter a Set
#
numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}
print("Original set:", numbers)

filtered = {x for x in numbers if x % 3 == 0}

print("Set values divisible by 3:", filtered)

#
#   21. Find Common Elements in Lists
#
list1 = [1, 2, 3, 4, 5, 3, 2] 
list2 = [3, 4, 5, 6, 7, 4, 5]

set_1 = set(list1)
set_2 = set(list2)

common = set_1 & set_2

print("Common elements (& method):", common)
print("Common elements (intersection method):", set_1.intersection(set_2))