import tkinter as tk

def start_page(window, show_page, exit, images):
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0, sticky='nsew')
    menuFrame.config(bg='#FFFFFF')

    # Title Label
    title = tk.Label(menuFrame, text="Hangman Games")
    title.grid(row=0,column=0,sticky='w')

    # Buttons
    Button_Start = tk.Button(
        menuFrame,
        image= images['startPhoto'],
        command=lambda: show_page('difficulty_page')
    )
    Button_Start.grid(row=1,column=0)

    Button_Exit = tk.Button(
        menuFrame,
        image= images['exitPhoto'],
        command=lambda: exit()
    )
    Button_Exit.grid(row=1, column=1)

    return menuFrame