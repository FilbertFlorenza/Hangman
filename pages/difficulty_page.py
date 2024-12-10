import tkinter as tk

def difficulty_page(window, show_page, show_game_page, images):
    # Difficulty Frame
    difficultyFrame = tk.Frame(window)
    difficultyFrame.grid(row=0,column=0, sticky='nsew', padx=10, pady=10)
    difficultyFrame.config(bg='#FFFFFF')
    difficultyFrame.rowconfigure(0, weight=1)
    difficultyFrame.columnconfigure(0, weight=1)

    # Title Label
    title = tk.Label(difficultyFrame, image=images['difficultyPhoto'])
    title.grid(row=0,column=0)

    # Buttons Frame
    buttonFrame = tk.Frame(difficultyFrame)
    buttonFrame.grid(row=1,column=0)

    # Buttons
    easyButton = tk.Button(
    buttonFrame,
    image=images['easyPhoto'],
    command=lambda: show_game_page('easy'),
    highlightthickness=0,
    borderwidth=0
    )
    easyButton.grid(row=2,column=0)

    mediumButton = tk.Button(
    buttonFrame,
    image=images['mediumPhoto'],
    command=lambda: show_game_page('medium'),
    highlightthickness=0,
    borderwidth=0
    )
    mediumButton.grid(row=2,column=1)

    hardButton = tk.Button(
    buttonFrame,
    image=images['hardPhoto'],
    command=lambda: show_game_page('hard'),
    highlightthickness=0,
    borderwidth=0
    )
    hardButton.grid(row=2,column=2)

    return difficultyFrame