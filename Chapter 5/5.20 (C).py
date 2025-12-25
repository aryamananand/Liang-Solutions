print("Pattern C")

for count in range (1,7):
    space = " " * (12 - 2 * count)
    print(space, end = '')
    for num in range(count,0,-1):
        print(num, "", end ='')
    print()
