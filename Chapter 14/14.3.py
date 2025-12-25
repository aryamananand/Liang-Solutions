import os.path
import sys

name = input("Enter file name: ")

if os.path.exists(name):
    main_file = open(name,"r")

    string2 = main_file.read()
    string1 = string2.replace(' ','')
    string3 = string1.replace("\n","-")
    string = string3.lower()
    lst = list(string)
    s1 = set(lst)
    print(s1)
    for x in s1:
        if x!="-":
            print(f"{x} appears {lst.count(x)} times.")
        else:
            print(f"\\n appears {lst.count("-")} times.")
