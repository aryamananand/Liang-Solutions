import time
class Time:
    def __init__(self):
        self.ti = int(time.time()) + 5 * 3600 + 30 * 60
        
    def addTime(self, sec):
        self.ti += sec
    def getTotalTime(self):
        return self.ti
    def setTime(self, seconds): #Only to set initial time manually (enter seconds)
        self.ti = seconds
    def setHour(self):
        self.hour = self.ti // 3600
        self.hour %= 24 
    def setMinute(self):
        x = self.ti - 3600 * (self.ti // 3600)
        self.minute = x // 60
    def setSecond(self):
        x = self.ti - 3600 * (self.ti // 3600)
        self.second = x % 60
    def getHour(self):
        return self.hour 
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second

def main():
    t1 = Time()
    t1.setHour()
    t1.setMinute()
    t1.setSecond()
    print(f"The current time is: {t1.getHour()}:{t1.getMinute()}:{t1.getSecond()}")
    n = eval(input("Enter elapsed time in seconds: "))
    t1.addTime(n)
    t1.setHour()    
    t1.setMinute()
    t1.setSecond()
    print(f"The time after elapsed time is: {t1.getHour()}:{t1.getMinute()}:{t1.getSecond()}")

main()

        


