hexString = ""
def decimalToHex(n):
    global hexString
    if n < 10:
        return str(n) + hexString
    elif 10 <= n < 16:
        return chr(n+55) + hexString
    else:
        rem = n%16
        if rem > 9:
            rem = chr(rem+55)
        hexString = str(rem) + hexString
        return(decimalToHex(n//16))

print(decimalToHex(256))