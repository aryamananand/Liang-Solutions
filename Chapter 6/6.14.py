def m(i):
    sum_ = 0
    for j in range (1,i+1):
        num = ((-1) ** (j + 1))/((2 * j) - 1)
        sum_ += num
        
    res = 4 * sum_
    return res

def main():
    print("i          m(i)")
    print()
    for i in range (1,902, 100): 
        print(i, "        ", m(i))
main()
