import os.path
import re
filename = input("Enter a filename: ")
count = 0
try:
    if os.path.isfile(filename):
        main_file = open(filename,"r")

        vowel_set = {'a','e','i','o','u'}

        text = main_file.read()
        cleaned = re.sub(r'[^A-Za-z0-9]', '', text)
        lst = list(cleaned)
        
        for x in lst:
            if x in vowel_set:
                count += 1
        print("Vowels:", count)
        print("Consonants:",len(lst)-count)
    
except:
    print("File not found.")
