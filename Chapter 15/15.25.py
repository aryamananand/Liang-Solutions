from tkinter import *
import math

class KochFractal:
    def __init__(self):
        self.window = Tk()
        self.window.title("Koch Fractal")
        self.window.geometry("630x690")

        self.canvas = Canvas(self.window, bg = "white", height = 600, width = 600)
        self.canvas.grid(row=1,column=1) 
        self.frame = Frame(self.window).grid(row=2,column=1)
        Label(self.frame, text = "Enter an order:").grid(row=2,column=1)
        self.order = StringVar()
        self.entry = Entry(self.frame,textvariable=self.order,justify="center").grid(row=3,column=1)
        self.button = Button(self.frame, text = "Display", command = self.draw_koch_fractal).grid(row=4,column=1)
        self.window.mainloop()

    def draw(self,x1,y1,x2,y2,depth):
    
        if depth == 0:
            self.canvas.create_line(x1,y1,x2,y2,fill="black")
        else:
            dx = (x2-x1)/3
            dy = (y2-y1)/3

            x3 = x1 + dx    #1/3rd point (x3,y3)
            y3 = y1 + dy
            x5 = x3 + dx     #2/3rd point (x5,y5)
            y5 = y3 + dy

            # To find apex (x4,y4) of triangle 
            angle = math.pi / 3
            cos60 = math.cos(angle)
            sin60 = math.sin(angle)
            rx = dx * cos60 - dy * sin60
            ry = dx * sin60 + dy * cos60
            x4 = x3 + rx
            y4 = y3 + ry

            self.draw(x1,y1,x3,y3,depth-1) #flat line 1
            self.draw(x3,y3,x4,y4,depth-1)  #triangle left side
            self.draw(x4,y4,x5,y5,depth-1)  #triangle right side
            self.draw(x5,y5,x2,y2,depth-1) #flat line 2

    def draw_koch_fractal(self):
        self.canvas.delete('all')
        depth = int(eval(self.order.get()))
        size = 300
        x_centre = 300
        y_centre = 300
        height = size*(3**0.5)/2

        p1x = x_centre - size/2 
        p1y = y_centre + height/3
        p2x = x_centre + size/2
        p2y = y_centre + height/3
        p3x = x_centre
        p3y = y_centre - 2*height/3
    
        self.draw(p1x,p1y,p2x,p2y,depth)
        self.draw(p3x,p3y,p1x,p1y,depth)
        self.draw(p2x,p2y,p3x,p3y,depth)
        
KochFractal()