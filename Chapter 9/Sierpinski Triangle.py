from tkinter import *
import random

px = 0.5

#A (350, 30)
xA = 350
yA = 30

#B (60, 450)
xB = 60
yB = 450

#C (640, 450)
xC = 640
yC = 450

#R (random point)
xR = 640
yR = 450

window = Tk()
window.title('Triangle Midpoint')
window.geometry('710x710')
canvas = Canvas(window, width = 700, height = 700, bg = 'white')
canvas.grid()

canvas.create_oval(xA - 5, yA - 5, xA + 6, yA + 6, fill = 'black')    
canvas.create_oval(xB - 5, yB - 5, xB + 6, yB + 6, fill = 'black')
canvas.create_oval(xC - 5, yC - 5, xC + 6, yC + 6, fill = 'black')

canvas.create_oval(xR - px, yR - px, xR + px + 1, yR + px +1,  fill = 'black', width = 0)


for i in range(75000):
        
    num = random.randint(1,3)
    if num == 1:
        xR = (xA + xR)/2 
        yR = (yA + yR)/2
        canvas.create_oval(xR - px, yR - px, xR + px + 1, yR + px + 1, fill = 'black', width = 0)
    if num == 2:
        xR = (xB + xR)/2 
        yR = (yB + yR)/2
        canvas.create_oval(xR - px, yR - px, xR + px + 1, yR + px + 1, fill = 'black', width = 0)
    if num == 3:
        xR = (xC + xR)/2 
        yR = (yC + yR)/2
        canvas.create_oval(xR - px, yR - px, xR + px + 1, yR + px + 1, fill = 'black', width = 0)
        

window.mainloop()