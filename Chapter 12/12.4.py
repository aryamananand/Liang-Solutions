import math
import sys


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
    def __str__(self):
        return f"The bounding rectangle is centred at ({self.x}, {self.y}) with width {self.width} and height {self.height}."
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


class BoundingRectangle(Rectangle2D):
    def __init__(self):
        self.pointList = input("Enter the points: ").split( )
        
        if len(self.pointList) % 2 != 0:
            print("Please check your input.")
            sys.exit()
        else:
            self.pointListFinal = []
            count = -1
            for i in range(0,len(self.pointList)-1,2):    # Make a 2D list with the points
                count += 1
                self.pointListFinal.append([])
                self.pointListFinal[count].append(float(self.pointList[i]))
                self.pointListFinal[count].append(float(self.pointList[i+1]))

        self.rectangleBounds()  # run the bounding function

    def rectangleBounds(self):    
        minX = self.pointListFinal[0][0]
        maxX = self.pointListFinal[0][0]
        minY = self.pointListFinal[0][1]
        maxY = self.pointListFinal[0][1]

        for i in range(len(self.pointListFinal)):
            if self.pointListFinal[i][0] < minX:
                minX = self.pointListFinal[i][0]
            if self.pointListFinal[i][0] > maxX:
                maxX = self.pointListFinal[i][0]
            if self.pointListFinal[i][1] < minY:
                minY = self.pointListFinal[i][1]
            if self.pointListFinal[i][1] > maxY:
                maxY = self.pointListFinal[i][1]

        print(minY, maxY)
        midX = (minX + maxX)/2
        midY = (minY + maxY)/2

        
        rect1 = Rectangle2D()
        rect1.setWidth(maxX-minX)
        rect1.setHeight(maxY-minY)
        rect1.setX(midX)
        rect1.setY(midY)
        print(rect1)

BoundingRectangle()


        

            
