import time
ITERATIONS = 1000
total = 0
for iterations in range(ITERATIONS):
        
    row1 = [0, 0, 0, 0, 0, 0, 0, 0]
    row2 = [0, 0, 0, 0, 0, 0, 0, 0]
    row3 = [0, 0, 0, 0, 0, 0, 0, 0]
    row4 = [0, 0, 0, 0, 0, 0, 0, 0]
    row5 = [0, 0, 0, 0, 0, 0, 0, 0]
    row6 = [0, 0, 0, 0, 0, 0, 0, 0]
    row7 = [0, 0, 0, 0, 0, 0, 0, 0]
    row8 = [0, 0, 0, 0, 0, 0, 0, 0]
    place=0
    #THE ABOVE IS OUR CHESSBOARD before PLACING QUEENS
    count = 0
    #loop 1
    a = time.time()
    for n in range(8):
        row1 = [0, 0, 0, 0, 0, 0, 0, 0]
        row1[n] = 1
        #loop 2
        
        for m in range(8):
            place += 1
            if m not in [n-1,n,n+1]:
                row2 = [0, 0, 0, 0, 0, 0, 0, 0]
                row2[m] = 1
                #loop 3
                for p in range(8):
                    place += 1
                    if p not in [n-2,n,n+2] and p not in [m-1,m,m+1]:
                        row3 = [0, 0, 0, 0, 0, 0, 0, 0]
                        row3[p] = 1
                        #loop4
                        
                        for q in range(8):
                            place += 1
                            if q not in [n-3,n,n+3] and q not in [m-2,m,m+2] and q not in [p-1,p,p+1]:
                                row4 = [0, 0, 0, 0, 0, 0, 0, 0]
                                row4[q] = 1
                                #loop5
                                
                                for r in range(8):
                                    place += 1
                                    if r not in [n-4,n,n+4] and r not in [m-3,m,m+3] and r not in [p-2,p,p+2] and r not in [q-1,q,q+1]:
                                        row5 = [0, 0, 0, 0, 0, 0, 0, 0]
                                        row5[r] = 1
                                        #loop6
                                        
                                        for s in range(8):
                                            place += 1
                                            if s not in [n-5,n,n+5] and s not in [m-4,m,m+4] and s not in [p-3,p,p+3] and s not in [q-2,q,q+2] and s not in [r-1,r,r+1]:
                                                row6 = [0, 0, 0, 0, 0, 0, 0, 0]
                                                row6[s] = 1
                                                #loop7
                                                
                                                for t in range(8):
                                                    place += 1
                                                    if t not in [n-6,n,n+6] and t not in [m-5,m,m+5] and t not in [p-4,p,p+4] and t not in [q-3,q,q+3] and t not in [r-2,r,r+2] and t not in [s-1,s,s+1]:
                                                        row7 = [0, 0, 0, 0, 0, 0, 0, 0]
                                                        row7[t] = 1
                                                        #loop8
                                                        
                                                        for u in range(8):
                                                            place += 1
                                                            if u not in [n-7,n,n+7] and u not in [m-6,m,m+6] and u not in [p-5,p,p+5] and u not in [q-4,q,q+4] and u not in [r-3,r,r+3] and u not in [s-2,s,s+2] and u not in [t-1,t,t+1]:
                                                                row8 = [0, 0, 0, 0, 0, 0, 0, 0]
                                                                row8[u] = 1
                                                                count += 1
                                                                
                                                                # print()
                                                                # print(f'Solution {count}:')

                                                                # print(row1)
                                                                # print(row2)
                                                                # print(row3)
                                                                # print(row4)
                                                                # print(row5)
                                                                # print(row6)
                                                                # print(row7)
                                                                # print(row8)
    b = time.time()

    # print('place: ', place)
    total += (b-a)

print(f"avg time taken for {ITERATIONS} iterations with BRUTE FORCE: {total/ITERATIONS}")