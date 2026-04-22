#
#   1. Basic Dictionary Operations
#
student = {"name": "Alice", "age": 20, "grade": "B"}
print("Original dictionary:", student)

student["city"] = "New York"
student["age"] = 21

print("New and Modified:", student)
print("Name:", student["name"])

#
#   2. Dictionary Operations
#
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
print("Original dictionary:", car)

car.pop("color")
car.items()

print(car)
print(car.items())
print("'brand' exists:", "brand" in  car)
print("'color' exists:", "color" in  car)

#
#   3. Dictionary from Two Lists
#
keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]
print("Original key dictionary:", keys)
print("Original values dictionary:", values)

mapped = list(zip(keys, values))

print("Mapped:", mapped)

#
#   4. Clear Dictionary
#
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
print("Original dictionary:", inventory)

inventory.clear()

print(inventory)

#
#   5. Merge Dictionaries
#
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print("Original first dictionary:", dict1)
print("Original second dictionary:", dict2)

merged = dict1 | dict2

print("Merged:", merged)

#
#   6. Access Nested Dictionary
#
person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
print("Original dictionary:", person)

print("City:", person.get("address", {}).get("city"))

#
#   7. Access ‘history’ Key From a Nested Dictionary
#
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
print("Original dictionary:", student)

print("History grade:", student.get("grades", {}).get("history"))

#
#   8. Initialize Dictionary with Default Values
#
keys = ["math", "science", "english", "history"]
print("Original dictionary:", keys)

default = 0
grades = dict.fromkeys(keys, default)
print("Initialized dictionary:", grades )