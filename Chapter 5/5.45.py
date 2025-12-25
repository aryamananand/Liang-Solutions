decimal = eval(input("Enter decimal number: "))

#decimal *= 16 ** 4

if decimal == 0:
    print(0)
    
else:
    string = ""
    while decimal >= 1:
        hexval = decimal % 16
        if hexval == 10:
            digit = "A"
        elif hexval == 11:
            digit = "B"
        elif hexval == 12:
            digit = "C"
        elif hexval == 13:
            digit = "D"
        elif hexval == 14:
            digit = "E"
        elif hexval == 15:
            digit = "F"
        else:
            digit = hexval

        #print(digit, end ='')
        string = str(digit) + string
        
        decimal //= 16

        
    print(string)

    #print(''.join(reversed(string)))

    # ''.join(reversed(string)) allows us to reverse a given string

    
