import random
import secrets
import string
import time
#
#   1. Generate 3 Random Integers between 100 and 999 also divisible by 5.
#
print("Generating 3 random integer number between 100 and 999 divisible by 5")

for num in range(3):
    print(random.randrange(100, 999, 5), end=", ")

#
#   2. Random Lottery Pick.
#      Code to generate 100 random lottery tickets and pick 
#      two lucky tickets from it as a winner.
#
lottery_ticket_list = []
print("Generating 100 random lottery tickets.")

for i in range(100):
    lottery_ticket_list.append(random.randrange(1000000000, 9999999999))

win = random.sample(lottery_ticket_list, 2)

print("Lucky 2 lottery tickets are:", win)

#
#   3. Generate 6 digit Random Secure OTP
#
secretGenerator = secrets.SystemRandom()

print("Generating 6 Digit OTP")
otp = secretGenerator.randrange(100000, 999999)

print("Secure OTP is:", otp)

#
#   4. Pick Random Character
#
string = "Learning_Python"
random_char = random.choice(string)

print("Random character:", random_char)

#
#   5. Generate Random String
#
def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

print("Random string:", randomString(5))

#
#   6. Generate Random Password
#
def randomPassword():
    source = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(source, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print("Password is:", randomPassword())

#
#   7. Calculate Multiplication
#
num1 = random.random()
print("First random float:", num1)
num2 = random.uniform(9.5, 99.5)
print("Second random float:", num2)

num3 = num1 * num2
print("Multiplication:", num3)

#
#   8. Generate Random Token and URL
#
print("Random secret tokens:", secrets.token_hex(64))
print("Random secret url: www.test.com/reset/",secrets.token_urlsafe(64))

#
#   9. Dice Roll
#
dice = [1, 2, 3, 4, 5, 6]

print("Dice roll number:", random.choice(dice))

#
#   10. Generate Random Date
#
def getRandomDate(startDate, endDate):
    print("Random date between", startDate, "and", endDate)
    randomGen = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGen * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))
