integer = eval(input("Enter an integer between 0 and 1000:"))

unit = integer % 10 #this is the units digit


unitless = integer // 10

tens = unitless % 10 #this is the tens digit

hundreds = unitless // 10 #this is the hundreds digit

summation = unit + tens + hundreds

print("The sum of the digits is:", summation)


