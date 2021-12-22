# **Find PI to the Nth Digit** - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

from math import pi

def pi_to_n_places(n):
    if n > 50:
        return '%.*f' %(50, pi)
    else:
        return '%.*f' %(n, pi)

while True:
    try:
        places = input("How many digits of pi would you like to see (up to 50, enter 'q' to quit)? ")
        places = int(places)
        print(pi_to_n_places(places))
    except:
        if 'q' in places:
            break
        print("Enter integers only.")