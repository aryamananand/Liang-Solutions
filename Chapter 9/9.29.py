from tkinter import *

class IntersectionPoint:
    def __init__(self):
        self.px = 3
        self.curDis = 5
        
        #Initial end points of lines
        self.x1 = 20
        self.x2 = 56
        self.y1 = 20
        self.y2 = 130
        self.x_1 = 100
        self.x_2 = 16
        self.y_1 = 20
        self.y_2 = 130

        #Mainscreen construct
        self.window = Tk()
        self.window.title('Intersecting Lines')
        self.window.geometry('510x510')
        self.canvas = Canvas(self.window, height = 500, width = 500, bg = 'white')
        self.canvas.grid()

        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = 'black', tags = 'xy')
        self.canvas.create_line(self.x_1, self.y_1, self.x_2, self.y_2, fill = 'black', tags = 'x_y')

        #Find Initial Intersection Point
        self.Intersection()
        self.canvas.create_oval(self.x - self.px, self.y - self.px, self.x + self.px, self.y + self.px, fill = 'black', tags = 'Point')

        self.canvas.bind('<Button1-Motion>', self.drag) #Main dragging indentifier

        self.window.mainloop()

    def drag(self, event):

        #For point (x1, y1):
        if (self.x1 - self.curDis <= event.x <= self.x1 + self.curDis) and (self.y1 - self.curDis <= event.y <= self.y1 + self.curDis):
            self.canvas.delete('Point', 'xy')
            self.canvas.create_line(event.x, event.y, self.x2, self.y2, fill = 'black', tags = 'xy')
            self.Intersection()
            
            self.x1 = event.x
            self.y1 = event.y


        #For point (x2, y2):
        if (self.x2 - self.curDis <= event.x <= self.x2 + self.curDis) and (self.y2 - self.curDis <= event.y <= self.y2 + self.curDis):
            self.canvas.delete('Point', 'xy')
            self.canvas.create_line(event.x, event.y, self.x1, self.y1, fill = 'black', tags = 'xy')
            self.Intersection()
            
            self.x2 = event.x
            self.y2 = event.y 


        #For point (x_1, y_1):
        if (self.x_1 - self.curDis <= event.x <= self.x_1 + self.curDis) and (self.y_1 - self.curDis <= event.y <= self.y_1 + self.curDis):
            self.canvas.delete('Point', 'x_y')
            self.canvas.create_line(event.x, event.y, self.x_2, self.y_2, fill = 'black', tags = 'x_y')
            self.Intersection()
            
            self.x_1 = event.x
            self.y_1 = event.y

        
        #For point (x_2, y_2):
        if (self.x_2 - self.curDis <= event.x <= self.x_2 + self.curDis) and (self.y_2 - self.curDis <= event.y <= self.y_2 + self.curDis):

            self.canvas.delete('Point', 'x_y')
            self.canvas.create_line(event.x, event.y, self.x_1, self.y_1, fill = 'black', tags = 'x_y')
            self.Intersection()
            
            self.x_2 = event.x
            self.y_2 = event.y 

    def Intersection(self):
        # (y1 - y2) * x - (x1 - x2) * y = (y1 - y2) * x1 - (x1 - x2) * y1
        # (y3 - y4) * x - (x3 - x4) * y = (y3 - y4) * x3 - (x3 - x4) * y3

        a = self.y1 - self.y2
        b = - (self.x1 - self.x2)
        e = (self.y1 - self.y2) * self.x1 - (self.x1 - self.x2) * self.y1
        c = self.y_1 - self.y_2
        d = - (self.x_1 - self.x_2)
        f = (self.y_1 - self.y_2) * self.x_1 - (self.x_1 - self.x_2) * self.y_1

        if (a * d - b * c) != 0:
            
            x = (e * d - b * f) / (a * d - b * c)
            y = (a * f - e * c) / (a * d - b * c)

            #Point has to belong to the segment
            if ((self.x1 < x < self.x2 or self.x2 < x < self.x1) and (self.y1 < y < self.y2 or self.y2 < y < self.y1)) and (self.x_1 < x < self.x_2 or self.x_2 < x < self.x_1) and (self.y_1 < y < self.y_2 or self.y_2 < y < self.y_1):
                self.x = x
                self.y = y
                self.canvas.create_oval(self.x - self.px, self.y - self.px, self.x + self.px, self.y + self.px, fill = 'black', tags = 'Point')
                self.canvas.delete('text')
                self.canvas.create_text(300, 460, text = f"Intersect: ({str(format(x, ".2f"))}, {str(format(y, ".2f"))})", fill = 'black', tags = 'text')
            else:
                self.canvas.delete('Point', 'text')


IntersectionPoint()