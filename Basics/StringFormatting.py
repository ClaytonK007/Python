#
# 1. Extracting from a string.
#    Get a domain from an email address using the split() function.
#
email = "username@domain.com"
extract = email.split('@')[1]

print(f"Domain: {extract}")

#
# 2. Reverse words in a string. 
#    Use join() and split() and slicing techniques. 
#
sentence = "Learning Python is great !"
reversed_sentence = " ".join(sentence.split()[::-1])

print(reversed_sentence)

#
# 3. Extract hashtags from a sentence.
#    Import the regular experssions module, use findall() and special sequences. 
#
import re

post = "Learning #Python is awesome! #Coding #ItsNotABug!"
hash = re.findall(r"#\w+",post)

print(f"Hashtags: {hash}")

#
# 4. Validate password strength. 
#    Import the regular experssions module, use match() and lookaheads to ensure 
#    requirements are within the string. Password must have atleast one uppercase
#    atleast one lowercase and one speical character.
#
import re

password = input("Enter Passwords: ")
is_valid = bool(re.match(r'^(?=.*[A-Za-z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))

print("Password valid." if is_valid else "Invalid Password. Try again.")

#
# 5. Remove unnecessary whitespaces from a sentence. 
#    Import the regular experssions module and use sub()
#
import re

text = "   It    is  fun  learning    Python!"
clean = re.sub(r'\s+', ' ',text).strip()

print(clean)

#
# 6. Convert string to title case. 
#    Use title() to convert the string.
#
text = "i love learning python!"
convert = text.title()

print(convert)

#
# 7. Replace a word in a string. 
#    Use replace() to replace a word in the string. 
#
text = "I hate learning Python!"
convert = text.replace("hate", "love")

print(convert)