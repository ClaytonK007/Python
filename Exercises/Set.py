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