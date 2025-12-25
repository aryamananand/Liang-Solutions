#Classic - The 8 Queens Problem

List = [1]

row_num = 2
while row_num <= 8:   
    i = 1
    while i <= 8:           #i is column number in the PARTICULAR ROW (count)
        if List.count(i) == 0 and i != row_num and list[i]:
            List.append(i)
            continue        
        i += 1
    row_num += 1
print(List)  