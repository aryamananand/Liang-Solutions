from tkinter import *

class RacingCar:
    def __init__(self):
        window = Tk()
        window.title('Racing Car')
        window.geometry('1000x400')
        self.canvas = Canvas(window, width = 1000, height = 800, bg = 'white')
        self.canvas.grid()
        self.dx = 5
        self.x = 5   #VARIABLE
        #y = 300    #CONSTANT
    
        self.canvas.bind('<Up>', self.speedUp)
        self.canvas.focus_set()

        self.canvas.bind('<Down>', self.speedDown)
        self.canvas.focus_set()

        while True:
            
            if self.x >= 950:
                self.x = 0
            self.canvas.delete('all')
            self.canvas.create_rectangle(self.x, 280, self.x + 50, 290, fill = 'blue')
            self.canvas.create_polygon(self.x + 10, 280, self.x + 20, 270, self.x + 30, 270, self.x + 40, 280, fill = 'red', outline = 'black')
            self.canvas.create_oval(self.x + 10, 290, self.x + 20, 300, fill = 'black', outline = 'black')
            self.canvas.create_oval(self.x + 30, 290, self.x + 40, 300, fill = 'black', outline = 'black')


            self.x += int(self.dx)

            self.canvas.after(100)
            self.canvas.update()

            

        window.mainloop()

    def speedUp(self, event):
        self.dx = self.dx * 1.2

    def speedDown(self, event):
        if self.dx >= 3:
            self.dx = self.dx / 1.15

    

RacingCar()