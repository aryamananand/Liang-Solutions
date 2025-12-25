class Account:
    def __init__ (self):
        self.id = 0 #Default id is 0
        self.balance = 100  #Initial balance is 100
        self.annualInterestRate = 0 #Intial annual interest rate is 0

    def setId(self, id):
        self.id = id 
    def getId(self):
        return self.id 
    def setBalance(self, balance):
        self.balance = balance
    def getBalance(self):
        return self.balance
    def setANR(self, ANR):
        self.annualInterestRate = ANR
    def getANR(self):
        return self.annualInterestRate
    def getMIR(self):
        return self.annualInterestRate / 12
    def getMonthlyInterest(self):
        MIR = self.annualInterestRate / 1200
        monthlyInterest = self.balance * MIR 
        return monthlyInterest
    def withdraw(self, amount):
        self.balance -= amount 
    def deposit(self, amount):
        self.balance += amount



a1 = Account()
a1.setId(1122)
a1.setBalance(20000)
a1.setANR(4.5)
a1.withdraw(2500)
a1.deposit(3000) 

print("Account a1 details below.")
print(f"    ID: {a1.getId()}")
print(f"    Balance: {a1.getBalance()}")
print(f"    Monthly Interest Rate: {a1.getMIR()}%")
print(f"    Monthly Interest: {a1.getMonthlyInterest()}")


    