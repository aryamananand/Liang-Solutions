from tkinter import *

class Consecutive4GUI:
    def __init__(self):
        # List of textvariables (one textvariable for each entry box)
        self.lst = []
        for i in range(6):
            self.lst.append([])
            for j in range(6):
                self.lst[i].append(0)

        # List of entries 
        self.Entry_list = []
        for k in range(6):
            self.Entry_list.append([])
            for l in range(6):
                self.Entry_list[k].append('')

        # List for entry boxes
        self.Box_list = []
        for f in range(6):
            self.Box_list.append([])
            for g in range(6):
                self.Box_list[f].append('')

        # Mainscreen (window)
        self.window = Tk()
        self.window.title('Consecutive Four')
        self.window.geometry('250x200')

        # Create textboxes in a grid pattern
        for i in range(6):
            for j in range(6):
               self.lst[i][j] = StringVar()
               self.Box_list[i][j] = Entry(self.window,width=2,textvariable = self.lst[i][j],justify='center')
               self.Box_list[i][j].grid(row=i,column=j+2)
               self.lst[i][j].set('0')

        # Create solve button
        Button(self.window, text = 'Solve', command = self.solve,bg = 'white').grid(row=6,column=4,columnspan=2,sticky='ew')
        self.window.mainloop()

    def isConsecutiveFour(self, lst):
        final_lst = [0,0,0,0]
        self.consecutiveListIndex = []
        self.check = None
        # Check rows
        for r in range(len(lst)):
            for c in range(len(lst[r])-3):
                if lst[r][c] == lst[r][c+1] == lst[r][c+2] == lst[r][c+3] != '0':
                    final_lst[0] = 1 
                    self.consecutiveListIndex.append(r)
                    self.consecutiveListIndex.append(c)
                    self.check = 1
                    break

        # Check columns if rows are not true (i.e. consecutive 4)
        if final_lst[0] != 1:
            for c in range(len(lst[0])):
                for r in range(len(lst)-3):
                    if lst[r][c] == lst[r+1][c] == lst[r+2][c] == lst[r+3][c] != '0':
                        final_lst[1] = 1
                        self.consecutiveListIndex.append(r)
                        self.consecutiveListIndex.append(c)
                        self.check = 2
                        break 
                        
            # if list is already true, then don't check diagonals
            if final_lst[1] != 1:
                # Check diagonals --> top left to bottom right
                for r in range(len(lst)-3):
                    for c in range(len(lst[0])-3):
                        if lst[r][c] == lst[r+1][c+1] == lst[r+2][c+2] == lst[r+3][c+3] != '0':
                            final_lst[2] = 1
                            self.consecutiveListIndex.append(r)
                            self.consecutiveListIndex.append(c)
                            self.check = 3
                            break
                # Check diagonals --> top right to bottom left 
                if final_lst[2] != 1:
                    for r in range(len(lst)-1,2,-1):
                        for c in range(len(lst[0])-3):
                            if lst[r][c] == lst[r-1][c+1] == lst[r-2][c+2] == lst[r-3][c+3] != '0':
                                final_lst[3] = 1
                                self.consecutiveListIndex.append(r)
                                self.consecutiveListIndex.append(c)
                                self.check = 4
                                break
        a = 0
        #print(final_lst)
        for x in final_lst:
            a += x
        if a == 0:
            return False
        else:
            return True
        
    def solve(self):
        # Reset all textboxes to black background
        for a in range(6):
            for b in range(6):
                Entry(self.window, width = 2,textvariable=self.lst[a][b],fg = 'white',justify='center').grid(row=a,column=b+2)
        
        # Check for all values
        for i in range(6):
            for j in range(6):
                self.Entry_list[i][j] = self.lst[i][j].get()
        if self.isConsecutiveFour(self.Entry_list) == True:
            row_num = self.consecutiveListIndex[0]  # Get value of row number to HIGHLIGHT
            column_num = self.consecutiveListIndex[1]   # Get value of column number to HIGHLIGHT

            if self.check == 1: # if consecutive in ROW
                for column in range(column_num,column_num+4):
                    self.Box_list[row_num][column] = Entry(self.window,width=2,textvariable = self.lst[row_num][column],bg = 'gray',fg = 'black',justify='center').grid(row=row_num,column=column+2)
           
            elif self.check == 2:   # if consecutive in columns
                for row in range(row_num,row_num+4):
                    self.Box_list[row][column_num] = Entry(self.window,width=2,textvariable = self.lst[row][column_num],bg = 'gray',fg = 'black', justify='center').grid(row=row,column=column_num+2)
            
            elif self.check == 3:   # if consecutive in diagonal top left to bottom right
                var1 = 0     # variable to HIGHLIGHT only diagonal (and not all 16 textboxes)
                for row in range(row_num,row_num+4):
                    var2 = 0
                    for column in range(column_num,column_num+4):
                            if var1 == var2:
                                self.Box_list[row][column] = Entry(self.window,width=2,textvariable = self.lst[row][column],bg = 'gray',fg = 'black',justify='center').grid(row=row,column=column+2)
                            var2 += 1
                    var1 += 1
          
            elif self.check == 4:   # if consecutive in diagonals top right to bottom left
                var3 = 0    # variable to HIGHLIGHT only diagonal (and not all 16 textboxes)
                for row in range(row_num,row_num-4,-1):
                    var4 = 0
                    for column in range(column_num,column_num+4):
                        if var3 == var4:
                            self.Box_list[row][column] = Entry(self.window,width=2,textvariable = self.lst[row][column],bg = 'gray',fg = 'black',justify='center').grid(row=row,column=column+2)
                        var4 -= 1
                    var3 -= 1    
            print('SUCCESS')



            
            
            
    
Consecutive4GUI()