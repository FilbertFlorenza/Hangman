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

    image_path = "congrats.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    congratsImage = Image.open(abs_image_path)
    congratsImage = congratsImage.resize((400,600))
    congratsPhoto = ImageTk.PhotoImage(congratsImage)
    images['Congratulations'] = congratsPhoto

    image_path = "game over.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    overImage = Image.open(abs_image_path)
    overImage = overImage.resize((400,600))
    overPhoto = ImageTk.PhotoImage(overImage)
    images['Game Over'] = overPhoto 
    
    image_path = "restart.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    restartImage = Image.open(abs_image_path)
    restartImage = restartImage.resize((60,60))
    restartPhoto = ImageTk.PhotoImage(restartImage)
    images['restartPhoto'] = restartPhoto

    image_path = "h1.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    h1Image = Image.open(abs_image_path)
    h1Image = h1Image.resize((400,600))
    h1Photo = ImageTk.PhotoImage(h1Image)
    images['h1'] = h1Photo 

    image_path = "h2.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    h2Image = Image.open(abs_image_path)
    h2Image = h2Image.resize((400,600))
    h2Photo = ImageTk.PhotoImage(h2Image)
    images['h2'] = h1Photo 

    image_path = "h3.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    h3Image = Image.open(abs_image_path)
    h3Image = h1Image.resize((400,600))
    h3Photo = ImageTk.PhotoImage(h3Image)
    images['h3'] = h3Photo 

    image_path = "h4.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    h4Image = Image.open(abs_image_path)
    h4Image = h1Image.resize((400,600))
    h4Photo = ImageTk.PhotoImage(h4Image)
    images['h4'] = h4Photo 

    image_path = "h5.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    h5Image = Image.open(abs_image_path)
    h5Image = h5Image.resize((400,600))
    h5Photo = ImageTk.PhotoImage(h5Image)
    images['h5'] = h5Photo 

    image_path = "h6.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    h6Image = Image.open(abs_image_path)
    h6Image = h6Image.resize((400,600))
    h6Photo = ImageTk.PhotoImage(h6Image)
    images['h6'] = h6Photo 

    image_path = "h7.jpg"
    abs_image_path = os.path.join(script_dir, image_path)
    h7Image = Image.open(abs_image_path)
    h7Image = h1Image.resize((400,600))
    h7Photo = ImageTk.PhotoImage(h7Image)
    images['h7'] = h7Photo 
    
    return images