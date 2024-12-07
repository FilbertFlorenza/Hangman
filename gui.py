# run pip install ttkbootstrap di terminal sebelum dijalanin
import os
import random
import string
import sys
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import StringVar


#Initialize window
window = tk.Tk()
window.geometry("400x600")
window.minsize(400,600)
window.maxsize(400,600)
window.title("Hangman Game")

difficulty = StringVar()

# Start Button Image
startButton = Image.open("C:\\Users\\SHE LINNA\\Pictures\\Saved Pictures\\hangman\\start button.jpg")
startButton = startButton.resize((40,40))
startPhoto = ImageTk.PhotoImage(startButton)

# Exit Button Image
exitButton = Image.open("C:\\Users\\SHE LINNA\\Pictures\\Saved Pictures\\hangman\\exit button.jpg")
exitButton = exitButton.resize((40,40))
exitPhoto = ImageTk.PhotoImage(exitButton)
def first_page():

    
    def start():
        menuFrame.destroy()
        second_page()
    def exit():
        window.destroy()

    
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0)

    # Title Label
    title = tk.Label(menuFrame, text="Hangman Games")
    title.grid(row=0,column=0,sticky='w')

    # Buttons
    
    
    Button_Start = tk.Button(
        window,
        image= startPhoto,
        command=start
    )
    Button_Start.place(x= 140, y=450)
    # startButton = tk.Button(menuFrame, command=start)

    Button_Exit = tk.Button(
        window,
        image= exitPhoto,
        command=exit
    )
    Button_Exit.place(x= 220, y=450)
   

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
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0)

    buttonFrame = tk.Frame(menuFrame)
    buttonFrame.grid(row=0,column=0,sticky='w')

    pauseButton = tk.Button(buttonFrame, command=pause, text="PAUSE")
    pauseButton.grid(row=1, column=0)


    difficultySetting = difficulty.get()
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

    def chooseWord(wordlist):
        """
        Choose a random word from the word list

        Parameters:
            wordlist (list): list of words

        Returns: 
            a word from wordlist at random (string)
        """
        return random.choice(wordlist)

    # Load the list of words into the variable wordlist
    # so that it can be accessed from anywhere in the program
    wordlist = loadWords()

    def isWordGuessed(secretWord, lettersGuessed):
        '''
        Check if word is guessed from the letters guessed

        Parameters:
            secretWord (string): the word the user is guessing
            lettersGuessed (list): what letters have been guessed so far
        returns: 
            boolean, True if all the letters of secretWord are in lettersGuessed (boolean)
        False otherwise
        '''
        return set(secretWord).issubset(lettersGuessed) 
            

    def getGuessedWord(secretWord, lettersGuessed):
        '''
        Parameters:
            secretWord (string): the word the user is guessing
            lettersGuessed (list): what letters have been guessed so far
        returns: 
            string, comprised of letters and underscores that represents what letters in secretWord have been guessed so far. (string)
        '''
        guessedWord = ''
        for letter in secretWord:
            if letter in lettersGuessed:
                guessedWord += letter
            else:
                guessedWord += '_ '
        return guessedWord


    def getAvailableLetters(lettersGuessed):
        '''
        Parameters:
            lettersGuessed (list): what letters have been guessed so far
        returns: 
            string, comprised of letters that represents what letters have not yet been guessed. (string)
        '''
        allLetters = string.ascii_lowercase
        availableLetters = ''
        for letter in allLetters:
            if letter not in lettersGuessed:
                availableLetters += letter
        return availableLetters
    
    word = chooseWord(wordlist)
    print(word)

def pause():

    def home():
        menuFrame.destroy()
        first_page()
    def game():
        menuFrame.destroy()
        game_page()
    def exit():
        window.destroy()

    # Menu Frame
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0)

    # Title Label
    title = tk.Label(menuFrame, text="Pause")
    title.grid(row=0,column=0,sticky='w')

    # Buttons Frame
    buttonFrame = tk.Frame(menuFrame)
    buttonFrame.grid(row=1,column=0)

    # Buttons
    resumeButton = tk.Button(buttonFrame, command=game,text="RESUME")
    mainmenuButton = tk.Button(buttonFrame, command=home,text="MAIN MENU")
    exitButton = tk.Button(buttonFrame, command=exit, text="EXIT")
    resumeButton.grid(row=1,column=0)
    mainmenuButton.grid(row=1,column=1)
    exitButton.grid(row=1,column=2)

first_page()
# customer_input()
# Run the application
window.mainloop()
