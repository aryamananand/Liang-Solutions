
# [77, 47, 1, 2, 78]
# [33, 49, 47, 38, 80, 20, 27, 19, 56]
# [67, 18, 91, 56, 64, 41, 66, 0]
# [53, 65, 28, 9, 88, 60, 82, 0, 81]
# [10, 95, 29, 48, 60]
# [52, 90, 46, 0, 25]
#[11, 72, 54, 38, 76, 39]
# [1, 33, 84, 16, 83, 42, 15, 56]
lst =  [88, 28, 19, 13, 92, 94]
# [40, 32, 62, 59, 23]


#pivot is middle value of unsorted list
if len(lst) % 2 == 0:
    pivot = lst[int(len(lst)/2)]
else:
    pivot = lst[int(len(lst)/2)+1]

lst.remove(pivot)

print('pivot is', pivot)

bigger_lst = [pivot]
smaller_lst = []

for t in lst:
    if t >= pivot:
        bigger_lst.append(t)
    else:
        smaller_lst.append(t)

final_lst = []

for u in smaller_lst:
    final_lst.append(u)
for r in bigger_lst:
    final_lst.append(r)

print(final_lst)