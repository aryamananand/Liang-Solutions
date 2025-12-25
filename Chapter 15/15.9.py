def reverseDisplay(s):
    if len(s) == 1:
        return s
    else:
        return s[len(s)-1]+reverseDisplay(s[:-1])


print(reverseDisplay("LEGENDS NEVER DIE"))