# run pip install ttkbootstrap di terminal sebelum dijalanin
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage


#Initialize window
window = tk.Tk()
window.geometry("400x600")
window.minsize(400,600)
window.maxsize(400,600)
window.title("Hangman Game")

def first_page():

    def start():
        menuFrame.destroy()
        second_page()
    def exit():
        window.destroy()

    # Menu Frame
    menuFrame = tk.Frame(window)
    menuFrame.grid(row=0,column=0)

    # Title Label
    title = tk.Label(menuFrame, text="Hangman Games")
    title.grid(row=0,column=0,sticky='w')

    # Buttons
    startButton = tk.Button(menuFrame, command=start,text="START")
    exitButton = tk.Button(menuFrame, command=exit,text="EXIT")
    startButton.grid(row=1,column=0,padx=10)
    exitButton.grid(row=1,column=1)
   

def second_page():
    pass
    

first_page()
# customer_input()
# Run the application
window.mainloop()
