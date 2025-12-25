from tkinter import *


COUNT_LIMIT = 60

def paint():
    x = -2.0
    while x < 2.0:
        y = -2.0
        while y < 2.0:
            c = count(complex(x, y))
            if c == COUNT_LIMIT:
                colour = 'blue2' # c is in a Mandelbrot set
            elif 40 < c < COUNT_LIMIT:
                colour = 'goldenrod1'
            elif 20 < c < 40:
                colour = 'magenta2'
            elif 15 < c < 20:
                colour = "black"
            elif 8 < c <= 15:
                colour = 'pink'
            elif 4 <= c < 8:
                colour = "AntiqueWhite"
            elif 2.5 <= c <= 4:
                colour = 'white'
            elif 1 < c < 2.5:
                colour = 'sienna1'
            elif 0.5 < c < 1:
                colour = 'limegreen'
            else: colour = 'black'

            # Fill a tiny rectangle with the specified colour
            canvas.create_rectangle(x * 100 + 200, y * 100 + 200,
                x * 100 + 200 + 6, y * 100 + 200 + 6, fill = colour)
            y += 0.05
        x += 0.05


# Return the iteration count
def count(c):
    z = complex(0, 0) # z0

    for i in range(COUNT_LIMIT):
        z = z * z + c # Get z1, z2, ...
        if abs(z) > 2: return i # The sequence is unbounded

    return COUNT_LIMIT # Indicate a bounded sequence

window = Tk()
window.title('Mandelbrot Fractal')
window.geometry('420x450')

canvas = Canvas(window,width=400,height=400,bg='white')
canvas.pack()

button = Button(window, text = 'Display', command = paint)
button.pack()

window.mainloop()