class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self):
        self.speed = 1   #Default speed is 1
        self.radius = 5   #Default radius is 5
        self.on = False     #Fan is initially off
        self.colour = "blue"    #Defult colour is blue

    def turnOn(self):
        self.on = True 
        return self.on
    def turnOff(self):
        self.on = False
        return self.on
    def setSpeed(self, speed):
        self.speed = speed
    def getSpeed(self, speed):
        self.speed = speed
        return self.speed
    def speedUp(self):
        if self.speed < 3:
            self.speed += 1 
    def speedDown(self):
        if self.speed > 1:
            self.speed -= 1
    def setRadius(self,radius):
        self.radius = radius
    def getRadius(self, radius):
        self.radius = radius
        return self.radius
    def setColour(self, colour):
        self.colour = colour
    def getColour(self, colour):
        self.colour = colour
        return self.colour
    
def main():
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    f1 = Fan()
    a = f1.turnOn()
    b = f1.getRadius(10)
    c = f1.getSpeed(max(SLOW, MEDIUM, FAST))
    d = f1.getColour("yellow")
    print(f"Fan 1 is on: {a}, it has a radius of {b}, a speed of {c} and a colour of {d}.")

    f2 = Fan()
    a_ = f2.turnOff()
    b_ = f2.getRadius(5)
    c_ = f2.getSpeed(MEDIUM)
    d_ = f2.getColour("blue")
    print(f"Fan 1 is on: {a_}, it has a radius of {b_}, a speed of {c_} and a colour of {d_}.")
main()

    
    
    


