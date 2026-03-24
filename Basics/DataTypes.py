#
# 1. Convert string to integer and vice versa along with data type.
#    Use the str() and int() functions.
#
str_value = "2026"
int_value = 2026

convert_1 = int(str_value)
convert_2 = str(int_value)

print(f"Sring to Integer : {convert_1}, Type : {type(convert_1)}")
print(f"Integer to String : {convert_2}, Type : {type(convert_2)}")

#
# 2. Convert float to integer and vice versa along with data type.
#    Use the flaot() and int() functions.
#
float_value = 20.26
integer_value = 2026

change_1 = int(float_value)
change_2 = float(integer_value)

print(f"Float to Integer : {change_1}, Type : {type(change_1)}")
print(f"Integer to Float: {change_2}, Type : {type(change_2)}")

#
# 3. Convert boolean to integer and vice versa along with data type.
#    Use the int() functions.
#
bool_1 = True
bool_2 = False
bool_to_int_1 = int(bool_1)
bool_to_int_2 = int(bool_2)

print(f"True as integer : {bool_to_int_1}")
print(f"False as integer : {bool_to_int_2}")

#
# 4. Convert list to a string and back.
#    Use the join() and split() functions.
#
words = ["Learning","Python", "is", "fun"]

list_to_string = " ".join(words)
string_to_list = list_to_string.split(" ")

print(f"List to string: {list_to_string}")
print(f"String to list: {string_to_list}")

#
# 5. Convert dictionary keys and values to a list.
#    Use the list(), keys() and values() functions.
#
dictionary = {
    "name" : "Mark",
    "age" : "30",
    "language" : "Python"
}

keys_to_list = list(dictionary.keys())
values_to_list = list(dictionary.values())

print(f"Keys: {keys_to_list}")
print(f"Values: {values_to_list}")
