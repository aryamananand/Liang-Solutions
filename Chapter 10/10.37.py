from tkinter import *
import random

class BinarySearchAnimation:
    def __init__(self):
        self.lst = [random.randint(0,100) for i in range(19)]
        self.low = 0
        self.high = len(self.lst)-1
        self.lst.sort()
        self.index = 0
        window = Tk()
        window.title('Binary Search Animation')
        window.geometry('440x260')
        self.canvas = Canvas(window, bg = 'white', width = 430, height = 200)
        self.canvas.grid(row=0, column=1, sticky = W)

        frame = Frame(window)
        frame.grid(row =1, column = 1)
        Label(frame, text = 'Enter a key (in float): ').grid(row=3,column=1)
        self.item = IntVar()
        self.num_entry = Entry(frame, textvariable = self.item, width = 4, justify = 'right').grid(row=3, column=2 )
        self.btnStep = Button(frame, text = 'Step', command = self.step).grid(row=3, column=3)
        self.btnReset = Button(frame, text = 'Reset', command = self.reset).grid(row=3, column=4) 
        
        self.bar_width = 380/len(self.lst)
        self.start_x = 10
        for u in self.lst:
            self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black')
            self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
            self.start_x += self.bar_width + 1
        
        window.mainloop()

    def step(self):
        self.start_x = 10
        for u in self.lst:
            if u <= self.lst[self.high]:     #to shade grey the selected region
                self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black', fill = 'grey')
                self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
                self.start_x += self.bar_width + 1
            if u >= self.lst[self.high]:
                self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black', fill = 'grey')
                self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
                self.start_x += self.bar_width + 1
        if self.high >= self.low:
            self.mid = (self.high + self.low) // 2
            if self.item.get() <= self.lst[self.mid]:
                self.high = self.mid - 1
                for u in self.lst:
                    self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black', fill = 'grey')
                    self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
                    self.start_x += self.bar_width + 1

            elif self.item.get() == self.mid:       #if key is found
                for u in self.lst:
                    if u != self.item.get():
                        self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black', fill = 'grey')
                        self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
                        self.start_x += self.bar_width + 1
                    else:
                        self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black', fill = 'black')
                        self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
                        
        else:
            self.canvas.create_text(205, 15, text = f"Item '{self.item.get()}'not found.", fill = 'green', font = ('Helvetica', 20))




    def reset(self):
        print()
        
BinarySearchAnimation()