def reverse(number_):
    number = number_
    count = -1
    while number_ >= 1:
        unitsDigit = number_ % 10 
        number_ = (number_ - unitsDigit)/10
        count += 1 #number of digits in integer

    

    
    order = 10 ** (count)
    sum_ = 0

    while number >= 1:
        unitsDigit_ = number % 10 #764 becomes 4
        tensPlace = number // 10 # 764 becomes 76 
        number = (number - unitsDigit_)/10
        sum_ += unitsDigit_ * order
        order /= 10
    
    return int(sum_)

def main():
    number_ = eval(input("Enter an integer: "))
    print(reverse(number_))

main()
