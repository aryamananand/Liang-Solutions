# a hangman game that randomly generates a word and
# prompts the user to self.guess one letter at a time
import random
from tkinter import *

class Hangman:
    def __init__(self):
        self.window = Tk()
        self.window.title("Hangman")
        self.window.geometry("500x410")
        Label(self.window,pady=10).pack()
        self.canvas = Canvas(self.window, width = 400, height = 300,bg="white")
        self.canvas.pack()
        Label(self.window).pack()
        b = Button(self.window,text="Close",command=self.close)
        b.pack()
        # base
        self.canvas.create_arc(20,270,110,310,start = 0, extent = 180, outline = "black")
        self.canvas.create_line(65,270,65,40,fill="black")
        self.canvas.create_line(65,40,165,40,fill="black")
        self.canvas.create_text(200,250,text=f"Guess a word:",tag='guessAWord',fill="black")
        self.canvas.bind("<Key>", self.play)
        self.canvas.focus_set()
        self.select_word()

        self.window.mainloop()
    
    def close(self):
        self.window.destroy()

    def select_word(self):  #Initialising function
        self.canvas.delete('man','hint','cont','finalText')
        self.canvas.create_text(200,250,text=f"Guess a word:",tag='guessAWord',fill="black")
        self.stage = 0
        words = ["apple", "mountain", "guitar", "storm", "castle", "rabbit", "cloud", 
            "freedom", "bridge", "butterfly", "universe", "ocean", "pencil", 
            "whale", "journey", "pyramid", "forest", "language", "galaxy", 
            "river", "memory", "paradise", "carpet", "village", "rocket", 
            "dawn", "dream", "mount", "eclipse", "glove", "sky"]
        self.word = words[random.randint(0,len(words)-1)]  #pick a random word from above list(user may vary list for better experience)
        print(self.word)    #Print to see solution
        self.word = list(self.word)   #transform string into list of letters
        self.guess = []  #this variable will change as user guesses - it is USER'S guess state
        for u in self.word:
            self.guess.append('*')
        self.final_print = ''.join(self.guess)
        self.canvas.create_text(290,250,text = self.final_print,fill="black",tag="finalText",font="Helevetica 16 bold")
        self.wrong_guesses = []  #list of self.guessed letters that are wrong
        self.total = 0   #to count number of self.guesses
        
    def play(self,event):
        if event.char.isalpha() and self.stage != 7:   #(stage != 7 => prevents game continual [accepting letters] after 7 erros)
            letter = event.char
            letter = letter.lower()
            if self.word.count(letter) > 0 and self.guess.count(letter) == 0:
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        self.guess[i] = letter
                self.final_print = ''.join(self.guess)    #convert list to printable string 
                self.canvas.delete('finalText')
                self.canvas.delete('hint')
                self.canvas.create_text(290,250,text = self.final_print,fill="black",tag="finalText",font="Helevetica 16 bold")
                if self.word == self.guess and self.guess != ['']*len(self.word):
                    self.canvas.delete('hint')
                    self.canvas.delete('missed')
                    self.canvas.create_text(250,100,text=f"'{''.join(self.word)}' is the word. You won in {self.total} guesses.",tag="hint",fill="green")
                    self.canvas.create_text(260,290,text = "To continue the game, press ENTER",fill="black",tag="cont")
            elif self.word.count(letter) <= 0:
                if self.wrong_guesses.count(letter) == 0:
                    self.wrong_guesses.append(letter)
                    self.stage += 1
                    self.canvas.delete("missed")
                    self.canvas.delete("hint")
                    self.canvas.create_text(250,280,text = f"Missed letters: {''.join(self.wrong_guesses)}",tag="missed",fill="black")
                    self.draw()
                    if self.stage == 7:
                        self.canvas.delete('answer','guessAWord','missed')
                        self.canvas.create_text(280,100,text=f"The word is {''.join(self.word)}.",fill="red",tag="hint")
                        self.canvas.create_text(220,290,text = "To continue the game, press ENTER",tag="cont",fill="black")
                        self.canvas.delete('finalText')
                        self.canvas.create_text(290,250,text = self.final_print,fill="grey",tag="finalText",font="Helevetica 16 bold")
                else:
                    self.canvas.delete('hint')
                    self.canvas.create_text(250,100,text=f"You have already guessed '{letter}'.",tag='hint',fill="grey")
            else:
                self.canvas.delete('hint')
                self.canvas.create_text(250,100,text=f"{letter} is already in the word.",tag = 'hint',fill="grey")
            self.total +=1
        if event.keysym == "Return" and ((self.word == self.guess and self.total!= 0) or self.stage == 7):
            self.select_word()

    def draw(self):
        if self.stage == 1:
            self.canvas.create_line(165,40,165,60,fill="black",tag ="man")
        if self.stage == 2:
            self.canvas.create_oval(150,60,180,90,outline="black",tag ="man")
        if self.stage == 3:
            self.canvas.create_line(160,90,135,120,fill="black",tag ="man")
        if self.stage == 4:
            self.canvas.create_line(172,88,210,120,fill="black",tag ="man")
        if self.stage == 5:
            self.canvas.create_line(165,95,165,145,fill="black",tag ="man")
        if self.stage == 6:
            self.canvas.create_line(165,145,150,160,fill="black",tag ="man")
        if self.stage == 7:
            self.canvas.create_line(165,145,180,160,fill = "black",tag ="man")
    

Hangman()
