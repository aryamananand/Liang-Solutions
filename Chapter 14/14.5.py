
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

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
            if x [0] != 0:
                x0 = x0_var 
                y0 = self.height - 15
                x1 = x0_var + bar_width
                y1 = y0 - int(x[0])   #height of the rectangle
                self.create_rectangle(x0,y0,x1,y1,fill = f"{x[2]}")
                self.create_text((x0+x1)/2, y0 + 10, text = f"{x[1]}")
                x0_var += bar_width
            else:
                x1 = x0_var + bar_width
                y1 = self.height
                self.create_rectangle(x0,y0,x1,y1,fill = f"{x[2]}")
                self.create_text((x0+x1)/2, y0 + 10, text = f"{x[1]}")
                x0_var += bar_width


# window = Tk()
# window.geometry("1000x800")
# window.title("2 Barcharts")
# data = [[40, "CS", "red"], [30, "IS", "blue"], [50, "IT","yellow"]]
# b1 = BarChart(window, data, width = 400, height = 300)
# b1.pack()
# data = [[140, "Freshman", "red"], [130, "Sophomore", "blue"], 
#         [150, "Junior", "yellow"], [80, "Senior", "green"]]
# b2 = BarChart(window, data, width = 500, height = 400)
# b2.pack()
# window.mainloop()


class LetterOccurence:
    def __init__(self): 
        window = Tk()
        window.title("Letter Occurence")
        window.geometry("850x350")
        self.frame1 = Frame(window)
        self.frame1.pack()
        

        self.frame2 = Frame(window)
        self.frame2.pack()
        Label(self.frame2,text="Enter a filename: ",width=15).grid(row=1,column=1)
        self.FILENAME = StringVar()
        Entry(self.frame2,width=50,textvariable=self.FILENAME).grid(row=1,column=2)
        Button(self.frame2,text="Browse",command=self.browse,width=5).grid(row=1,column=3)

        Button(self.frame2,text="Show Result",command=self.show_result,width=8).grid(row=1,column=4)

        window.mainloop()
    
    def browse(self):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        try:
            fileToRead = askopenfilename()
            main_file = open(fileToRead,"r")
            string1 = main_file.read()
            self.data = []
            for x in alphabet:
                colour = "white" if ord(x) % 2 == 0 else "grey" # alternate white and grey
                mini_lst = []
                length = len(string1)
                # Normalise the graph
                if length < 200:
                    D = 0.1
                elif length < 1000:
                    D = 1
                else:
                    D = 10
                mini_lst.append(f"{int(string1.count(x)/D)}")
                mini_lst.append(f"{x}")
                mini_lst.append(colour)
                self.data.append(mini_lst)
                self.FILENAME.set(fileToRead)
        except:
            Label(self.frame2,text="File can't be opened!")
    def show_result(self):
        try:
            self.b1.delete('all')
            print(self.data)
            self.b1 = BarChart(self.frame1,self.data,width=520,height=300)
            self.b1.grid(row=1,column=1)
        except:
            print(self.data)
            self.b1 = BarChart(self.frame1,self.data,width=520,height=300)
            self.b1.grid(row=1,column=1)
        

LetterOccurence()