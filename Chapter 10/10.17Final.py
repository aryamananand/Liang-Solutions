lst1 = list(input('Enter a word:').strip(''))
lst2 = list(input('Enter a word:').strip(''))

for x in lst1:
    if x == ' ':
        lst1.remove(x)

for y in lst2:
    if y  == ' ':
        lst2.remove(y)

for i in range(len(lst1)):
    lst1[i] = lst1[i].upper()
    lst1[i] = int(ord(lst1[i]))


for j in range(len(lst2)):
    lst2[j] = lst2[j].upper()
    lst2[j] = int(ord(lst2[j]))

#print(lst1)
#print(lst2)

lst1.sort()
lst2.sort()

#print(lst1)
#print(lst2)

if len(lst1) != len(lst2):
    print('Is not an anagram')
elif lst1 == lst2:
    print('Is an anagram.')
else:
    print('Is not an anagram.')

