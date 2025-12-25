import time


number = round(time.time() * 1000)

#get random values from 0 to 25
number2 = number % 26

#CAP -> ASCII: 65 to 90 
code = number2 + 65

letter = chr(code)
print("Random uppercase letter: ", letter)


