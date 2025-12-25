from tkinter import *
import random 

px = 5
total_balls = 10
window = Tk()
window.title('Random Balls')
window.geometry('410x410')
canvas = Canvas(window, height = 400, width = 400, bg = 'white')
canvas.grid()



for ballCount in range (total_balls):
    x = random.randint(0, 400)
    y = random.randint(0, 400)

    loc = ['blue', 'green', 'red', 'pink', 'yellow', 'white', 'black', 'cyan', 'orange', 'SpringGreen2']
    colour = random.choice(loc)
    canvas.create_oval(x - px, y - px, x + px + 1, y + px + 1, fill = str(colour))

window.mainloop()