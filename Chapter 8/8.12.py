s1 = str(input("Enter a genome string: ").strip())
s = s1.upper() 

#First reverse the string
gs = ''
for i in range (len(s)-1,-1,-1):
    gs += s[i]
print(gs)   #To see reversed string

#Condition to check if genome exists or not.
if len(gs) % 3 != 0  or gs.count("GTA") == 0 or (gs.count("GAT") == 0 and gs.count("AAT") == 0 and gs.count("AGT") == 0):
    print("No gene is found.")
else:
    a = gs.rfind("GTA") #Find first occurence of "ATG" (reversed because string is also reversed)
    t = ''
    for i in range (a,len(gs)):
        t += str(gs[i])
        var = 0
        if t == "AGT":
            var = 1
            print("var1") 
        elif t == "GAT":
            var = 2
            print("var2")
        elif t == "AAT":
            var = 3
            print("var3")
        if var == 1:
            print(gs[a+2 : gs.rfind("AGT")])
        elif var == 2:
            print(gs[a+2 : gs.rfind("GAT")])
        elif var == 3:
            print(gs[a+2:gs.rfind("AAT")])
        

        