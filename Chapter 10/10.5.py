FinalList = input('Enter ten numbers:').split(' ')
for i in range (100):
    if str(i) in FinalList:
        print(i, end = ' ')
