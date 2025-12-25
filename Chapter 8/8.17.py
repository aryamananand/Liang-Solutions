import math 
class Point:
    def __init__ (self):
        self.x = 0
        self.y = 0 
        self.x = 0
        self.dist = 0
    def setX(self, x):
        self.x = x
    def getX(self) -> int:
        return self.x
    def setY(self, y):
        self.y = y
    def getY(self) -> int:
        return self.y
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def distance(self, p2) -> float:
            distance = math.sqrt((p2.getX() - self.x)**2 + (p2.getY() - self.y)**2)
            self.dist = distance
            return distance 
    def isNearby(self) -> bool:
        if self.dist <= 5:
            return "The two points are nearby."
        else:
            return "The two points are not nearby."




def main():
    x1, y1, x2, y2 = eval(input("Enter x1, y1, x2, y2: "))
    p1 = Point()
    p2 = Point()
    p1.setX(x1)
    p1.setY(y1)
    p2.setX(x2)
    p2.setY(y2)
    print(f"The distance between the two points is {p1.distance(p2)}")
    print(p1.isNearby())
    print(p1)
main()
