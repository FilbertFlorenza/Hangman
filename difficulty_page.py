import tkinter as tk

def difficulty_page(window, show_page, images):
    # def select_difficulty(difficultyString):
    #     difficulty.set(difficultyString)
    #     difficultyFrame.destroy()
    #     game_page()
    # Menu Frame
    difficultyFrame = tk.Frame(window)
    difficultyFrame.grid(row=0,column=0, sticky='nsew')
    difficultyFrame.config(bg='#FFFFFF')


    # Title Label
    title = tk.Label(difficultyFrame, text="Select Difficulty")
    title.grid(row=0,column=0,sticky='w')

    # Buttons Frame
    buttonFrame = tk.Frame(difficultyFrame)
    buttonFrame.grid(row=1,column=0)

    # Buttons
    easyButton = tk.Button(buttonFrame, command=lambda:show_page('game_page'),text="EASY")
    mediumButton = tk.Button(buttonFrame, command=lambda:show_page('game_page'),text="MEDIUM")
    hardButton = tk.Button(buttonFrame, command=lambda:show_page('game_page'),text="HARD")
    easyButton.grid(row=1,column=0)
    mediumButton.grid(row=1,column=1)
    hardButton.grid(row=1,column=2)

    return difficultyFrame