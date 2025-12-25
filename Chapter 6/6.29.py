

def sumOfDoubleEvenPlace (number):
    sum_ = 0
    count = 1
    while number >= 1:
        x = 0
        if count % 2 == 0:
            digit = 2 *( number % 10)
            x = getDigit(digit)     
        sum_ += x
        number //= 10
        count += 1

    return sum_

def sumOfOddPlace (number):
    sum_ = 0
    count = 0
    while number >= 1:
        x = 0
        if count % 2 == 0:
            digit = ( number % 10)
            sum_ += digit        
        
        number //= 10
        count += 1

    return sum_

def getDigit(digit):
    if digit > 9:
        digit = digit % 10 + digit // 10
    return digit



def prefixMatched (number):
    a = number // (10 ** 15)
    b = number // (10 ** 14)
    c = number // (10 ** 13)
    d = number // (10 ** 12)
    e = number // (10 ** 11)


    if a == 4 or b == 4 or c == 4 or d == 4:
        return True
    elif a == 5 or b == 5 or c == 5 or d == 5:
        return True
    elif a == 6 or b == 6 or c == 6 or d == 6:
        return True
    elif b == 37 or c == 37 or d == 37 or e == 37:
        return True
    else:
        return False
        

def getSize(number):
    a = number // (10 ** 15)
    b = number // (10 ** 14)
    c = number // (10 ** 13)
    d = number // (10 ** 12)
    e = number // (10 ** 11)
    
    if a == 4 or b == 4 or c == 4 or d == 4:
        d_ = 1
    elif a == 5 or b == 5 or c == 5 or d == 5:
        d_ = 1
    elif a == 6 or b == 6 or c == 6 or d == 6:
        d_ = 1
    elif b == 37 or c == 37 or d == 37 or e == 37:
        d_ = 2
    else:
        d_ = "None"

    return d_

def isValid(n):
    if prefixMatched(n) is True and (sumOfDoubleEvenPlace(n) + sumOfOddPlace(n)) % 10 == 0:
        return "Credit card is valid."
    else:
        return "Credit card is invalid."

def main():
    number = eval(input("Enter credit card number: "))
    print(isValid(number))
main()
    
                
     
