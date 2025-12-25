from tkinter import *
import random 
import math
  #Dot size

class TriangleAngles:
    def __init__(self):
        self.px = 3
        self.cursorCheck = 'arrow'  #State of the cursor
        self.xA = random.randint(10,500)
        self.yA = random.randint(10,500)

        self.xB = random.randint(10,500)
        self.yB = random.randint(10,500)

        self.xC = random.randint(10,500)
        self.yC = random.randint(10,500)
        self.curDis = 10    #Area for cursor change


        self.window = Tk()
        self.window.title('Triangle Angle 2')
        self.window.geometry('510x510')
        self.canvas = Canvas(self.window, height = 500, width = 500, bg = 'white')
        self.canvas.grid()

        self.canvas.create_oval(self.xA - self.px, self.yA - self.px, self.xA + self.px, self.yA + self.px, fill = 'black', tags = 'A')
       # self.canvas.create_oval(self.xA - self.curDis, self.yA - self.curDis, self.xA + self.curDis, self.yA + self.curDis, fill = None, outline = 'black')
        self.canvas.create_text(self.xA + 10, self.yA - 10, text = 'A', fill = 'black', tags = 'text_A')
        self.canvas.create_oval(self.xB - self.px, self.yB - self.px, self.xB + self.px, self.yB + self.px, fill = 'black', tags = 'B')
        #self.canvas.create_oval(self.xB - self.curDis, self.yB - self.curDis, self.xB + self.curDis, self.yB + self.curDis, fill = None, outline = 'black')
        self.canvas.create_text(self.xB + 10, self.yB - 10, text = 'B', fill = 'black', tags = 'text_B')
        self.canvas.create_oval(self.xC - self.px, self.yC - self.px, self.xC + self.px, self.yC + self.px, fill = 'black', tags = 'C')
        #self.canvas.create_oval(self.xC - self.curDis, self.yC - self.curDis, self.xC + self.curDis, self.yC + self.curDis, fill = None, outline = 'black')
        self.canvas.create_text(self.xC + 10, self.yC - 10, text = 'C', fill = 'black', tags = 'text_C')

        self.canvas.create_line(self.xA, self.yA, self.xB, self.yB, fill = 'black', width = 2, tags = 'AB')
        self.canvas.create_line(self.xB, self.yB, self.xC, self.yC, fill = 'black', width = 2, tags = 'BC')
        self.canvas.create_line(self.xA, self.yA, self.xC, self.yC, fill = 'black', width = 2, tags = 'AC')
        

        self.canvas.bind('<Button1-Motion>', self.cursor)
        
        self.window.mainloop()

   
    def cursor(self, event):
        if (self.xA - self.curDis <= event.x <= self.xA + self.curDis) and (self.yA - self.curDis <= event.y <= self.yA + self.curDis):
    
            self.cursorCheck = 'arrow' 
            self.changeCursor()
            self.a = 1
        if self.a == 1:
            self.canvas.bind('<Button1-Motion>', self.dragA(event))
            
        if (self.xB - self.curDis <= event.x <= self.xB + self.curDis) and (self.yB - self.curDis <= event.y <= self.yB + self.curDis):
            
            self.cursorCheck = 'arrow'
            self.changeCursor()
        if (self.xC - self.curDis <= event.x <= self.xC + self.curDis) and (self.yC - self.curDis <= event.y <= self.yC + self.curDis):
            self.cursorCheck = 'arrow'
            self.changeCursor()
            self.cursorCheck = 'arrow'
            
        self.canvas.bind('<Motion>', self.cursorRemove)

    def changeCursor(self):
        if self.cursorCheck == 'arrow':
            string = 'cross'
        elif self.cursorCheck == 'cross':
            string = 'arrow'
        self.window.config(cursor = string)

    def cursorRemove(self, event):
        if ((self.xA - self.curDis <= event.x <= self.xA + self.curDis) and (self.yA - self.curDis <= event.y <= self.yA + self.curDis)) is False:
            self.cursorCheck = 'cross' 
            self.changeCursor()
            
        if ((self.xB - self.curDis <= event.x <= self.xB + self.curDis) and (self.yB - self.curDis <= event.y <= self.yB + self.curDis)) is False:
            self.cursorCheck = 'cross'
            self.changeCursor()
   
        if ((self.xC - self.curDis <= event.x <= self.xC + self.curDis) and (self.yC - self.curDis <= event.y <= self.yC + self.curDis)) is False:
            self.cursorCheck = 'cross'
            self.changeCursor()

        self.canvas.bind('<Motion>', self.cursor)
    def dragA (self, event):
        self.canvas.delete('A', 'AB', 'AC' )
        print('Success!!')
        self.canvas.create_oval(event.x - self.px, event.y - self.px, event.x + self.px, event.y + self.px, fill = 'black', tags = 'A')
        self.canvas.create_text(self.xA + 10, self.yA - 10, text = 'A', fill = 'black', tags = 'text_A')
        self.canvas.create_line(event.x, event.y, self.xB, self.yB, fill = 'black', width = 2, tags = 'AB')
        self.canvas.create_line(event.x, event.y, self.xC, self.yC, fill = 'black', width = 2, tags = 'AC')


        

TriangleAngles()



'''

    def check(self, event):
        if (self.xA - self.curDis <= event.x <= self.xA + self.curDis) and (self.yA - self.curDis <= event.y <= self.yA + self.curDis):
            self.canvas.bind('<Button1-Motion>', self.dragA)
            
        if (self.xB - self.curDis <= event.x <= self.xB + self.curDis) and (self.yB - self.curDis <= event.y <= self.yB + self.curDis):
            self.canvas.bind('<Button1-Motion>', self.drag)
        
        if (self.xC - self.curDis <= event.x <= self.xC + self.curDis) and (self.yC - self.curDis <= event.y <= self.yC + self.curDis):
            self.canvas.bind('<Button1-Motion>', self.dragC)

'''

    
    




