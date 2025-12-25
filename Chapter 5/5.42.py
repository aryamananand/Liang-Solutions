#   A square is divided into four smaller regions.
#   If you throw a dart into the square one million times, what is the probability
#   for the dart to fall into an odd-numbered region?
#   Write a program to simulate the process and display the result.

import random


#print(x, y)

ITERATIONS = 100000

count1 = 0
count2 = 0
count3 = 0
count4 = 0

for total in range(ITERATIONS):
    x_ = random.random()
    y_ = random.random()

    x = x_ * 2 -1
    y = y_ * 2 -1

    if x <= 0:
        count1 += 1
    elif 0 <= x  and y <= -x + 1 and y >= 0:
        count3 += 1
    elif x >= 0 and y >= 0 and y >= -x + 1:
        count2 += 1
    else:
        count4 += 1

probability1 = count1 / ITERATIONS
print("1 probability is:", format(probability1 * 100, ".2f"), "% for", ITERATIONS, "simulations.")


probability2 = count2 / ITERATIONS
print("2 probability is:", format(probability2 * 100, ".2f"), "% for", ITERATIONS, "simulations.")


probability3 = count3 / ITERATIONS
print("3 probability is:", format(probability3 * 100, ".2f"), "% for", ITERATIONS, "simulations.")


probability4 = count4 / ITERATIONS
print("4 probability is:", format(probability4 * 100, ".2f"), "% for", ITERATIONS, "simulations.")


print(probability1 + probability2 + probability3 + probability4)
