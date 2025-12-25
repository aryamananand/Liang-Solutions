from tkinter import *
import random 

class RacingCars(Canvas):
    def __init__(self):
        self.window = Tk()
        self.window.title("Racing Cars")
        self.window.geometry('1000x400')

        self.x = 0
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0

        self.canvas = Canvas(self.window, height = 100, width = 1000)
        self.canvas.grid(row=1, column=1)
        self.canvas.create_rectangle(self.x, 280, self.x + 50, 290, fill = 'blue')
        self.canvas.create_polygon(self.x + 10, 280, self.x + 20, 270, self.x + 30, 270, self.x + 40, 280, fill = 'red', outline = 'black')
        self.canvas.create_oval(self.x + 10, 290, self.x + 20, 300, fill = 'black', outline = 'black')
        self.canvas.create_oval(self.x + 30, 290, self.x + 40, 300, fill = 'black', outline = 'black')

        self.canvas1 = Canvas(self.window, height = 100, width = 1000)
        self.canvas1.grid(row=2,column=1)
        self.canvas1.create_rectangle(self.x1, 280, self.x1 + 50, 290, fill = 'blue')
        self.canvas1.create_polygon(self.x1 + 10, 280, self.x1 + 20, 270, self.x1 + 30, 270, self.x1 + 40, 280, fill = 'red', outline = 'black')
        self.canvas1.create_oval(self.x1 + 10, 290, self.x1+ 20, 300, fill = 'black', outline = 'black')
        self.canvas1.create_oval(self.x1 + 30, 290, self.x1 + 40, 300, fill = 'black', outline = 'black')

        self.canvas2 = Canvas(self.window, height = 100, width = 1000)
        self.canvas2.grid(row=3,column=1)
        self.canvas2.create_rectangle(self.x2, 280, self.x2 + 50, 290, fill = 'blue')
        self.canvas2.create_polygon(self.x2 + 10, 280, self.x2 + 20, 270, self.x2 + 30, 270, self.x2 + 40, 280, fill = 'red', outline = 'black')
        self.canvas2.create_oval(self.x2 + 10, 290, self.x2 + 20, 300, fill = 'black', outline = 'black')
        self.canvas2.create_oval(self.x2 + 30, 290, self.x2 + 40, 300, fill = 'black', outline = 'black')


        self.canvas3 = Canvas(self.window, height = 100, width = 1000)
        self.canvas3.grid(row=4,column=1)
        self.canvas3.create_rectangle(self.x3, 280, self.x3 + 50, 290, fill = 'blue')
        self.canvas3.create_polygon(self.x3 + 10, 280, self.x3 + 20, 270, self.x3 + 30, 270, self.x3 + 40, 280, fill = 'red', outline = 'black')
        self.canvas3.create_oval(self.x3 + 10, 290, self.x3 + 20, 300, fill = 'black', outline = 'black')
        self.canvas3.create_oval(self.x3 + 30, 290, self.x3 + 40, 300, fill = 'black', outline = 'black')


        Button(self.window, text = "Start Race", command = self.race).grid(row=5,column=1)

        
        self.window.mainloop()

    def race(self):

        if self.game == True:

            self.canvas.create_rectangle(self.x, 280, self.x + 50, 290, fill = 'blue')
            self.canvas.create_polygon(self.x + 10, 280, self.x + 20, 270, self.x + 30, 270, self.x + 40, 280, fill = 'red', outline = 'black')
            self.canvas.create_oval(self.x + 10, 290, self.x + 20, 300, fill = 'black', outline = 'black')
            self.canvas.create_oval(self.x + 30, 290, self.x + 40, 300, fill = 'black', outline = 'black')

            self.dx = random.randint(1,5)
            self.x += int(self.dx)

            self.canvas1.create_rectangle(self.x1, 280, self.x1 + 50, 290, fill = 'blue')
            self.canvas1.create_polygon(self.x1 + 10, 280, self.x1 + 20, 270, self.x1 + 30, 270, self.x1 + 40, 280, fill = 'red', outline = 'black')
            self.canvas1.create_oval(self.x1 + 10, 290, self.x1+ 20, 300, fill = 'black', outline = 'black')
            self.canvas1.create_oval(self.x1 + 30, 290, self.x1 + 40, 300, fill = 'black', outline = 'black')
            
            self.dx = random.randint(1,5)
            self.x1 += int(self.dx)


            
            self.canvas2.create_rectangle(self.x2, 280, self.x2 + 50, 290, fill = 'blue')
            self.canvas2.create_polygon(self.x2 + 10, 280, self.x2 + 20, 270, self.x2 + 30, 270, self.x2 + 40, 280, fill = 'red', outline = 'black')
            self.canvas2.create_oval(self.x2 + 10, 290, self.x2 + 20, 300, fill = 'black', outline = 'black')
            self.canvas2.create_oval(self.x2 + 30, 290, self.x2 + 40, 300, fill = 'black', outline = 'black')

            self.dx = random.randint(1,5)
            self.x2 += int(self.dx)

            
            self.canvas3.create_rectangle(self.x3, 280, self.x3 + 50, 290, fill = 'blue')
            self.canvas3.create_polygon(self.x3 + 10, 280, self.x3 + 20, 270, self.x3 + 30, 270, self.x3 + 40, 280, fill = 'red', outline = 'black')
            self.canvas3.create_oval(self.x3 + 10, 290, self.x3 + 20, 300, fill = 'black', outline = 'black')
            self.canvas3.create_oval(self.x3 + 30, 290, self.x3 + 40, 300, fill = 'black', outline = 'black')

            self.dx = random.randint(1,5)
            self.x3 += int(self.dx)

            self.canvas.after(100)
            self.canvas.update()    

            self.canvas1.after(100)
            self.canvas1.update()  

            self.canvas2.after(100)
            self.canvas3.update()  

            self.canvas3.after(100)
            self.canvas3.update()   

            

            a = True
            b = True
            c = True
            d = True

            if self.x <= 950:
                self.move_car(self.x)
                a = False
            if self.x1 <= 950:
                self.move_car(self.x1)
                b = False
            if self.x2 <= 950:
                self.move_car(self.x2)
                c = False
            if self.x3 <= 950:
                self.move_car(self.x3)
                d = False
            if a == b == c == d == True:
                self.game = False

            self.race()

        else:
            self.canvas2.create_text(200,50,text = "RACE OVER.", font = "Helvetica 12 Bold")

RacingCars()
