import time

offsetHours = eval(input("Enter timezone offset to GMT in hours:"))

GMTtime = time.time()
offsetTime = offsetHours * 3600

currentTime = GMTtime + offsetTime

totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinute = totalMinutes % 60

totalHours = totalMinutes // 60

currentHour = totalHours % 24

print("The current time is:", currentHour, ":", currentMinute, ":", currentSecond)


