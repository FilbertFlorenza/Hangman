import tkinter as tk
import random
from tkinter import StringVar, IntVar

def game_page(window,show_page, difficulty, wordlist, images):
    # Game Frame
    gameFrame = tk.Frame(window)
    gameFrame.grid(row=0,column=0, sticky='nsew', padx=10, pady=10)
    gameFrame.rowconfigure(0, weight=1)
    gameFrame.columnconfigure(0, weight=1)

    buttonFrame = tk.Frame(gameFrame)
    buttonFrame.grid(row=0,column=0)

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
            show_page('difficulty_page')
        elif(timesGuessed == maxGuessVar.get()):
            show_page('game_over_page')

    # Set Variables
    difficultySetting = difficulty
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