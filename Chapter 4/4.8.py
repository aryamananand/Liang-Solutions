number1, number2, number3 = eval(input("Enter three different integers: "))


if number1 < number2 and number2 < number3:
    result = "The numbers sorted in increasing order are: " + str(number1) + ", " + str(number2) + ", " + str(number3)

elif number1 < number2 and number2 > number3:
    result = "The numbers sorted in increasing order are: " + str(number1) + ", " + str(number3) + ", " +  str(number2)

elif number1 < number2 and number2 > number1:
    result = "The numbers sorted in increasing order are: " + str(number3) + ", " +  str(number1) + ", " +  str(number2)
    
elif number1 > number2 and number2 < number3:
    result = "The numbers sorted in increasing order are: " + str(number2) + ", " +  str(number1) + ", " +  str(number3)
    
elif number1 > number2 and number2 > number1:
    result = "The numbers sorted in increasing order are: " + str(number3) + ", " +  str(number2) + ", " +  str(number1)

elif number1 > number2 and number2 < number1:
    result = "The numbers sorted in increasing order are: " + str(number2) + ", " +  str(number3) + ", " +  str(number1)

print(result)

'''
if number1 < number2 < number3:
    result = "The numbers sorted in increasing order are: " + str(number1) + ", " + str(number2) + ", " + str(number3)
if number1 < number3 < number
    
    
'''
