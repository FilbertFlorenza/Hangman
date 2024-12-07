import os

script_dir = os.path.dirname(__file__)
WORDLIST_FILENAME = "words.txt"
abs_word_path = os.path.join(script_dir, WORDLIST_FILENAME)

def loadWords():
    # inFile: file
    inFile = open(abs_word_path, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    
    return wordlist