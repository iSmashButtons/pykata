# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
# The Fibonacci Sequence is generated when each number is the sum of the two preceding numbers.

while True:
    print("How many Fibonacci numbers would you like to see?")
    try:
        qty = input("(q to quit)>>> ")
        qty = int(qty)
    except:
        print("Integers only please.")