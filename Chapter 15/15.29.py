from tkinter import *

class HTreeFractal:
    def __init__(self):
        self.window = Tk()
        self.window.title("H-Tree Fractal")
        self.window.geometry("630x690")

        self.canvas = Canvas(self.window, bg = "white", height = 600, width = 600)
        self.canvas.grid(row=1,column=1) 
        self.frame = Frame(self.window).grid(row=2,column=1)
        Label(self.frame, text = "Enter an order:").grid(row=2,column=1)
        self.order = StringVar()
        self.entry = Entry(self.frame,textvariable=self.order,justify="center").grid(row=3,column=1)
        self.button = Button(self.frame, text = "Display", command = self.draw_HTreeFractal).grid(row=4,column=1)
        self.window.mainloop()

    def draw_HTreeFractal(self):
        self.canvas.delete('all')
        depth = int(eval(self.order.get()))

        self.draw(300,300,150,depth)
        
    def draw(self,x,y,size,order):
        if order == 0:
            return
        else:
            #top left point
            x0 = x - size
            y0 = y - size
            #bottom right point
            x1 = x + size
            y1 = y + size

            self.canvas.create_line(x0,y,x1,y,fill="black")
            self.canvas.create_line(x0,y0,x0,y1,fill = "black")        
            self.canvas.create_line(x1,y0,x1,y1,fill = "black")

            self.draw(x0,y0,size/2,order-1)
            self.draw(x0,y1,size/2,order-1)
            self.draw(x1,y0,size/2,order-1)
            self.draw(x1,y1,size/2,order-1)

HTreeFractal()