import random
# Generate the table
table = []
for row in range(8):
    table.append([]) 
    for column in range(7):
        table[row].append(random.randint(0, 8))

print(table) 

#Place in decreasing order

lst = []   # list employee worked hours
total = 0 
for i in range(8):
    for j in range(7):
        total += table[i][j] 
        if j == 6:
            lst.append(total)
            total = 0 

#print(lst)

num_lst = []

for x in range(len(lst)):
    num_lst.append(x)

  

count = 0
while count < (len(lst) - 1):
    for i in range (len(lst) - 1): 
        #compare lst[i] and lst[i + 1]
        if lst[i]  > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]          #Switch their position
            num_lst[i], num_lst[i+1] = num_lst[i+1], num_lst[i]
            count = 0   #Completely reset to zero so that no double counting
        else:
            count += 1  #this happens if no change occurs
        if count == len(lst) - 1:    #if no change is necessary anywhere => list is sorted
            print(num_lst)	#this is bubble-sorted list
            print(lst)
            break


for q in range(len(lst)-1,-1,-1):
        print(f'Employee {num_lst[q]} has {lst[q]} work hours.')