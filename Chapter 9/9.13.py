from tkinter import *

class Mouse:
    def __init__(self):
        window = Tk()
        window.title('Event Specififer')
        self.canvas = Canvas(window, bg = 'white', width = 400, height = 400)
        self.canvas.grid()

        self.canvas.bind('<Button-1>', self.processMouseEvent)
        self.canvas.focus_set()
        window.mainloop()


    def processMouseEvent(self, event):
        self.canvas.delete('all')
        str1 = '(' + str(event.x) + ', ' + str(event.y) + ')'
        self.canvas.create_text(event.x, event.y - 30, text = str1, fill = 'black')
        print(str1)

Mouse()