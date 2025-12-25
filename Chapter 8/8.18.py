import math
class Circle2D:
    def __init__(self):
        self.x = 0
        self.y = 0 
        self.radius = 0
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x
    def setY(self, y):
        self.y = y
    def getY(self):
        return self.y
    def setRadius(self, radius):
        self.radius = radius 
    def getRadius(self):
        return self.radius 
    def getArea(self):
        return math.pi * (self.radius ** 2)
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    def containsPoint(self, x, y):
        dist = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        if dist <= self.radius:
            return True 
        else:
            return False 

    def overlaps(self, c1, c2) -> bool:
        if c1.contains(c2) == "c1 contains c2." or c1.contains(c2) == "c2 contains c1.":
            return "The circles contain one another:"
        else:
            centDis = math.sqrt((self.x - c2.getX()) ** 2 + (self.y - c2.getY()) ** 2)
            if centDis == self.radius + c2.getRadius():
                return ("The circle are tangential.")
            elif centDis < self.radius + c2.getRadius():
                return ("The circles are overlapping.")
            else:
                return ("The circles are not overlapping.")
        

    def contains(self, c2) -> bool:
        centDis = math.sqrt((self.x - c2.getX()) ** 2 + (self.y - c2.getY()) ** 2)
        if centDis + c2.radius < self.radius:
            return ("c1 contains c2.")
        elif centDis + self.radius < c2.radius:
            return ("c2 contains c1.")
        else:
            return ("Neither circle contains the other.")
    def __cmp__(self, c2):
        if self.getArea() < c2.getArea():
            return -1 
        elif self.getArea() == c2.getArea():
            return 0
        elif __self.getArea() > c2.getArea():
            return 1
    def __eq__(self, c2):
        if self.getArea() == c2.getArea():
            return True
        else:
            return False
    def __lt__(self, c2):
        if self.getArea() < c2.getArea():
            return True
        else:
            return False
    def __le__(self, c2):
        if self.getArea() <= c2.getArea():
            return True
        else:
            return False
    def __ne__(self, c2):
        if self.getArea() != c2.getArea():
            return True
        else:
            return False
    def __gt__(self, c2):
        if self.getArea() > c2.getArea():
            return True
        else:
            return False
    def __ge__(self, c2):
        if self.getArea() >= c2.getArea():
            return True
        else:
            return False
def main():
    x1, y1, r1 = eval(input("Enter x1, y1 and radius1: "))
    x2, y2, r2 = eval(input("Enter x2, y2 and radius2: "))
    #Constructor
    c1 = Circle2D()
    c1.setX(x1)
    c1.setY(y1)
    c1.setRadius(r1)
    c2 = Circle2D()
    c2.setX(x2)
    c2.setY(y2)
    c2.setRadius(r2)
    print("The area for c1 is", c1.getArea())
    print("The perimeter for c1 is", c1.getPerimeter())
    print("The area for c2 is", c2.getArea())
    print("The perimeter for c2 is", c2.getPerimeter())
    print(c1.overlaps(c1, c2))
    print(c1.contains(c2))
    print(c1 == c2)
    print(c1 > c2)
    print(c1 <= c2)
main()
