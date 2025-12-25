from tkinter import *
import sys 

window = Tk()
window.title("Display a graph.")
window.geometry("200x200")

canvas = Canvas(window, height = 190, width = 190, bg = "white")
canvas.pack()

file_name = "/Users/aryamananand/Desktop/PYTHON/PLAINTEXT/GraphVertices.txt"

def get_centre_x(point):
    x1,y1,x2,y2 = canvas.bbox(point)
    return (x1+x2)/2

def get_centre_y(point):
    x1,y1,x2,y2 = canvas.bbox(point)
    return (y1+y2)/2

try:
    main_file = open(file_name, "r")
    num = main_file.readline(1)
    lineCount = 0
    for line in main_file:   
        if lineCount != 0 and line != '':
            newList = line.split(' ')
            newList[len(newList)-1] = newList[len(newList)-1].strip()
            print(newList)
            x = int(newList[1])
            y = int(newList[2])
            canvas.create_oval(x-3,y-3,x+4,y+4, fill='black', tag = f"point{newList[0]}")
        lineCount += 1
        
    main_file.seek(0)

    for line in main_file:
        newList = line.split(' ')
        newList[len(newList)-1] = newList[len(newList)-1].strip()
        for i in range(3,len(newList)):
            canvas.create_line(int(newList[1])+1, int(newList[2])+1, get_centre_x(f"point{newList[i]}"), get_centre_y(f"point{newList[i]}"), fill = "black")

except:
    print("File can't be opened.")
    sys.exit()

window.mainloop()