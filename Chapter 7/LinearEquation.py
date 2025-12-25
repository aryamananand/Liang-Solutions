class LinearEquation: 
    def __init__ (self):
        self.a = int
        self.b = int
        self.c = int
        self.d = int
        self.e = int
        self.f = int
    
    def setA(self, a):
        self.a = a 
    def setB(self, b):
        self.b = b
    def setC(self, c):
        self.c = c
    def setD(self, d):
        self.d = d
    def setE(self, e):
        self.e = e  
    def setF(self, f):
        self.f = f 

    def getA (self):
        return self.a 
    def getB (self):
        return self.b
    def getC (self):
        return self.c 
    def getD (self):
        return self.d 
    def getE (self):
        return self.e
    def getF (self):
        return self.f 
    
    def isSolvable(self):
        if (self.a * self.d - self.b * self.c) != 0:
            return 1
        else:
            return 0
    def getX(self):
        x = (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)
        return x
    def getY(self):
        y = (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)
        return y



