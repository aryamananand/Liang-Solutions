from tkinter import *
import math

class RegularPolygonCanvas(Canvas):
    def __init__(self, parent, numberOfSides):
        super().__init__(parent, width = 400, height = 300, bg = "white")
        self.draw_polygon(numberOfSides)
        
    def draw_polygon(self,n):
        x_centre = 200
        y_centre = 150
        radius = 100
        a = x_centre + radius
        b = y_centre
        lst = []    # Stores the list of vertice--co-ordinates

        
        for k in range(1,n+1):
            angle = 2 * math.pi * k/n 
            x_n = x_centre + radius * math.cos(angle)
            y_n = y_centre + radius * math.sin(angle)
            lst.append(x_n)
            lst.append(y_n)
        self.create_polygon(lst,fill='black')


class nSidedPolygonDrawer(RegularPolygonCanvas):
    def __init__(self):
        self.numberOfSides = 3
        window = Tk()
        window.title('n-sided Polygons')
        window.geometry("500x450")
        self.frame1 = Frame(window)
        self.frame1.grid(row=1,column=1)
        frame2 = Frame(window)
        frame2.grid(row=2,column=1)
        self.draw_polygon()
        
        plus_button = Button(frame2, text = "+1", command = self.add_side)
        plus_button.grid(row=1, column=1)
        minus_button = Button(frame2, text = "-1", command = self.remove_side)
        minus_button.grid(row=1, column=2)
        

        window.mainloop()

    def draw_polygon(self):
        p = RegularPolygonCanvas(self.frame1,self.numberOfSides)
        p.grid(row=1,column=1)
    def add_side(self):
        self.numberOfSides += 1
        self.draw_polygon()
    def remove_side(self): 
        if self.numberOfSides > 3:
            self.numberOfSides -= 1
        self.draw_polygon()

nSidedPolygonDrawer()