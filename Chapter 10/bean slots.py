import random 
import time
import matplotlib.pyplot as plt
#=================== PART 1 - The Simulation ====================  


m = 10000
n = 40
#m = eval(input('Enter the number of balls: '))
#n = eval(input('Enter the number of slots: '))

slot = 0
slot_list_1 =[]   #List for slot
for i in range (m):    #i counts balls
    lst = []    #lst is a list for slots of each ball
    j = 0
    
    slot = 0
    while j < n:    #j counts slots for each ball
        var = random.randint(0,1)
        lst.append(var)
        j += 1

    for x in lst:       #1 = right, 0 = left
        slot += x
    slot_list_1.append(slot)     #Get slot number for ball 
    
    #print(lst)
    for k in range(len(lst)):   
        if lst[k] == 0:
            lst[k] = 'L' 
        else: 
            lst[k] = 'R'
        #print(lst[k], end = '')     #print final sequence
    #print()     #Next line after each sequence
    
#print(f'Initial slot: {slot_list_1}')

#=============================== PART 2 - The Analysis ============================
slot_list = []
i = 0
while i <= max(slot_list_1):
    slot_list.append(slot_list_1.count(i))
    i += 1
#print('Final slots:', slot_list)

#================================ PART 3 - The Printing =============================

print()
#the following code is to increase all integers in the list by 1 since the bottom row print was incomplete
index = 0
for x in slot_list:
    x += 1
    slot_list[index] = x
    index += 1

new_list = []
for x in slot_list:
    new_list.append(x)
    
print(slot_list)

a = max(slot_list)

BallsPerSlot = 0
for x in range(a-1):
    lst = []
    for y in range(len(slot_list)): 	#most number of balls for whichever slot, is number of different lines to be printed
        if slot_list[y] == a:
            lst.append('o')      #1 means ball to be placed
            slot_list[y] -= 1  #reduce value, since top ball is printed  
            BallsPerSlot += 1 
        else:
            lst.append(' ')
    a -= 1      #reduce max value at the end of a scanning round
    #print(lst)
    #for z in lst:
        #print(z, end = '')	   #print the lst as a string
    #print()     #to go to next line


x_slot = [x for x in range (len(new_list))]


plt.plot(x_slot, new_list, '-c')
plt.show()








