#Program for bubble-sorting a list 
import random
import time
lst = [random.randint(1,100) for i in range(10000)]
a = time.time()

count = 0

while count < (len(lst) - 1):
    for i in range (len(lst) - 1): 
        #compare lst[i] and lst[i + 1]
        if lst[i]  > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]          #Switch their position
            count = 0   #Completely reset to zero so that no double counting
        else:
            count += 1  #this happens if no change occurs
        if count == len(lst) - 1:    #if no change is necessary anywhere => list is sorted
            b = time.time()
            print(f"time taken: {b - a}")
            print('sorted')	#this is bubble-sorted list
            break
 

