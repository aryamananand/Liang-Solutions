#   (Game: scissor, rock, paper) Write a program that plays the popular scissor-rock- paper game.
#   (A scissor can cut a paper, a rock can knock a scissor, and a paper can wrap a rock.)
#   The program randomly generates a number 0, 1, or 2 representing scissor, rock, and paper.
#   The program prompts the user to enter a number 0, 1, or 2 and displays a message indicating
#   whether the user or the computer wins, loses, or draws.

import random

computer = random.randint(0,2)

user = eval(input("Enter scissors (0), rock (1) or paper (2): "))

if computer == 0:
    comp_print = "scissors"
elif computer == 1:
    comp_print = "rock"
else:
    comp_print = "paper"


if user == 0:
    user_print = "scissors"
elif user == 1:
    user_print = "rock"
else:
    user_print = "paper"



if computer == user:
    result = "It is a draw."
elif ((computer == 0 and user == 1) \
     or (computer == 1 and user == 2) \
     or (computer == 2 and user == 0)):
    result = "You win!"
else:
    result = "You lose."

print("The computer is " + str(comp_print) + ". You are " + str(user_print) + ". " + str(result))
