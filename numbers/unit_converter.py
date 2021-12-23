# **Unit Converter (temp, currency, volume, mass and more)** - Converts various
# units between one another. The user enters the type of unit being entered, the
# type of unit they want to convert to and then the value. The program will then
# make the conversion.

import os

def title_bar(cFrom=None, cTo=None):
    '''
    Clear the terminal and print out title bar.
    '''
    TITLE_WIDTH = 50
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * TITLE_WIDTH)
    print('*' + 'Unit Converter'.center(TITLE_WIDTH - 2) + '*')
    print('*' + f'From: {cFrom}'.ljust((TITLE_WIDTH-2)//2) + '*' if cFrom != None else '*'.ljust(25) + '*'.rjust(25))
    print('*' * TITLE_WIDTH)

def get_unit_type():
    print("What type of units are you converting?")

def get_unit(source=None, product=None):
    UNITS = ['inch', 'millimeter', ]
    if source:
        print("Which unit are you converting from?")

title_bar()