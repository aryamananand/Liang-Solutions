def binary(decimal):
    if decimal == 0:
        return 0
    else:
        order = 1
        total = 0
        while decimal >= 1:
            remainder = decimal % 2
            digit = remainder * order 
            order *= 10
            total += digit
            decimal //= 2
        return str(total)
    
num = eval(input('Enter a number between 0 and 511: '))
lst = list(binary(num))

#print(lst)
for i in range(9-len(lst)):
    lst.insert(i,'0')


print(lst)
for k in range(9):
    if lst[k] == '1':
        lst[k] = 'T'
    else:
        lst[k] = 'H'

#print(lst)
lst1 = []

var = 0
for i in range(3):
    lst1.append([])234
    for j in range(3):
        lst1[i].append(lst[var])
        var += 1

#print(lst1)
for i in range(3):
    print()
    for j in range(3):
        print(lst1[i][j], end = ' ')
        