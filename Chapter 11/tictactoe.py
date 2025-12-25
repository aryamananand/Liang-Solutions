from tkinter import *
class TicTacToe:
    def __init__(self):

        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.count = 0   # Odd is CROSS and Even is CIRCLE
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.window.geometry('310x410')

        self.var1 = 0 
        self.var2 = 0 
        self.var3 = 0 
        self.var4 = 0
        self.var5 = 0
        self.var6 = 0 
        self.var7 = 0
        self.var8 = 0
        self.var9 = 0

        # The Board

        self.c00 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c00.grid(row=1,column=1)
        self.c01 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c01.grid(row=1,column=2)
        self.c02 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c02.grid(row=1,column=3)
        self.c10 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c10.grid(row=2,column=1)
        self.c11 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c11.grid(row=2,column=2)
        self.c12 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c12.grid(row=2,column=3)
        self.c20 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c20.grid(row=3,column=1)
        self.c21 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c21.grid(row=3,column=2)
        self.c22 = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.c22.grid(row=3,column=3)

        self.canvas = Canvas(self.window, height = 100, width = 100, bg = 'white')
        self.canvas.grid(row=4,column=2)

        self.button = Button(self.window,text = 'Close', command = self.close)
        self.button.grid(row=4,column=1)

        self.button2 = Button(self.window, text = 'New Game', command = self.reset)
        self.button2.grid(row=4,column=3)
        
        # The Click

        self.c00.bind('<Button-1>',self.play1)
        self.c01.bind('<Button-1>',self.play2)
        self.c02.bind('<Button-1>',self.play3)
        self.c10.bind('<Button-1>',self.play4)
        self.c11.bind('<Button-1>',self.play5)
        self.c12.bind('<Button-1>',self.play6)
        self.c20.bind('<Button-1>',self.play7)
        self.c21.bind('<Button-1>',self.play8)
        self.c22.bind('<Button-1>',self.play9)

        
        self.done = [[0,0,0],[0,0,0],[0,0,0]]

        self.window.mainloop()
    
    # The placement of the cross and circle

    def play1 (self,event):
        if self.count % 2 == 0:
            self.c00.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[0][0] = 1
            self.done[0][0] = 1
            self.count += 1
        elif self.var1 == 0:
            self.c00.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c00.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[0][0] = 2
            self.count += 1
        self.var1 = 1    
        self.result()
    def play2 (self,event):
        if self.count % 2 == 0 and self.var2 == 0:
            self.c01.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[0][1] = 1
            self.count += 1
        elif self.var2 == 0:
            self.c01.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c01.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[0][1] = 2
            self.count += 1
        self.var2 = 1
        self.result()
    def play3 (self,event):
        if self.count % 2 == 0 and self.var3 == 0:
            self.c02.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[0][2] = 1
            self.count += 1
        elif self.var3 == 0:
            self.c02.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c02.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[0][2] = 2
            self.count += 1
        self.var3 = 1
        self.result()
    def play4 (self,event):
        if self.count % 2 == 0 and self.var4 == 0:
            self.c10.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[1][0] = 1
            self.count += 1
        elif self.var4 == 0:
            self.c10.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c10.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[1][0] = 2
            self.count += 1
        self.var4 = 1
        self.result()
    def play5 (self,event):
        if self.count % 2 == 0 and self.var5 == 0:
            self.c11.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[1][1] = 1
            self.count += 1
        elif self.var5 == 0:
            self.c11.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c11.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[1][1] = 2
            self.count += 1
        self.var5 = 1
        self.result()
    def play6 (self,event):
        if self.count % 2 == 0 and self.var6 == 0:
            self.c12.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[1][2] = 1
            self.count += 1
        elif self.var6 == 0:
            self.c12.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c12.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[1][2] = 2
            self.count += 1
        self.var6 = 1
        self.result()
    def play7 (self,event):
        if self.count % 2 == 0 and self.var7 == 0:
            self.c20.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[2][0] = 1
            self.count += 1
        elif self.var7 == 0:
            self.c20.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c20.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[2][0] = 2
            self.count += 1
        self.var7 = 1
        self.result()
    def play8 (self,event):
        if self.count % 2 == 0 and self.var8 == 0:
            self.c21.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[2][1] = 1
            self.count += 1
        elif self.var8 == 0:
            self.c21.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c21.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[2][1] = 2
            self.count += 1
        self.var8 = 1
        self.result()
    def play9 (self,event):
        if self.count % 2 == 0 and self.var9 == 0:
            self.c22.create_oval(10,10,91,91, outline = 'blue', width = 3)
            self.board[2][2] = 1
            self.count += 1
        elif self.var9 == 0:
            self.c22.create_line(10,10,91,91, fill= 'red', width = 3)
            self.c22.create_line(90,10,9,91, fill = 'red', width = 3)
            self.board[2][2] = 2
            self.count += 1
        self.var9 = 1
        self.result()

    def result(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0 \
                or self.board[1][0] == self.board[1][1] == self.board[1][2] != 0 \
                or self.board[2][0] == self.board[2][1] == self.board[2][2] != 0 \
                or self.board[0][0] == self.board[1][0] == self.board[2][0] != 0 \
                or self.board[0][1] == self.board[1][1] == self.board[2][1] != 0 \
                or self.board[0][2] == self.board[1][2] == self.board[2][2] != 0 \
                or self.board[0][0] == self.board[1][1] == self.board[2][2] != 0 \
                or self.board[2][0] == self.board[1][1] == self.board[0][2] != 0:
            
            player = '×'
            if self.count % 2 != 0:
                player = '◯'

            self.canvas.create_text(52,50, text = f'Player "{player}" won.',fill = 'green',font = ('Times',13,'bold'))
            self.var1 = 1 
            self.var2 = 1
            self.var3 = 1
            self.var4 = 1
            self.var5 = 1
            self.var6 = 1
            self.var7 = 1
            self.var8 = 1
            self.var9 = 1
        elif self.count == 9:
            self.canvas.create_text(52,50,text='Game drawn.', fill = 'grey',font = ('Times',17,))
        

    def reset(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

        self.count = 0   # Odd is CROSS and Even is CIRCLE

        self.var1 = 0 
        self.var2 = 0 
        self.var3 = 0 
        self.var4 = 0
        self.var5 = 0
        self.var6 = 0 
        self.var7 = 0
        self.var8 = 0
        self.var9 = 0

        # The Board
        self.c00.delete('all')
        self.c01.delete('all')
        self.c02.delete('all')
        self.c10.delete('all')
        self.c11.delete('all')
        self.c12.delete('all')
        self.c20.delete('all')
        self.c21.delete('all')
        self.c22.delete('all')
        self.canvas.delete('all')
        
    def close(self):
        self.window.destroy()

TicTacToe()
