from tkinter import *

window = Tk()
window.title('Canvas Chessboard')
window.geometry('400x400')


rowf = 1
while rowf < 9:
    columnf = 1
    if rowf % 2 == 0:
        while columnf < 9:
            if columnf % 2 == 0:
                white = Canvas(window, bg = 'white', width = 30, height = 30)
                white.grid(row = rowf, column = columnf)
            else:
                black = Canvas(window, bg = 'black', width = 30, height = 30)
                black.grid(row = rowf, column = columnf)
            columnf += 1
    else:
        while columnf < 9:
            if columnf % 2 != 0:
                white = Canvas(window, bg = 'white', width = 30, height = 30)
                white.grid(row = rowf, column = columnf)
            else:
                black = Canvas(window, bg = 'black', width = 30, height = 30)
                black.grid(row = rowf, column = columnf)
            columnf += 1
        
    rowf += 1

window.mainloop()