from tkinter import *
class Rectangle2D:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
    def setX(self, x):
        self.x = x
    def getX(self) -> int:
        return self.x
    def setY(self, y):
        self.y = y
    def getY(self) -> int:
        return self.y
    def setWidth(self, width):
        self.width = width
    def getWidth(self):
        return self.width
    def setHeight(self, height):
        self.height = height
    def getHeight(self):
        return self.height
    def getArea(self):
        return self.width * self.height
    
    def getx1(self):
        return self.getX() - self.getWidth()/2
    def gety1(self):
        return self.getY() - self.getHeight()/2
    def getx2(self):
        return self.getX() + self.getWidth()/2
    def gety2(self):
        return self.getY() + self.getHeight()/2


    def getPerimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        return f"The bounding rectangle is centred at ({self.x}, {self.y}) with width {self.width} and height {self.height}."
    def containsPoint(self, x, y):
        limX1 = self.x - (self.width/2)
        limX2 = self.x + (self.width/2)
        limY1 = self.y - (self.height/2)
        limY2 = self.y + (self.height/2)

        if limX1 <= x <= limX2 and limY1 <= y <= limY2:
            return True 
        else:
            return False
    def overlaps(self, r1, r2):
        if abs(int(r2.getX() - r1.getX()))  < int(r1.getWidth()/2 + r2.getWidth()/2) and abs(int(r2.getY() - r1.getY())) < int(r1.getHeight()/2 + r2.getHeight()/2):
            return "The rectangles intersect."
        else:
            return "The rectangles do not intersect."

    def __cmp__(self, c2):
        if self.getArea() < c2.getArea():
            return -1 
        elif self.getArea() == c2.getArea():
            return 0
        elif self.getArea() > c2.getArea():
            return 1
    def __eq__(self, c2):
        if self.getArea() == c2.getArea():
            return True
        else:
            return False
    def __lt__(self, c2):
        if self.getArea() < c2.getArea():
            return True
        else:
            return False
    def __le__(self, c2):
        if self.getArea() <= c2.getArea():
            return True
        else:
            return False
    def __ne__(self, c2):
        if self.getArea() != c2.getArea():
            return True
        else:
            return False
    def __gt__(self, c2):
        if self.getArea() > c2.getArea():
            return True
        else:
            return False
    def __ge__(self, c2):
        if self.getArea() >= c2.getArea():
            return True
        else:
            return False
        
class RectangleIntersection(Rectangle2D):
    def __init__(self):
        self.window = Tk()
        self.window.title("Two Rectangles")
        self.window.geometry("400x465")
        self.canvas = Canvas(self.window, bg = "white", width = 300, height = 200)
        self.canvas.pack(pady=10)
        self.frame = Frame(self.window)
        self.frame.pack(pady=10)
        self.frame1 = Frame(self.window)
        self.frame1.pack(pady=10)
        self.frame2 = Frame(self.window)
        self.frame2.pack(pady=10)
        
        # Create two rectangles as instances of class Rectangle2D
        self.rectangle1 = Rectangle2D()
        self.rectangle1.setX(172)
        self.rectangle1.setY(47)
        self.rectangle1.setWidth(60)
        self.rectangle1.setHeight(30)

        self.rectangle2 = Rectangle2D()
        self.rectangle2.setX(109)
        self.rectangle2.setY(66)
        self.rectangle2.setWidth(30)
        self.rectangle2.setHeight(30)
        
        # Intersection Canvas
        self.intersection_canvas = Canvas(self.frame, width = 400, height = 30)
        self.intersection_canvas.pack()
        self.intersection_canvas.create_text(200,15, text = f"{self.overlaps(self.rectangle1, self.rectangle2)}", tags = 'text')

        # R1 Labels
        Label(self.frame1, text = "R1 Centre x: ", justify = CENTER).grid(row = 1,column = 1)
        Label(self.frame1, text = "R1 Centre y: ", justify = CENTER).grid(row = 2,column = 1)
        Label(self.frame1, text = "R1 Width: ", justify = CENTER).grid(row = 3, column = 1)
        Label(self.frame1, text = "R1 Height: ", justify = CENTER).grid(row = 4, column = 1)

        # R1 Entryboxes
        self.r1_x_value = IntVar()
        self.r1_x_entry = Entry(self.frame1,textvariable = self.r1_x_value, justify = RIGHT, width = 5).grid(row=1, column=2)
        self.r1_y_value = IntVar()
        self.r1_y_entry = Entry(self.frame1,textvariable = self.r1_y_value, justify = RIGHT, width = 5).grid(row=2, column=2)
        self.r1_width_value = IntVar()
        self.r1_width_entry = Entry(self.frame1, textvariable = self.r1_width_value, justify = RIGHT, width = 5).grid(row=3, column = 2)
        self.r1_height_value = IntVar()
        self.r1_height_entry = Entry(self.frame1, textvariable = self.r1_height_value, justify = RIGHT, width = 5).grid(row=4, column=2)

        # R2  Labels
        Label(self.frame1, text = "R2 Centre x: ", justify = CENTER).grid(row = 1, column = 3)
        Label(self.frame1, text = "R2 Centre y: ", justify = CENTER).grid(row = 2, column = 3)
        Label(self.frame1, text = "R2 Width: ", justify = CENTER).grid(row = 3, column = 3)
        Label(self.frame1, text = "R2 Height: ", justify = CENTER).grid(row = 4, column = 3)

        # R2 Entryboxes
        self.r2_x_value = IntVar()
        self.r2_x_entry = Entry(self.frame1,textvariable = self.r2_x_value, justify = RIGHT, width = 5).grid(row=1, column=4)
        self.r2_y_value = IntVar()
        self.r2_y_entry = Entry(self.frame1,textvariable = self.r2_y_value, justify = RIGHT, width = 5).grid(row=2, column=4)
        self.r2_width_value = IntVar()
        self.r2_width_entry = Entry(self.frame1, textvariable = self.r2_width_value, justify = RIGHT, width = 5).grid(row=3, column=4)
        self.r2_height_value = IntVar()
        self.r2_height_entry = Entry(self.frame1, textvariable = self.r2_height_value, justify = RIGHT, width = 5).grid(row=4, column=4)

        # Initialise values to display rectangles at the opening of the window
        self.r1_x_value.set(172)
        self.r1_y_value.set(47)
        self.r1_width_value.set(60)
        self.r1_height_value.set(30)

        self.r2_x_value.set(109)
        self.r2_y_value.set(66)
        self.r2_width_value.set(30)
        self.r2_height_value.set(30)

        # Draw the initial rectangles
        self.canvas.create_rectangle(self.rectangle1.getx1(), self.rectangle1.gety1(), 
                                     self.rectangle1.getx2()+1, self.rectangle1.gety2(),
                                     outline = 'blue', tags = 'rectangle1')
         
        self.canvas.create_rectangle(self.rectangle2.getx1(), self.rectangle2.gety1(), 
                                     self.rectangle2.getx2()+1, self.rectangle2.gety2(),
                                     outline = 'blue', tags = 'rectangle2')
        

        Button(self.frame2, text = "Redraw Rectangles", command = self.draw).pack()

        self.canvas.bind('<Button1-Motion>', self.drag)
        self.canvas.bind('<Button-1>', self.verif)

        self.window.mainloop()

    # Get methods for  x1, y1 and x2, y2 coordinates of rectangles to facilitate drawing
    def reset_entries(self):
        self.r1_x_value.set(self.rectangle1.getX())
        self.r1_y_value.set(self.rectangle1.getY())
        self.r2_x_value.set(self.rectangle2.getX())
        self.r2_y_value.set(self.rectangle2.getY())
        self.r1_width_value.set(self.rectangle1.getWidth())
        self.r1_height_value.set(self.rectangle2.getHeight())
        self.r2_width_value.set(self.rectangle2.getWidth())
        self.r2_height_value.set(self.rectangle2.getHeight())

    def draw(self):
        self.canvas.delete('all')

         # Update the instance rectangle 1 specs
        self.rectangle1.setX(self.r1_x_value.get())
        self.rectangle1.setY(self.r1_y_value.get())
        self.rectangle1.setHeight(self.r1_height_value.get())
        self.rectangle1.setWidth(self.r1_width_value.get())

        # Create Rectangle1
        self.canvas.create_rectangle(self.rectangle1.getx1(), self.rectangle1.gety1(), 
                                     self.rectangle1.getx2()+1, self.rectangle1.gety2()+1,
                                     outline = 'blue', tags = 'rectangle1')
        
        # Update the instance rectangle 2 specs
        self.rectangle2.setX(self.r2_x_value.get())
        self.rectangle2.setY(self.r2_y_value.get())
        self.rectangle2.setHeight(self.r2_height_value.get())
        self.rectangle2.setWidth(self.r2_width_value.get())

        # Create Rectangle2
        self.canvas.create_rectangle(self.rectangle2.getx1(), self.rectangle2.gety1(), 
                                     self.rectangle2.getx2()+1, self.rectangle2.gety2(),
                                     outline = 'blue', tags = 'rectangle2')
        
        # Intersection 
        self.intersection_canvas.delete('all')
        self.intersection_canvas.create_text(200,15, text = f"{self.overlaps(self.rectangle1, self.rectangle2)}")
        
    def drag(self, event):
        # For Rectangle 1
        if self.rectangle1.getx1() <= event.x <= self.rectangle1.getx2() \
        and self.rectangle1.gety1() <= event.y <= self.rectangle1.gety2():
            self.canvas.delete('rectangle1')
            
            # Update the instance for rectangle 1
            self.rectangle1.setX(event.x - self.shift_r1_X)
            self.rectangle1.setY(event.y - self.shift_r1_Y)

            self.reset_entries()
            
            # Redraw the rectangle with new specs
            self.canvas.create_rectangle(self.rectangle1.getx1(), self.rectangle1.gety1(), 
                                         self.rectangle1.getx2()+1, self.rectangle1.gety2()+1,
                                         outline = 'blue', tags = 'rectangle1')
            
            self.intersection_canvas.delete('all')
            self.intersection_canvas.create_text(200,15, text = f"{self.overlaps(self.rectangle1, self.rectangle2)}", tags = 'text')
       
        # For Rectangle 2
        if self.rectangle2.getx1() <= event.x <= self.rectangle2.getx2() \
        and self.rectangle2.gety1() <= event.y <= self.rectangle2.gety2():
            self.canvas.delete('rectangle2')
            
            # Update the instance for rectangle 1
            self.rectangle2.setX(event.x - self.shift_r2_X)
            self.rectangle2.setY(event.y - self.shift_r2_Y)

            self.reset_entries()
            
            # Redraw the rectangle with new specs
            self.canvas.create_rectangle(self.rectangle2.getx1(), self.rectangle2.gety1(), 
                                         self.rectangle2.getx2()+1, self.rectangle2.gety2()+1,
                                         outline = 'blue', tags = 'rectangle2')
            # Intersection 
            self.intersection_canvas.delete('all')
            self.intersection_canvas.create_text(200,15, text = f"{self.overlaps(self.rectangle1, self.rectangle2)}", tags = 'text')

    def verif(self, event):
        self.shift_r1_X = event.x - self.rectangle1.getX()
        self.shift_r1_Y = event.y - self.rectangle1.getY()

        self.shift_r2_X = event.x - self.rectangle2.getX()
        self.shift_r2_Y = event.y - self.rectangle2.getY()

RectangleIntersection()
