# TO REDO PROBLEM 
# find largest block with 1s

from tkinter import *
import random as rand

class LargestBlock:
    def __init__(self):
        # List of textvariables (one textvariable for each entry box)
        self.lst = []
        for i in range(10):
            self.lst.append([])
            for j in range(10):
                self.lst[i].append('')

        # List of entries 
        self.Entry_list = []
        for k in range(10):
            self.Entry_list.append([])
            for l in range(10):
                self.Entry_list[k].append('')

        # List for entry boxes
        self.Box_list = []
        for f in range(10):
            self.Box_list.append([])
            for g in range(10):
                self.Box_list[f].append('')

        # Mainscreen (window)
        self.window = Tk()
        self.window.title('Largest 3x3 Block')
        self.window.geometry('305x310')

        # Create textboxes in a grid pattern
        for i in range(10):
            for j in range(10):
               self.lst[i][j] = StringVar()
               self.Box_list[i][j] = Entry(self.window,width=2,justify='center',textvariable = self.lst[i][j]).grid(row=i,column=j)
               self.lst[i][j].set(str(rand.randint(0,1)))

        # Create solve button
        b = Button(self.window, text = 'Refresh',command = self.refresh,bg = 'white')
        b.grid(row=11,column=0,columnspan=5,sticky='ew')
        b1 = Button(self.window, text = 'Find Largest Block', command = self.findButton,bg = 'white')
        b1.grid(row=11,column=5,columnspan = 5,sticky='ew')
        
        self.window.mainloop()

    def findLargestBlock(self,lst):
        new_list = []   # structure: [sum of boxes1, principal row1, principal column1, sum of...]
        for row in range(len(lst)-2):
            for column in range(len(lst)-2):
                var = 0
                for i in range (row,row+3):
                    for j in range(column,column+3):
                        var += lst[i][j]
                new_list.append(var)
                new_list.append(row)
                new_list.append(column) 
                
        temp_list = []      # to keep track of largest block location
        for i in range(0,len(new_list),3):  # make list with only sum of boxes (every three from new_list)
            temp_list.append(new_list[i])
        a = max(temp_list)  # # check which (sum of boxes) is largest from list of (sum of boxes)
        for i in range(0,len(new_list),3):
             if new_list[i] == a:   # match with new_list
                self.row_largestBlock = new_list[i+1]    #obtain principal row number (beside the sum value)
                self.column_largestBlock = new_list[i+2] #obtain principal column number (beside row value)

    def findButton(self):   # to HIGHLIGHT the largest block
        for ro in range(10):
            for co in range(10):
               self.Box_list[ro][co] = Entry(self.window,width=2,justify='center',textvariable = self.lst[ro][co]).grid(row=ro,column=co)

        #convert to Entry_list for checking
        for r in range(10):
            for q in range(10):
                self.Entry_list[r][q] = int(self.lst[r][q].get())

        self.findLargestBlock(self.Entry_list)
        for row in range(self.row_largestBlock,self.row_largestBlock+3):
            for column in range(self.column_largestBlock,self.column_largestBlock+3):
                self.Box_list[row][column] = Entry(self.window,width=2,justify='center',textvariable=self.lst[row][column],bg = 'gray')
                self.Box_list[row][column].grid(row=row,column=column)
        
    def refresh(self):
        for i in range(10):
            for j in range(10):
               self.lst[i][j] = StringVar()
               self.Box_list[i][j] = Entry(self.window,width=2,justify='center',textvariable = self.lst[i][j]).grid(row=i,column=j)
               self.lst[i][j].set(str(rand.randint(0,1)))

LargestBlock()