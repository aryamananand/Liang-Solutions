count = 0
def countUppercase(s):
    global count
    if len(s) == 1 and 65 <= ord(s) <= 90:
        count += 1
        return count
    elif len(s) == 1:
        return count
    else:
        if 65 <= ord(s[len(s)-1]) <= 90:
            count += 1
        return countUppercase(s[:-1])
        
print(countUppercase("AUYEHF67AWEgwyugaqw6h"))