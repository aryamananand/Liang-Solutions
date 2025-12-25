
number = eval(input("Enter an integer, input ends if it is 0: "))

sum = 0

neg_count = 0
pos_count = 0
tot_count = 0

while number != 0:
    sum += number
    if number < 0:
        neg_count += 1
    else:
        pos_count += 1
    number = eval(input("Enter an integer, input ends if it is 0: "))
    tot_count += 1 

print("The number of positives is: ", pos_count)
print("The number of negatives is: ", neg_count)
print("The total is: ", tot_count)

if tot_count != 0:
    print("The average is: ", format(sum / tot_count, ".2f"))
else:
    print("The average is: ",0)
