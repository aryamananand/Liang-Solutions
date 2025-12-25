import time
class Time:
    def __init__(self):
        self.ti
        self.hour
        self.minute 
        self.second 
    def ti(self):
        self.ti = int(time.time() + 5 * 3600 + 30 * 60)
    def destroyTime(self):
        self.ti = 0
    def setTime(self, seconds): #Only to set initial time manually (enter seconds)
        self.ti = seconds
    def hour(self):
        self.hour = self.ti // 3600
        self.hour %= 24 
    def minute(self):
        self.ti = self.ti - 3600 * (self.ti // 3600)
        self.minute = self.ti // 60
    def second(self):
        self.second = self.ti % 60
    def getHour(self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second
    def addTime(self, sec):
        self.ti += sec

def main():
    t1 = Time()
    t1.ti()
    t1.hour()
    t1.minute()
    t1.second()
    print(f"The current time is: {t1.getHour()}:{t1.getMinute()}:{t1.getSecond()}")
    n = eval(input("Enter elapsed time in seconds: "))
    t1.addTime(n)
    t1.hour()
    t1.minute()
    t1.second()
    print(f"The time after elapsed time is: {t1.getHour()}:{t1.getMinute()}:{t1.getSecond()}")

main()

        


