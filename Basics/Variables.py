#
# 1. Declare and print a variable
#
name = "Tom"
students = "40"
language = "Python"

print(f"The instructor's name is {name}. He teaches {students} students and they are learning {language}.")
print("The instructor's name is " + name + ". He teaches " + students + " students and they are learning " + language)

#
# 2. Swap two variables without creating a third variable
#
var1 = "Day"
var2 = "Night"

# Before swap
print("Before swap: " + var1 + " & " + var2)
print(f"Before swap: {var1} & {var2}")

# After swap
var1, var2 = var2, var1

print("Before swap: " + var1 + " & " + var2)
print(f"Before swap: {var1} & {var2}")

#
# 3. Assign multiple variables in one line
#
animal_1, animal_2, animal_3 = "Dog", "Cat", "Bird"

print("The three different animals: " + animal_1 + ", " + animal_2 + ", " + animal_3 )
print(f"The three different animals: {animal_1}, {animal_2}, {animal_3}")

#
# 4. Check the data type of a variable
#
string_var = "Dog, Cat, Bird"
integer_var = 2026
float_var = 20.26
boolean_var = True
list_var = ["Dog", "Cat", "Bird"]
tuple_var = ("Dog", "Cat", "Bird")
dict_var = {"Dog" : "JaBarkus", "Cat" : "Loki", "Bird" : "Duck Norris"}
set_var = {"Dog", "Cat", "Bird"}
binary_var = b"Dog, Cat, Bird"
none_var = None

print(f"{string_var} is of {type(string_var)} type")
print(f"{integer_var} is of {type(integer_var)} type")
print(f"{float_var} is of {type(float_var)} type")
print(f"{boolean_var} is of {type(boolean_var)} type")
print(f"{list_var} is of {type(list_var)} type")
print(f"{tuple_var} is of {type(tuple_var)} type")
print(f"{dict_var} is of {type(dict_var)} type")
print(f"{set_var} is of {type(set_var)} type")
print(f"{binary_var} is of {type(binary_var)} type")
print(f"{none_var} is of {type(none_var)} type")

#
# 5. Concatenating strings
#
instructor = "Mr.Ted Mosby"
job = "architect"

sentence = instructor + " is an " + job + "."

print(sentence)
print(instructor + " is an " + job + ".")
print(f"{instructor} is an {job}.")