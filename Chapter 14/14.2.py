string1 = "1 1116 95422 1 2 322 19- 12 342 3873 12 31 321"
string2 = string1.replace(' ','')
string = string2.replace('-','')

tuple1 = tuple(string)

set1 = set(string)
lst = [0,0]    #lst[0] ~ num name, lst[1] ~ num count
for s in set1:
    t_c = tuple1.count(s)
    if t_c == lst[1]:
        lst.append(s)
        lst.append(t_c)
    if t_c > lst[1]:
        lst = [s,t_c]

for i in range(0,len(lst),2):
    print(f"The digit {lst[i]} appears {lst[i+1]} times.")
    
