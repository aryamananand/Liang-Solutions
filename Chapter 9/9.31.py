from tkinter import *

class CircleDrag:
    def __init__(self):
        self.a = 0  #Variable for control
        self.b = 1
        #Circle size:
        self.size = 60
        self.shiftX = 0
        self.shiftY = 0
        #Initial coordinates for circle:
        self.xBlue = 20
        self.yBlue = 90

        self.window  = Tk()
        self.window.title('Circle Drag')
        self.window.geometry('510x510')
        self.canvas = Canvas(self.window, width = 500, height = 500, bg = 'white')
        self.canvas.grid()
        
        self.canvas.create_oval(self.xBlue, self.yBlue, self.xBlue + self.size, self.yBlue + self.size, fill = 'blue', outline = 'black', tags = 'blue')
        self.canvas.create_oval(90, 90, 150, 150, fill = 'black', outline = 'black')
        self.canvas.create_oval(160, 90, 220, 150, fill = 'green', outline = 'black')
        self.canvas.create_oval(55, 120, 115, 180, fill = 'white', outline = 'black')
        self.canvas.create_oval(125, 120, 185, 180, fill = 'yellow', outline = 'black')

        self.canvas.bind('<Button1-Motion>', self.drag)
        self.canvas.bind('<Button-1>', self.verif)
        self.window.mainloop()

    def drag(self, event):

        if self.xBlue <= event.x <= self.xBlue + self.size and self.yBlue <= event.y <= self.yBlue + self.size: 
            self.canvas.delete('blue')

            self.startX = event.x - self.shiftX
            self.startY = event.y - self.shiftY

            self.endX = self.startX + self.size
            self.endY = self.startY + self.size

            self.canvas.create_oval(self.startX, self.startY, self.endX, self.endY, fill = 'blue', outline = 'black', tags = 'blue')
            
            self.xBlue = event.x - self.shiftX
            self.yBlue = event.y - self.shiftY
            self.a = 0

    def verif (self, event):
        self.shiftX = event.x - self.xBlue
        self.shiftY = event.y - self.yBlue

    

CircleDrag()
