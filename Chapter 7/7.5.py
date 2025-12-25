import math 
class RegularPolygon:
    def __init__ (self):
        self.n = 3  #Default n = 3
        self.side = 1     #Default side is 1
        self.x = 0
        self.y = 0    #Default (x,y) = (0,0)
    def setn(self, n):
        self.n = n
    def setSide(self, side):
        self.side = side
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y 
    def getPerimeter(self):
        perimeter = self.side * self.n
        return perimeter
    def getArea(self):
        area = (self.n * (self.side)**2) / (4 * (math.tan(math.pi / self.n))) 
        return area
    
def main():
    rp1 = RegularPolygon()
    rp1.setn(6)
    rp1.setSide(4)
    
    rp2 = RegularPolygon()
    rp2.setn(10)
    rp2.setSide(4)
    rp2.setX(5.6)
    rp2.setY(7.8)

    print("Regular Polygon 1: ")
    print(f"Area: {rp1.getArea()}")
    print(f"Perimeter: {rp1.getPerimeter()}")
    print()
    print("Regular Polygon 2: ")
    print(f"Area: {rp2.getArea()}")
    print(f"Perimeter: {rp2.getPerimeter()}")
main()
    