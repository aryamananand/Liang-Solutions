def findLargest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        a = lst[len(lst)-1]
        lst.remove(a)
        return max(a,findLargest(lst))
    
lst = [1,23,21,4,325,34,14,23,3]
print(findLargest(lst))