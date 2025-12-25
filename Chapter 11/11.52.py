import sys
side = eval(input("Enter number n: "))

# to generate A B C D...list so as to match later
alphabet_lst = []
for i in range(65,65+side):
    alphabet_lst.append(chr(i))

lst = []
for i in range(side):
    lst.append([])
    lst[i] = input(f'Enter {side} rows of letters separated by spaces: ').split(' ')
    if sorted(lst[i]) != alphabet_lst:
        print(f'Wrong input. The letters must be from A to {alphabet_lst[side-1]}')
        sys.exit()
    

#print(alphabet_lst)

var = 0
# Checking 
for row in range(side):
    row_check_lst = sorted(lst[row])    # sort each row and match with A B C D....list 
    if row_check_lst != alphabet_lst:
        print('This is not a Latin square.')
        break
    else:
        var += 1

var2 = 0
if var == side:     # this is if all rows are satisfied
    for column in range(side):
        temp_row = []
        for row in range(side):
            temp_row.append(lst[row][column])

        
        if sorted(temp_row) == alphabet_lst:
            var2 += 1

if var2 == side:
    print('The input list is a Latin Square.')
else:
    print(f'This is not a Latin Square.')
