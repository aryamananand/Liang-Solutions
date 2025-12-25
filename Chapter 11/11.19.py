lst = [[2,1,9,7,0,6,1], [9,2,7,8,7,0,1], [5,7,3,4,6,6,6], [7,3,4,1,1,8,7], [1,4,9,5,2,0,7], [2,1,6,3,4,2,7]]
for i in range(len(lst)):
    print(lst[i])

def isConsecutiveFour(lst):

    final_lst = [0,0,0,0]
    # Check rows
    for r in range(len(lst)):
        for c in range(len(lst[r])-3):
            if lst[r][c] == lst[r][c+1] == lst[r][c+2] == lst[r][c+3]:
                final_lst[0] = 1
                
      
    # Check columns if rows are not true (i.e. consecutive 4)
    if final_lst[0] != 1:
        for c in range(len(lst[0])):
            for r in range(len(lst)-3):
                if lst[r][c] == lst[r+1][c] == lst[r+2][c] == lst[r+3][c]:
                    final_lst[1] = 1
                    break 
                    
        # if list is already true, then don't check diagonals
        if final_lst[1] != 1:
            # Check diagonals --> top left to bottom right
            for r in range(len(lst)-3):
                for c in range(len(lst[0])-3):
                    if lst[r][c] == lst[r+1][c+1] == lst[r+2][c+2] == lst[r+3][c+3]:
                        final_lst[2] = 1
                        break

            if final_lst[2] != 1:
                for r in range(len(lst)-1,2,-1):
                    for c in range(len(lst[0])-3):
                        if lst[r][c] == lst[r-1][c+1] == lst[r-2][c+2] == lst[r-3][c+3]:
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
    

print(isConsecutiveFour(lst))