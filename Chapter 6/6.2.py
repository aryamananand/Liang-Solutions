


def sumDigits(number):
    sum_ = 0
    while number >= 1:
        unitsDigit = number % 10 #764 becomes 4
        sum_ += unitsDigit
        number //= 10
         

    return sum_

def main():
    num = eval(input("Enter an integer: "))
    print("The sum of the digits is", sumDigits(num))
        
main()

