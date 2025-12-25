from tkinter import *
import math

class Pendulum:
    def __init__(self):
        window = Tk()
        window.title("Pendulum")
        window.geometry('410x410')
        self.canvas = Canvas(window, width = 400, height = 400, bg = 'white')
        self.canvas.grid()
        self.l = 100    #Pendulum length 
        self.angle = 135    #Starting angle 
        self.dA = -5       #Speed Increment
        self.speed = 5     #Speed of pendulum 

        self.canvas.bind('<Key-BackSpace>', self.destroy)   #Close the window 

        self.canvas.bind('<Up>', self.speedUp)
        self.canvas.focus_set() 

        self.canvas.bind('<Down>', self.speedDown)
        self.canvas.focus_set()
    
        self.canvas.bind('<Key-r>', self.resume) # 'RESUME' command
        self.canvas.focus_set()
        
        self.canvas.bind('<Key-s>', self.stop)  # 'STOP' command
        self.canvas.focus_set()

        while True:

            self.canvas.delete('all')
            self.canvas.create_oval(197, 197, 204, 204, fill = 'black')
            xEnd = self.l * math.cos(self.angle * math.pi/180) + 200    #   One could also use 'math.radians' here, 
            yEnd = self.l * math.sin(self.angle * math.pi/180) + 200    #   instead of '* math.pi/180' 

            self.angle += self.dA

            if self.angle < 45:
                self.dA = self.speed
            if self.angle > 135:
                self.dA = -self.speed

            self.canvas.create_line(200, 200, xEnd, yEnd, fill = 'black', width = 2)
            self.canvas.create_oval(xEnd - 12, yEnd - 12, xEnd + 13, yEnd + 13, fill = 'black')
            
            #self.canvas.create_text(365, 367.5, text = 'd_Angle: ' + str(self.dA), fill = 'black')    #Change in angle display
            self.canvas.create_text(365, 380, text = 'Speed: ' + str(self.speed), fill = 'black')   #Speed display
            self.canvas.create_text(365, 355, text = 'Angle: ' + str(self.angle), fill = 'black')   #Angle display


            self.canvas.after(50)
            self.canvas.update()

        window.mainloop()

    def speedUp(self, event):
        if self.dA != 0 and self.speed < 50:    # --> No Speed change when pendulum is stopped
            self.speed += 1
            

    def speedDown(self, event):
        if self.dA != 0 and self.speed > 1:    # --> No Speed change when pendulum is stopped
            self.speed -= 1
        
    def stop(self, event):
        self.realdA = self.dA 
        self.dA = 0
            
    def resume(self, event):
        if self.dA == 0: #Resume button activates only if stop button is activated.
            if self.realdA < 0:
                self.dA -= self.speed   
            else:
                self.dA += self.speed

    def destroy(self, event):
        self.canvas.destroy()

Pendulum()

        

