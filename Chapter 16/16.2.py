s = input("Enter a string: ")

final_lst = []
for i in range(len(s)):
    temp_lst = [s[i]]
    a = s[i]
    for j in range(i+1, len(s)):
        if s[j] > a:
            temp_lst.append(s[j])
            a = s[j]
    final_lst.append(temp_lst)


maxi = final_lst[0]     
for x in final_lst:
    if len(x) > len(maxi):
        maxi = x

print("Maximum consecutive substring is:", maxi)

# Time complexity: O(n^2)
# Double nested loop => n^2