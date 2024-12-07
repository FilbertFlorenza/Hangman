import tkinter as tk

def difficulty_page(window, show_page, show_game_page, images):
    # Difficulty Frame
    difficultyFrame = tk.Frame(window)
    difficultyFrame.grid(row=0,column=0, sticky='nsew', padx=10, pady=10)
    difficultyFrame.config(bg='#FFFFFF')
    difficultyFrame.rowconfigure(0, weight=1)
    difficultyFrame.columnconfigure(0, weight=1)

    # Title Label
    title = tk.Label(difficultyFrame, text="Select Difficulty")
    title.grid(row=0,column=0)

    # Buttons Frame
    buttonFrame = tk.Frame(difficultyFrame)
    buttonFrame.grid(row=1,column=0)

    # Buttons
    easyButton = tk.Button(buttonFrame, command=lambda:show_game_page('easy'),text="EASY")
    mediumButton = tk.Button(buttonFrame, command=lambda:show_game_page('medium'),text="MEDIUM")
    hardButton = tk.Button(buttonFrame, command=lambda:show_game_page('hard'),text="HARD")
    easyButton.grid(row=1,column=0)
    mediumButton.grid(row=1,column=1)
    hardButton.grid(row=1,column=2)

    return difficultyFrame