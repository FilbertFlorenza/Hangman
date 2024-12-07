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
    
    print()
    pass
first_page()
# customer_input()
# Run the application
window.mainloop()
