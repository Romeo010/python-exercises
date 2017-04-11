# Name: Romeo Ekirapa
# MIT Username: 
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = ['p']

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
    
# testing

#print word_guessed()



def print_guessed():
    '''
    Returns a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    global secret_word
    global letters_guessed

    character_list = []

    for letter in secret_word:
        if letter in letters_guessed:
            character_list.append(letter)
        else:
            character_list.append('-')
            
    print join(character_list, '')
    
# testing

#print print_guessed()

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    start = True

    while start:
        print MAX_GUESSES-mistakes_made, "guesses left"
        print print_guessed()

        guess = lower(raw_input("Enter your guessed letter: "))
        while len(guess) > 1:
            guess = lower(raw_input("Enter only one guessed letter: "))

        if guess in letters_guessed:
            print "letter", guess, " already guessed."
        elif guess in secret_word:
            letters_guessed.append(guess)
            print "Letter", guess, " is correct."

            if word_guessed():
                print "Word", secret_word, " is correctly guessed."
        else:
            letters_guessed.append(guess)
            mistakes_made = mistakes_made + 1
            print "Letter", guess, "is incorrect."

            if mistakes_made == 6:
                print "Maximum guesses", MAX_GUESSES, "reached."
                print "Secret word was", secret_word

                start = False

################### Results ###################

Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Loading word list from file...
   55900 words loaded.
Enter play_hangman() to play a game of hangman!
>>> play_hangman()
6 guesses left
-------
None
Enter your guessed letter: a
Letter a  is correct.
6 guesses left
-a-----
None
Enter your guessed letter: e
Letter e is incorrect.
5 guesses left
-a-----
None
Enter your guessed letter: i
Letter i  is correct.
5 guesses left
-a-i---
None
Enter your guessed letter: o
Letter o  is correct.
5 guesses left
-a-io--
None
Enter your guessed letter: u
Letter u is incorrect.
4 guesses left
-a-io--
None
Enter your guessed letter: w
Letter w is incorrect.
3 guesses left
-a-io--
None
Enter your guessed letter: s
Letter s  is correct.
3 guesses left
-a-io-s
None
Enter your guessed letter: x
Letter x is incorrect.
2 guesses left
-a-io-s
None
Enter your guessed letter: z
Letter z is incorrect.
1 guesses left
-a-io-s
None
Enter your guessed letter: v
Letter v is incorrect.
Maximum guesses 6 reached.
Secret word was cations
>>> 
    
