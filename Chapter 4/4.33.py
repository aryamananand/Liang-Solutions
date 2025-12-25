decimal = eval(input("Enter a decimal value (0 - 15): "))


if (decimal <= 9 and decimal >= 0):
    print("The hex value is", decimal)

elif (decimal > 9 and decimal <= 15):
    hexval = decimal + 56
    print("The hex value is", chr(hexval))
else: 
    print("Input is invalid")


'''

elif decimal == 10:
    print("The hex value is A")
elif decimal == 11:
    print("The hex value is B")
elif decimal == 12:
    print("The hex value is C")
elif decimal == 13:
    print("The hex value is D")
elif decimal == 14:
    print("The hex value is E")
elif decimal == 15:
    print("The hex value is F")
else: 
    print("Input is invalid")

'''
