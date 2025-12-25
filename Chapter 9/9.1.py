from tkinter import *

class CanvasDemo:
    def __init__(self):
        self.dist = 10
        self.x = 0
        self.y = 0 
        window = Tk()
        window.title('Move the Ball')

        self.canvas = Canvas(window, width = 500, height = 300, bg = 'white')
        self.canvas.grid()

        frame = Frame(window)
        frame.grid()
        left = Button(frame, text = 'Left', command = self.ballLeft)
        right = Button(frame, text = 'Right', command = self.ballRight)
        up = Button(frame, text = 'Up', command = self.ballUp)
        down = Button(frame, text = 'Down', command = self.ballDown)

        #Set up buttons on mainscreen (window)
        up.grid(row = 1, column = 1)
        down.grid(row = 1, column = 2)
        left.grid(row = 1, column = 3)
        right.grid(row = 1, column = 4)

        self.canvas.create_oval(100, 100, 50, 50, fill = 'red', tags = 'circle')
        
        window.mainloop()

    #Define buttons' commands
    def ballRight(self):
        if self.x <= 370:
            dx = self.dist
            self.canvas.move('circle', dx, 0)
            self.x += 10
    def ballDown(self):
        if self.y <= 190:
            dy = self.dist
            self.canvas.move('circle', 0, dy)
            self.y += 10
    def ballLeft(self):
        if self.x >= -30:
            dx = -1 * self.dist
            self.canvas.move('circle', dx, 0)
            self.x -= 10
    def ballUp(self):
        if self.y >= -30:
            dy = -1 * self.dist
            self.canvas.move('circle', 0, dy)
            self.y -= 10
 

CanvasDemo()