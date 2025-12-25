from tkinter import *

class Mouse:
    def __init__(self):
        window = Tk()
        window.title('Event Specififer')
        self.canvas = Canvas(window, bg = 'white', width = 400, height = 400)
        self.canvas.grid()

        self.canvas.bind('<Button-1>', self.processMouseEvent)
        self.canvas.bind('<ButtonRelease-1>', self.processEvent)
        window.mainloop()


    def processMouseEvent(self, event):
        self.canvas.create_text(event.x_root, event.y_root, text = f"({str(event.x_root)}, {str(event.y_root)})", width = 3, fill = 'black')

    def processEvent(self, event):
        self.canvas.delete('all')

Mouse()