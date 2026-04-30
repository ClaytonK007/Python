#
#   1. Basic Tuple Operations
#
fruits = ("apple", "banana", "cherry", "date")
print("Original tuple:", fruits)

print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Length:", len(fruits))

#
#   2. The Trailing Comma
#
tup = (50,)
print("Original tuple:", tup)

print("Type:", type(tup))

#
#   3. Tuple Repetition
#
colors = ("red", "green")
print("Original tuple:", colors)

print("Repeated 3 times:", (colors * 3))

#
#   4. Tuple Concatenation
#
a = (1, 2)
b = (3, 4)
c = (5, 6)
print("Original tuple A:", a)
print("Original tuple B:", b)
print("Original tuple C:", c)

joined = a + b + c

print("Concatenated:", joined)

#
#   5. Tuple Slicing
#
numbers = (10, 20, 30, 40, 50, 60, 70)
print("Original tuple:", numbers)

print("Tuple slicing:", numbers[2:5])

#
#   6. Tuple Reversal
#
items = (1, 2, 3, 4, 5)
print("Original tuple:", items)

print("Reversed tuple:", items[::-1])

#
#   7. Type Casting
#
my_list = [10, 20, 30, 40, 50]
print("Original tuple:", my_list)

tup = tuple(my_list)

print("Converted list to tuple:", tup)
print("Data type:", type(tup))

#
#   8. Tuple to String
#
chars = ('a', 'b', 'c')
print("Original tuple:", chars)

string = "".join(chars)

print("Converted tuple to list:", string)

#
#   9. Tuple Membership Testing
#
fruits = ("apple", "banana", "cherry", "date")
print("Original tuple:", fruits)

print("cherry" in fruits)
print("mango" in fruits)

#
#   10. Counting
#
votes = ("yes", "no", "yes", "yes", "no", "yes")
print("Original tuple:", votes)

print("Number of 'yes' votes:", votes.count("yes"))
print("Number of 'no' votes:", votes.count("no"))

#
#   11. Tuple Unpacking
#
person = ("Alice", 30, "Engineer", "Pune")

name, age, job, city = person

print("Name:", name)
print("Age:", age)
print("Job:", job)
print("City:", city)

#
#   12. The Swap Trick
#
a = 100 
b = 200
print("Before swap: a=", a, "& b=", b)

a, b = b, a
print("After swap: a=", a, "& b=", b)

#
#   13. Nested Tuple Access
#
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print("Nested tuple access:", matrix[1][2])

#
#   14. Tuple Statistics
#
scores = (88, 95, 70, 62, 99, 74, 85)

print("Sum  of tuple:", sum(scores))
print("Max of tuple:", max(scores))
print("Min of tuple:", min(scores))

#
#   15. Tuple Filtering
#
numbers = (3, 14, 7, 22, 9, 41, 18, 5)

print("Filtered:", [x for x in numbers if x > 10])

#   OR

filtered = list(filter(lambda x: x > 10, numbers))

print("Filtered:", filtered)

#
#   16. Tuple Mapping
#
numbers = (1, 2, 3, 4, 5, 6)

def square(n):
    return n ** n

squared_map1 = tuple(map(square, numbers))
squared_map2 = tuple(map(lambda x: x ** 2, numbers))
squared_exp  = tuple(x ** 2 for x in numbers)

print("Squared (mapping with function):", squared_map1)
print("Squared (mapping with lambda):", squared_map2)
print("Squared (with expression:", squared_exp)

#
#   17. Tuple Dictionary Mapping
#
keys = ("name", "age", "city") 
values = ("Alice", 30, "Pune")

dictionary = dict(zip(keys, values))
dictionary1 = {keys: values for keys, values in zip(keys, values)}

print("Dictionary mapping (zip):", dictionary)
print("Dictionary mapping (expression):", dictionary1)

#
#   18. Tuple Intersection
#
t1 = (1, 2, 3, 4, 5, 6) 
t2 = (4, 5, 6, 7, 8, 9)

common = tuple(sorted(set(t1) & set(t2)))
common_exp = tuple(x for x in t1 if x in t2)

print("Common elements (conversion method):", common)
print("Common elements (expression method):", common_exp)

#
#   19. The “Modification” Hack
#
colours = ("red", "green", "blue")
print("Original tuple:", colours)

change = list(colours)
change[1] = "yellow"

colours = tuple(change)
print("Modified tuple:", colours)

#
#   20. Tuple Mutability
#
t = (1, 2, [3, 4, 5])
print("Original tuple:", t)
print("Tuple id before:", id(t))

t[2].append(99)

print("Appended tuple:", t)
print("Tuple id after:", id(t))

print("Same object?:", id(t) == id(t))