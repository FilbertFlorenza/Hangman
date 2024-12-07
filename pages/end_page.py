import tkinter as tk
def end_page(window, show_page, exit, images, message):
    # End Frame
    endFrame = tk.Frame(window)
    endFrame.grid(row=0,column=0, sticky='nsew', padx=10, pady=10)
    endFrame.rowconfigure(0, weight=1)
    endFrame.columnconfigure(0, weight=1)

    # Title Label
    title = tk.Label(endFrame, text=message)
    title.grid(row=0,column=0)

    # Buttons Frame
    buttonFrame = tk.Frame(endFrame)
    buttonFrame.grid(row=1,column=0)
    # Buttons
    startButton = tk.Button(buttonFrame, command=lambda: show_page('start_page'),text="RESTART")
    exitButton = tk.Button(buttonFrame, command=lambda: exit(),text="EXIT")
    startButton.grid(row=1,column=0)
    exitButton.grid(row=1,column=1)

    return endFrame