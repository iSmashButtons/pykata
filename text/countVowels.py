# [**Count Vowels**](./text/vowelcount.py) Enter a string
# and the program counts the number of vowels in the text. For added complexity
# have it report a sum of each vowel found.

VOWELS = ['a','e','i','o','u']

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

# TODO: finish this function
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
    print("Enter a string and I will tell you the total number of vowels ('q' to quit').")
    #instring = input('>>> ')
    instring = "I fart in your general direction!"
    print('Total vowels: ', total_vowels(instring))
    vowel_totals_gen = (i for i in sum_each_vowel(instring).values())
    for i in vowel_totals_gen:
        print(type(i), i)
    #sum_vowels = sum(vowel_totals_gen)
    print('Sum of each vowel: ', sum_each_vowel(instring))
    break