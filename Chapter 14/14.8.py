import os.path

file = input("Enter a filename: ")

try:
    if os.path.isfile(file):
        main_file = open(file)
        string1 = main_file.read()
        string1 = string1.lower()
        string1 = string1.replace('.','')
        string1 = string1.replace(',','')
        string1 = string1.replace('—','')
        words = string1.split()
        s1 = set(words)
        lst_final = list(s1)
        lst_final.sort()
        print(lst_final)
        
except:
    print("File not found.")
    