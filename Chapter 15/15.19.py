binString = ""
def decimalToBinary(n):
    global binString
    if n <= 1:
        binString = str(n) + binString
        return binString
    else:
        binString = f"{n%2}" + binString
        return(decimalToBinary(n//2))
    
print(decimalToBinary(123))