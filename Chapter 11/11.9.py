#TIC-TAC-TOE

board = [[0,0,0],[0,0,0],[0,0,0]]
for i in  range(3):
    print(board[i][0],board[i][1],board[i][2])
count = 0
game = True 
while game == True:
    count += 1
    if count % 2 != 0:
        a = eval(input('Enter a row (0, 1, or 2) for player 1:'))
        b = eval(input('Enter a column (0, 1, or 2) for player 1:'))
        board[a][b] = 1 
    else:
        a = eval(input('Enter a row (0, 1, or 2) for player 1:'))
        b = eval(input('Enter a column (0, 1, or 2) for player 1:'))
        board[a][b] = 2

    for i in  range(3):
        print(board[i][0],board[i][1],board[i][2])
    
    if board[0][0] == board[0][1] == board[0][2] != 0 \
            or board[1][0] == board[1][1] == board[1][2] != 0 \
            or board[2][0] == board[2][1] == board[2][2] != 0 \
            or board[0][0] == board[1][0] == board[2][0] != 0 \
            or board[0][1] == board[1][1] == board[2][1] != 0 \
            or board[0][2] == board[1][2] == board[2][2] != 0 \
            or board[0][0] == board[1][1] == board[2][2] != 0 \
            or board[2][0] == board[1][1] == board[0][2] != 0:
        
        player = 2
        if count % 2 != 0:
            player = 1

        print(f'Player {player} won.') 
        game = False   
    elif count == 9:
        print('Draw. Game over.')
        game = False 



    
    

    
