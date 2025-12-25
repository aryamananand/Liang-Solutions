
double_lst = input("Enter students' names and score: ").split(' ')

individual_lst = []
count = 0
for i in range(0,len(double_lst)-1,2):
    individual_lst.append([])
    individual_lst[count].append(int(double_lst[i+1]))
    individual_lst[count].append(double_lst[i])
    count += 1

individual_lst.sort()
print(individual_lst)

for x in range (len(individual_lst)):
    print(individual_lst[x][1], ' - ', individual_lst[x][0])


