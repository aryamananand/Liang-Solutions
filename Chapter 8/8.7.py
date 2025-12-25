def convert(s):
    for i in range (len(s)):
        if s[i].isalpha() == True:
            if  97 <= ord(s[i]) <= 99:
                dig = 2
            elif 100 <= ord(s[i]) <= 102:
                dig = 3
            elif 103 <= ord(s[i]) <= 105:
                dig = 4
            elif 106 <= ord(s[i]) <= 108:
                dig = 5
            elif 109 <= ord(s[i]) <= 111:
                dig = 6 
            elif 112 <= ord(s[i]) <= 115:
                dig = 7
            elif 116 <= ord(s[i]) <= 118:
                dig = 8
            elif 119 <= ord(s[i]) <= 122:
                dig = 9
            else: 
                print("Input is invalid.")
        else:
            dig = s[i] 

        print(dig, end = '')
    

def main():
    s = str(input("Enter some alphanumeric code: "))
    sn = s.lower()
    convert(sn)
main()

