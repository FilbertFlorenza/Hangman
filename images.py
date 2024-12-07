import os
from PIL import ImageTk, Image
from tkinter import PhotoImage

def load_image():
    images = {}
    # Image Path
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

    # Start Button Image
    image_path = "images\\start button.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    startImage = Image.open(abs_image_path)
    startImage = startImage.resize((40,40))
    startPhoto = ImageTk.PhotoImage(startImage)
    images['startPhoto'] = startPhoto

    # Exit Button Image
    image_path = "images\\exit button.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    exitImage = Image.open(abs_image_path)
    exitImage = exitImage.resize((40,40))
    exitPhoto = ImageTk.PhotoImage(exitImage)
    images['exitPhoto'] = exitPhoto

    return images