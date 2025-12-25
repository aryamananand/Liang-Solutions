import random
import time

NUMBER_OF_RUNS = 10
correctCount = 0
count = 0

start_time = time.time()

while count < NUMBER_OF_RUNS:
    number1 = random.randint(1,15)
    number2 = random.randint(1,15)

    if number1 < number2:
        number1, number2 = number2, number1

    answer = eval(input("What is " + str(number1) + "-" + str(number2) + "?"))

    if number1 - number2 == answer:
        print("The answer is correct!")
        correctCount += 1
    else:
        print("The answer is wrong.\n", number1, "-", number2, "is", number1 - number2)

    count += 1

end_time = time.time()
tot_time = int(end_time - start_time)
print("Correct count is", correctCount, "out of", NUMBER_OF_RUNS, "\nTest time is", tot_time, "seconds")

if correctCount == 10:
    print("Excellent, you got everything right!")
elif correctCount >= 6:
    print("Good.")
else:
    print("Poor.")
