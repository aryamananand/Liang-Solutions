'''(Science: day of the week) Zeller’s congruence is an algorithm developed by Christian Zeller to calculate the day of the week. The formula is
h = ¢q + j26(m + 1)k + k + jkk + jjk + 5j≤%7 10 44
where
■ h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday, 4: Wednesday, 5: Thursday, 6: Friday).
■ q is the day of the month.
■ m is themonth(3 : March, 4 : April, ..., 12 : December). January and February are counted as months 13 and 14 of the previous year.
■ j is the century (i.e., j
■ k is the year of the century(i.e., year/100).

Write a program that prompts the user to enter a year, month, and day of the month, and then it displays the name of the day of the week.'''

import math

year = eval(input("Enter year (e.g. 2012): "))
month = eval(input("Enter month (1 - 12): "))
d = eval(input("Enter day of the month (1 - 31): "))

if month < 1 or month > 12:
    print("Month is invalid.")
elif (month == 1 or month == 2):
    month += 12
    year -= 1
    

k = year % 100
j = math.floor(year / 100)


result = ( d + math.floor(( 26 * (month + 1)) / 10) + k + math.floor(k / 4) + math.floor(j / 4) + 5 * j) % 7



if result == 2:
    day = "Monday"
elif result == 3:
    day = "Tuesday"
elif result == 4:
    day = "Wednesday"
elif result == 5:
    day = "Thursday"
elif result == 6:
    day = "Friday"
elif result == 0:
    day = "Saturday"
else:
    day = "Sunday"

print("Day of the week is", day)
