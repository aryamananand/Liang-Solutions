'''
Datafields:
-numerator: int
-denominator: int
Rational(numerator = 0: int, denominator = 1: int)
_ _add_ _(secondRational: Rational): Rational
_ _sub_ _(secondRational: Rational): Rational
_ _mul_ _(secondRational: Rational): Rational
_ _truediv_ _(secondRational: Rational): Rational
_ _lt_ _(secondRational: Rational): bool
Also __le__, __eq__, __ne__, __gt__, __ge__ are supported
__int__(): int __float__(): float __str__(): str
_ _getitem_ _(i)

CUSTOM MODIFICATIONS:

    func decimalApproximation: returns the decimal equivalent. Exact upto 9 digits, 10th digit is approximation.

'''

def gcd(n, d):
    n1 = abs(n)
    n2 = abs(d)
    gcd = 1

    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k 
        k += 1
    return gcd

class Rational:
    def __init__(self, numerator = 1, denominator = 0):
        divisor = gcd(numerator, denominator)
        self.__numerator = (1 if denominator > 0 else -1) \
            * int (numerator / divisor)
        self.__denominator = int(abs(denominator) / divisor)

    #Add a rational number to this rational number
    def __add__(self, secondRational):
        n = self.__numerator * secondRational[1] + \
            self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n , d)
    
    #Subtract a rational number from this rational number
    def __sub__(self, secondRational):
        n = self.__numerator * secondRational[1] - \
            self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)
    
    #Multiply a rational number by this rational number
    def __mul__(self, secondRational):
        n = self.__numerator * secondRational[0]
        d = self.__numerator * secondRational[1]
        return Rational(n , d)
    
    #Divide a rational number by this rational number
    def __truediv__(self, secondRational):
        n = self.__numerator * secondRational[1]
        d = self.__denominator * secondRational[0]
        return Rational(n, d)
    
    #Return a float fro the rational number
    def __float__(self):
        return self.__numerator / self.__denominator

    def decimalApproximation(self):
        a =  self.__numerator / self.__denominator
        if len(str(a)) <= 9:
            return a
        else:
            return str(a) + " (Approx.)"
    
    #Return an integer for the rational number
    def __int__(self):
        return int(self.__float__())
    
    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)
    def __lt__(self, secondRational):
        return self.__cmp__(secondRational) < 0 
    
    def __le__(self, secondRational):
        return self.__cmp__(secondRational) <= 0
    
    def __gt__(self, secondRational):
        return self.__cmp(secondRational) > 0
    def __ge__(self, secondRational):
        return self.__cmp__(secondRational) >= 0    
    
    #Compare two number 
    def __cmp__(self, secondRational):
        temp = self.__sub__(secondRational)
        if temp[0] > 0:
            return 1
        elif temp[0] < 0:
            return -1
        else:
            return 0
        
    #Return numerator and denominator using an index operator 
    def __getitem__(self, index):
        if index == 0:
            return self.__numerator
        else:
            return self.__denominator


    

    