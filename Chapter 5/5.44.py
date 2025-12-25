decimal = eval(input("Enter a decimal number: "))
if decimal == 0:
    print(0)

else:

    order = 1
    total = 0
    
    while decimal >= 1:
        remainder = decimal % 2
        digit = remainder * order
        order *= 10
        total += digit
        #print(1)  #for debugging
        
        decimal //= 2
        


    print(total)
        
