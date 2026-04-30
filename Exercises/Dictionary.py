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

#
#   9. Rename a Key of Dictionary
#
employee = {"fname": "John", "age": 30, "dept": "Engineering"}
print("Original dictionary:", employee)

new = {"first_name" if key == "fname" else key: value for key, value in employee.items()}

print("New key name:", new)

#
#   10. Delete a List of Keys
#
product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
print("Original dictionary:", product)

product.pop("stock")
product.pop("warehouse")

print(product)

#   OR
product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
print("Original dictionary:", product)

remove = ["stock", "warehouse"]

for key in remove:
    product.pop(key, None)

print(product)

#
#   11. Check Value Existence
#
roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}

print("'editor' exists as a value:", "editor" in roles.values())
print("'manager' exists as a value:", "manager" in roles.values())

#
#   12. Sum All Values
#
expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
print("Expenses dictionary:", expenses)

total = sum(expenses.values())
print("Total of expenses:", total)

#
#   13. Extract Subset of Keys
#
user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
print("User dictionary:", user)

keys_to_keep = ["id", "username", "email"]
subset = {k: user[k] for k in keys_to_keep if k in user}
print("Extracted subset:", subset)

#
#   14. Map Two Lists (zip)
#
attributes = ["brand", "model", "year", "color"] 
details = ["Honda", "Civic", 2023, "silver"]
print("Keys:", attributes)
print("Values:", details)

mapped = dict(zip(attributes, details))

print("Mapped into dicitonary:", mapped)

#
#   15. Count Character Frequencies
#
text = "hello world"
letters = {}

for char in text:
    letters[char] = letters.get(char, 0) + 1

print("Character frequency:", letters)

#
#   16. Modify Nested Dictionary
#
company = {"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}
print("Original dictionary:", company)

company["location"]["city"] = "Munich"
print("Modified dictionary:", company)

#
#   17. Update Deeply Nested Key
#
data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}}
print("Original dictionary:", data)

data["school"]["department"]["class"]["students"] = 35
print("Modified dictionary:", data)

#
#   18. Dictionary Comprehension
#
data = {n: n**2 for n in range(1, 11) }
print(data)

#
#   19. Filter Dictionary
#
scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
filtered = {k: v for k, v in scores.items() if v > 60}
print("Original dictionary:", scores)
print("Filtered dictionary:", filtered)

#
#   20. Key of Minimum Value
#
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
min_key = min(stock, key=stock.get)

print("Original dictionary:", stock)
print("Lowest stock item:", min_key)