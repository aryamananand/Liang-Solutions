

today = eval(input("Enter today's day's number (0-6): "))

if 0 <= today  <= 6:
    if today == 0:
        today_ = "Sunday"
    elif today == 1:
        today_ = "Monday"
    elif today == 2:
        today_ = "Tuesday"
    elif today == 3:
        today_ = "Wednesday"
    elif today == 4:
        today_ = "Thursday"
    elif today == 5:
        today_ = "Friday"
    elif today == 6:
        today_ = "Saturday"





    daysGone = eval(input("Enter number of days elapsed since today: "))

    today = (today + daysGone) % 7

    if today == 0:
        today = "Sunday"
    elif today == 1:
        today = "Monday"
    elif today == 2:
        today = "Tuesday"
    elif today == 3:
        today = "Wednesday"
    elif today == 4:
        today = "Thursday"
    elif today == 5:
        today = "Friday"
    else:
        today = "Saturday"

    print("Today is ", today_)
    print("The future day is", today)

else:
    today_ = "Out of bounds!"

    print(today_)
