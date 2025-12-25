s = str(input("Enter a string: ").strip())
sRev = ""
for i in range (len(s)-1,-1,-1):
    sRev += s[i]

print(sRev)

