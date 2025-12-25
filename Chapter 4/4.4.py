import random

number1 = random.randint(0,100)
number2 = random.randint(0,100)

answer = eval(input("What is " + str(number1) + " + " + str(number2) + "?"))

if answer == number1 + number2:
    print("True")
else:
    print("False")
    


