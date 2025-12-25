
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
        self.window.title('Largest Square Block')
        self.window.geometry('350x340')

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
        broke = False
        count = 0   # (each row,column has one separate 'count' sublist for its [size, row, coumn])
        new_list = []   # store [size,row,column]
        for row in range(len(lst)):
            for column in range(len(lst)):
                if lst[row][column] == 1:   # if starting point is 1
                    for size in range(2,min(10-row,10-column)):   # the largest square matrix possible from a value (row,column) 
                                                                # is the smaller value: 10 - row or 10 - column (space remaining)

                        #print('size',size)
                        for t_row in range(row,row+size):
                            for t_column in range(column,column+size):
                                
                                if lst[t_row][t_column] != 1:   # break if some element in the sq mat is not 1
                                    print(f't_row: {t_row}, t_col: {t_column}')
                                    broke = True    
                                    break   # break from t_column loop
                            if broke:   
                                break       # break from t_row loop
                        if broke and size != 0:     # break from size (if size ≠ 0, append to new list with coordinates)
                            new_list.append([])
                            #print(f'for r {row} & c {column}, size = {size-1}')
                            new_list[count].append(size-1)      # save the grid size (of 1s)
                            new_list[count].append(row)         # add the row number
                            new_list[count].append(column)      # add the column number
                            count += 1
                            break
                    
        print('new list: ', new_list)                
        final_list = []
        for x in range(0,len(new_list),3):
            final_list.append(new_list[x][0])
        real_lst = sorted(final_list)  # sort in ascending order (sizes of different square mats across grid)
        print('real list:',real_lst)
        biggest_grid = real_lst[len(real_lst)-1]  #biggest term
        for i in range(0,len(new_list)-1,3):
            if biggest_grid == new_list[i] and new_list != [] :
                self.Xval = new_list[i+1]    # start x for HIGHLIGHTING
                self.Yval = new_list[i+2]    # start y for HIGHLIGHTING
                self.size = biggest_grid     # size of HIGHLIGHT square matrix
                break

    def findButton(self):
        for ro in range(10):
            for co in range(10):
               self.Box_list[ro][co] = Entry(self.window,width=2,justify='center',textvariable = self.lst[ro][co]).grid(row=ro,column=co)
        
        for r in range(10):
            for q in range(10):
                self.Entry_list[r][q] = int(self.lst[r][q].get())

        self.findLargestBlock(self.Entry_list)
        for row in range(self.Xval,self.Xval+self.size):
            for column in range(self.Yval,self.Yval+self.size):
                self.Box_list[row][column] = Entry(self.window,width=2,justify='center',textvariable=self.lst[row][column],bg = 'gray')
                self.Box_list[row][column].grid(row=row,column=column)
        
    def refresh(self):
        for i in range(10):
            for j in range(10):
               self.lst[i][j] = StringVar()
               self.Box_list[i][j] = Entry(self.window,width=2,justify='center',textvariable = self.lst[i][j]).grid(row=i,column=j)
               self.lst[i][j].set(str(rand.randint(0,1)))

LargestBlock()

