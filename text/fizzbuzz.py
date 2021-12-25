# **Fizz Buzz** - Write a program that prints the numbers from 1 to 100. But for
# multiples of three print “Fizz” instead of the number and for the multiples of
# five print “Buzz”. For numbers which are multiples of both three and five print
# “FizzBuzz”.

def fizzbuzz(n):
    if (n % 5 == 0) and (n % 3 == 0):
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return n

for i in range(1, 101):
    print(fizzbuzz(i))