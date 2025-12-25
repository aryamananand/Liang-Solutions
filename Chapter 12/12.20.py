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


window = Tk()            
window.geometry("500x500")
window.title("n-sided Polygon")
for i in range(3,6):
    p = RegularPolygonCanvas(window, i)
    p.grid(row=1,column=i)

Canvas()
window.mainloop()

