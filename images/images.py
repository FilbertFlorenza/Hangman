import os
from PIL import ImageTk, Image
from tkinter import PhotoImage

def load_image():
    images = {}
    # Image Path
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

    # difficulty Screen Image
    image_path = "hangman.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    titleImage = Image.open(abs_image_path)
    titleImage = titleImage.resize((400,600))
    titlePhoto = ImageTk.PhotoImage(titleImage)
    images['titlePhoto'] = titlePhoto

    # Start Button Image
    image_path = "start button.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    startImage = Image.open(abs_image_path)
    startImage = startImage.resize((60,60))
    startPhoto = ImageTk.PhotoImage(startImage)
    images['startPhoto'] = startPhoto

    # Exit Button Image
    image_path = "exit button.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    exitImage = Image.open(abs_image_path)
    exitImage = exitImage.resize((60,60))
    exitPhoto = ImageTk.PhotoImage(exitImage)
    images['exitPhoto'] = exitPhoto

    image_path = "select difficulty.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    difficultyImage = Image.open(abs_image_path)
    difficultyImage = difficultyImage.resize((200,100))
    difficultyPhoto = ImageTk.PhotoImage(difficultyImage)
    images['difficultyPhoto'] = difficultyPhoto

    image_path = "easy button.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    easyImage = Image.open(abs_image_path)
    easyImage = easyImage.resize((60,60))
    easyPhoto = ImageTk.PhotoImage(easyImage)
    images['easyPhoto'] = easyPhoto

    image_path = "medium button.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    mediumImage = Image.open(abs_image_path)
    mediumImage = mediumImage.resize((60,60))
    mediumPhoto = ImageTk.PhotoImage(mediumImage)
    images['mediumPhoto'] = mediumPhoto

    image_path = "hard button.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    hardImage = Image.open(abs_image_path)
    hardImage = hardImage.resize((60,60))
    hardPhoto = ImageTk.PhotoImage(hardImage)
    images['hardPhoto'] = hardPhoto

    image_path = "resume.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    resumeImage = Image.open(abs_image_path)
    resumeImage = resumeImage.resize((60,60))
    resumePhoto = ImageTk.PhotoImage(resumeImage)
    images['resumePhoto'] = resumePhoto

    image_path = "main menu.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    mainmenuImage = Image.open(abs_image_path)
    mainmenuImage = mainmenuImage.resize((60,60))
    mainmenuPhoto = ImageTk.PhotoImage(mainmenuImage)
    images['mainmenuPhoto'] = mainmenuPhoto

    image_path = "exit button.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    exitImage = Image.open(abs_image_path)
    exitImage = exitImage.resize((60,60))
    exitPhoto = ImageTk.PhotoImage(exitImage)
    images['exitPhoto'] = exitPhoto

    image_path = "pause.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    pauseImage = Image.open(abs_image_path)
    pauseImage = pauseImage.resize((60,60))
    pausePhoto = ImageTk.PhotoImage(pauseImage)
    images['pausePhoto'] = pausePhoto

    return images