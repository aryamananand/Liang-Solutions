num_lock = 100      #enter number of lockers here
num_locker = num_lock + 1
lst = []
for i in range (num_locker):
    lst.append(0)   #0 because all lockers closed


for student in range(1, 100):
    lock_num = student      #lock_num is locker to be opened (we subtract 1 since list index begins with 0)
    while lock_num < 100:
        if lst[lock_num-1] == 1:      #lst is list of lockers 
            lst[lock_num-1] = 0
        else:
            lst[lock_num-1] = 1
        lock_num += student


for x in range (1, 101):
    print(f"{x}: {lst[x-1]}|", end = ' ')

lockerNumber = 0
for x in lst:
    lockerNumber += 1
    if x == 1:
        print(f"locker {lockerNumber} is open")

