import os.path 
import random 

# Common English first names
first_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", 
    "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
    "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", 
    "Charles", "Karen"
]

# Common English last names
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", 
    "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", 
    "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", 
    "Taylor", "Moore", "Jackson", "Martin"
]

position = [
    "assistant", "associate", "full" 
]

try:
    main_file = open("/Users/aryamananand/Desktop/PYTHON/PLAINTEXT/salary.txt", "w")
    for i in range (1000):
        a = random.randint(0,len(first_names)-1)
        firstName = first_names[a]
        b = random.randint(0,len(last_names)-1)
        lastName = last_names[b]
        c = random.randint(0,2)
        pos = position[c]

        salary = random.randint(75000,130000) 
        if pos == "assistant":
            salary = random.randint(50000,80000)
        elif pos == "associate":
            salary = random.randint(60000,110000)
        
        final_string = firstName + ' ' + lastName + ' ' + pos + ' ' + str(salary) + "\n" 
        print(final_string)
        main_file.write(final_string)
    print("Done.")
except:
    print("Unable to write onto file.")