

def sumDigits(n):
    if n // 10 == 0:
        return n
    else:
        return (n % 10) + sumDigits(n//10)


print(sumDigits(92183))


