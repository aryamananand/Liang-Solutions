
def sqrt(n):

    a = 0
    lastGuess = 1
    while a != 1:
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        if abs (nextGuess - lastGuess) <= 0.0001:
            a = 1
            break
        lastGuess = nextGuess
        
        
    return format(nextGuess, ".3f")


def main():
    n = eval(input("Enter an integer: "))
    print(f"Square root of {n} is {sqrt(n)}")
main()
