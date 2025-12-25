from tkinter import *

class TextFormat:
    def __init__(self):
        self.window = Tk()
        self.window.title("Radio buttons and Buttons")
        self.window.geometry('410x410')
        self.x = 200    #Starting position of text
        self.y = 200    #Starting position of text
        self.step = 10  #Step size 



        self.canvas = Canvas(self.window, height = 300, width = 400, bg = 'white')
        self.canvas.grid(row = 2, column = 1)
        self.canvas.create_text(self.x, self.y, text = 'Text Sample', fill = 'black', tags = 'tex')

        self.frame = Frame(self.window)
        self.frame.grid(row = 1, column = 1)

        self.redVar = IntVar()
        Radiobutton(self.frame, text = 'Red', variable = self.redVar, value = 1, command = self.red).grid(row = 1, column = 1)
        self.yellowVar = IntVar()
        Radiobutton(self.frame, text = 'Yellow', variable = self.yellowVar, value = 1, command = self.yellow).grid(row = 1, column = 2)
        self.whiteVar = IntVar()
        Radiobutton(self.frame, text = 'White', variable = self.whiteVar, value = 1, command = self.white).grid(row = 1, column = 3)
        self.whiteVar.set(1)
        self.greyVar = IntVar()
        Radiobutton(self.frame, text = 'Grey', variable = self.greyVar, value = 1, command = self.grey).grid(row = 1, column = 4)
        self.greenVar = IntVar()
        Radiobutton(self.frame, text = 'Green', variable = self.greenVar, value = 1, command = self.green).grid(row = 1, column = 5)

        self.frame2 = Frame(self.window)
        self.frame2.grid(row = 3, column = 1)

        Button(self.frame2, text = '<=', command = self.moveLeft).grid(row = 1, column = 1)
        Button(self.frame2, text = '=>', command = self.moveRight).grid(row = 1, column = 2)

        self.window.mainloop()

    def moveLeft(self):
        if self.x > 50:
            self.x -= self.step
            self.canvas.delete('tex')
            self.canvas.create_text(self.x, self.y, text = 'Text Sample', fill = 'black', tags = 'tex')
    def moveRight(self):
        if self.x < 360:
            self.x += self.step
            self.canvas.delete('tex')
            self.canvas.create_text(self.x, self.y, text = 'Text Sample', fill = 'black', tags = 'tex')
    def red(self):
        if self.redVar.get() == 1:
            self.canvas.create_rectangle(0,0, 410, 410, fill = 'red')
            self.canvas.create_text(self.x, self.y, text = 'Text Sample', fill = 'black', tags = 'tex')
            self.yellowVar.set(0)
            self.whiteVar.set(0)
            self.greyVar.set(0)
            self.greenVar.set(0)
    def yellow(self):
        if self.yellowVar.get() == 1:
            self.canvas.create_rectangle(0,0, 410, 410, fill = 'yellow')
            self.canvas.create_text(self.x, self.y, text = 'Text Sample', fill = 'black', tags = 'tex')
            self.redVar.set(0)
            self.whiteVar.set(0)
            self.greyVar.set(0)
            self.greenVar.set(0)
    def white(self):
        if self.whiteVar.get() == 1:
            self.canvas.create_rectangle(0,0, 410, 410, fill = 'white')
            self.canvas.create_text(self.x, self.y, text = 'Text Sample', fill = 'black', tags = 'tex')
            self.redVar.set(0)
            self.yellowVar.set(0)
            self.greyVar.set(0)
            self.greenVar.set(0)
    def grey(self):
        if self.greyVar.get() == 1:
            self.canvas.create_rectangle(0,0, 410, 410, fill = 'grey')
            self.canvas.create_text(self.x, self.y, text = 'Text Sample', fill = 'black', tags = 'tex')
            self.redVar.set(0)
            self.yellowVar.set(0)
            self.whiteVar.set(0)
            self.greenVar.set(0)
    def green(self):
        if self.greenVar.get() == 1:
            self.canvas.create_rectangle(0,0, 410, 410, fill = 'green')
            self.canvas.create_text(self.x, self.y, text = 'Text Sample', fill = 'black', tags = 'tex')
            self.redVar.set(0)
            self.yellowVar.set(0)
            self.whiteVar.set(0)
            self.greyVar.set(0)
    
TextFormat()