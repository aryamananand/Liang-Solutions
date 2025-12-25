from pathlib import Path
count = 0
def wordCount_main(ent):
    global count
    folder = Path(ent)
    word = input("Enter the word to be searched:")

    wordList = []
    for item in folder.iterdir():
        if item.is_file():
            s = open(item,"r")
            s1 = s.read()
            s.close()
            s_final = s1.split()
            for x in s_final:
                 wordList.append(x)
            wordCount(wordList,word)
    print(f"The word {word} appears {wordCount(wordList)} times.")
def wordCount(lst,word):
        global count
        if len(lst) == 0:
            return count
        else:
            if lst[-1] == word:
                count += 1
                lst.remove(lst[-1])
                return wordCount(lst)
filename = input("Enter directory name:")
print(wordCount_main(filename))