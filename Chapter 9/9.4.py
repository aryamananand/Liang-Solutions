from tkinter import *

window = Tk()
window.title('Rectangles')
window.geometry('510x410')


canvas = Canvas(window, bg = 'white', width = 500, height = 400)
canvas.grid()


i = 1
while i < 202:
    canvas.create_rectangle(i, i, 502 - i, 402 - i, outline = 'black', tags = 'rect')
    i += 10

window.mainloop()
