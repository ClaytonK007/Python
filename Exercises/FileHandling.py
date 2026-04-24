#
#   1. Read a File and print its content
#
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")

#
#   2. Read File Line by Line
#
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")

#
#   3. Read Specific Lines From a File
#
try:
    with open("sample.txt", "r") as file:
        for line in range(5):
            content = file.readline()
            print(content.strip())
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")

#
#   4. Count Words From a File
#
import re

def count(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().lower()
            words = re.findall(r"\b\w+\b", content)
            return len(words)
    except FileNotFoundError:
        print("Error: 'sample.txt' not found.")

word_count = count("sample.txt")
print(f"Total words in file: {word_count}")

#
#   5. Count Total Number of Characters in File
#
filename = input("Enter file name:")
try:
    with open(filename, "r") as file:
        char_count = file.read()
        print(f"Total characters in file: {len(char_count)}") 
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")

#
#   6. Count Specific Word From a File
#
def count_word(filename, word):
    try:
        with open(filename, "r") as file:
            content = file.read().lower()
            words = content.split()
            count = 0
            for w in words:
                clean_word = w.strip('.,!?"\'()[]{};:')
                if clean_word == word.lower():
                    count += 1
            return count
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

filename = "sample.txt"
word_to_count = "test"
occurrences = count_word(filename, word_to_count)
print(f"The word '{word_to_count}' appears {occurrences} times in '{filename}'")

#
#   7. Write To a File
#
filename = "output.txt"
content = "Hello, im learning Python."
try:
    with open(filename, "w") as file:
        file.write(content)
    print(f"Successfully wrote '{filename}' file.")
except Exception as e:
    print(f"An error has occured: {e}")

#
#   8. Append To a File
#
filename = "output.txt"
content = "\nThis is an appended line."
try:
    with open(filename, "a") as file:
        file.write("\n" + content)
    print(f"Successfully appended to '{filename}' file.")
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")
except Exception as e:
    print(f"An error has occured: {e}")

#
#   9. Copy a File
#
import shutil

source = input("Enter source file name:")
destination = "new_file.txt"
try:
    shutil.copy2(source, destination)
    print(f"Successfully copied '{source}' file to '{destination}'.")
except FileNotFoundError:
    print(f"Error: '{source}' not found.")
except Exception as e:
    print(f"An error has occured: {e}")
except PermissionError:
    print("Permission denied.")

#   OR
def copy_file(source, destination):
    try:
        with open(source, "r") as source_file:
            content = source_file.read()
        with open(destination, "w") as destination:
            destination.write(content)
        print(f"Successfully copied '{source}' file.")
    except FileNotFoundError:
        print(f"Error: '{source}' not found.")
    except Exception as e:
        print(f"An error has occured: {e}")
    except PermissionError:
        print("Permission denied.")

source = input("Enter source file name:")
destination = "new_file.txt"
copy_file(source, destination)

#
#   10. Read and Write Binary
#
def copy_file(source, destination):
    try:
        with open(source, "rb") as source_file:
            content = source_file.read()
        with open(destination, "wb") as destination:
            destination.write(content)
        print(f"Successfully copied '{source}' file.")
    except FileNotFoundError:
        print(f"Error: '{source}' not found.")
    except Exception as e:
        print(f"An error has occured: {e}")
    except PermissionError:
        print("Permission denied.")

source = input("Enter source file name:")
destination = "binary_file.bin"
copy_file(source, destination)