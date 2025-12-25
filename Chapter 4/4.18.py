#   (Financials: currency exchange) Write a program that prompts the user to enter
#   the currency exchange rate between U.S. dollars and Chinese Renminbi (RMB).
#   Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for vice versa.
#   Prompt the user to enter the amount in U.S. dollars or Chinese RMB
#   to convert it to Chinese RMB or U.S. dollars, respectively.

exchangeRate = eval(input("Enter the exchange rate from Dollars to RMB: "))
conversion = eval(input("Enter 0 to convert Dollars to RMB and 1 vice versa: "))

if conversion == 0:
    dollar = eval(input("Enter the amount in dollars: "))
    RMB = format(dollar * exchangeRate, ".3f")
    print("$" + str(dollar) + " is " + str(RMB) + " RMB.")
else:
    RMB = eval(input("Enter the amount in RMB: "))
    dollar = format(RMB / exchangeRate, ".3f")
    print(str(RMB) + " RMB is $" + str(dollar) + ".")
    
