import sys

class Location():
    def __init__(self):
        self.Row = 0
        self.Column = 0
        self.maximum = 0
        RCcount = input("Enter the number of rows and columns in the list (separated by comma, no space):  ").split(',')
        rowCount = int(RCcount[0])
        columnCount = int(RCcount[1])
        self.lst = []
        for i in range(rowCount):
            self.lst.append([])
            vals = input(f"Enter row {i}: ").split(' ')
            for c in range(columnCount):
                self.lst[i].append(vals[c])
        
        #print(self.lst)

    def locateLargest(self):
        self.maximum = self.lst[0][0]
        for row in range(len(self.lst)):
            for column in range(len(self.lst[0])):
                if self.lst[row][column] > self.maximum:
                    self.maximum = self.lst[row][column]
                    self.Row = row
                    self.Column = column
        return str(f"Location of largest element is {self.maximum} at ({self.Row}, {self.Column}).")
    
    def getRow(self):   # Returns only the row of the maximum value
        return self.Row
    
    def getColumn(self):    # Returns only the column of the maximum value
        return self.Column
    
    def getMaxVal(self):    # Returns only the maximum value
        return self.maximum

    def reset(self):        # Accepts a new list
        self.__init__()
    

lst = Location()
print(lst.locateLargest())



