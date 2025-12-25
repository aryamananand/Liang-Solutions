


def printChars(ch1, ch2, numberPerLine):
    ord1 = ord(ch1)  #get ascii code for ch1
    ord2 = ord(ch2)  #get ascii code for ch2

    count_ = 1 #count for number of literals
    count = ord1
    
    for count in range (ord1, ord2 +1):
        print(chr(count), end = '')
        if count_ % numberPerLine == 0:
            print()

        count_ += 1
    return ''

def main():
    ch1 = input("Enter character 1: ")
    ch2 = input("Enter character 2: ")
    numberPerLine =  eval(input("Enter number of character per line: "))
    print(printChars(ch1, ch2, numberPerLine))
main()
