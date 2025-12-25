hexval = input("Enter a hex character: (0 - F) ")

#Get ASCII number for letter
code = ord(hexval)


if code >= 65 and code <= 70:
    print("The decimal value is: ", code - 55)
          
elif int(hexval) >= 0 and int(hexval) <= 9:
    print("The decimal value is: ",hexval)

    


