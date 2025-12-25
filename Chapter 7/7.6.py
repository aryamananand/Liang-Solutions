import math
class QuadraticEquation:
    def __init__ (self):
        self.a = 0
        self.b = 0
        self.c = 0 
        self.d = 1
    def setA(self, a):
        self.a = a
    def setB(self, b):
        self.b = b
    def setC(self, c):
        self.c = c
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def setDiscriminant(self):
        self.d = self.b ** 2 - 4 * self.a * self.c
    def getDiscriminant(self):
        return self.d
    def getRoot1(self):
        if self.d >= 0:
            root1 = (-self.b - math.sqrt(self.d)) / (2 * self.a)
            return root1
        else: 
            print("This quadratic equation has no real roots.")
    def getRoot2(self):
        if self.d > 0:
            root2 = (-self.b + math.sqrt(self.d)) / (2 * self.a)
            return root2
        if self.d == 0:
            return "This quadratic equation has only one root."
        else:
            return ""

def main():
    eq1 = QuadraticEquation()
    a = eval(input("Enter coefficient a: "))
    b = eval(input("Enter coefficient b: "))
    c = eval(input("Enter coefficient c: "))
    eq1.setA(a) 
    eq1.setB(b)
    eq1.setC(c)
    eq1.setDiscriminant()
    if eq1.getDiscriminant() > 0:
        print(f"The roots are {eq1.getRoot1()} and {eq1.getRoot2()}")
    elif eq1.getDiscriminant() == 0:
        print(f"The root is {eq1.getRoot1()}")
    else:
        print("This equation has no real roots.")
main()