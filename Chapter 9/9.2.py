from tkinter import *

class InvestmentCalculator:
    def __init__(self):

        window = Tk()
        window.title('Investment Calculator')
        
        a = Label(window, text = 'Investment Amount')
        self.v1 = StringVar()
        a1 = Entry(window, width = 5, textvariable = self.v1, justify = RIGHT)
        b = Label(window, text = 'Years')
        self.v2 = StringVar()
        b1 = Entry(window, width = 5, textvariable = self.v2, justify = RIGHT)
        c = Label(window, text = 'Annual Interest Rate')
        self.v3 = StringVar()
        c1 = Entry(window, width = 5, textvariable = self.v3, justify = RIGHT)
        d = Label(window, text = 'Future Value')
        self.futureValue = StringVar()
        d1 = Label(window, textvariable = self.futureValue)
        e = Button(window, text = 'Calculate', command = self.CalcFutVal)


        a.grid(row = 1, column = 1, sticky = W)
        b.grid(row = 2, column = 1, sticky = W)
        c.grid(row = 3, column = 1, sticky = W)
        d.grid(row = 4, column = 1, sticky = W)
        e.grid(row = 5, column = 2, sticky = E)
        a1.grid(row = 1, column = 2, sticky = E)
        b1.grid(row = 2, column = 2, sticky = E)
        c1.grid(row = 3, column = 2, sticky = E)
        d1.grid(row = 4, column = 2, sticky = E)

        mainloop()

    def CalcFutVal(self):
        futureValue = self.calcFutureValue(float(self.v1.get()), float(self.v3.get()) / 1200, int(self.v2.get())) #invAmou, annual/12 = monthly, numberOfYears
        self.futureValue.set(format(futureValue, ".2f"))
        
    
    def calcFutureValue(self, investmentAmount, monthlyInterestRate, years):
        futureValue  = investmentAmount * ((1 + monthlyInterestRate) ** (years * 12))
        return futureValue



        
        
InvestmentCalculator()

