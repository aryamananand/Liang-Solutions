



def reverse(number):
    a = 0
    while number >= 1:
        k = number % 10 #764 becomes 4
        a = a * 10 + k
        number //= 10
        

    return a

def isPalindrome(number):
    if reverse(number) == number:
        return True
    
    return False
    

def main():
    n = eval(input("Enter an integer: "))
    print(isPalindrome(n))

main()
    



