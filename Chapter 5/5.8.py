import math

print("Number       Square Root")
print()

number = 0
for number in range (0,10):
    print(number, "          ", format(math.sqrt(number), ".4f"))
    number += 1

#This is for alignment:
number = 10
for number in range (10,21):
    print(number, "         ", format(math.sqrt(number), ".4f"))
    number += 1
