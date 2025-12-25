from tkinter import *

window = Tk()
window.title('Canvas Chessboard')
window.geometry('400x400')




for rowf in range(1,9):
    columnf = 1
    if rowf % 2 == 0:
        for columnf in range(1,9):
            if columnf % 2 == 0:
                white = Canvas(window, bg = 'white', width = 30, height = 30)
                white.grid(row = rowf, column = columnf)
            else:
                black = Canvas(window, bg = 'black', width = 30, height = 30)
                black.grid(row = rowf, column = columnf)
            
    else:
        for columnf in range(1, 9):
            if columnf % 2 != 0:
                white = Canvas(window, bg = 'white', width = 30, height = 30)
                white.grid(row = rowf, column = columnf)
            else:
                black = Canvas(window, bg = 'black', width = 30, height = 30)
                black.grid(row = rowf, column = columnf)
            
window.mainloop()