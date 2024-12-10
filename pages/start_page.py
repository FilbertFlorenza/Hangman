import tkinter as tk
def start_page(window, show_page, exit_func, images):
    # Menu Frame
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
    menuFrame.rowconfigure(0, weight=1)
    menuFrame.columnconfigure(0, weight=1)

    # Title Label with Image
    titleLabel = tk.Label(menuFrame, image=images['titlePhoto'])
    titleLabel.grid(row=0, column=0)

    # Button Frame
    buttonFrame = tk.Frame(menuFrame)
    buttonFrame.grid(row=1, column=0, pady=(10, 0))  # Add some padding above the button frame

    # Buttons
    Button_Start = tk.Button(
        buttonFrame,
        image=images['startPhoto'],
        command=lambda: show_page('difficulty_page'),
        highlightthickness=0,
        borderwidth=0
    )
    Button_Start.grid(row=0, column=0, padx=5)  # Add some padding between buttons

    Button_Exit = tk.Button(
        buttonFrame,
        image=images['exitPhoto'],
        command=exit_func,  # Use exit_func instead of exit
        highlightthickness=0,
        borderwidth=0
    )
    Button_Exit.grid(row=0, column=1, padx=5)  # Add some padding between buttons

    return menuFrame