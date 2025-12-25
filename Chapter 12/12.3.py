
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



class ATMmachine (Account):
    def __init__(self):
        self.accountNum = []
        for i in range(10):
            self.accountNum.append(i)
        
        # Create the accounts    
        for acc in range(10):
            self.accountNum[acc] = Account()
            self.accountNum[acc].setBalance(100)
        self.loop()  

    def loop(self):
        while True:
            work = 0    # Initialise
            number = eval(input("Enter an account ID: "))
            while work != 4:
                work = int(eval(input("        \n" \
                                " Main menu \n" \
                                "   1: Check balance \n" \
                                "   2: Withdraw \n" \
                                "   3: Deposit \n" \
                                "   4: Exit \n" \
                                "              \n" \
                                "Enter option: ")))
                
                if work == 1:   # Check balance
                    print(f"The balance of account {number} is {self.accountNum[number].getBalance()}.")

                elif work == 2: # Withdraw
                    amount = eval(input("Enter an amount to withdraw: "))
                    self.accountNum[number].withdraw(amount)

                elif work == 3: # Deposit
                    amount = eval(input("Enter an amount to deposit: "))
                    self.accountNum[number].deposit(amount)

                elif work == 4: # Exit
                    print()     # Exits the loop by default

                else:   # Error
                    print("Error - check your input.")

# Run it                
ATMmachine()
        

