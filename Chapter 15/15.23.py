

def displayPermutation(s1,s2=""):  # letters shift from s1 to s2
    if len(s1) == 0:
        print(s2)
    else:
        for i in range(len(s1)):
            curChar = s1[i]
            rem = s1[:i] + s1[i+1:] #s1[:i/i:] --> (part before/after 'i'th char).
            displayPermutation(rem, s2 + curChar)

print(displayPermutation("ABC"))

