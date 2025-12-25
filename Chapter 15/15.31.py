from tkinter import *
import math

class RecursiveTree:
    def __init__(self):
        self.window = Tk()
        self.window.title("Recursive Tree")
        self.window.geometry("630x690")

        self.canvas = Canvas(self.window, bg = "white", height = 600, width = 600)
        self.canvas.grid(row=1,column=1) 
        # Fix widget assignment
        self.frame = Frame(self.window)
        self.frame.grid(row=2,column=1)
        Label(self.frame, text = "Enter an order:").grid(row=1,column=1)
        self.order = StringVar()
        self.entry = Entry(self.frame,textvariable=self.order,justify="center")
        self.entry.grid(row=2,column=1)
        self.button = Button(self.frame, text = "Display", command = self.draw_RecursiveTree)
        self.button.grid(row=3,column=1)
        self.window.mainloop()
    
    def draw_RecursiveTree(self):
        self.canvas.delete('all')
        try:
            order = int(self.order.get())
        except Exception:
            order = 0
        size = 150
        x = 300
        y = 500

        if order != 0:
            # Start with direction=1 for angle alternation
            self.draw(x, y, size, 90, order, 1)

    def draw(self, x, y, size, angle, order, direction):
        if order > 0:
            a = math.radians(angle)
            x2 = x + size * math.cos(a)
            y2 = y - size * math.sin(a)

            self.canvas.create_line(x, y, x2, y2, fill="black")

            # Alternate angle direction for each branch
            self.draw(x2, y2, size * 0.7, angle + 30 * direction, order - 1, -direction)
            self.draw(x2, y2, size * 0.7, angle - 30 * direction, order - 1, direction)
    
RecursiveTree()