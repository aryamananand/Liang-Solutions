import random

def printMatrix(n):
    for column in range (1, n+1):
        for i in range (1,n+1):
            a = random.randint(0,1)
            print(a, end = ' ')
        print()

def main():
    n = eval(input("Enter n: "))
    printMatrix(n)
main()
