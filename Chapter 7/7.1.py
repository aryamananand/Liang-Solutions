class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getPerimeter(self):
        return 2 * (self.width + self.height)
    def getArea(self):
        return self.height * self.width
    
r1 = Rectangle(4, 40)
r2 = Rectangle(3.5, 35.7)

print(f"Dimensions of Rectangle 1: width = {r1.width} & height = {r1.height} ")
print(f"Dimensions of Rectangle 2: width = {r2.width} & height = {r2.height} ")

print(f"Rectangle1 has an area of: {r1.getArea()}")
print(f"Rectangle2 has an area of: {r2.getArea()}")

print(f"Rectangle 1 has a perimeter of: {r1.getPerimeter()}")
print(f"Rectangle 2 has a perimeter of: {r2.getPerimeter()}")


