# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # basically check if the letter is in the guessed per character of secretWord
    for ch in secretWord:
        if ch not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # Empty String
    currentString = ""
    for ch in secretWord:
        if ch in lettersGuessed:
            currentString = currentString + ch
        else:
            currentString = currentString + " _ " 
    return currentString
            


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters  represents what letters have not
      yet been guessed.
    '''
    # Get alphabet
    alphabet = string.ascii_lowercase
    if(lettersGuessed == []):
        return alphabet
    for ch in lettersGuessed:
        if ch in alphabet:
            alphabet = alphabet.replace(ch,"")
    return alphabet
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Start game
    print("Welcome the game, Hangman!")
    #Annouce length of letters
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    wordGuess = False
    amountofGuesses = 8
    lettersGuessed = []
    legitletter = string.ascii_lowercase
    
    while wordGuess == False and amountofGuesses > 0:
        print("-------------")
        print("You have " + str(amountofGuesses) + " left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        currentGuess = input("Please guess a letter: ").lower()
        #First, lets see if its been written already
        if(currentGuess not in getAvailableLetters(lettersGuessed)):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            continue
        elif(currentGuess in legitletter and currentGuess in getAvailableLetters(lettersGuessed)):
            #means it is a legit letter, and it is NOT been guessed
            if(currentGuess in secretWord):
                #menas its in the word
                lettersGuessed.append(currentGuess)
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                #Check win 
                if(isWordGuessed(secretWord, lettersGuessed)):
                    wordGuess = True
                else:
                    continue
                
            else:
                #obviously not in the word
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(currentGuess) #add to the list of guesses
                amountofGuesses = amountofGuesses - 1 #lose a guess
                continue
        else:
            print("That is not a letter!")
            continue
    
    if(amountofGuesses <= 0):
        #player lost
        print("-----------")
        print("Sorry, you ran out of guesses. The word was " + secretWord)
    if(wordGuess == True):
        print("-----------")
        print("Congratulations, you won!")




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
