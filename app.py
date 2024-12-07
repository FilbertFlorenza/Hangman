# run pip install ttkbootstrap di terminal sebelum dijalanin
import tkinter as tk
import random
from tkinter import StringVar, IntVar
from helper.words import loadWords
from images.images import load_image
from pages.start_page import start_page
from pages.difficulty_page import difficulty_page
from pages.game_page import game_page
from pages.end_page import end_page

def main():
    #Initialize window
    window = tk.Tk()
    window.geometry("400x600")
    window.minsize(400,600)
    window.maxsize(400,600)
    window.title("Hangman Game")

    # Import word list from words.txt
    wordlist = loadWords()

    # Import images
    images = load_image()

    windowFrame = tk.Frame(window)
    windowFrame.pack(fill='both',expand=True)
    windowFrame.rowconfigure(0,weight=1)
    windowFrame.columnconfigure(0,weight=1)

    def show_page(page_name):
        page = pages[page_name]
        page.tkraise()

    def show_game_page(difficulty):
        page_game_page = game_page(
            windowFrame,
            show_page,
            difficulty,
            wordlist,
            images
            )
        page_game_page.tkraise()

    def exit():
        window.destroy()

    pages = {}
    pages['start_page'] = start_page(windowFrame, show_page, exit, images)
    pages['difficulty_page']  = difficulty_page(windowFrame, show_page, show_game_page, images)
    pages['congratulation_page'] = end_page(windowFrame, show_page, exit, images, 'Congratulations')
    pages['game_over_page'] = end_page(windowFrame, show_page, exit, images, 'Game Over')

    show_page('start_page')

    # Run window tkinter
    window.mainloop()

# Run the application
if __name__ == '__main__':
    main()


