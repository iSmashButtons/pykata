# Count Vowels: Enter a string and the program counts the number of vowels in
# the text. For added complexity have it report a sum of each vowel found.

import os

VOWELS = ['a','e','i','o','u']

def clear():
    '''
    Clear the terminal.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Vowel Counter'.center(50))
    print("-------------".center(50))
    print("Enter a string and I will count the number of\nvowels individually and in total. Press 'q' at\nany prompt to quit.")
    print('*' * 50)

def total_vowels(s):
    """ 
    Counts the vowels within a string and returns the total.
    """ 
    words =  s.lower().split(' ')
    num_vowels = 0
    for word in words:
        for l in word:
            if l in VOWELS:
                num_vowels += 1

    return num_vowels

def sum_each_vowel(s):
    """Counts the vowels witin a string and returns a dictionary with the sum
    total of each vowl.
    """   
    words =  s.lower().split(' ')
    sv = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for word in words:
        for l in word:
            if l in VOWELS:
                sv[l] += 1
    
    return sv

while True:
    clear()
    instring = input('\n>>> ')

    clear()
    print(f'\nCounting the vowels in "{instring}"... ')
    print('\nTotal vowels: ', total_vowels(instring))

    vowel_totals = sum_each_vowel(instring)
    print('\nSum of each vowel: ')
    for item in vowel_totals.items():
        print(f"{item[0]}: {item[1]}")
    print()
    break