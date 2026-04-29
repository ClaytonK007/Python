#
#   1. Perform Basic List Operations 
#
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

print("Third element in list:", numbers[2])
print("Length of list:", len(numbers))

empty = len(numbers) == 0
print("Is list empty:", empty)

#
#   2. Perform List Manipulation
#
initial_list = [100, 50, 400, 500]
print("Original list:", initial_list)

initial_list[1] = 200
print("Updated list (change):", initial_list)

initial_list.append(600)
print("Updated list (append):", initial_list)

initial_list.insert(2, 300)
print("Updated list (insert):", initial_list)

initial_list.remove(600)
print("Updated list (remove by value):", initial_list)

initial_list.pop(0)
print("Updated list (remove by index):", initial_list)

#
#   3. Sum and Average of All Numbers in a List
#
numbers = [10, 20, 30, 40, 50]

sum_num = sum(numbers)
average = sum_num / len(numbers)

print("Original list:", numbers)
print("Sum of numbers:", sum_num)
print("Average of list of numbers:", average)

#
#   4. Find Maximum and Minimum from List
#
data = [45, 12, 89, 2, 67]

print("Original list:", data)
print("Maximun:", max(data))
print("Minimum:", min(data))

#
#   5. Calculate the Product of All Elements
#
data = [2, 3, 5, 7]
product = 1

for num in data:
    product *= num

print("Original list:", data)
print("Product of all elements in list:", product)

#
#   6. Count Even and Odd Numbers
#
data = [10, 21, 4, 45, 66, 93, 11]
print("Original list:", data)
even_count = 0
odd_count = 0

for num in data:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

#
#   7. Reverse a List
#
data = [100, 200, 300, 400, 500]
print("Original list:", data)

data.reverse()
print("Reversed list:", data)

#   OR
data = [100, 200, 300, 400, 500]
reversed_num = data[::-1]
print("Reversed list:", reversed_num)

#
#   8. Sort a List of Numbers
#
data = [56, 12, 89, 3, 22]
print("Original list:", data)

data.sort()
print("Sorted list:", data)

#
#   9. Create a Copy of a List
#
data = ["Apple", "Banana", "Cherry"]
print("Original list:", data)

data.copy()
print("Copied list:", data)

#
#   10. Combine Two Lists
#
list1 = ["Physics", "Chemistry"]
list2 = ["Maths", "Biology"]

combined = list1 + list2
print("First list:", list1)
print("Second list:", list2)
print("Combined list:", combined)

#
#   11. List Slicing: Extract Middle Elements
#
data = [10, 20, 30, 40, 50, 60, 70]
print("Original list:", data)

middle = data[2:5]
print("Sliced list:", middle)