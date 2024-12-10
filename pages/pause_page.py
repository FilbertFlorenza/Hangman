import tkinter as tk
def pause_page(window, show_page, exit, pause_countdown, stop_countdown, images):
    
    def resume():
        show_page('game_page')
        pause_countdown.set()
    
    def main_menu():
        show_page('start_page')
        stop_countdown.set()

    # Menu Frame
    pauseFrame = tk.Frame(window)
    pauseFrame.grid(row=0,column=0, sticky='nsew', padx=10, pady=10)
    pauseFrame.rowconfigure(0, weight=1)
    pauseFrame.columnconfigure(0, weight=1)

    # Buttons Frame
    buttonFrame = tk.Frame(pauseFrame)
    buttonFrame.grid(row=1,column=0)

    resumeButton = tk.Button(
    buttonFrame,
    image=images['resumePhoto'],
    command=resume,
    highlightthickness=0,
    borderwidth=0
    )
    resumeButton.grid(row=1,column=0)

    mainmenuButton = tk.Button(
    buttonFrame,
    image=images['mainmenuPhoto'],
    command=main_menu,
    highlightthickness=0,
    borderwidth=0
    )
    mainmenuButton.grid(row=1,column=1)

    exitButton = tk.Button(
    buttonFrame,
    image=images['exitPhoto'],
    command=exit,
    highlightthickness=0,
    borderwidth=0
    )
    exitButton.grid(row=1,column=2)
    

    
    return pauseFrame