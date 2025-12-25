def numberOfAlphabets(s):    
    count = 0
    for i in range (len(s)):
        if s[i].isdecimal() == True:
            count += 1  #Count how many alphabets in the string.
    return count

def isValid(s):
    if len(s) >= 8 and numberOfAlphabets(s) >= 2 and s.isalnum() == True:
        return print("Password is valid.")
    else:
        return print("Password is invalid.")

def main():
    s = str(input("Enter your password: "))
    isValid(s)
main()
