# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0: # If true, number is not prime
            return False # number is not a prime
        divisor += 1
    return True # number is prime
 
def main():
    count = -2 #0 and 1 are not primes
    for number in range (10001):
        if isPrime(number) == True: 
            count += 1

    print(f"There are {count} prime numbers from 0 to 10000.")
    
main()
