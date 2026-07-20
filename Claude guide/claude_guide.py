#   From Zero to Expert
#   A Practical, Hands-On Guide to Becoming a Skilled Programmer

#   1. Python Fundamentals
#   1.1 Variables and data types

name = "Ada"        # str
age = 36            # int
height = 1.71       # float
is_coding = True    # bool

print(f"{name} is {age} years old and is {height}m tall. Is coding?: {is_coding}")

#   1.2 Exercise - Print the numbers 1 to 20. For multiples of 3, 
#   print “Fizz” instead of the number. For multiples of 5, 
#   print “Buzz”. For multiples of both, print “FizzBuzz”.

for n in range(1,21):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)

#   2.Data Structures
#   2.1 There are 4 types of data structures in Python:
#   List — ordered, changeable
#   Tuple — ordered, unchangeable
#   Dict — key/value pairs
#   Set — unordered, no duplicates

list_example = [1, 2, 3]
tuple_example = (1, 2, 3)
dict_example = {"id": 1, "name": "Ada"}
set_example = {1, 2, 3}

print(list_example)
print(tuple_example)
print(dict_example)
print(set_example)

#   2.2 Exercise - word frequency counter:
#   Given a sentence, count how many times each word appears, ignoring case.

def word_count(sentence):
    count = {}
    for word in sentence.lower().split():
        count[word] = count.get(word, 0) + 1
    return count

sentence = input("Input a sentence for a word count:")

print(word_count(sentence))

#   3. Functions & Scope
#   3.1  Exercise - a reusable validator:
#   Write a function that returns True if an age is between 0 and 120 inclusive, 
#   and False otherwise.

def is_valid_age(age):
    return 0 <= age <= 120

print(is_valid_age(33))     # Ture
print(is_valid_age(-5))     # False
print(is_valid_age(130))    # False