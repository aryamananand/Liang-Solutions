from tkinter import *

class LineDrawer:
    def __init__(self):
        window = Tk()
        window.title('Line Drawer')
        window.geometry('410x410')
        self.canvas = Canvas(window, bg = 'white', width = 400, height = 400)
        self.canvas.grid()
        self.startX = 200
        self.startY = 200
        self.step = 20

        self.canvas.bind("<Right>", self.rightEvent)
        self.canvas.focus_set()
        
        self.canvas.bind("<Left>", self.leftEvent)
        self.canvas.focus_set()

        self.canvas.bind("<Up>", self.upEvent)
        self.canvas.focus_set()

        
        self.canvas.bind("<Down>", self.downEvent)
        self.canvas.focus_set()
        

        window.mainloop()
        
    def rightEvent(self, event):
        
        self.x = self.startX + self.step
        self.y = self.startY
        self.canvas.create_line(self.startX, self.startY, self.x, self.y, width = 2, fill = 'black')
        self.startX += self.step

    def leftEvent(self, event):
        
        self.x = self.startX - self.step
        self.y = self.startY
        self.canvas.create_line(self.startX, self.startY, self.x, self.y, width = 2, fill = 'black')
        self.startX -= self.step

    def upEvent(self, event):
        self.x = self.startX
        self.y = self.startY - self.step
        self.canvas.create_line(self.startX, self.startY, self.x, self.y, width = 2, fill = 'black')
        self.startY -= self.step

    def downEvent(self, event):
        self.x = self.startX
        self.y = self.startY + self.step
        self.canvas.create_line(self.startX, self.startY, self.x, self.y, width = 2, fill = 'black')
        self.startY += self.step
        
LineDrawer()