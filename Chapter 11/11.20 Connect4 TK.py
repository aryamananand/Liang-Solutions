from tkinter import *

window = Tk()
window.title('Connect Four')
window.geometry('652x430')

count = 0   # Initialise turn checker

y0_1 = 300
y0_2 = 360
y1_1 = 300
y1_2 = 360
y2_1 = 300
y2_2 = 360
y3_1 = 300
y3_2 = 360
y4_1 = 300
y4_2 = 360
y5_1 = 300
y5_2 = 360
y6_1 = 300
y6_2 = 360

# =========================== GAME ANALYSIS STARTS ===========================

def isConsecutiveFour(lst, player):

    final_lst = [0,0,0,0]
    # Check rows
    for r in range(len(lst)):
        for c in range(len(lst[r])-3):
            if lst[r][c] == lst[r][c+1] == lst[r][c+2] == lst[r][c+3] == player:
                final_lst[0] = 1
                
      
    # Check columns if rows are not true (i.e. consecutive 4)
    if final_lst[0] != 1:
        for c in range(len(lst[0])):
            for r in range(len(lst)-3):
                if lst[r][c] == lst[r+1][c] == lst[r+2][c] == lst[r+3][c] == player:
                    final_lst[1] = 1
                    break 
                    
        # if list is already true, then don't check diagonals
        if final_lst[1] != 1:
            # Check diagonals --> top left to bottom right
            for r in range(len(lst)-3):
                for c in range(len(lst[0])-3):
                    if lst[r][c] == lst[r+1][c+1] == lst[r+2][c+2] == lst[r+3][c+3] == player:
                        final_lst[2] = 1
                        break

            if final_lst[2] != 1:
                for r in range(len(lst)-1,2,-1):
                    for c in range(len(lst[0])-3):
                        if lst[r][c] == lst[r-1][c+1] == lst[r-2][c+2] == lst[r-3][c+3] == player:
                            final_lst[3] = 1
                            break
    a = 0
    #print(final_lst)
    for x in final_lst:
        a += x
    if a == 0:
        return False
    else:
        return True
    
    # Board analysis
board = []

for r in range(6):
    board.append([])
    for c in range(7):
        board[r].append(' ')


# ============================ GAME ANALYSIS ENDS ===============================
def check_for_draw():
    check = 0
    for r in range(7):
        for c in range(7):
            if board[r][c] != ' ':
                check += 1
    if check == 42:
        return True
    else:
        return False
    

def draw_popup():
    win3 = Toplevel(window)
    win3.title('Column Full')
    win3.geometry('120x100')
    Label(win3).grid(row=1,column=1)
    Label(win3, text = 'Game Drawn.').grid(row=2,column=1)
    Label(win3).grid(row=3,column=1)
    Button(win3, text = 'New Game', command = new).grid(row=4,column=1)
    Button(win3, text = 'Close', command = win3.destroy).grid(row=5,column=1)






def popup_full():
    win2 = Toplevel(window)
    win2.title('Column Full')
    win2.geometry('250x100')
    Label(win2).grid(row=1,column=1)
    Label(win2, text = 'Column is full! Please try another column.').grid(row=2,column=1)
    Label(win2).grid(row=3,column=1)
    Button(win2, text = 'Close', command = win2.destroy).grid(row=4,column=1)

def error_popup():
    tex = 'E R R O R  !'
    win1 = Toplevel(window)
    win1.title('Error')
    win1.geometry('150x150')
    Label(win1, text = 'Invalid move! Please try again!', font = 'Helevetica 20 medium')
    Button(win1, text = 'Close',command = win1.destroy)

def popup():
    global count

    win = Toplevel(window) 
    win.title('Game Result')
    Label(win).grid(row=1,column=2)
    if count % 2 == 0:
        te = 'Y E L L O W   W I N S !'
        win.geometry('290x150')
    else:
        te = 'R E D   W I N S !'
        win.geometry('210x150')
    Label(win, text = te, font = 'Helvetica 20 bold', bg = 'green').grid(row=2,column=1)
    Label(win).grid(row=3,column=1)
    Button(win, text = 'New Game', command = new).grid(row=4,column=1)
    Button(win, text = 'Close', command = win.destroy).grid(row=5,column=1)


def play0():
    global count
    global y0_1
    global y0_2
    if y0_1 < 0:
        popup_full()
    else:
        if count % 2 == 0:
            for j in range(len(board)):
                if board[j][0] != ' ':
                    board[j-1][0] = 'R'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][0] = 'R'
            c0.create_oval(3,y0_1,62,y0_2, fill = 'red')
            y0_1 -= 60
            y0_2 -= 60
        else:
            for j in range(len(board)):
                if board[j][0] != ' ':
                    board[j-1][0] = 'Y'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][0] = 'Y'
            c0.create_oval(3,y0_1,62,y0_2, fill = 'goldenrod1')
            y0_1 -= 60
            y0_2 -= 60
        count += 1
        if isConsecutiveFour(board,'R') == True:
            popup()
        elif isConsecutiveFour(board,'Y') == True:
            popup()
def play1():
    global count
    global y1_1
    global y1_2
    if y1_1 < 0:
        popup_full()
    else:
        if count % 2 == 0:
            for j in range(len(board)):
                if board[j][1] != ' ':
                    board[j-1][1] = 'R'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][1] = 'R'
            c1.create_oval(1,y1_1,61,y1_2, fill = 'red')
            y1_1 -= 60
            y1_2 -= 60
        else:
            for j in range(len(board)):
                if board[j][1] != ' ':
                    board[j-1][1] = 'Y'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][1] = 'Y'
            c1.create_oval(1,y1_1,61,y1_2, fill = 'goldenrod1')
            y1_1 -= 60
            y1_2 -= 60
        count += 1
        if isConsecutiveFour(board,'R') == True:
            popup()
        elif isConsecutiveFour(board,'Y') == True:
            popup()
def play2():
    global count
    global y2_1
    global y2_2 
    if y2_1 < 0:
        popup_full()
    else:
        if count % 2 == 0:
            for j in range(len(board)):
                if board[j][2] != ' ':
                    board[j-1][2] = 'R'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][2] = 'R'
            c2.create_oval(1,y2_1,61,y2_2, fill = 'red')
            y2_1 -= 60
            y2_2 -= 60
        else:
            for j in range(len(board)):
                if board[j][2] != ' ':
                    board[j-1][2] = 'Y'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][2] = 'Y'
            c2.create_oval(1,y2_1,61,y2_2, fill = 'goldenrod1')
            y2_1 -= 60
            y2_2 -= 60
        count += 1
        if isConsecutiveFour(board,'R') == True:
            popup()
        elif isConsecutiveFour(board,'Y') == True:
            popup()


def play3():
    global count
    global y3_1
    global y3_2 
    if y3_1 < 0:
        popup_full()
    else:
        if count % 2 == 0:
            for j in range(len(board)):
                if board[j][3] != ' ':
                    board[j-1][3] = 'R'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][3] = 'R'
            c3.create_oval(1,y3_1,61,y3_2, fill = 'red')
            y3_1 -= 60
            y3_2 -= 60
        else:
            for j in range(len(board)):
                if board[j][3] != ' ':
                    board[j-1][3] = 'Y'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][3] = 'Y'
            c3.create_oval(1,y3_1,61,y3_2, fill = 'goldenrod1')
            y3_1 -= 60
            y3_2 -= 60
        count += 1
        if isConsecutiveFour(board,'R') == True:
            popup()
        elif isConsecutiveFour(board,'Y') == True:
            popup()
    

def play4():   
    global count
    global y4_1
    global y4_2
    if y4_1 < 0:
        popup_full()
    else:
        if count % 2 == 0:
            for j in range(len(board)):
                if board[j][4] != ' ':
                    board[j-1][4] = 'R'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][4] = 'R'
            c4.create_oval(1,y4_1,61,y4_2, fill = 'red')
            y4_1 -= 60
            y4_2 -= 60
        else:
            for j in range(len(board)):
                if board[j][4] != ' ':
                    board[j-1][4] = 'Y'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][4] = 'Y'
            c4.create_oval(1,y4_1,61,y4_2, fill = 'goldenrod1')
            y4_1 -= 60
            y4_2 -= 60
        count += 1
        if isConsecutiveFour(board,'R') == True:
            popup()
        elif isConsecutiveFour(board,'Y') == True:
            popup()


def play5():
    global count
    global y5_1
    global y5_2
    if y5_1 < 0:
        popup_full()
    else:

        if count % 2 == 0:
            for j in range(len(board)):
                if board[j][5] != ' ':
                    board[j-1][5] = 'R'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][5] = 'R'
            c5.create_oval(1,y5_1,61,y5_2, fill = 'red')
            y5_1 -= 60
            y5_2 -= 60
        else:
            for j in range(len(board)):
                if board[j][5] != ' ':
                    board[j-1][5] = 'Y'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][5] = 'Y'
            c5.create_oval(1,y5_1,61,y5_2, fill = 'goldenrod1')
            y5_1 -= 60
            y5_2 -= 60
        count += 1
        if isConsecutiveFour(board,'R') == True:
            popup()
        elif isConsecutiveFour(board,'Y') == True:
            popup()
            

def play6():
    global count
    global y6_1
    global y6_2
    if y6_1 < 0:
        popup_full()
    else:
        if count % 2 == 0:
            for j in range(len(board)):
                if board[j][6] != ' ':
                    board[j-1][6] = 'R'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][6] = 'R'
            c6.create_oval(1,y6_1,61,y6_2, fill = 'red')
            y6_1 -= 60
            y6_2 -= 60
        else:
            for j in range(len(board)):
                if board[j][6] != ' ':
                    board[j-1][6] = 'Y'
                    break
                elif j == 5:    # When a column is started to be used
                    board[j][6] = 'Y'
            c6.create_oval(1,y6_1,61,y6_2, fill = 'goldenrod1')
            y6_1 -= 60
            y6_2 -= 60
        count += 1
        if isConsecutiveFour(board,'R') == True:
            popup()
        elif isConsecutiveFour(board, 'Y') == True:
            popup()
        else:
            if check_for_draw() == True:
                draw_popup()


# The buttons 

def new ():
    global win
    
    global board
    global count
    global y0_1
    global y0_2
    global y1_1
    global y1_2
    global y2_1
    global y2_2
    global y3_1
    global y3_2
    global y4_1
    global y4_2
    global y5_1
    global y5_2
    global y6_1
    global y6_2

    count = 0
    y0_1 = 300
    y0_2 = 360
    y1_1 = 300
    y1_2 = 360
    y2_1 = 300
    y2_2 = 360
    y3_1 = 300
    y3_2 = 360
    y4_1 = 300
    y4_2 = 360
    y5_1 = 300
    y5_2 = 360
    y6_1 = 300
    y6_2 = 360

    # Clear the board 
    board = []
    for r in range(7):
        board.append([])
        for c in range(7):
            board[r].append(' ')

    c0.delete('all')
    c1.delete('all')
    c2.delete('all')
    c3.delete('all')
    c4.delete('all')
    c5.delete('all')
    c6.delete('all')
    side2.delete('all')

# The board interface

side = Canvas(window, height = 360, width = 90, bg = 'black')
side.grid(row=2,column=1)

c0 = Canvas(window, height = 360, width = 60, bg = 'white')
c0.grid(row=2,column=2)
c1 = Canvas(window, height = 360, width = 60, bg = 'white')
c1.grid(row=2,column=3)
c2 = Canvas(window, height = 360, width = 60, bg = 'white')
c2.grid(row=2,column=4)
c3 = Canvas(window, height = 360, width = 60, bg = 'white')
c3.grid(row=2,column=5)
c4 = Canvas(window, height = 360, width = 60, bg = 'white')
c4.grid(row=2,column=6)
c5 = Canvas(window, height = 360, width = 60, bg = 'white')
c5.grid(row=2,column=7)
c6 = Canvas(window, height = 360, width = 60, bg = 'white')
c6.grid(row=2,column=8)

side2 = Canvas(window, height = 360, width = 90, bg = 'black')
side2.grid(row=2,column=9)


b0 = Button(window, text = 'Drop', command = play0)
b0.grid(row=1,column=2)
b1 = Button(window, text = 'Drop', command = play1)
b1.grid(row=1,column=3)
b2 = Button(window, text = 'Drop', command = play2)
b2.grid(row=1,column=4)
b3 = Button(window, text = 'Drop', command = play3)
b3.grid(row=1,column=5)
b4 = Button(window, text = 'Drop', command = play4)
b4.grid(row=1,column=6)
b5 = Button(window, text = 'Drop', command = play5)
b5.grid(row=1,column=7)
b6 = Button(window, text = 'Drop', command = play6)
b6.grid(row=1,column=8)

b_new = Button(window, height = 1, width =1, text = 'Reset', command = new)
b_new.grid(row=3,column=4)
b_close = Button(window, height = 1, width = 1, text = 'Close', command = window.destroy)
b_close.grid(row=3,column =6)

window.mainloop()
