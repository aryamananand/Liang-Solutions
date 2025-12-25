sum_ = 0
for denominator in range (1,50001):
    sum_ += (1/denominator)

print(sum_)

Sum = 0
for denom in range (50000,0,-1):
    Sum += (1/denom)

print(Sum)

print(format(abs(sum_ - Sum), "10.2e"))
