# Check if Palindrome: Checks if the string entered by the user is a
# palindrome. That is that it reads the same forwards as backwards like “racecar”

def reverse_string(inputstr):
    if len(inputstr) == 0:
        return inputstr
    else:
        return reverse_string(inputstr[1:]) + inputstr[0]

def is_palindrome(inword):
    """
    Checks to see if `inword` is a palindrome (reversing the order of the letters
    produces the same word.) Returns True or False
    """
    if inword == reverse_string(inword):
        return True
    else:
        return False

teststr1 = 'racecar'
teststr2 = 'recursive'
teststr3 = 'kayak'

print(is_palindrome(teststr1))
print(is_palindrome(teststr2))
print(is_palindrome(teststr3))