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

#
#   11. Subtract a Week From a Given Date
#
given_date = datetime(2025, 3, 15)
new = given_date - timedelta(weeks=1)

print("Original:", given_date)
print("Minus week:", new)

#
#   12. Add Week to Given Date
#
given_date = datetime(2025, 3, 15)
new = given_date + timedelta(weeks=1)

print("Original:", given_date)
print("Adding week:", new)

#
#   13. Calculate Days Between Two Dates
#
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 3, 15)

delta = date2 - date1

print("Days between dates:", delta.days)

#
#   14. Convert Unix Timestamp to Datetime
#
timestamp = 1672531200

convert = datetime.fromtimestamp(timestamp)
print("Unix to datetime:", convert)

#
#   15. Get ISO Week Number
#
given_date = datetime(2026, 1, 1)

iso = int(given_date.strftime("%V"))
print("ISO week number", iso)

#
#   16. Subtract 5 Hours and 30 Minutes
#
current = datetime.now()
new = current - timedelta(hours=5, minutes=30)

print("5h 30min before now:", new)

#
#   17. Check for Leap Year
#
import calendar

def leap(year):
    return calendar.isleap(year)

year = int(input("Enter a year:"))
print(f"Is {year} is a leap year?: {leap(year)}")

#
#   18. Calculate Age in Days
#
birthdate = date(1995, 6, 15)
today = date.today()
delta = (today - birthdate).days

print("Age in days:", delta)

#
#   19. Difference in Seconds
#
dt1 = datetime(2025, 1, 1, 9, 0, 0) 
dt2 = datetime(2025, 1, 1, 11, 45, 30)

delta = (dt2 - dt1).total_seconds()

print("Difference in seconds:", delta)

#
#   20. Print a Monthly Calendar
#
year = int(input("Enter a year:"))
month = int(input("Enter a month:"))

formatted = calendar.month(year, month)

print("Calendar:")
print(formatted)
