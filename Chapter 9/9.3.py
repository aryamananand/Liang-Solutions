from tkinter import *

class Drawer:
    def __init__(self):
        window = Tk()
        window.title('Radiobuttons and Checkbuttons')
        self.canvas = Canvas(window, width = 400, height = 300, bg = 'white')
        self.canvas.grid(row = 1, column = 1)
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

        frame = Frame(window).grid()
        
        self.rect = IntVar()
        self.radbtRectangle = Radiobutton(frame, text = 'Rectangle', variable = self.rect, value = 1, command = self.processRadiobutton)
        self.oval = IntVar()
        self.radbtOval = Radiobutton(frame, text = 'Oval', variable = self.oval, value = 1, command = self.processRadiobutton2)
        self.Filled = IntVar()
        self.cbt = Checkbutton(frame, text = 'Filled', variable = self.Filled, command = self.fillCheck)
        self.radbtRectangle.grid(row = 2, column = 1)
        self.radbtOval.grid(row = 2, column = 2)
        self.cbt.grid(row = 2, column = 3)
        window.mainloop()

    def processRadiobutton(self):
        if self.rect.get() == 1:
            self.canvas.create_rectangle (10, 10, 350, 200, outline = 'black', fill = 'white', tags = 'rect')
            self.canvas.delete('oval')
            self.radbtOval.deselect()
            self.fillCheck()
    def processRadiobutton2(self):
        if self.oval.get() == 1:
            self.canvas.create_oval (10, 10, 190, 90, outline = 'black', fill = 'white', tags = 'oval')
            self.canvas.delete('rect')
            self.radbtRectangle.deselect()
            self.fillCheck()
    def fillCheck(self):
        if self.Filled.get() == 1 and self.rect.get() == 1:
            self.canvas.create_rectangle (10, 10, 350, 200, fill = 'blue', tags = 'rect')
        elif self.Filled.get() == 1 and self.oval.get() == 1:
            self.canvas.create_oval (10, 10, 190, 90, fill = 'blue', tags = 'oval')
        elif self.Filled.get() == 0 and self.rect.get() == 1:
            self.canvas.create_rectangle (10, 10, 350, 200, outline = 'black', fill = 'white', tags = 'rect')
        elif self.Filled.get() == 0 and self.oval.get() == 1:
            self.canvas.create_oval (10, 10, 190, 90, outline = 'black', fill = 'white', tags = 'oval')

Drawer()