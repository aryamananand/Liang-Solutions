# a hangman game that randomly generates a word and
# prompts the user to guess one letter at a time
import random
import time 

Q = 'y'   #initialise 
while Q == 'y':
    words = ["apple", "mountain", "guitar", "storm", "castle", "rabbit", "cloud", 
    "freedom", "bridge", "butterfly", "universe", "ocean", "pencil", 
    "whale", "journey", "pyramid", "forest", "language", "galaxy", 
    "river", "memory", "paradise", "carpet", "village", "rocket", 
    "dawn", "dream", "mount", "eclipse", "glove", "sky"]
    word = words[random.randint(0,len(words)-1)]  #pick a random word from above list(user may vary list for better experience)
    #print(word)    #Print to see solution
    word = list(word)   #transform string into list of letters
    time1 = time.time()
    guess = []  #this is variable that will change as user guesses
    for u in word:
        guess.append('*')
    final_print = ''.join(guess)
    wrong_guesses = []  #list of guessed letters that are wrong
    total = 0   #to count number of guesses
    while guess != word:
        letter = input(f"(Guess) Enter a letter in the word {final_print} -> ")
        letter = letter.lower()

        if word.count(letter) > 0 and guess.count(letter) == 0:
            for i in range(len(word)):
                if word[i] == letter:
                    guess[i] = letter
            final_print = ''.join(guess)    #convert list to printable string 
        elif word.count(letter) <= 0:
            print(f"{letter} is not in the word.")
            if wrong_guesses.count(letter) == 0:
                wrong_guesses.append(letter)
            else:
                print(f"You had already guessed '{letter}'.")
        else:
            print(f"{letter} is already in the word.")
        total +=1

    print(f"'{''.join(word)}' is the word. You won in {total} guesses.")
    time2 = time.time()
    print(f"You took {int(time2 - time1)} seconds to guess.")
    Q = input('Do you want to guess another word? Enter y or n: ')
