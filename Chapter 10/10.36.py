from tkinter import *
import random 

class LinearSearchAnimation:
    def __init__(self):
        self.var = 0    #to prevent self.index += 1
        self.lst = [random.randint(0,100) for i in range(20)]
        self.index = 0
        window = Tk()
        window.title('Linear Search Animation')
        window.geometry('410x260')
        self.canvas = Canvas(window, bg = 'white', width = 400, height = 200)
        self.canvas.grid(row=0, column=1, sticky = W)

        self.frame = Frame(window)
        self.frame.grid(row =1, column = 1)
        Label(self.frame, text = 'Enter a key (in float): ').grid(row=3,column=1)
        self.item = IntVar()
        self.num_entry = Entry(self.frame, textvariable = self.item, width = 4, justify = 'right').grid(row=3, column=2 )
        self.btnStep = Button(self.frame, text = 'Step', command = self.step).grid(row=3, column=3)
        self.btnReset = Button(self.frame, text = 'Reset', command = self.reset).grid(row=3, column=4) 
        
        self.bar_width = 380/len(self.lst)
        self.start_x = 10
        for u in self.lst:
            self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black')
            self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
            self.start_x += self.bar_width + 1
        
        window.mainloop()

    def reset(self):
        self.canvas.delete('all')
        self.item.set(0)
        self.index = 0
        self.lst = [random.randint(0,100) for i in range(20)]
        self.bar_width = 380/len(self.lst)
        self.start_x = 10
        for u in self.lst:
            self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black')
            self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
            self.start_x += self.bar_width + 1

    def step(self):
        count = 0   #variable to prevent 2 similar items from being selected
        self.start_x = 10
        self.canvas.delete('all')
        for u in self.lst:
            if u != self.lst[self.index]:
                self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black')
                self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
            elif count == 0:
                self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black', fill = 'grey')
                self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black')
                if u == self.item.get():
                    self.canvas.create_text(205, 15, text = f"Item '{self.item.get()}' found.", fill = 'green', font = ('Helvetica', 20))
                    self.index = -1
                    self.var == 1   #to prevent self.index += 1
                    count = 1
            self.start_x += self.bar_width + 1
        if u != self.item.get() and self.index < len(self.lst):
            self.index += 1
            



LinearSearchAnimation()        

    # CODE TO SKIP ANIMATION:
    # def step(self):
    #     self.canvas.delete('all')
    #     self.start_x = 10
    #     for u in self.lst:
    #         if u != self.item.get():
    #             self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black')
    #             self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black') 
    #         else:
    #             self.canvas.create_rectangle(self.start_x, 180-u, self.start_x + self.bar_width+1, 181, outline = 'black', fill = 'grey')
    #             self.canvas.create_text(self.start_x + self.bar_width/2, 170 - u, text = u, fill = 'black')
    #         self.start_x += self.bar_width + 1

