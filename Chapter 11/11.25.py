def isMarkovMatrix(lst):
    x = 0
    for r in range(3):
        for c in range(3):
            if lst[r][c] > 0:
                x += 1
    if x == 9:
        b = 0
        for r in range(3):
            a = 0
            for c in range(3):
                a += lst[c][r]
            if a == 1:
                b += 1
        if b == 3:
            return True
        else:
            return False
    else:
        return False

lst = [[0.15, 0.875, 0.375],[0.55,0.005,0.225],[0.30,0.12,0.4]]
print(isMarkovMatrix(lst))
