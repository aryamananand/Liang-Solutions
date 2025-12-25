from tkinter import *
import random 
import math
  #Dot size

class TriangleAngles:
    def __init__(self):
        self.px = 3
        self.xA = random.randint(0,500)
        self.yA = random.randint(0,500)

        self.xB = random.randint(0,500)
        self.yB = random.randint(0,500)

        self.xC = random.randint(0,500)
        self.yC = random.randint(0,500)


        self.window = Tk()
        self.window.title('Triangle Angles')
        self.window.geometry('510x510')
        self.canvas = Canvas(self.window, height = 500, width = 500, bg = 'white')
        self.canvas.grid()

        self.A = self.canvas.create_oval(self.xA - self.px, self.yA - self.px, self.xA + self.px, self.yA + self.px, fill = 'black', tags = 'A')
        self.canvas.create_text(self.xA + 10, self.yA - 10, text = 'A', fill = 'black')
        self.B = self.canvas.create_oval(self.xB - self.px, self.yB - self.px, self.xB + self.px, self.yB + self.px, fill = 'black', tags = 'B')
        self.canvas.create_text(self.xB + 10, self.yB - 10, text = 'B', fill = 'black')
        self.C = self.canvas.create_oval(self.xC - self.px, self.yC - self.px, self.xC + self.px, self.yC + self.px, fill = 'black', tags = 'C')
        self.canvas.create_text(self.xC + 10, self.yC - 10, text = 'C', fill = 'black')

        self.canvas.create_line(self.xA, self.yA, self.xB, self.yB, fill = 'black', width = 2, tags = 'AB')
        self.canvas.create_line(self.xB, self.yB, self.xC, self.yC, fill = 'black', width = 2, tags = 'BC')
        self.canvas.create_line(self.xA, self.yA, self.xC, self.yC, fill = 'black', width = 2, tags = 'AC')
        
        

        self.window.mainloop()

    def cursor(self, event):
        if (self.xA - self.px <=  event.x_root <= self.xA + self.px) and (self.yA - self.px <= event.y_root <= self.yA + self.px):
            self.canvas.bind('<Motion>', self.cursor)
            self.changeCursor()
        if (self.xB - self.px <= event.x_root <= self.xB + self.px) and (self.yB - self.px <= event.y_root <= self.yB + self.px):
            self.canvas.bind('<Motion>', self.cursor)
            self.changeCursor()
        if (self.xC - self.px <= event.x_root <= self.xC + self.px) and (self.yC - self.px <= event.y_root <= self.yC + self.px):
            self.canvas.bind('<Motion>', self.cursor)
            self.changeCursor()
    
    def changeCursor(self, event):
        self.window.config(cursor = 'cross')



TriangleAngles()



'''
    def cursor(self, event):
        if self.xA - self.px <=  event.x_root <= self.xA + self.px and self.yA - self.px <= event.y_root <= self.yA + self.px:
            self.window.config(cursor = 'cross')
        if self.xB - self.px <= event.x_root <= self.xB + self.px and self.yB - self.px <= event.y_root <= self.yB + self.px:
            self.window.config(cursor = 'cross')
        if self.xC - self.px <= event.x_root <= self.xC + self.px and self.yC - self.px <= event.y_root <= self.yC + self.px:
            self.window.config(cursor = 'cross')

'''









    
        
        



'''
        self.canvas.bind('<Button-1>', self.dragA)
        self.canvas.focus_set()

        self.canvas.bind('<ButtonRelease-1>')
        self.canvas.focus_set()

        


    def dragA (event):
        print("success!")
        if (self.xA - self.px <= event.x_root <= self.xA + self.px) and self.yA - self.px <= event.y_root <= self.yA + self.px:
            self.canvas.delete('A', 'AB', 'AC')
            self.canvas.create_oval(event.x_root - self.px, event.y_root - self.px, event.x_root + self.px, event.y_root + self.px, fill = 'black')
            self.canvas.create_line(event.y_root, event.y_root, self.xB, self.yB, fill = 'black', width = 2, tags = 'BC')
            self.canvas.create_line(event.x_root, event.y_root, self.xC, self.yC, fill = 'black', width = 2, tags = 'AC') 
'''




    
    




