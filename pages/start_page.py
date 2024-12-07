import tkinter as tk

def start_page(window, show_page, exit, images):
    # Menu Frame
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0, sticky='nsew', padx=10, pady=10)
    menuFrame.rowconfigure(0, weight=1)
    menuFrame.columnconfigure(0, weight=1)

    # Title Label
    title = tk.Label(menuFrame, text="Hangman Game")
    title.grid(row=0,column=0)

    # Button Frame
    buttonFrame = tk.Frame(menuFrame)
    buttonFrame.grid(row=1,column=0)

    # Buttons
    Button_Start = tk.Button(
        buttonFrame,
        image= images['startPhoto'],
        command=lambda: show_page('difficulty_page'),
        highlightthickness=0,
        borderwidth=0 
    )
    Button_Start.grid(row=1,column=0)

    Button_Exit = tk.Button(
        buttonFrame,
        image= images['exitPhoto'],
        command=lambda: exit(),
        highlightthickness=0,
        borderwidth=0 
    )
    Button_Exit.grid(row=1, column=1)

    return menuFrame