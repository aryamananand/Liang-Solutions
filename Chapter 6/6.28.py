
import random

sum_of_rolls = 0
previousRoll = 1
winVal = 0
a = 1 #variable to confirm first roll
while sum_of_rolls != 7:
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    sum_of_rolls = roll1 + roll2

    print(f"You rolled  {roll1} + {roll2} = {sum_of_rolls}.")
    if winVal == sum_of_rolls:
        print("You win")
        break 

    if (sum_of_rolls == 2 or sum_of_rolls == 3 or sum_of_rolls == 12) and a == 1:
        #Only for first round
        print("You lose.")
        break
    elif ((sum_of_rolls == 7 and a == 1) or sum_of_rolls == 11) and a == 1:
        #Only for first round
        print("You win.")
        break
    elif sum_of_rolls == 7 and a != 1:
        #second round onwards
        print("You lose")
        break
    else:
        if a == 1:
            print(f"Your point is {sum_of_rolls}")
            winVal = sum_of_rolls #winVal is the first point
    a += 1 #Change the value of A 

