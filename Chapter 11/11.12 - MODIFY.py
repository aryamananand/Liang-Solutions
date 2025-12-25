import sys 

status = eval(input( 
    "(O-single filer, 1-married jointly,\n" +
    "2-married separately, 3-head of household,\n" +
    "Enter the filing status: "))
# Exit if invalid status is entered.
if not 0 <= status <= 3:
    print('Invalid status.')
    sys.exit()

income = eval(input("Enter your income: "))

brackets = [
[8350, 33950, 82250, 171550, 372950], # Single filer
[16700, 67900, 137050, 208850, 372950], # Married jointly
[8350, 33950, 68525, 104425, 186475], # Married separately
[11950, 45500, 117450, 190200, 372950] # Head of household
] 

rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

# Compute tax

def taxcount (status,income):
    if income >= brackets[status][4]:
        tax = (income - brackets[status][4]) * rates[5]
    if income >= brackets[status][3]:
        if income >= brackets[status][4]:
            tax += (brackets[status][4] - brackets[status][3]) * rates[4]
        else:
            tax += (income - brackets[status][3]) * rates[4]
    if income >= brackets[status][2]:
        if income >= brackets[status][3]:
            tax += (brackets[status][3]- brackets[status][2]) * rates[3]
        else:
            tax += (income - brackets[status][2]) * rates[3]
    if income >= brackets[status][2]:
        if income >= brakets[status][2]:
            tax += 
        tax += brackets[status][2]
       
    return tax 

print("Taxable amount: ", taxcount(status,income))
print(brackets)
