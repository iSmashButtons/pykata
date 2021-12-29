# [**Count Vowels**](./text/vowelcount.py) Enter a string
# and the program counts the number of vowels in the text. For added complexity
# have it report a sum of each vowel found.

def total_vowels(s):
    """ 
    Counts the vowels within a string and returns the total.
    """ 
    VOWELS = ['a','e','i','o','u']
    words =  s.lower().split(' ')
    num_vowels = 0
    for word in words:
        for l in word:
            if l in VOWELS:
                num_vowels += 1

    return num_vowels

# TODO: finish this function
def sum_each_vowel(s):
    pass

while True:
    print("Enter a string and I will tell you the total number of vowels ('q' to quit').")
    instring = input('>>> ')
    print(total_vowels(instring))
    break