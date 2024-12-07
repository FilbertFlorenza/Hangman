# run pip install ttkbootstrap di terminal sebelum dijalanin
import tkinter as tk
import random
from tkinter import StringVar, IntVar
from helper.words import loadWords
from images import load_image
from start_page import start_page
from difficulty_page import difficulty_page
# from game_page import game_page
# from end_page import end_page

def main():
    #Initialize window
    window = tk.Tk()
    window.geometry("400x600")
    window.minsize(400,600)
    window.maxsize(400,600)
    window.title("Hangman Game")

    # Import word list from words.txt
    wordlist = loadWords()

    # Import images
    images = load_image()

    # App variables
    difficulty = StringVar()

    windowFrame = tk.Frame(window)
    windowFrame.pack(fill='both',expand=True)
    windowFrame.rowconfigure(0,weight=1)
    windowFrame.columnconfigure(0,weight=1)

    def show_page(page_name):
        page = pages[page_name]
        page.tkraise()

    def exit():
        window.destroy()

    def game_page(window, show_page, images):
        gameFrame = tk.Frame(window)
        gameFrame.grid(row=0,column=0)

        buttonFrame = tk.Frame(gameFrame)
        buttonFrame.grid(row=0,column=0,sticky='w')

        # pauseButton = tk.Button(buttonFrame, command=pause, text="PAUSE")
        # pauseButton.grid(row=1, column=0)

        def chooseWord(wordlist):
            return random.choice(wordlist)

        def isWordGuessed(secretWord, lettersGuessed):
            return set(secretWord).issubset(lettersGuessed) 
                
        def guessWord(secretWord, letter):
        
            guessedWord = ''
            lettersGuessed = lettersGuessedVar.get()
            lettersGuessed = lettersGuessed + letter
            lettersGuessedVar.set(lettersGuessed)
            timesGuessed = timesGuessedVar.get()
            timesGuessed += 1
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessedWord += letter
                else:
                    guessedWord += '_ '

            guessedWordVar.set(guessedWord)
            timesGuessedVar.set(timesGuessed)
            
            if isWordGuessed(secretWord,lettersGuessed):
                gameFrame.destroy()
                # end_page('congratulations')
            elif(timesGuessed == maxGuessVar.get()):
                gameFrame.destroy()
                # end_page('game over')

        # Set Variables
        difficultySetting = difficulty.get()
        isTimer = False
        secretWord = chooseWord(wordlist)
        guessedWordVar = StringVar()
        lettersGuessedVar = StringVar()
        maxGuessVar = IntVar()
        timesGuessedVar = IntVar()

        if difficultySetting == 'easy':
            maxGuessVar.set(8)
        elif difficultySetting == 'medium':
            maxGuessVar.set(6)
            isTimer = True
        else:
            maxGuessVar.set(4)
            isTimer = True

        # Word Label
        guessWord(secretWord, '')
        wordLabel = tk.Label(gameFrame, textvariable=guessedWordVar).grid(row=0,column=0)

        # Alphabet Buttons
        alphabets = [
            ['A','B','C','D','E','F'],
            ['G','H','I','J','K','L'],
            ['M','N','O','P','K','R'],
            ['S','T','U','V','W','X'],
            ['Y','Z']
        ]

        alphabetFrame = tk.Frame(gameFrame)
        alphabetFrame.grid(row=1,column=0)
        
        for indexRow,row in enumerate(alphabets):
            for indexColumn,letter in enumerate(row):
                letterButton = tk.Button(alphabetFrame, text=letter, command=lambda l=letter.lower():  guessWord(secretWord, l))
                letterButton.grid(row=indexRow+1, column=indexColumn,pady=5) 
            
        return gameFrame
    
    pages = {}
    pages['start_page'] = start_page(windowFrame, show_page, exit, images)
    pages['difficulty_page']  = difficulty_page(windowFrame, show_page, images)
    pages['game_page'] = game_page(windowFrame, show_page, images)
    # pages['end_page'] = end_page(windowFrame, show_page, images)

    show_page('start_page')
    # Run window tkinter
    window.mainloop()

# Run the application
if __name__ == '__main__':
    main()


