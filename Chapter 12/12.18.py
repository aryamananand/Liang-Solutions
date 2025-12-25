from tkinter import *

class BarChart(Canvas):
    def __init__(self, parent, data, width, height):
        super().__init__(parent, width = width, height = height)
        self.width = width
        self.height = height
        self.data = data
        self.draw_chart()

    def draw_chart(self):
        num_bars = len(self.data)   # number of bars
        bar_width = (self.width - 20)/num_bars   # width of each bar
        x0_var = 10   # x0 point for each bar

        for x in self.data:
            x0 = x0_var 
            y0 = self.height - 15
            x1 = x0_var + bar_width
            y1 = y0 - x[0]     #height of the rectangle
            self.create_rectangle(x0,y0,x1,y1,fill = f"{x[2]}")
            self.create_text((x0+x1)/2, y0 + 10, text = f"{x[1]}")
            x0_var += bar_width

window = Tk()
window.geometry("1000x800")
window.title("2 Barcharts")
data = [[40, "CS", "red"], [30, "IS", "blue"], [50, "IT","yellow"]]
b1 = BarChart(window, data, width = 400, height = 300)
b1.pack()
data = [[140, "Freshman", "red"], [130, "Sophomore", "blue"], 
        [150, "Junior", "yellow"], [80, "Senior", "green"]]
b2 = BarChart(window, data, width = 500, height = 400)
b2.pack()
window.mainloop()
