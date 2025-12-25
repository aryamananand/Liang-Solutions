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
                for r in range(len(lst)-1,3,-1):
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
    
board = []

for r in range(6):
    board.append([])
    for c in range(7):
        board[r].append(' ')

for i in range(6):
    print('|', end = '')
    for j in range(7):
        print(board[i][j], end = '|')
    print()

game = True    # Initialise
count = 0
while game == True: 
    if count % 2 == 0:  # Even => R's turn
        count += 1
        val = eval(input("Drop a red disk at column (0-6): "))  
        for j in range(len(board)):
            if board[j][val] != ' ':
                board[j-1][val] = 'R'
                break
            elif j == 5:    # When a column is started to be used
                board[j][val] = 'R'
        for i in range(6):
            print('|', end = '')
            for j in range(7):
                print(board[i][j], end = '|')
            print()
        if isConsecutiveFour(board, 'R') == True:
            print('The red player won.')
            game = False

    else:
        count += 1
        val = eval(input("Drop a yellow disk at column (0-6): ")) 
        for j in range(len(board)):
            if board[j][val] != ' ':
                board[j-1][val] = 'Y'
                break
            elif j == 5:    # When a column is started to be used
                board[j][val] = 'Y'
        for i in range(6):
            print('|', end = '')
            for j in range(7):
                print(board[i][j], end = '|')
            print()
        if isConsecutiveFour(board, 'Y') ==  True:
            print('The yellow player won.')
            game = False

