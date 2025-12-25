class GeometricObject():
    def __init__ (self, colour = 'green', filled = True):
        self.__colour = colour 
        self.__filled = filled

    def getColour(self):
        return self.__colour
    
    def setColour(self, colour):
        self.__colour = colour
    
    def isFilled(self):
        return self.__filled
    
    def setFilled(self, filled):
        self.__filled = filled
    
    def __str__(self):
        return "colour: " + self.__colour + \
            " and filled: " + str(self.__filled)
    
    

class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def setSide1(self, side1):
        self.__side1 = side1
    
    def setSide2(self, side2):
        self.__side2 = side2
    
    def setSide3(self, side3):
        self.__side3 = side3
    
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3
    
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        
        area = (s*(s-self.__side1)*(s-self.__side2)*(s-self.__side3))**0.5
        
        return format(area, ".2f")
    
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    
    def __str__(self):
        return "Triangle: side 1: " + str(self.__side1) + \
            "side 2: " + str(self.__side2) + \
            "side 3: " + str(self.__side2) 
    

tri1 = Triangle()
side1 = eval(input(f"Enter side 1: "))
tri1.setSide1(side1)
side2 = eval(input(f"Enter side 2: "))
tri1.setSide2(side2)
side3 = eval(input(f"Enter side 3: "))
tri1.setSide3(side3)
colour = input("Enter colour: ")
tri1.setColour(colour)
filled_input = eval(input("Filled? (1  - Yes, 0 - No): "))
filled = False
if filled_input == 1:
    filled = True
tri1.setFilled(filled)

print("Area: " + str(tri1.getArea()) + "\n" + \
      "Perimeter: " + str(tri1.getPerimeter()) + "\n" + \
      "Colour: " + str(tri1.getColour()) + "\n" + \
      "Filled: " + str(tri1.isFilled()))
