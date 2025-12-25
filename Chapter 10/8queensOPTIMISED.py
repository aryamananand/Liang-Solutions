import time
ITERATIONS = 1000
total = 0
for iterations in range(ITERATIONS):
    a = time.time()
    def rem(a):
        LIST = [0,1,2,3,4,5,6,7]
        for u in a:
            if u in LIST and u >= 0:
                LIST.remove(u)
        return LIST

    board = []
    for row in range(8):
        board.append([])
        for column in range(8):
            board[row].append(0)
    count = 0
    #loop 1
    place=0
    for n in range(8):
        board[0] = [0,0,0,0,0,0,0,0]
        board[0][n] = 1
        place += 1
        #loop 2
        lst2 = rem([n-1,n,n+1])
        for m in lst2:
            board[1] = [0,0,0,0,0,0,0,0]
            board[1][m] = 1
            #loop 3
            lst3 = rem([n-2,n,n+2,m-1,m,m+1])
            place += 1
            for p in lst3:
                board[2] = [0,0,0,0,0,0,0,0]
                board[2][p] = 1
                #loop4
                lst4 = rem([n-3,n,n+3,m-2,m,m+2,p-1,p,p+1])
                place += 1
                for q in lst4:
                    board[3] = [0,0,0,0,0,0,0,0]
                    board[3][q] = 1
                    #loop5
                    lst5 = rem([n-4,n,n+4,m-3,m,m+3,p-2,p,p+2,q-1,q,q+1])
                    place += 1
                    for r in lst5:
                        board[4] = [0,0,0,0,0,0,0,0]
                        board[4][r] = 1
                        #loop6
                        lst6 = rem([n-5,n,n+5,m-4,m,m+4,p-3,p,p+3,q-2,q,q+2,r-1,r,r+1])
                        place += 1
                        for s in lst6:
                            board[5] = [0,0,0,0,0,0,0,0]
                            board[5][s] = 1
                            #loop7
                            lst7 = rem([n-6,n,n+6,m-5,m,m+5,p-4,p,p+4,q-3,q,q+3,r-2,r,r+2,s-1,s,s+1])
                            place += 1
                            for t in lst7:
                                board[6] = [0,0,0,0,0,0,0,0]
                                board[6][t] = 1
                                #loop8
                                lst8 = rem([n-7,n,n+7,m-6,m,m+6,p-5,p,p+5,q-4,q,q+4,r-3,r,r+3,s-2,s,s+2,t-1,t,t+1])
                                place += 1
                                for u in lst8:
                                    board[7] = [0,0,0,0,0,0,0,0]
                                    board[7][u] = 1
                                    count += 1
                                    # print()
                                    # print(f'Solution {count}:')
                                    # print(board)
                                    place += 1
    b = time.time()
    # print('================END================')
    total += (b-a)
    # print('Iterations: ', place)
    # print(f"time: {format(b-a,".5f")}")

print(f"avg time taken for {ITERATIONS} iterations after OPTIMISATION: {total/ITERATIONS}")