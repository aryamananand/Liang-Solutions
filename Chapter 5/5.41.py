number = eval(input("Enter a number (0: for end input): "))

Max = number
count = 1

while number != 0:
    number = eval(input("Enter a number (0: for end input): "))
    if number > Max:
        Max = number
        count = 1
    elif number == Max:
        count += 1

print("The largest number is: ", Max)
print("The occurence count of the largest number", Max, "is:", count) 
    
