def isSubstring(str1, str2):
    if str2.find(str1) != -1:
        return print(f"'{str1}' is a substring of '{str2}'.")
    else:
        return print(f"{str1} is not a substring of {str2}")

def main():
    str1 = str(input("Enter the first string: "))
    str2 = str(input("Enter the second string: "))
    isSubstring(str1, str2)
main()

