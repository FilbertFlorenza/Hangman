# run pip install ttkbootstrap di terminal sebelum dijalanin
import os
import random
import string
import sys
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import PhotoImage, StringVar, IntVar


#Initialize window
window = tk.Tk()
window.geometry("400x600")
window.minsize(400,600)
window.maxsize(400,600)
window.title("Hangman Game")

difficulty = StringVar()

# !!! IMPORTANT !!!!!
# words.txt directory, change to the directory of words.txt on your device. Example: C:/Documents/hangman/words.txt
# change this or else the program won't work
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def first_page():
    def start():
        menuFrame.destroy()
        second_page()
    def exit():
        window.destroy()

    # Menu Frame
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0)

    # Title Label
    title = tk.Label(menuFrame, text="Hangman Games")
    title.grid(row=0,column=0,sticky='w')

    # Buttons Frame
    buttonFrame = tk.Frame(menuFrame)
    buttonFrame.grid(row=1,column=0)

    # Buttons
    startButton = tk.Button(buttonFrame, command=start,text="START")
    exitButton = tk.Button(buttonFrame, command=exit,text="EXIT")
    startButton.grid(row=1,column=0)
    exitButton.grid(row=1,column=1)
   
def second_page():
    def select_difficulty(difficultyString):
        difficulty.set(difficultyString)
        menuFrame.destroy()
        game_page()
    # Menu Frame
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0)

    # Title Label
    title = tk.Label(menuFrame, text="Select Difficulty")
    title.grid(row=0,column=0,sticky='w')

    # Buttons Frame
    buttonFrame = tk.Frame(menuFrame)
    buttonFrame.grid(row=1,column=0)

    # Buttons
    easyButton = tk.Button(buttonFrame, command=lambda:select_difficulty('easy'),text="EASY")
    mediumButton = tk.Button(buttonFrame, command=lambda:select_difficulty('medium'),text="MEDIUM")
    hardButton = tk.Button(buttonFrame, command=lambda:select_difficulty('hard'),text="HARD")
    easyButton.grid(row=1,column=0)
    mediumButton.grid(row=1,column=1)
    hardButton.grid(row=1,column=2)
    
def game_page():
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
            end_page('congratulations')
        elif(timesGuessed == maxGuessVar.get()):
            gameFrame.destroy()
            end_page('game over')

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
   
    # Game Frame
    gameFrame = tk.Frame(window)
    gameFrame.grid(row=0,column=0)

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

def end_page(message):

    def restart():
        menuFrame.destroy()
        second_page()
    def exit():
        window.destroy()
    # Menu Frame
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0)

    # Title Label
    title = tk.Label(menuFrame, text=message)
    title.grid(row=0,column=0,sticky='w')

    # Buttons Frame
    buttonFrame = tk.Frame(menuFrame)
    buttonFrame.grid(row=1,column=0)

    # Buttons
    startButton = tk.Button(buttonFrame, command=restart,text="RESTART")
    exitButton = tk.Button(buttonFrame, command=exit,text="EXIT")
    startButton.grid(row=1,column=0)
    exitButton.grid(row=1,column=1)

first_page()
# customer_input()
# Run the application
window.mainloop()
