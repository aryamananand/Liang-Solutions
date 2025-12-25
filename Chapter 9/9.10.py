from tkinter import *


window = Tk()
window.title('Pie Chart')
window.geometry('410x410')

canvas = Canvas(window, width = 410, height = 410, bg = 'white')
canvas.grid()

canvas.create_arc(0, 0, 401, 401, start = 0, extent = 72, width = 1, outline = 'black', fill = 'red')
canvas.create_arc(0, 0, 401, 401, start = 72, extent = 36, width = 1, outline = 'black', fill = 'blue')
canvas.create_arc(0, 0, 401, 401, start = 108, extent = 108, width = 1, outline = 'black', fill = 'green')
canvas.create_arc(0, 0, 401, 401, start = 216, extent = 144, width = 1, outline = 'black', fill = 'orange')


canvas.create_text(300, 300, text = 'Final -- 40%')
canvas.create_text(300, 70, text = 'Project -- 20 %')
canvas.create_text(200, 40, text = 'Quizzes -- 10%')
canvas.create_text(100, 180, text = 'Midterm -- 30%')
window.mainloop() 