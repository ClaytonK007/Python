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