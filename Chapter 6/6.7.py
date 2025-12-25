
def futureInvestmentValue(investmentAmount, monthlyInterest, years):
    fiv = investmentAmount * ((1 + monthlyInterest) ** (years * 12))
    return format(fiv, ".2f")
def main():
    investmentAmount = eval(input("The amount invested: "))
    annualInterestRate = eval(input("Annual interest rate: "))
    print("Years  Future Value")
    print()
    for years in range (1,31):
        monthlyInterest = annualInterestRate/1200
        print(years, "     ", futureInvestmentValue(investmentAmount, monthlyInterest, years))
main()
    
