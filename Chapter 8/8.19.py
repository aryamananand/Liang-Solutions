import math
class Rectangle2D:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
    def setX(self, x):
        self.x = x
    def getX(self) -> int:
        return self.x
    def setY(self, y):
        self.y = y
    def getY(self) -> int:
        return self.y
    def setWidth(self, width):
        self.width = width
    def getWidth(self):
        return self.width
    def setHeight(self, height):
        self. height = height
    def getHeight(self):
        return self.height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return 2 * (self.width + self.height)
    def containsPoint(self, x, y):
        limX1 = self.x - (self.width/2)
        limX2 = self.x + (self.width/2)
        limY1 = self.y - (self.height/2)
        limY2 = self.y + (self.height/2)

        if limX1 <= x <= limX2 and limY1 <= y <= limY2:
            return True 
        else:
            return False
    def overlaps(self, r1, r2):
        if r1.contains(r2) == "Neither rectangle contains the other.":

            if abs(int(r2.getX() - self.x))  < self.width/2 + r2.getWidth()/2 and abs(int(r2.getX() - self.x)) < self.height/2 + r2.getHeight()/2:
                return "R1 overlaps R2."
            else:
                return "R1 does not overlap R2."
        else:
            return "The rectangles contain one another."
    def contains(self, r2):
        if abs(int(r2.getX() - self.x))  < self.width/2 + r2.getWidth()/2 and  \
            abs(int(r2.getX() - self.x)) < self.height/2 + r2.getHeight()/2 and \
            r2.getWidth() <= self.width and r2.getHeight() <= self.height:
            return "R1 contains R2."
        elif abs(int(r2.getX() - self.x))  < self.width/2 + r2.getWidth()/2 and \
             abs(int(r2.getX() - self.x)) < self.height/2 + r2.getHeight()/2 and \
             self.width <= r2.getWidth() and self.height <= r2.getHeight():
            return "R2 contains R1."
        else:
            return "Neither rectangle contains the other."
    def __cmp__(self, c2):
        if self.getArea() < c2.getArea():
            return -1 
        elif self.getArea() == c2.getArea():
            return 0
        elif self.getArea() > c2.getArea():
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
    x1, y1, h1, w1 = eval(input("Enter x1, y1, height1 and width1: "))
    x2, y2, h2, w2 = eval(input("Enter x2, y2, height2 and width2: "))
    r1 = Rectangle2D()
    r1.setX(x1)
    r1.setY(y1)
    r1.setHeight(h1)
    r1.setWidth(w1)
    r2 = Rectangle2D()
    r2.setX(x2)
    r2.setY(y2)
    r2.setHeight(h2)
    r2.setWidth(w2)
    print(r1.overlaps(r1, r2))
    print(r1.contains(r2))
    print(r1 < r2)
    print(r1 >= r2)
    print(r2 == r2)
main()
