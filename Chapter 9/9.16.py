from tkinter import *

#Create a fan
bladeSize = 30


window = Tk()
window.title('Running Fan')
window.geometry('410x410')

canvas = Canvas(window, width = 400, height = 400, bg = 'white') 
canvas.grid()

x = 0
while True:


    canvas.delete('all')

    canvas.create_arc(0, 0, 401, 401, start = x, extent = bladeSize, fill = 'black', tags = 'arc1')
    canvas.create_arc(0, 0, 401, 401, start = x + 90, extent = bladeSize, fill = 'black', tags = 'arc2')
    canvas.create_arc(0, 0, 401, 401, start = x + 180, extent = bladeSize, fill = 'black', tags = 'arc3')
    canvas.create_arc(0, 0, 401, 401, start = x + 270, extent = bladeSize, fill = 'black', tags = 'arc4')

    canvas.update()
    canvas.after(10)

    x += 3







window.mainloop()



