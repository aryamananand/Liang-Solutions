class Stock:
    def __init__(self):
        self.symbol = "INTC"    #Default symbol is INTC
        self.name = "Intel Corporation" #Defaul name is Intel Corporation
        self.previousClosingPrice = 20.5    #Default
        self.currentPrice = 20.35   #Default

    def getStockName(self, name):
        self.name = name 
        return self.name
    def getStockSymbol(self, symbol):
        self.symbol = symbol
        return self.symbol
    def setCurrentStockPrice(self, stockPrice):
        self.currentPrice = stockPrice
    def getCurrentStockPrice(self):
        return self.currentPrice
    def getPreviousStockPrice(self):
        return self.previousClosingPrice
    def setPreviousStockPrice(self, previousStockPrice):
        self.previousClosingPrice = previousStockPrice
    def getChangePercent(self):
        changePercent = (100 / self.previousClosingPrice) * self.currentPrice 
        return changePercent
    

def main():
    s1 = Stock()
    stockName = s1.getStockName("Intel Corporation")
    stockSymbol = s1.getStockSymbol("INTC")
    currentStockPrice = s1.getCurrentStockPrice()
    previousClosingPrice = s1.getPreviousStockPrice()
    percent = format(s1.getChangePercent(), ".2f")
    print(f"Stock Symbol: {stockSymbol} and Stock Name: {stockName}.")
    print(f"Current Stock Price: {currentStockPrice} and Previous Stock Price: {previousClosingPrice}. ")
    print(f"Change Percent is {percent}")
main()


        
