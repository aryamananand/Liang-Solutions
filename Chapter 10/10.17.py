def bubble_sort(lst):
    #Program for bubble-sorting a list 
    count = 0
    while count < (len(lst) - 1):
        for i in range (len(lst) - 1): 
            #compare lst[i] and lst[i + 1]
            if lst[i]  > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]                 #Switch their position
                count = 0   #Completely reset to zero so that no double counting
            else:
                count += 1  #this happens if no change occurs
            if count == len(lst) - 1:    #if no change is necessary anywhere => list is sorted
                return (lst)	#this is bubble-sorted list
                break

def main():
    lst1 = list(input('Enter a word:').strip())
    lst2 = list(input('Enter a word:').strip())
    if bubble_sort(lst1) == bubble_sort(lst2):
        print('Is an anagram.')
    else:
        print('Is not an anagram.')
main()
