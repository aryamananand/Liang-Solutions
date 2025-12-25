from tkinter import *
import random 
import math

class TriangleAngles:
    def __init__(self):
        #Variables for control
        self.a = 0  
        self.b = 0
        self.c = 0
        
        self.curDis = 10  #Mouse range
        self.px = 3  #Point size

        self.xA = random.randint(0,500)
        self.yA = random.randint(0,500)

        self.xB = random.randint(0,500)
        self.yB = random.randint(0,500)

        self.xC = random.randint(0,500)
        self.yC = random.randint(0,500)

        self.window = Tk()
        self.window.title('Triangle Angles')
        self.window.geometry('510x510')
        self.canvas = Canvas(self.window, height = 500, width = 500, bg = 'white')
        self.canvas.grid()

        #Draw Initial Triangle 
        self.A = self.canvas.create_oval(self.xA - self.px, self.yA - self.px, self.xA + self.px, self.yA + self.px, fill = 'black', tags = 'A')
        self.canvas.create_text(self.xA + 10, self.yA - 10, text = 'A', fill = 'black', tags = 'text_A')
        self.B = self.canvas.create_oval(self.xB - self.px, self.yB - self.px, self.xB + self.px, self.yB + self.px, fill = 'black', tags = 'B')
        self.canvas.create_text(self.xB + 10, self.yB - 10, text = 'B', fill = 'black', tags = 'text_B')
        self.C = self.canvas.create_oval(self.xC - self.px, self.yC - self.px, self.xC + self.px, self.yC + self.px, fill = 'black', tags = 'C')
        self.canvas.create_text(self.xC + 10, self.yC - 10, text = 'C', fill = 'black', tags = 'text_C')

        self.canvas.create_line(self.xA, self.yA, self.xB, self.yB, fill = 'black', width = 2, tags = 'AB')
        self.canvas.create_line(self.xB, self.yB, self.xC, self.yC, fill = 'black', width = 2, tags = 'BC')
        self.canvas.create_line(self.xA, self.yA, self.xC, self.yC, fill = 'black', width = 2, tags = 'AC')
        
        #Transformation into standard Cartesian coordinates
        self.mod_yA = -1 * self.yA  
        self.mod_yB = -1 * self.yB
        self.mod_yC = -1 * self.yC

        #Initial calculation of side lengths
        self.AB = math.sqrt((self.xA - self.xB) ** 2 + (self.mod_yA - self.mod_yB) ** 2)
        self.BC = math.sqrt((self.xB - self.xC) ** 2 + (self.mod_yB - self.mod_yC) ** 2)
        self.AC = math.sqrt((self.xA - self.xC) ** 2 + (self.mod_yA - self.mod_yC) ** 2)

        #Initial calculation of angles
        self.A = format(math.degrees(math.acos((self.BC ** 2 - self.AC ** 2 - self.AB ** 2 ) / (-2 * self.AC * self.AB))), ".2f")
        self.canvas.create_text(self.xA, self.yA + 10, text = f"{self.A}", fill = 'black', tags = 'ang_A')

        self.B = format(math.degrees(math.acos((self.AC ** 2 - self.BC ** 2 - self.AB ** 2 ) / (-2 * self.BC * self.AB))), ".2f")
        self.canvas.create_text(self.xB, self.yB + 10, text = f"{self.B}", fill = 'black', tags = 'ang_B')

        self.C = format(math.degrees(math.acos((self.AB ** 2 - self.BC ** 2 - self.AC ** 2 ) / (-2 * self.BC * self.AC))), ".2f")
        self.canvas.create_text(self.xC, self.yC + 10, text = f"{self.C}", fill = 'black', tags = 'ang_C')

        self.canvas.bind('<Button1-Motion>', self.drag) #Main dragging indentifier

        self.window.mainloop()
    

    def drag(self, event):

        #Dragging for point A (only if cursor is on point A):
        if (self.xA - self.curDis <= event.x <= self.xA + self.curDis) and (self.yA - self.curDis <= event.y <= self.yA + self.curDis):
            self.a = 1
        if self.verif == True:
            self.a = 0
        if self.a == 1: 
            self.canvas.delete('A', 'AB', 'AC', 'text_A', 'ang_A', 'ang_B', 'ang_C')
            self.canvas.create_oval(event.x - self.px, event.y - self.px, event.x + self.px, event.y + self.px, fill = 'black', tags = 'A')
            self.canvas.create_text(self.xA + 10, self.yA - 10, text = 'A', fill = 'black', tags = 'text_A')
            self.canvas.create_line(event.x, event.y, self.xB, self.yB, fill = 'black', width = 2, tags = 'AB')
            self.canvas.create_line(event.x, event.y, self.xC, self.yC, fill = 'black', width = 2, tags = 'AC')

            #Re-calculating side lengths 
            self.AB = math.sqrt((self.xA - self.xB) ** 2 + (self.mod_yA - self.mod_yB) ** 2)
            self.BC = math.sqrt((self.xB - self.xC) ** 2 + (self.mod_yB - self.mod_yC) ** 2)
            self.AC = math.sqrt((self.xA - self.xC) ** 2 + (self.mod_yA - self.mod_yC) ** 2)

            #Re-calculating angles
            self.A = format(math.degrees(math.acos((self.BC ** 2 - self.AC ** 2 - self.AB ** 2 ) / (-2 * self.AC * self.AB))), ".2f")
            self.canvas.create_text(self.xA, self.yA + 10, text = f"{self.A}", fill = 'black', tags = 'ang_A')
            self.B = format(math.degrees(math.acos((self.AC ** 2 - self.BC ** 2 - self.AB ** 2 ) / (-2 * self.BC * self.AB))), ".2f")
            self.canvas.create_text(self.xB, self.yB + 10, text = f"{self.B}", fill = 'black', tags = 'ang_B')
            self.C = format(math.degrees(math.acos((self.AB ** 2 - self.BC ** 2 - self.AC ** 2 ) / (-2 * self.BC * self.AC))), ".2f")
            self.canvas.create_text(self.xC, self.yC + 10, text = f"{self.C}", fill = 'black', tags = 'ang_C')

            self.xA = event.x
            self.yA = event.y
            self.mod_yA = -1 * self.yA
            self.a = 0

        #Dragging for point B (only if cursor is on point B):
        if (self.xB - self.curDis <= event.x <= self.xB + self.curDis) and (self.yB - self.curDis <= event.y <= self.yB + self.curDis):
            self.b = 1
        if self.verif == True:
            self.b = 0
        if self.b == 1:
            self.canvas.delete('B', 'BC', 'AB', 'text_B', 'ang_A', 'ang_B', 'ang_C')
            self.canvas.create_oval(event.x - self.px, event.y - self.px, event.x + self.px, event.y + self.px, fill = 'black', tags = 'B')
            self.canvas.create_text(self.xB + 10, self.yB - 10, text = 'B', fill = 'black', tags = 'text_B')
            self.canvas.create_line(event.x, event.y, self.xC, self.yC, fill = 'black', width = 2, tags = 'BC')
            self.canvas.create_line(event.x, event.y, self.xA, self.yA, fill = 'black', width = 2, tags = 'AB')

            #Re-calculating side lengths 
            self.AB = math.sqrt((self.xA - self.xB) ** 2 + (self.mod_yA - self.mod_yB) ** 2)
            self.BC = math.sqrt((self.xB - self.xC) ** 2 + (self.mod_yB - self.mod_yC) ** 2)
            self.AC = math.sqrt((self.xA - self.xC) ** 2 + (self.mod_yA - self.mod_yC) ** 2)

            #Re-calculating angles
            self.A = format(math.degrees(math.acos((self.BC ** 2 - self.AC ** 2 - self.AB ** 2 ) / (-2 * self.AC * self.AB))), ".2f")
            self.canvas.create_text(self.xA, self.yA + 10, text = f"{self.A}", fill = 'black', tags = 'ang_A')
            self.B = format(math.degrees(math.acos((self.AC ** 2 - self.BC ** 2 - self.AB ** 2 ) / (-2 * self.BC * self.AB))), ".2f")
            self.canvas.create_text(self.xB, self.yB + 10, text = f"{self.B}", fill = 'black', tags = 'ang_B')
            self.C = format(math.degrees(math.acos((self.AB ** 2 - self.BC ** 2 - self.AC ** 2 ) / (-2 * self.BC * self.AC))), ".2f")
            self.canvas.create_text(self.xC, self.yC + 10, text = f"{self.C}", fill = 'black', tags = 'ang_C')

            self.xB = event.x
            self.yB = event.y 
            self.mod_yB = -1 * self.yB
            self.b = 0

        #Dragging for point C (only if cursor is on point C):
        if (self.xC - self.curDis <= event.x <= self.xC + self.curDis) and (self.yC - self.curDis <= event.y <= self.yC + self.curDis):
            self.c = 1
        if self.verif == True:
            self.c = 0
        if self.c == 1:
            self.canvas.delete('C', 'AC', 'BC', 'text_C', 'ang_A', 'ang_B', 'ang_C')
            self.canvas.create_oval(event.x - self.px, event.y - self.px, event.x + self.px, event.y + self.px, fill = 'black', tags = 'C')
            self.canvas.create_text(self.xC + 10, self.yC - 10, text = 'C', fill = 'black', tags = 'text_C')
            self.canvas.create_line(event.x, event.y, self.xB, self.yB, fill = 'black', width = 2, tags = 'BC')
            self.canvas.create_line(event.x, event.y, self.xA, self.yA, fill = 'black', width = 2, tags = 'AC')

            #Re-calculating side lengths 
            self.AB = math.sqrt((self.xA - self.xB) ** 2 + (self.mod_yA - self.mod_yB) ** 2)
            self.BC = math.sqrt((self.xB - self.xC) ** 2 + (self.mod_yB - self.mod_yC) ** 2)
            self.AC = math.sqrt((self.xA - self.xC) ** 2 + (self.mod_yA - self.mod_yC) ** 2)

            #Re-calculating angles
            self.A = format(math.degrees(math.acos((self.BC ** 2 - self.AC ** 2 - self.AB ** 2 ) / (-2 * self.AC * self.AB))), ".2f")
            self.canvas.create_text(self.xA, self.yA + 10, text = f"{self.A}", fill = 'black', tags = 'ang_A')
            self.B = format(math.degrees(math.acos((self.AC ** 2 - self.BC ** 2 - self.AB ** 2 ) / (-2 * self.BC * self.AB))), ".2f")
            self.canvas.create_text(self.xB, self.yB + 10, text = f"{self.B}", fill = 'black', tags = 'ang_B')
            self.C = format(math.degrees(math.acos((self.AB ** 2 - self.BC ** 2 - self.AC ** 2 ) / (-2 * self.BC * self.AC))), ".2f")
            self.canvas.create_text(self.xC, self.yC + 10, text = f"{self.C}", fill = 'black', tags = 'ang_C')

            self.xC = event.x
            self.yC = event.y 
            self.mod_yC = -1 * self.yC
            self.c = 0
        
    #Function to return true for confirmation of buttonRelease
    def verif(self):
        return True

TriangleAngles()