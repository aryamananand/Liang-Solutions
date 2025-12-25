ISBN_12 = str(input("Enter the first 12 digits of an ISBN-13 as a string: ")).strip()


sum = 0
for i in range (0,12): 
    a = int(ISBN_12[i]) 
    if i % 2 == 0: 
        sum += a
    else:
        sum += 3 * a 
if sum == 10:
    sum == 0
    
res = 10 - sum % 10 

print(f"The ISBN-13 number is {ISBN_12}{str(res)}.")
    
