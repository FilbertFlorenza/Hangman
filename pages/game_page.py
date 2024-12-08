import tkinter as tk
import random
import time
import threading
from tkinter import StringVar, IntVar
from pages.pause_page import pause_page

def game_page(window, show_page, difficulty, exit, wordlist, images):
    # Game Frame
    gameFrame = tk.Frame(window)
    gameFrame.grid(row=0,column=0, sticky='nsew', padx=10, pady=10)
    gameFrame.rowconfigure(0, weight=1)
    gameFrame.columnconfigure(0, weight=1)

    def chooseWord(wordlist):
        return random.choice(wordlist)

    def isWordGuessed(secretWord, lettersGuessed):
        return set(secretWord).issubset(lettersGuessed) 
                
    def guessWord(secretWord, letter, stop_countdown):
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
            stop_countdown.set()
            show_page('congratulation_page')
        elif(timesGuessed == maxGuessVar.get()):
            stop_countdown.set()
            show_page('game_over_page')

    def set_timer(duration_in_seconds, stop_countdown, pause_countdown):
        def count_down():
            for i in range(duration_in_seconds, 0, -1):
                if stop_countdown.is_set():
                    return
                pause_countdown.wait()
                mins, secs = divmod(i, 60)
                timer = '{:02d}:{:02d}'. format(mins,secs)
                timerVar.set(timer)
                time.sleep(1)
            window.after(0, show_page('game_over_page'))

        # Run countdown on separate thread else it will block the main gui
        countdownThread = threading.Thread(target=count_down, daemon=True)
        countdownThread.start()

    def open_menu(menuFrame, pause_countdown):
        pause_countdown.clear()
        menuFrame.tkraise()

    # Set Variables
    difficultySetting = difficulty
    secretWord = chooseWord(wordlist)
    guessedWordVar = StringVar()
    lettersGuessedVar = StringVar()
    maxGuessVar = IntVar()
    timesGuessedVar = IntVar()
    timerVar = StringVar()

    stop_countdown = threading.Event()
    pause_countdown = threading.Event()
    # Check difficulty setting
    if difficultySetting == 'easy':
        maxGuessVar.set(8)
    elif difficultySetting == 'medium':
        maxGuessVar.set(6)
        pause_countdown.set()
        set_timer(60, stop_countdown, pause_countdown)
    else:
        maxGuessVar.set(4)
        pause_countdown.set()
        set_timer(30, stop_countdown, pause_countdown)

    # Pause Frame
    pauseFrame = pause_page(window, show_page, exit, pause_countdown, stop_countdown, images)

    # Menu Button
    menuButton = tk.Button(gameFrame, text='Pause', command=lambda: open_menu(pauseFrame, pause_countdown))
    menuButton.grid(row=0,column=0,sticky='nw')

    # Timer Label
    timerLabel = tk.Label(gameFrame, textvariable=timerVar).grid(row=0,column=0)

    # Word Label
    guessedWordVar.set('_ '*len(secretWord)) #Set initial hidden word
    wordLabel = tk.Label(gameFrame, textvariable=guessedWordVar).grid(row=1,column=0)

    # Alphabet Buttons Array
    alphabets = [
        ['A','B','C','D','E','F'],
        ['G','H','I','J','K','L'],
        ['M','N','O','P','K','R'],
        ['S','T','U','V','W','X'],
        ['Y','Z']
    ]

    # Alphabet Buttons Frame
    alphabetFrame = tk.Frame(gameFrame)
    alphabetFrame.grid(row=2,column=0)
        
    # Create button through loop
    for indexRow,row in enumerate(alphabets):
        for indexColumn,letter in enumerate(row):
            letterButton = tk.Button(alphabetFrame, text=letter, command=lambda l=letter.lower():  guessWord(secretWord, l, stop_countdown))
            letterButton.grid(row=indexRow+1, column=indexColumn,pady=5) 
        
    return gameFrame