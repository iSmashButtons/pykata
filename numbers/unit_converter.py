# **Unit Converter (temp, currency, volume, mass and more)** - Converts various
# units between one another. The user enters the type of unit being entered, the
# type of unit they want to convert to and then the value. The program will then
# make the conversion.

# NOTE: 3rd-party module PyInputPlus used because the program requires a lot of input validation.

import os
from pyinputplus import inputMenu

def title_bar(cFrom=None, cTo=None):
    '''
    Clear the terminal and print out title bar.
    '''
    TITLE_WIDTH = 50
    TITLE_HALF_WIDTH = (TITLE_WIDTH - 2) // 2
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * TITLE_WIDTH)
    print('*' + 'Unit Converter'.center(TITLE_WIDTH - 2) + '*')
    print(f'* From: {cFrom}'.ljust(TITLE_HALF_WIDTH) + '*'.rjust(TITLE_HALF_WIDTH+2) if cFrom != None else '* From:'.ljust(25) + '*'.rjust(25))
    print(f'* To: {cTo}'.ljust(TITLE_HALF_WIDTH) + '*'.rjust(TITLE_HALF_WIDTH+2) if cTo != None else '* To:'.ljust(25) + '*'.rjust(25))
    print('*' * TITLE_WIDTH)

def get_unit_type():
    '''
    Gets type of units to covert from the user. Returns a list of units of that type. 
    '''
    OPTIONS = [
        'volume',
        'length',
        'weight',
        'temperature',
        'speed'
    ]
    title_bar()
    print("What type of units are you converting?")
    unit_type = inputMenu(OPTIONS)
    
    if unit_type == OPTIONS[0]: # volume
        units = [
            'milliliters',
            'cubic centimeters',
            'liters',
            'cubic meters',
            
        ]
    elif unit_type == OPTIONS[1]: # length
        pass
    elif unit_type == OPTIONS[2]: # weight
        pass
    elif unit_type == OPTIONS[3]: # temp
        pass
    elif unit_type == OPTIONS[4]: # speed
        pass

def get_unit(source=None, product=None):
    UNITS = ['inch', 'millimeter', ]
    if source:
        print("Which unit are you converting from?")

title_bar()