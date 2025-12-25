
stringVal = input("Enter a string: ")

# For completely decreasing order string:
count = 0
for i in range(len(stringVal)):
    if stringVal[i] < stringVal[i-1]:
        count += 1
if count == len(stringVal)-1:
    print("No two letters are in increasing order.")
else:
    # At least two letters are in increasing order:
    lst = []
    for i in range(len(stringVal)):
        a = stringVal[i]
        for j in range(i+1, len(stringVal)):
            a += stringVal[j]
            if (stringVal[j] > stringVal[j-1]):
                lst.append(a)
            else:
                break
    max = lst[0]
    for x in lst:
        if len(x) > len(max):
            max = x
    print(max)


    # Time complexity: O(n^2)

    # if n is the length of the string, then in the worst case, we go through the program (n + n^2 + n) times.
    # n --> first loop (to verify completely decreasing), n^2 --> nested loop, 
    # n --> third loop (finding max value) 
    # Hence loop total: O(n + n^2 + n) = O(n^2)
