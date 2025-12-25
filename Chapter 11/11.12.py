import sys 

status = eval(input( 
    "(O-single filer, 1-married jointly,\n" +
    "2-married separately, 3-head of household,\n" +
    "Enter the filing status: "))
if status >= 4:
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

def taxcount (s,i):
    if i <= brackets[s][0]:
        tax = i * rates[0]
    elif i <= brackets[s][1]:
        tax = brackets[s][0] * rates[0] + \
        (i - brackets[s][0]) * rates[1]
    elif i <= brackets[s][2]:
        tax = brackets[s][0] * rates[0] + \
        (brackets[s][1] - brackets[s][0]) * rates[1] + \
        (i - brackets[s][1]) * rates[2]
    elif i <= brackets[s][3]:
        tax = brackets[s][0] * rates[0] + \
        (brackets[s][1] - brackets[s][0]) * rates[1] + \
        (brackets[s][2] - brackets[s][1]) * rates[2] + \
        (i - brackets[s][2]) * rates[3]
    elif i <= brackets[s][4]:
        tax = brackets[s][0] * rates[0] + \
        (brackets[s][1] - brackets[s][0]) * rates[1] + \
        (brackets[s][2] - brackets[s][1]) * rates[2] + \
        (brackets[s][3] - brackets[s][2]) * rates[3] + \
        (i - brackets[s][3]) * rates[4]
    else:
        tax = brackets[s][0] * rates[0] + \
        (brackets[s][1] - brackets[s][0]) * rates[1] + \
        (brackets[s][2] - brackets[s][1]) * rates[2] + \
        (brackets[s][3] - brackets[s][2]) * rates[3] + \
        (brackets[s][4] - brackets[s][3]) * rates[4] + \
        (i - brackets[s][4]) * rates[5]
    return tax


print(taxcount(status,income))

