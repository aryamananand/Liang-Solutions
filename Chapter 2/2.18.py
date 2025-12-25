import time

GMToffset = eval(input("Enter offset from GMT in hours:"))

currentTimeGMT = time.time()
totalSeconds = int(currentTimeGMT)

#convert user input to seconds

GMToffsetSeconds = GMToffset * 3600

#To modify time as per user input

realTime = totalSeconds - GMToffsetSeconds

currentSecond = realTime % 60

currentMinute = totalSeconds % 60
totalMinutes = realTime // 60


totalHours = totalMinutes // 60

currentHour = totalHours % 24

print("The current time is:", currentHour, ":", currentMinute, ":", currentSecond)
