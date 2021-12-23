# **Coin Flip Simulation** - Write some code that simulates flipping a single
# coin however many times the user decides. The code should record the outcomes
# and count the number of tails and heads.

from random import randint

def flip_coin(n):
    '''
    Simulate the flipping of a coin `n` number of times.
    Returns a list of results where each element is the result of a coin flip.
    '''
    results = []
    for i in range(n):
        outcome = randint(0, 100)
        if outcome <= 50:
            results.append('heads')
        else:
            results.append('tails')

    return results

def count_results(cflips):
    '''
    Count the number of head/tails results in a list of coinflip results.
    '''
    count = {'heads': 0, 'tails': 0}
    for i in cflips:
        if i == 'heads':
            count['heads'] += 1
        else:
            count['tails'] += 1

    return count

while True:
    try:
        nflips = input('Enter number of coin flips to simulate: ')
        if 'q' in nflips:
            break
        nflips = int(nflips)
    except:
        print('Integers only please.')
        
    results = flip_coin(nflips)
    total = count_results(results)
    print(f"Heads: {total['heads']}\nTails: {total['tails']}")
