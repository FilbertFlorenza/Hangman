import tkinter as tk
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

    resumeButton = tk.Button(buttonFrame, command=game,text="RESUME")
    mainmenuButton = tk.Button(buttonFrame, command=home,text="MAIN MENU")
    exitButton = tk.Button(buttonFrame, command=exit, text="EXIT")
    resumeButton.grid(row=1,column=0)
    mainmenuButton.grid(row=1,column=1)
    exitButton.grid(row=1,column=2)