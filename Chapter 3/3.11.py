number = eval(input("Enter a four-digit integer: "))

#ABCD becomes D
p1 = number % 10

#ABCD becomes ABC 
s1 = number // 10

#ABC becomes C
p2 = s1 % 10

#ABC becomes AB
s2 = s1 // 10

#AB becomes B
p3 = s2 % 10

#AB becomes A
p4 = s2 // 10

P = p1 * 1000 + p2 * 100 + p3 * 10 + p4

print("The reversed number is:", P)

