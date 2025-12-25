import os.path

infile = input("Enter a filename: ")


if os.path.isfile(infile):
    try:
        main_file = open(infile, "r")

        string2 = main_file.readlines()
        lineCount = len(string2)

        main_file.seek(0)

        string = main_file.read()
        lst = string.split()
        wordCount = len(lst)
        

        string3 = list("".join(string))
        charCount = len(string3)
        main_file.close()

        print(charCount, " characters")
        print(wordCount, " words")
        print(lineCount, "lines")
    except:
        print("File can't be opened.")
else:
    print("File not found.")

