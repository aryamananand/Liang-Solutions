

def isSubstring(s1,s2):

    i = 0   # index of string
    j = 0   # index of substring

    while True:
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif s1[i] != s2[j]:
            i -= j-1
            j = 0
        if j == len(s2) - 1:
            print("Matched at index", i - len(s2)+1)
            break
        if i == len(s1)-1 and j != len(s2)-1:
            print(f"{s2} is not a substring of {s1}.")
            break
        
    


def main():
    isSubstring("Mississipi", "sip")
main()

# This is actually a O(m x n) algorithm, but eliminating the possibility of 
# consecutive identical characters, it becomes a O(n) algorithm [as required by the problem]