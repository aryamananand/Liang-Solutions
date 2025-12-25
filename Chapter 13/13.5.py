import os.path

filename = input("Enter a filename: ")

if os.path.isfile(filename):

    main_file = open(filename, "r")
    wordsString = main_file.read()

    wordsList = wordsString.split()

    oldString = input("Enter the old string to be replaced: ").strip()
    newString = input("Enter the new string to replace the old string: ").strip()

    for x in range(len(wordsList)):
        if wordsList[x] == oldString:
            wordsList[x] = newString

    main_file.close()

    main_file = open(filename, "w")
    write_str = " ".join(wordsList)
    main_file.write(write_str)
    print("Done.")

else:
    print("File does not exist.")