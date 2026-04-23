from datetime import *

#
#   1. Print Current Date and Time
#
now = datetime.now()

print("Current date and time:", now)

#
#   2. Format DateTime
#
now = datetime.now()
formatted = now.strftime("%d-%b-%Y %I:%M:%S %p")

print("Formatted date and time:", formatted)

#
#   3. Find Day of Week
#
dt = datetime(2025, 1, 15)
day = dt.strftime("%A")

print("Day of week:", day)

#
#   4. Convert Datetime into String
#
dt = datetime(2025, 6, 15, 10, 30, 45)
day = str(dt)

print("Date into string:", day)

#
#   5. Extract Components
#
dt = datetime(2025, 8, 20, 14, 35, 50)

print("Year:", dt.year)
print("Month:", dt.month)
print("Day:", dt.day)
print("Hour:", dt.hour)
print("Minutes:", dt.minute)
print("Second:", dt.second)

#
#   6. Print Time with AM/PM
#
current = datetime.now()
now = current.strftime("%I:%M %p")

print("Current time AM or PM:", now)

#
#   7. Print Current Time in Milliseconds
#
current = datetime.now()
now = current.strftime("%I:%M:%S.%f %p")

print("Current time in milli:", now)

#
#   8. Get the Day of the Year
#
dt = datetime(2025, 3, 15)
day = int(dt.strftime("%j"))

print("Day of the year:", day)

#
#   9. Combine Date and Time Objects
#
d = date(2025, 5, 20)
t = time(9, 45, 0)

merged = datetime.combine(d, t)

print(merged)

#
#   10. Convert String Into Datetime Object
#
date_string = "20 January, 2025"
format = datetime.strptime(date_string, "%d %B, %Y")

print(format)