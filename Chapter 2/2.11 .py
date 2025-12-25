finalAccountValue = eval(input("Enter final account value:"))
annualInterestRate = eval(input("Enter annual interest rate in percent:"))
numberOfYears = eval(input("Enter number of years:"))

numberOfMonths = numberOfYears * 12

monthlyInterestRate = annualInterestRate / 1200

initialDepositAmount = finalAccountValue / ((1 + monthlyInterestRate) ** (numberOfMonths))

print("Initial deposit value is:", initialDepositAmount)
