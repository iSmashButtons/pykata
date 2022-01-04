# **Pig Latin** - Pig Latin is a game of alterations played on the English
# language game. To create the Pig Latin form of an English word the initial
# consonant sound is transposed to the end of the word and an ay is affixed
# (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on
# rules.

import os

def title_bar():
    '''
    Clear the terminal and print out title bar.
    '''
    TITLE_WIDTH = 50
    TITLE_HALF_WIDTH = (TITLE_WIDTH - 2) // 2
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * TITLE_WIDTH)
    print('*' + 'Pig Latin Translator'.center(TITLE_WIDTH - 2) + '*')
    print('*' + 'Enter an English phrase, and I will'.center(TITLE_WIDTH - 2) + '*')
    print('*' + 'to translate to Piglatin'.center(TITLE_WIDTH - 2) + '*')
    print('*' * TITLE_WIDTH)


def piglatin(engStr: str):
    try:
        assert type(engStr) == str
    except:
        print('input must be a string object.')
        return None

    engStr = engStr.lower()

    # convert string to a list of words
    engWords = engStr.split(' ')

    for i, word in enumerate(engWords):
        # remove symbols, punctuation and numbers from the string
        for l in word:
            if l in r'!@#$%^&*()[]{}-_<>?/\\`~1234567890':
                word = word.replace(l, '')

        # remove the first letter
        first_letter = word[0]
        word = word[(word.index(first_letter) + 1):]

        # add the first letter and 'ay' to the end
        platin_word = word + first_letter + 'ay'

        # replace the word in the list with the new pig latin word.
        engWords[i] = platin_word

    # convert the list of words back into a string.
    retStr = ' '.join(engWords)

    return retStr

title_bar()
while True:
    print("Enter English ('q' to quit):")
    english = input('>>> ')
    if english == 'q':
        break

    pl = piglatin(english)
    print('\n' + pl)
    input()
    title_bar()