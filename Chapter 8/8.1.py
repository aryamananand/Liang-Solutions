

s = str(input("Enter SSN: "))
a = s[0] + s[1] + s[2] + s[4] + s[5] + s[7] + s[8] + s[9] + s[10]
if ord(s[3]) == 45 and ord(s[6]) == 45 and len(s) == 11 and a.isdigit() == True:
    print("Valid SSN. ")
else:
    print("Invalid SSN. ")

