import random

a = random.randint(20,50)
b = random.randint(80,100)
c = random.randint(7,12)    #random length for lst1
d = random.randint(7,12)   #ranodm length for lst2

lst1 = [random.randint(0,a) for i in range(c)]
lst1.sort()
print(lst1)

lst2 = [random.randint(0,b) for i in range(d)]
lst2.sort()
print(lst2)

final_list = []

i1 = 0  #index number for list 1
i2 = 0  #index number for list 2

biggest = len(lst1)
if len(lst2) > biggest:
    biggest = len(lst2)

for i in range (len(lst1) + len(lst2) + 1):
    if lst1[i1] <= lst2[i2]:
        final_list.append(lst1[i1])
        if i1 == len(lst1)-1:
            #print('broke from OPT 1')
            break
        else: i1 += 1     #increase index num for list 1 only if it is smaller than list2's current item
    
    else:
        final_list.append(lst2[i2])
        if i2 == len(lst2)-1:
            #print('broke from OPT 2')
            break
        else: i2 += 1     #incrEase index num for list 2 only if it is smaller than 'i1'th element of list 1

#print('before processing')
#print(final_list)

#print('i1 = ', i1)
#print('i2 = ', i2)


if i1 == len(lst1)-1:
    for k in range(i2, len(lst2)):
        final_list.append(lst2[k])
else:
    for p in range(i1, len(lst1)):
        final_list.append(lst1[p])

print(final_list)


'''
#if list 1 is longer 
if biggest == len(lst1):
    for j in range(len(lst1)):
        if lst1[j] >= lst2[len(lst2)-1]:
            final_list.append(lst1[j])
    #print('success for OPTION 1')
#if list 2 is longer
if biggest == len(lst2):
    for k in range(len(lst2)):
        if lst2[k] >= lst1[len(lst1)-1]:
            final_list.append(lst2[k])
    #print('success for OPTION 2')

print(final_list)
'''