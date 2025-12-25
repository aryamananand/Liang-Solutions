integer = eval(input("Enter an integer: "))

half = integer / 2

number = 2

while number < half:
    
    isPrime = True
    divisor = 2
 
    while divisor <= number / 2:
        
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1

        
    if isPrime and integer % number == 0:
        print(number, ", ", end = '')
        integer /= number
    else:
        number += 1



    

        
    

'''

    while integer > 1:
        if integer % number == 0:
            divisor1 = number
            integer /= number
            print(divisor1, ", ", end= '')
'''             

    


'''
number = 2
isPrime = True
divisor = 2

num = int(number/2 + 1)
for divisor in range(2, num):
    if number % divisor == 0:
        isPrime = False
        break
    number += 1

    if isPrime:
        prime = number
        print(prime, ", ", end ='')
    divisor += 1

    while integer > 1:
        print(prime, ", ", end ='')
        integer /= prime
'''

    
