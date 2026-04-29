#
#   1: List Creation using two lists
#
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
final = list()

odd = list1[1::2]
even = list2[0::2]

print("Element at odd-index position of first list:", odd)
print("Element at even-index position of second list:", even)

final.extend(odd)
final.extend(even)
print("Both lists added:", final)

#
#   2. Remove and add item in a list
#
list1 = [54, 44, 27, 79, 91, 41]
print("Original list:", list1)

index = list1.pop(4)
print("List After removing element at index 4:", list1)

list1.insert(2, index)
print("List after Adding element at index 2:", list1)

list1.append(index)
print("List after Adding element at last:", list1)

#
#   3. Slice list into 3 equal chunks and reverse each chunk
#
list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list:", list1)

length = len(list1)
chunk = int(length / 3)
start = 0
end = chunk

for item in range(3):
    index = slice(start, end)

    list_chunk = list1[index]
    print("Chunk", item, list_chunk)

    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk

#
#   4. Count the occurrence of each element from a list
#
list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list:", list1)

count = dict()
for item in list1:
    if item in count:
        count[item] += 1
    else:
        count[item]= 1

print("Count of each element:", count)

#
#   5. Paired Elements from Two Lists as a Set
#
list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4, 9, 16, 25, 36, 49, 64]
print("Original list 1:", list1)
print("Original list 2:", list2)

paired = set(zip(list1, list2))

print(paired)

#
#   6. Set Intersection and Removal
#
set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
print("Original list 1:", set1)
print("Original list 2:", set2)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

for item in intersection:
    set1.remove(item)

print("Set after removing common element:", set1)

#
#   7. Subset or Superset of another set
#
set1 = {27, 43, 34}
set2 = {34, 93, 22, 27, 43, 53, 48}
print("Original list 1:", set1)
print("Original list 2:", set2)

print("Set 1 is a subset of Set 2", set1.issubset(set2))
print("Set 2 is a subset of Set 1", set2.issubset(set1))

print("Set 1 is a superset of Set 2", set1.issubset(set2))
print("Set 2 is a superset of Set 1", set2.issubset(set1))


if set1.issubset(set2):
    set1.clear()

if set2.issubset(set1):
    set2.clear()

print("Set 1:", set1)
print("Set 2:", set2)

#
#   8. Filter List Against Dictionary Values
#
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print("List:", roll_number)
print("Dictionary:", sample_dict)

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]

print("After removing unwanted elements from list:", roll_number)

#
#   9. Extract Unique Dictionary Values to List
#
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary values:", speed.values())

speed_list = list()

for val in speed.values():
    if val not in speed_list:
        speed_list.append(val)

print("Unique list:", speed_list)

#   OR
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
unique = list(set(speed.values()))

print("Unique list:", unique)