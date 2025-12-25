from tkinter import *
import time
import math

radHour = 80    #Radius of hour hand
radMin = 100    #Radius of minute hand
radSec = 120    #Radius of second hand

window = Tk()
window.title('Current Time')
window.geometry('410x410')

#Get Current Time in IST:

totalSeconds = int(time.time()) + 5 * 3600 + 30 * 60

currentSec = totalSeconds & 60  #IMP

totalMinutes = totalSeconds // 60 

currentMinute = totalMinutes % 60   #IMP

totalHours = totalMinutes // 60 

currentHour = totalHours % 24   #IMP

if currentHour > 12:
    currentHour -= 12


#Draw the clock:

canvas = Canvas(window, bg = 'white', width = 400, height = 400)
canvas.grid()

canvas.create_oval(10,10, 390, 390, outline = 'black', width = 2, tags = 'circle')
canvas.create_text(195, 20, text = '12', fill = 'black')
canvas.create_text(380, 195, text = '3', fill = 'black')
canvas.create_text(195, 380, text = '6', fill = 'black')
canvas.create_text(20, 195, text = '9', fill = 'black')


#Find the angle from +x-axis for each hour:

currentHour += currentMinute/60 + currentSec/3600   #For additional precision.

angle = ((currentHour - 3) * (math.pi / 6))     #2pi - this. But cos(2pi - x) = cos(-x) [= cos(x)]

#Coordinates of end-point for hour hand 

xEnd = radHour * math.cos(angle) + 195
yEnd = radHour * math.sin(angle) + 195

canvas.create_line(195, 195, xEnd, yEnd, fill = 'black', width = 4)

#Find the angle from +ve x-axis for each minute:

currentMinute += currentSec/60    #For additional precision

angleMinute = (currentMinute - 15) * (math.pi/30)

#Coordinates of end point for minute hand

xEndMin = radMin * math.cos(angleMinute) + 195
yEndMin = radMin * math.sin(angleMinute) + 195

canvas.create_line(195, 195, xEndMin, yEndMin, fill = 'black', width = 3)

#Find the angle for the second hand

angleSecond = (currentSec - 15) * (math.pi/30)

xEndSec = radSec * math.cos(angleSecond) + 195
yEndSec = radSec * math.sin(angleSecond) + 195

canvas.create_line(195, 195, xEndSec, yEndSec, fill = 'black', width = 1)
print('success')


window.mainloop()

