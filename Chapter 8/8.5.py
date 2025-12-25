def count(s1, s2):
    return s1.count(s2)
def main():
    s1 = str(input("Enter string 1: "))
    s2 = str(input("Enter string 2: "))
    print(f"'{s2}' can be found {count(s1, s2)} times in '{s1}'")
main()
