import tkinter as tk
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