#Caution: DO NOT PUT SPACEBAR AFTER LAST INPUT
lst = input('Enter list:').split(' ')

#Make a separate copy of the original list
originalLst = lst
#print(originalLst)

def selectionSort(lst):
    for i in range (len(lst) - 1):
        currentMin = lst[i]
        currentMinIndex = i
    for j in range (i + 1, len(lst)):
        if currentMin > lst[j]:
            currentMin = lst[j]
            currentMinIndex = j 
    if currentMinIndex != i:
        lst[currentMinIndex] = lst[i]
        lst[i] = currentMin
    
def insertionSort (lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1
        lst[k + 1] = currentElement
    return lst

#print('sorted list: ', insertionSort(lst))

#insertionSort function called here

x = 0
while x < (len(lst) - 1):
    if lst[x] > lst[x + 1]:
        break
    x += 1    

#print(x)
if x == len(lst) - 1:
    print('This list is sorted')
else:
    print('This list is not sorted.')

