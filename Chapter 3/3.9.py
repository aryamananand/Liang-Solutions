name = input("Enter employee's name: ")

hours = eval(input("Enter numbers of hours worked in a week: "))

hourlyPayRate = eval(input("Enter hourly pay rate: "))

tax_1 = eval(input("Enter federal tax withholding rate in percentage: "))

tax_2 = eval(input("Enter state tax withholding rate in percentage: "))

tax1 = tax_1 / 100
tax2 = tax_2 / 100

grossPay = hourlyPayRate * hours

federalWithholding = tax1 * grossPay

stateWithholding = tax2 * grossPay

totalDeduction = federalWithholding + stateWithholding
netPay = grossPay - totalDeduction

print(" \n",
      "Employee name: ", name, "\n",
      "Hours Worked: ", hours, "\n",
      "Pay Rate: $", hourlyPayRate, "\n",
      "Gross Pay: $", grossPay, "\n",
      "Deductions:\n",
      "\t", "Federal Withholding (", format(tax_1, ".2f"), "% ): $", format(federalWithholding, ".2f"), "\n",
      "\t", "State Withholding (", format(tax_2, ".2f"), "% ): $", format(stateWithholding, ".2f"), "\n",
      "\t", "Total deduction: $", format(totalDeduction, ".2f"), "\n",
      "Net Pay: $", format(netPay, ".2f"))
      
