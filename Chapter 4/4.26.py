#code for 4 DIGIT Palindrome number:

'''

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


if P == number:
    print(number, "is a palindrome number")
else:
    print(number, "is not a palindrome number")

'''

#code for 3 DIGIT Palindrome number:

number = eval(input("Enter a three-digit number: "))

p1 = number % 10
p_2 = number // 10
p2 = p_2 % 10
p3 = p_2 // 10

P = p1 * 100 + p2 * 10 + p3

if P == number:
    print(number, "is a palindrome number")
else:
    print(number, "is not a palindrome number")
