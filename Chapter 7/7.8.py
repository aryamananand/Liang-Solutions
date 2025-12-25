import time
class Stopwatch:
    def __init__ (self):
        self.startTime = int
        self.endTime = int

    def setStartTime(self):
        self.startTime = time.time()
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
    
    def start(self):
        self.startTime = time.time()
    def stop(self):
        self.endTime = time.time()

    def getElapsedTime(self):
        elapsedTime = self.endTime - self.startTime
        return format(elapsedTime, ".3f")
    
def main():
    sw1 = Stopwatch()
    sw1.start()
    sum = 0
    for i in range (1,1000001):
        sum += i
    sw1.stop()
    print("Elapsed Time is: ", sw1.getElapsedTime())

main()




