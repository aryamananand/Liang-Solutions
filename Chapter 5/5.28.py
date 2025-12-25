
for count in range (10000, 100001, 10000):
    e = 1
    factorial = 1
    for i in range (1,count+1):
        factorial *= i
        e += (1/factorial)


    print(e)
    

