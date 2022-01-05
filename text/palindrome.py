# Check if Palindrome: Checks if the string entered by the user is a
# palindrome. That is that it reads the same forwards as backwards like “racecar”

def is_palindrome(inword):
    """
    Checks to see if `inword` is a palindrome (reversing the order of the letters
    produces the same word.) Returns True or False
    """
    # reverse the input word
    revWord = inword[::-1]

    # Compare the input and reversed words.
    non_matching_letters = 0
    for i, l in enumerate(revWord):
        if inword[i] == l:
            continue
        else:
            non_matching_letters += 1

    if non_matching_letters > 0:
        return False
    else:
        return True

while True:
    # Get user input
    print("Enter a word or numbers and I will tell you if it\nis a palindrome.\nEnter 'q' to quit.")
    user_in = input('>>> ')
    user_in = user_in.lower()
    if 'q' == user_in:
        break

    # Print success/fail message
    if is_palindrome(user_in):
        print(f"\nYup! {user_in} is a palindrome!")
    else:
        print(f"\nNope. {user_in} is not a palindrome.")

    input('Press enter to continue.\n')