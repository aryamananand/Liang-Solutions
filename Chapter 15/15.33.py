from tkinter import *
import math

class HilbertCurve:
    def __init__(self):
        self.window = Tk()
        self.window.title("Hilbert Curve")
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
        self.button = Button(self.frame, text = "Display", command = self.draw_HilbertCurve)
        self.button.grid(row=3,column=1)
        self.window.mainloop()

    def draw_HilbertCurve(self):
        self.canvas.delete('all')
        order = int(eval(self.order.get()))
        size = 600 // (2 ** order)
        margin = size // 2
        # Center the curve horizontally and vertically
        start_x = margin
        start_y = 600 - margin
        self.draw(300, 300, size, order, 0, 1)

    def draw(self, x, y, size, depth, angle, rotation):
        if depth == 0:
            return x, y
        angle90 = math.pi / 2

        # Quadrant 1
        angle1 = angle + rotation * angle90
        x, y = self.draw(x, y, size, depth - 1, angle1, -rotation)

        # Forward
        x_new = x + size * math.cos(angle)
        y_new = y + size * math.sin(angle)
        self.canvas.create_line(x, y, x_new, y_new, fill="black")
        x, y = x_new, y_new

        # Quadrant 2
        angle2 = angle
        x, y = self.draw(x, y, size, depth - 1, angle2, rotation)

        # Forward
        x_new = x + size * math.cos(angle)
        y_new = y + size * math.sin(angle)
        self.canvas.create_line(x, y, x_new, y_new, fill="black")
        x, y = x_new, y_new

        # Quadrant 3
        x, y = self.draw(x, y, size, depth - 1, angle2, rotation)

        # Forward
        x_new = x + size * math.cos(angle)
        y_new = y + size * math.sin(angle)
        self.canvas.create_line(x, y, x_new, y_new, fill="black")
        x, y = x_new, y_new

        # Quadrant 4
        angle4 = angle - rotation * angle90
        x, y = self.draw(x, y, size, depth - 1, angle4, -rotation)

        return x, y

HilbertCurve()