import random
import string
import sys


#karena manusia tempatnya salah dan lupa wajarlah manusia bukan nabi boyyyy

# !!! IMPORTANT !!!!!
# words.txt directory, change to the directory of words.txt on your device. Example: C:/Documents/hangman/words.txt
# change this or else the program won't work
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    Choose a random word from the word list

    Parameters:
        wordlist (list): list of words

    Returns: 
        a word from wordlist at random (string)
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    Check if word is guessed from the letters guessed

    Parameters:
        secretWord (string): the word the user is guessing
        lettersGuessed (list): what letters have been guessed so far
    returns: 
        boolean, True if all the letters of secretWord are in lettersGuessed (boolean)
      False otherwise
    '''
    return set(secretWord).issubset(lettersGuessed) 
            



def getGuessedWord(secretWord, lettersGuessed):
    '''
    Parameters:
        secretWord (string): the word the user is guessing
        lettersGuessed (list): what letters have been guessed so far
    returns: 
        string, comprised of letters and underscores that represents what letters in secretWord have been guessed so far. (string)
    '''
    guessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += '_ '
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    Parameters:
        lettersGuessed (list): what letters have been guessed so far
    returns: 
        string, comprised of letters that represents what letters have not yet been guessed. (string)
    '''
    allLetters = string.ascii_lowercase
    availableLetters = ''
    for letter in allLetters:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters
            
    

def hangman(secretWord):
    '''
    Parameters:
        secretWord (string): the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    # Initialize variables
    lettersGuessed = []
    mistakesMade = 0

    # Print welcome message
    print(f'Welcome to the game, Hangman!\nI am thinking of a word that is {len(secretWord)} letters long.')
    # Loop until game over or user guessed all words
    while(True):
      # Get Available Letters and guessWord
      availableLetters = getAvailableLetters(lettersGuessed)

      # Get user guess
      print('-------------')
      print(f'You have {8-mistakesMade} guesses left')
      print(f'Available letters: {availableLetters}')
      try:
        guess = str(input("Please guess a letter: ")).lower()
        # Check if user input valid a-z letter
        if guess not in string.ascii_lowercase:
            raise ValueError
      except ValueError:
          print("Please input valid letter")
      except KeyboardInterrupt:
          print("\nGame ended")
          sys.exit()

      # Check guess
      if guess in lettersGuessed:
          print("Oops! You've already guessed that letter: ", guessedWord)
          continue
      
      lettersGuessed.append(guess)

      if guess in secretWord:
          guessedWord = getGuessedWord(secretWord,lettersGuessed)
          print('Good guess: ', guessedWord)
      else:
          guessedWord = getGuessedWord(secretWord,lettersGuessed)
          print('Oops! That letter is not in my word: ', guessedWord)
          mistakesMade += 1

      if isWordGuessed(secretWord,lettersGuessed):
          print('-------------')
          print('Congratulations, you won!')
          break
      
      if mistakesMade >= 8:
          print('-------------')
          print(f'Sorry, you ran out of guesses. The word was {secretWord}.')
          break
           







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman('test')
