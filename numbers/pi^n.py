# **Find PI to the Nth Digit** - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
# Python has a standard math library that includes a constant variable that holds
# the value of Pi out to 15 places. So 15 places will be the limit for this program
# since, you know, that's easiest. 

import math

def pi_to_n_places(n):
    pi = math.pi
    return round(pi, n)

places = 4
print(pi_to_n_places(places))