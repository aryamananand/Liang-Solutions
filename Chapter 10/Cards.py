import matplotlib.pyplot as plt
import random

Slot = [0 for x in range (40)]

x_slot = [x for x in range (40)]


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

ITERATIONS = 10000

total = 0

for i in range(ITERATIONS):
    
    suit = random.randint(0,3)
    rank = random.randint(0,12)
    lstSUITS = []
    card = str(ranks[rank] + ' of ' + suits[suit])
    lstSUITS.append(str(suits[suit]))

    #print(lstSUITS)

    lstCARDS = []
    lstCARDS.append(card)

    #print(lstCARDS)

    count = 1   #since we start with a card
    while len(lstSUITS) <= 3:
        suit = random.randint(0,3)
        rank = random.randint(0,12)
        if lstCARDS.count(str(ranks[rank] + ' of ' + suits[suit])) == 0:  #if card is not there, add it to the list.
            card = str(ranks[rank] + ' of ' + suits[suit])
            lstCARDS.append(card)
            count += 1 
            #print(card)
        if lstSUITS.count(str(suits[suit])) == 0:
            lstSUITS.append(str(suits[suit]))
    total += count

    Slot[count] += count

print(total/i)  #average draw

print(Slot)



plt.bar(x_slot, Slot)
plt.show()
