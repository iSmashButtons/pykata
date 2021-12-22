# **Find e to the Nth Digit** - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

from math import e

def e_to_n_places(n):
    if n > 50:
        return '%.*f' %(50, e)
    else:
        return '%.*f' %(n, e)

while True:
    try:
        places = input("How many digits of Euler's number would you like to see?\n(up to 50, enter 'q' to quit)>>> ")
        places = int(places)
        print(e_to_n_places(places))
    except:
        if 'q' in places:
            break
        print("Enter integers only.")