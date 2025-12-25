investmentAmount = eval(input("Enter investment value:"))
annualInterestRate = eval(input("Enter annual interest rate:"))
numberOfYears = eval(input("Enter number of years:"))

monthlyInterestRate = annualInterestRate / 1200
numberOfMonths = numberOfYears * 12

futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** (numberOfMonths)

print("Accumulated Value is:", futureInvestmentValue)
