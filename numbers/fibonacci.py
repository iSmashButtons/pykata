# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
# The Fibonacci Sequence is generated when each number is the sum of the two preceding numbers.

def fibonacci(n: int):
    '''
    Returns the Fibonacci sequence out to `n` numbers. 
    '''
    if n > 50:
        n = 50

    fib = [0, 1]
    if n <= 1:
        print(fib[0])
    else:
        for i in fib:
            print(i, end=' ')

    for i in range(1, n-1):
        next = fib[-2] + fib[-1]
        fib.append(next)
        print(fib[-1], end=' ')

while True:
    print("\nHow many Fibonacci numbers would you like to see (max 50)?")
    try:
        qty = input("(q to quit)>>> ")
        if 'q' in qty:
            break
        qty = int(qty)
        fibonacci(qty)
    except:
        print("Integers only please.")