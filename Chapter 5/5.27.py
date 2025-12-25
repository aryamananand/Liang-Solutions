

for loops in range (10000, 100001, 10000):
    sum_ = 0
    for i in range (1, loops):
        sum_ += ((-1) ** (i + 1))/(2 * i-1)
    print(sum_ * 4)
