def linearEquation(a,b):
    if a[0][0]*a[1][1] - a[0][1]*a[1][0] != 0:
        x = (b[0]*a[1][1]-b[1]*a[0][1])/(a[0][0]*a[1][1]-a[0][1]*a[1][0])
        y = (b[1]*a[0][0]-b[0]*a[1][0])/(a[0][0]*a[1][1]-a[0][1]*a[1][0])
        print(f"x is {format(x,".2f")} and y is {format(y,".2f")}.")
    elif a[0][0]*a[1][1] - a[0][1]*a[1][0] == 0:
        print('The equation has no solution.')

lst1 = input('Enter a00, a01, a10, a11, b0, b1: ').split(', ')

lst = []
for i in lst1:
    lst.append(float(i))


a = [[lst[0], lst[1]], [lst[2], lst[3]]]
b = [lst[4], lst[5]]

linearEquation(a,b)


