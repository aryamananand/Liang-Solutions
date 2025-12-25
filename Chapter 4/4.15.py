import random

lottery = random.randint(0,999)

'''print(lottery)'''

guess = eval(input("Enter your lottery pick (three digits): "))

lotteryDigit1 = lottery // 100          #Hundreds digit
lotteryDigit_2 = lottery // 10
lotteryDigit2 = lotteryDigit_2 % 10     #Tens digit
lotteryDigit3 = lottery % 10            #Units digit


guessDigit1 = guess // 100          #Hundreds digit
guessDigit_2 = guess // 10
guessDigit2 = guessDigit_2 % 10     #Tens digit
guessDigit3 = guess % 10            #Units digit


'''print(lottery, guess)

print(lotteryDigit1, " ", lotteryDigit2, " ", lotteryDigit3)
print(guessDigit1, " ", guessDigit2, " ", guessDigit3)'''

#MATCHING PROCESS BEGINS:

print("The lottery number is ", lottery)


if guess == lottery:
    print("Exact match: you win $10,000!")
    
elif ((guessDigit1 == lotteryDigit1 and guessDigit2 == lotteryDigit3 and guessDigit3 == lotteryDigit2) \
     or (guessDigit1 == lotteryDigit2 and guessDigit2 == lotteryDigit1 and guessDigit3 == lotteryDigit3) \
      or (guessDigit1 == lotteryDigit3 and guessDigit2 == lotteryDigit1 and guessDigit3 == lotteryDigit2) \
      or (guessDigit1 == lotteryDigit2 and guessDigit2 == lotteryDigit3 and guessDigit3 == lotteryDigit1) \
      or (guessDigit1 == lotteryDigit3 and guessDigit2 == lotteryDigit2 and guessDigit3 == lotteryDigit)):
    
    print("Match all digits: you win $3,000.")
    
elif ((lotteryDigit1 == guessDigit1 or lotteryDigit1 == guessDigit2 or lotteryDigit1 == guessDigit3) \
      or (lotteryDigit2 == guessDigit1 or lotteryDigit2 == guessDigit2 or lotteryDigit2 == guessDigit3) \
      or (lotteryDigit3 == guessDigit1 or lotteryDigit3 == guessDigit2 or lotteryDigit3 == guessDigit3)):
    print("Match at least one digit: you win $1,000")
else:
    print("Sorry, no match.")



    
