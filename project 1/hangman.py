#Muthee Francis
#project 1
#hangman.py
# Oct 19, 2011

from time import sleep
import random
import string

WORDLIST_FILENAME = "words.txt"

hangman_pics = ['''

   +---+

   |   |

       |

       |

       |

       |

 =========''', '''

    +---+

    |   |

    O   |

        |

        |

        |

  =========''', '''

     +---+

     |   |

     O   |

     |   |

         |

         |

   =========''', '''

   +---+

      |   |

      O   |

     /|   |

          |

          |

    =========''', '''
    
       +---+

       |   |

       O   |

      /|\  |

           |

           |

     =========''', '''
     
        +---+

        |   |

        O   |

       /|\  |

       /    |

            |

      =========''', '''

         +---+

         |   |

         O   |

        /|\  |

        / \  |

             |

       =========''']

def loadWords():
    print "\n Loading words from the file ........."
    sleep(2)
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "\n ["+ str(len(wordlist)) +"] words loaded !!!"
    return wordlist

def chooseWord(wordlist):
    #Returns a word from wordlist at random
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    global hangman_pics
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += '_ '
    return string


def repeat_game(user_choice):
    while True:
        if user_choice == 'Y' or user_choice == 'YES':
            play_hangman(secretWord)
        else:
            break

def play_hangman(secretWord):
    global hangman_pics
    print("\n WELCOME TO THE GAME OF HANGMAN !!! ")
    print("\n [ Guess a word that is ( " + str(len(secretWord)) +" ) letters long ]")
    lettersGuessed = []
    guesses = 7
    hangman_index = 0
    # while all the letters of secretWord are not yet in lettersGuessed and guesses left is more than 0
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print("\n You have " + str(guesses) +" guesses left")
        while True:
            guessLetter = raw_input("\n Guess a letter: ").lower()
            if guessLetter in lettersGuessed:
                print("\n You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("\n You have " + str(guesses) +" guesses left")
            elif len(guessLetter) > 1:
                print "\n Guess only one letter !!! "
            else:
                break

        lettersGuessed += guessLetter

        if isWordGuessed(secretWord, lettersGuessed):
            print("\n Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            sleep(2)
            print("\n CONGRATULATION !!! YOU SURVIVED THE HANGMAN !!! YOU WON !!! ")
            user_choice = raw_input('Would you like to play again [If you wish so type [Y or YES] or [N or NO] to quit]')
            repeat_game(user_choice)
            break
        # else if the guess letter is in secret word
        elif guessLetter in secretWord:
             print("\n Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        # else the guess letter is not in secret word
        else:
            print("\n You guessed incorrectly: " + getGuessedWord(secretWord, lettersGuessed))
            print hangman_pics[hangman_index]
            hangman_index +=1
            guesses -= 1
        # if ran out of guesses
        
        if guesses == 0:
            sleep(2)
            print("\n [ GAME OVER !!! YOU LOSE !!! THE HANGMAN GOT YOU !!! The word was " + secretWord + " ] ")
            user_choice = raw_input(' \n You can always try again !!! [If you wish so type [Y or YES] or [N or NO] to quit] : ')
            repeat_game(user_choice)

secretWord = chooseWord(wordlist).lower()
play_hangman(secretWord)
