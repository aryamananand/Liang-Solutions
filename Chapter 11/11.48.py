from tkinter import *

class BoundingRectangle:
    def __init__(self):
        self.circleList = []    # list of coordinates for a circle
        self.nameList = []      # list of tag names for circles (for deletion of circle)
        self.var = 0    # number of circle (for lists)

        #variables to draw bounding rectangle
        self.max_x = 0
        self.max_y = 0
        self.min_x = 0
        self.min_y = 0


        self.window = Tk()
        self.window.geometry('600x200')
        self.window.title('Bounding Rectangle')
        self.canvas = Canvas(self.window,height = 200,width = 600,bg ='white')
        self.canvas.pack()
        self.canvas.create_rectangle(20,20,200,120,outline ='black')
        self.canvas.create_text(80,50,text = 'INSTRUCTIONS',fill ='black')
        self.canvas.create_text(100,80,text = 'Add:   Left Click',fill='black',justify = 'center')
        self.canvas.create_text(100, 100, text = 'Remove:   Right Click',fill = 'black',justify='center')

        self.canvas.bind('<Button-1>',self.addCircle)
        self.canvas.bind('<Button-3>',self.removeCircle)

        self.window.mainloop()

    def addCircle(self,event):  
        if 125 < event.x < 595 and 5 < event.y < 195:
            self.nameList.append('Circle'+str(self.var))
            self.circleList.append([])                  # add a new list [x,y] to mainlist
            self.circleList[self.var].append(event.x)   # add x value of the circle
            self.circleList[self.var].append(event.y)   # add y value of the circle
            self.canvas.create_oval(event.x-5,event.y-5,event.x+6,event.y+6, outline = 'black',tags =str(self.nameList[self.var]))
            self.createRectangle()
            self.var += 1   # index for list of coordinates of circle
        self.createRectangle()
    def removeCircle(self,event):
        for circle in range(len(self.circleList)):
            if self.circleList[circle][0]-5 <= event.x <=  self.circleList[circle][0]+5:
                if self.circleList[circle][1]-5 <= event.y <= self.circleList[circle][1]+5:
                    self.canvas.delete(str(self.nameList[circle]))
                    self.var -= 1
                    self.circleList.pop(circle)
                    self.nameList.pop(circle)
                    print(self.circleList)
                    break
        self.canvas.delete('rectangle')
        self.createRectangle()
    def createRectangle(self):
        self.canvas.delete('rectangle')
        #make a temporary list of all x values
        temp_x = []
        temp_y = []
        for val in range (len(self.circleList)):
            temp_x.append(self.circleList[val][0])
            temp_y.append(self.circleList[val][1])
        startX = min(temp_x)-5
        startY = min(temp_y)-5
        endX = max(temp_x)+1+5
        endY = max(temp_y)+1+5
        self.canvas.create_rectangle(startX,startY,endX,endY,outline = 'black',tags = 'rectangle')
        
        
        
       
    
BoundingRectangle()