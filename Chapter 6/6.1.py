def getPentagonalNumber(n):
    number = n * (3 * n - 1)/2 
    return number


def main():
    for i in range (1, 101):
        print(int(getPentagonalNumber(i)), end = ' ')
        if i % 10 == 0:
            print("\n ")
            
main()
