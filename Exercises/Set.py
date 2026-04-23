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